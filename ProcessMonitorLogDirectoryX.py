import psutil
import os
import time

def CreateLog(FolderName,Data):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = timestamp.ctime()
    timestamp = timestamp.replace(" "," ")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileNmae = os.path.join(FolderName, "Marvellous%s.log" %(timestamp))

    fobj = open(FileNmae, "w")

    border = "_"*80
    fobj.write(border)
    fobj.write("\n\t\tMarvellous Infosystem Process Log\n")
    fobj.write("\n\t\tLog file is created at : "+time.ctime()+"\n")
    fobj.write(border)

    for value in Data:
        fobj.write("%s \n" %value)

    fobj.write(border)

    fobj.close()    

   

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
    Arr = ProcessScan()
    CreateLog("MarvellousProcess", Arr)
    
if __name__=="__main__":
    main()



