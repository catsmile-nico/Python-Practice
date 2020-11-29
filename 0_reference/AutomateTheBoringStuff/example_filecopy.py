import shutil, os

# copy file
shutil.copy(str((os.getcwd()) + "\\hello.txt"),str((os.getcwd()) + "\\newfolder\\hello.txt"))
shutil.copy(str((os.getcwd()) + "\\hello.txt"),str((os.getcwd()) + "\\newfolder\\hellohello.txt"))

# copy files and folders
shutil.copytree(str(os.getcwd()), str(os.getcwd()) + "\\newfolder_backup\\")

# move
os.makedirs(str((os.getcwd()) + "\\newfolder_backup2"))
shutil.move(str(os.getcwd()) + "\\newfolder_backup\\", str(os.getcwd()) + "\\newfolder_backup2\\")

# delete file permanently
os.unlink(str((os.getcwd()) + "\\newfolder_backup2\\newfolder_backup\\hello.txt"))

# delete folder permanently
# shutil.rmtree(str((os.getcwd()) + "\\newfolder_backup2"))
# os.rmdir(str((os.getcwd()) + "\\newfolder_backup2")) only can delete empty dir

import send2trash
# send to recycle bin isntead of permanent delete
send2trash.send2trash(str((os.getcwd()) + "\\newfolder_backup2"))
