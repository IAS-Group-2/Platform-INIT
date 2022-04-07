from storage_manager import config
import os

def getRemoteFileList(DIRECTORY):
    """
    Get a list of files in the remote directory
    """
    command = "chmod +x storage_manager/copydir.exp"
    os.system(command)
    os.system("ssh "+config.STORAGE_VM_NAME+"@"+config.STORAGE_VM_IP+" ls -l "+ DIRECTORY)

def pullFile(TARGET_IP,TARGET_NAME,TARGET_PATH,SOURCE_PATH="./"):
    """
    Copy a file from the remote directory to the local directory
    """
    TARGET_PATH = "/home/"+TARGET_NAME+"/"+TARGET_PATH
    command = "chmod +x storage_manager/copydir.exp"
    os.system(command)
    command = "./copydir.exp "+TARGET_NAME+" "+TARGET_IP+" "+TARGET_PATH+" "+SOURCE_PATH+" "+config.STORAGE_VM_PASSWORD
    os.system(command)

def pullDirecory(TARGET_IP,TARGET_NAME,TARGET_PATH,SOURCE_PATH="./"):
    """
    Copy a directory from the remote directory to the local directory
    """
    TARGET_PATH = "/home/"+TARGET_NAME+"/"+TARGET_PATH
    command = "chmod +x storage_manager/copydir.exp"
    os.system(command)
    command = "./storage_manager/copydir.exp "+TARGET_NAME+" "+TARGET_IP+" "+TARGET_PATH+" "+SOURCE_PATH+" "+config.STORAGE_VM_PASSWORD
    os.system(command)

def push(SOURCE_PATH,TARGET_PATH,TARGET_IP=config.STORAGE_VM_IP,TARGET_NAME=config.STORAGE_VM_NAME):
    """
    Copy a directory from the remote directory to the local directory
    """
    TARGET_PATH = "/home/"+TARGET_NAME+"/"+TARGET_PATH
    # command = "scp -r "+TARGET_NAME+"@"+TARGET_IP+":"+TARGET_PATH+" "+SOURCE_PATH
    # os.system(command)
    #make file copydir excutable
    command = "chmod +x storage_manager/push.exp"
    os.system(command)
    command = "./storage_manager/push.exp "+TARGET_NAME+" "+TARGET_IP+" "+SOURCE_PATH+" "+TARGET_PATH+" "+config.STORAGE_VM_PASSWORD
    os.system(command)


# if __name__ == "__main__":
    pass
    # getRemoteFileList("storage_unit/non_essentials/applications")
    # push(config.STORAGE_VM_IP, config.STORAGE_VM_NAME, "application_68.zip", "storage_unit/non_essentials/applications")
        
    # pullFile(config.STORAGE_VM_IP,config.STORAGE_VM_NAME,"storage_unit/non_essentials/models/model_39.zip")
