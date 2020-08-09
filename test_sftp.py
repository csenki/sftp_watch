#! python
import sys
import sftp_lister
import email_sender
from configobj import ConfigObj

def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 



exit(0)
if len(sys.argv) < 2:
    print('First argument the config file need')
    exit(1)
conf_file_cmd=sys.argv[1]
try:
    config=ConfigObj(conf_file_cmd)
except :
    print("First argument the config file")
    if sys.argv[1] != "" :
        print('Cant open ',sys.argv[1])
    raise


lst=sftp_lister.sftp_file_list()
#Read config variables
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

try:
    res=lst.list_dir()
except:
    print("Cant list directory")
    raise
    


#Read old list file
old_list=[]
with open(config.get('old_list_file'), 'r') as filehandle:
    filecontents = filehandle.readlines()
    for line in filecontents:
        # remove linebreak which is the last character of the string
        current_place = line[:-1]

        # add item to the list
        old_list.append(current_place)

#Compare old and new
diff=Diff(res,old_list)


if len(diff)>0 :
    print('was change')
    es=email_sender.email_sender()
    es.email_to="cstt@opten.hu"
    es.email_from="cstt@opten.hu"
    es.email_smtp="mail.opten.hu"
    es.email_subj="Helló"
    es.send_email()
    #saving changes to list
    with open(config.get('old_list_file'), 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in res)
else:
    print('no change')

