def new(num_buckets=256):
    aMap = []
    for i in range(0,num_buckets):
        aMap.append([])
    return aMap

aMap = new()
bucket = aMap[hash("kel") % len(aMap)]
print bucket
for i,kv in enumerate(bucket):
    k,v = kv
    print i,k,v

