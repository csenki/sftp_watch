#! python
import sys
import pysftp
import stat
import warnings
import re


warnings.filterwarnings("ignore", category=UserWarning)
class sftp_file_list:
   hostname="127.0.0.1"
   userName=""
   Port="22"
   password=""
   private_key=""
   private_key_pass=""
   remote_dir="/"
   include_regexp="*"
   
   def list_dir(self):
      cnopts = pysftp.CnOpts()
      cnopts.hostkeys = None
      sftp = pysftp.Connection(host=self.hostname, username=self.userName, password=self.password,cnopts=cnopts)
      if self.remote_dir != "":
         sftp.chdir(self.remote_dir)
      directory_structure = sftp.listdir_attr()
      filelist=[]
      for attr in directory_structure:
          re_return=0
          try:
              re_return=re.search(".*$",attr.filename)
          except :
              print("Bad regexp!!!!")
              raise
          if (not stat.S_ISDIR(attr.st_mode)) and re_return :
              filelist.append(attr.filename)
      sftp.close()
      print('ready')
      return filelist
