p = 'ls.txt'
# 
# for x in range(1000):
#     with open(p,'a') as f:
#         f.write(l+"\n")
with open(p,'r') as g:
    l=g.readlines()
print(l)