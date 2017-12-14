mylist = [20, 30, 25, 20]
from collections import defaultdict
D = defaultdict(list)
for i,item in enumerate(mylist):
    D[item].append(i)
D = {k:v for k,v in D.items() if len(v)>1}
print D