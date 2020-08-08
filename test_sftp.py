#! python
import sys
import sftp_lister
from configobj import ConfigObj

def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 

conf_file_cmd=sys.argv[1]
config=ConfigObj(conf_file_cmd)

lst=sftp_lister.sftp_file_list()
if config.get('hostname')!="" :
    lst.hostname=config.get('hostname')
if config.get('password')!="" :
    lst.password=config.get('password')
if config.get('user')!="" :    
    lst.userName=config.get('user')
if config.get('remote_dir')!="" :    
    lst.remote_dir=config.get('remote_dir')
if config.get('port')!="" :        
    lst.Port=config.get('port')
res=lst.list_dir()
#for x in res:
#   print(x)
#with open('listfile.txt', 'w') as filehandle:
#    filehandle.writelines("%s\n" % place for place in res)
old_list=[]
with open('listfile.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()
    for line in filecontents:
        # remove linebreak which is the last character of the string
        current_place = line[:-1]

        # add item to the list
        old_list.append(current_place)
print(Diff(res,old_list))