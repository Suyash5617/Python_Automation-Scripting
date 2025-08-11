import psutil
import os
import time

def CreateLog(FolderName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = time.replace(" "," ")
    timestamp = time.replace(":","_")
    timestamp = time.replace("/","_")

    FileNmae = os.path.join(FolderName, "Marvellous%s.log" %(timestamp))

    fobj = open(FileNmae, "w")

    border = "_"*80
    fobj.write(border)
    fobj.write("\n\t\tMarvellous Infosystem Process Log\n")
    fobj.write("\n\t\tLog file is created at : "+time.ctime()+"\n")
    fobj.write(border)

   

def ProcessScan():
    
    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(info)
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess
def main():
    CreateLog("MarvellousProcess")
    
if __name__=="__main__":
    main()



