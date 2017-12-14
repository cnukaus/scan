# -*-  coding: utf-8 -*-
#https://stackoverflow.com/questions/7646520/is-this-an-appropriate-use-of-pythons-built-in-hash-function
import os
import sys
import Tkinter as tk#GUI
import win32api
import logging
import shutil

'''import subprocess
import collections
import pandas as pd
import matplotlib
import seaborn as sns
import re
'''

rootdir = sys.argv[1]
#ExtractDir = sys.argv[2]
print rootdir

all_filename=[]
all_fileext=[]
all_filewords=[]

def scan2():
    for folder, subs, files in os.walk(rootdir):

            for filename in files:
                      print filename

                      a=open(os.path.join(folder, filename),"r"); b=a.read(); rows=b.split('\n')
                      p=set([])

                      for x in rows:
                       #match = x.split('\')[-1]
                       #x[x.rindex('/')+1:]#re.findall(r'[^/]+$',x)

                       for y in match:
                         print (y)
                         p.add(y)
                         all_fileext.append(y)
def scan2_show():
    counter=collections.Counter(all_fileext)


    df=pd.DataFrame([counter.values(),counter.keys()])
    df2=df.transpose()
    df2.columns=['cnt','fname']
    df3=df2.sort_values(['cnt'],ascending=[True])
    print df3
    df2.head()
    #ax = sns.barplot(x="fname", y="cnt", data=df3)
    #sns.plt.show()




def scan(dir_name="D:\\",whitelist=[],lengthofFuzzy=0):
    outputList=[]
    for drive in dir_name:
        for itemParent in os.listdir(drive):
          #print itemParent
          try:
              from exceptions import WindowsError
              if os.path.isdir(os.path.join(drive,itemParent)):
                for item1 in os.listdir(os.path.join(drive,itemParent)):
                 #print (drive,itemParent,item1)
                 if any(item1.lower() in word for word in whitelist) and len(item1)>lengthofFuzzy:
                        #WindowsError: [Error 5] Access is denied: 'D:\\$RECYCLE.BIN\\S-1-5-21-1842349746-1869193258-3302827637-1002/*.*' 
                            print ("MATCHED directory name"+item1)
                            outputList.append(os.path.join(drive,itemParent, item1))
                            
                 if os.path.isdir(os.path.join(drive,itemParent,item1)):
        
                  for item in os.listdir(os.path.join(drive,itemParent,item1)) :  # would have exception because of file fed into listdir(): WindowsError: [Error 267] The directory name is invalid: 'D:\\GoodDNS_record.txt/*.*'
                      if os.path.isfile(os.path.join(drive,itemParent,item1, item)) and item in whitelist:
                        #WindowsError: [Error 5] Access is denied: 'D:\\$RECYCLE.BIN\\S-1-5-21-1842349746-1869193258-3302827637-1002/*.*' 
                            print ("MATCHED l2"+item)
                            outputList.append(os.path.join(drive,itemParent,item1, item))
              elif itemParent.lower() in whitelist:
                                   outputList.append(os.path.join(drive,itemParent))
                                   print ("MATCHED root")
          except WindowsError, e:
                      #logging.warning(os.path.isdir(os.path.join(drive,itemParent)))
                      if sys.platform.startswith('win'):
                          if isinstance(e, WindowsError) and e.winerror == 267:
                              logging.warning("custom err1")#raise InvalidFile, ('uses Windows special name (%s)' % e)
                      #pass#raise
    return outputList  


# https://stackoverflow.com/questions/1210118/handling-windows-specific-exceptions-in-platform-independent-way
def _dir_list(self, dir_name, whitelist):
    outputList = []
    for root, dirs, files in os.walk(dir_name):
        dirs[:] = [d for d in dirs if is_good(d)] #prevent recursing sub-folders
        for f in files:
            if os.path.splitext(f)[1] in whitelist:  #ONLY need surfix as whitelist
                outputList.append(os.path.join(root, f))
            else:
                self._email_to_("ignore")
    return outputList


def list_drive():

    print "All drives listed"
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives


def nextChip(operator="Operator1"):
  var=raw_input("ok").decode(sys.stdin.encoding)
  #请输入硬件编号 Enter Chip sequence".encode('gb2312'))
  return operator,var

class HelloWorld(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="What's your input?", command=self.on_button)
        self.button.pack()
        self.entry.pack()

    def on_button(self):
        answer = self.entry.get()
        if answer == "a":
            print("Hello World")
        elif answer == "b":
            print("Hello World 2")
        elif answer == "c":
            root.destroy()

def savetodisk(listname,diskid="disk param1",destname="d:\\tmp\\list.txt"):
    thefile=open(destname,'w')
    for item in listname:
      thefile.write("%s\n" % item)

def saveoutput(outputpath=sys.path[0],listname=[]):

    from collections import defaultdict
    
    D = defaultdict(list)

    listname_lastsection=set([x.split("\\")[-1] for x in listname])
    for i,item in enumerate(listname_lastsection):
      D[item].append(i)
    D = {k:v for k,v in D.items() if len(v)>1}

    logging.warning("Saving"+str(listname))
    savetodisk(listname)
    cnt=-1
    for fileitem in listname:
         
        cnt=cnt+1
        insert_unique=""
        try:
          from exceptions import WindowsError
              

          # don't write self
          if fileitem.encode('string-escape') != os.path.join(outputpath,fileitem.split("\\")[-1]).encode('string-escape'):
             if fileitem in D:
                insert_unique=string.replace(fileitem,"\\","_")

             shutil.copyfile(fileitem.encode('string-escape'),os.path.join(outputpath,insert_unique+fileitem.split("\\")[-1]).encode('string-escape'))
        except IOError, e:
                          
                                  logging.warning(e)#raise 
        except:
          print "Unexpected error:", sys.exc_info()[0]
          raise       




def main():
  runlist=["we.txt",r"bi.txt","Filelist.xml",r"pizza.jpg","54.pdf"]
  with open(os.path.join(sys.path[0], "words.lst")) as f:
    listadd=f.readlines()
    
  with open(os.path.join(sys.path[0], "candidate.lst")) as f:
    chunk=f.read(5)
  #listadd = [x.strip() for x in listadd]
  runlist.extend(listadd) #
  print runlist

  saveoutput("d:\\tmp",scan(["c:\\","d:\\"],runlist)) 
  print os.path.splitext("c:\\a.txt")
  print "Successful**"

main() #要解决结果文件重名,ID
#root = HelloWorld()
#root.mainloop()

'''
check meaning of r here
>>> print os.path.splitext("c:\1.txt")
('c:\x01', '.txt')
>>> print os.path.splitext(r"c:\1.txt")
('c:\\1', '.txt')

try:
    from exceptions import WindowsError
except ImportError:
    class WindowsError(OSError): pass
    '''



