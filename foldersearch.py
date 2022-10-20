import os
cwd=os.getcwd()
#print(cwd)
#print(os.listdir("/home/dci-admin/Documents/excercises"))
list=os.listdir(cwd)
for l in list:
    print(l)

