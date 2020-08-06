import os

for folderName, subFolders, fileNames in os.walk(str(os.getcwd())):
    print("The folder is " + folderName)
    print("The subfolders in " + folderName + " are: " + str(subFolders))
    print("The filenames in " + folderName + " are: " + str(fileNames))
    print()

    for subfolder in subFolders:
        if "hello" in subfolder:
            print("subfolder: " + subfolder)
