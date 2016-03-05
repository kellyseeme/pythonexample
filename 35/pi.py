#!/usr/bin/env python
import pickle
account_info = {
"993295289852":["kel",15000,15000],
"242534536363":["pick",9000,9090]
}
aList = [1,2,3,4,5]
f = file("kel.pkl","wb")
pickle.dump(account_info,f)
pickle.dump(aList,f)
f.close()

