import os
file_namelist = os.listdir(".")
for name in sorted([name for name in file_namelist if name.endswith('jpg')], 
                            key=lambda x:int(x[:-4])):
    print name