#
#13.	Flatten the list  [1,2,3,4,5,6,7]  into 1234567  using reduce().

from functools import reduce
ans = reduce(lambda s,i: s+str(i),[1,2,3,4,5,6,7],'')
print(ans)