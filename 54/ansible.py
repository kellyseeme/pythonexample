#!/usr/bin/env python
import fnmatch
from optparse import OptionParser
import os
from multiprocessing import Process,Pipe
from itertools import izip
import json
import paramiko

DEFAULT_HOST_LIST = '~/ansible_hosts'
DEFAULT_MODULE_PATH = '~/ansible'
DEFAULT_MODULE_NAME = 'ping'
DEFAULT_PATTERN = '*'
DEFAULT_MODULE_ARGS = ''
DEFAULT_FORKS = 3

class Pooler(object):
    @classmethod
    def spawn(cls,f):
        def fun(pipe,x):
            pipe.send(f(x))
            pipe.close()
        return fun

    @classmethod
    def parmap(cls,f,X):
        pipe=[Pipe() for x in X]
        proc=[Process(target=cls.spawn(f),args=(c,x)) for x,(p,c) in izip(X,pipe)]
        [p.start() for p in proc]
        [p.join() for p in proc]
        return [p.recv() for (p,c) in pipe]

class Cli(object):
    'def the class of command line interface'
    def __init__(self):
        pass

    def runner(self):
        parser = OptionParser()
        parser.add_option('-H','--host-list',dest='host_list'
                            ,help='path to host list',default=DEFAULT_HOST_LIST)
        parser.add_option('-L','--library',dest='module_path'
                            ,help='path to module library',default=DEFAULT_MODULE_PATH)
        parser.add_option('-F','--forks',dest='forks'
                            ,help='level of parallelism',default=DEFAULT_FORKS)
        parser.add_option('-n','--name',dest='module_name'
                            ,help='module name to execute',default=DEFAULT_MODULE_NAME)
        parser.add_option('-a','--args',dest='module_args'
                            ,help='module arguments',default=DEFAULT_MODULE_ARGS)
        parser.add_option('-p','--pattern',dest='pattern'
                            ,help='hostname pattern',default=DEFAULT_PATTERN)

        options,args = parser.parse_args()
        host_list = self._host_list(options.host_list)

        return Runner(
            module_name=options.module_name,
            module_path=options.module_path,
            module_args=options.module_args,
            host_list=host_list,
            forks=options.forks,
            pattern=options.pattern,
            )

    def _host_list(self,host_list):
        'find the core host file and return the host_list in the file'
        host_list = os.path.expanduser(host_list)
        return file(host_list).read().split('\n')

class Runner(object):
    
    def __init__(self,host_list=[],module_path=None,
        module_name=None,module_args='',
        forks=3,timeout=60,pattern='*'):
        
        self.host_list=host_list
        self.module_path = module_path
        self.module_name=module_name
        self.forks=forks
        self.pattern=pattern
        self.module_args=module_args
        self.timeout=timeout

    def _matches(self,host_name):
        'check the host name is matched'
        if host_name == '':
            return False
        if fnmatch.fnmatch(host_name,self.pattern):
            return True
        return False

    def _connect(self,host):
        'use the paramiko to connect the host'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host,username='root',
                allow_agent=True,lock_for_keys=True)
            return ssh
        except:
            return None

    def _executor(self,host):
        conn=self._connect(host)
        if not conn:
                return [host,None]
        outpath = self._copy_module(conn)
        print outpath
        self._exec_command(conn,'chmod +x %s' % outpath)
        cmd = self._command(outpath)
        result = self._exec_command(conn,cmd)
        result = json.loads(result)
        return [host,result]

    def _command(self,outpath):
        cmd='%s %s' %(outpath,self.module_args)
        return cmd

    def _exec_command(self,conn,cmd):
        stdin,stdout,stderr = conn.exec_command(cmd)
        results = stdout.read()
        return results

    def _copy_module(self,conn):
        inpath=os.path.expanduser(os.path.join(self.module_path,self.module_name))
        print inpath
        outpath=os.path.join('/var/spool/','ansible_%s' % self.module_name)
        print outpath
        ftp=conn.open_sftp()
        ftp.put(inpath,outpath)
        ftp.close()
        return outpath

    def run(self):
        hosts = [h for h in self.host_list if self._matches(h)]
        def executor(x):
            return self._executor(x)
        results=Pooler.parmap(executor,hosts)
        by_host = dict(results)
        return by_host


if __name__ == '__main__':
    result = Cli().runner().run()
    print json.dumps(result,sort_keys=True,indent=4)

    r= Runner(
        host_list = ['127.0.0.1'],
        module_path='~/ansible',
        module_name='ping',
        module_args='',
        pattern='*',
        forks=3
        )
  #  print r.run()
