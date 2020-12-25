"""Python File Organizer
This pyhton program will create a folder called 'FOLDERs' in your current directory(or spicified path) 
and move all the folders in you current directory(or spicified path) and then it will create folders
based on all different file extensions 
in that folder and move all the files in there respective extensions folders.
Author: Mohit Shandilya"""
#! usr/bin/env python3

#import modules
import os
import shutil

path = ""
if path == "":
    path = os.getcwd()

def folder_mover(path):
    """This will move all the already existing folders to a new folder
       called FOLDERs"""
    folderlist = []   
    listdir = os.listdir(path) # creates a list of all the files and folders in a particular path 
    #first make 'FOLDERs' folder if it doesn't exist
    try:
        os.mkdir("FOLDERs")
    except OSError as error:
        print(error)
    target = os.path.join(path,"FOLDERs")
    for items in listdir:
        if os.path.isdir(items):
            folderwithpath = os.path.join(path,items)
            try:
                shutil.move(folderwithpath,target)
            except OSError as error:
                print(error)
            folderlist.append(items)    
    #print ("FUNCTION folder_mover : {} folders were moved to a now created folder named : 'FOLDERs'".format(folderlist))
    print ("FUNCTION folder_mover : Total {} folders were moved to folder named: 'FOLDERs'.".format(len(folderlist)))
    return folderlist

def file_extension_checker(path):
    """returns a list of all file extensions present in current working 
       directory"""
    listdir = os.listdir(path) # creates a list of all the files and folders in a particular path   
    extension_list = []
    filewithpath = "" #to save complete file name with tha path
    extension = "" #to save just the extension of the file
    for file in listdir :
        filewithpath = os.path.join(path, file)
        if os.path.isfile(filewithpath):
            extension = os.path.splitext(filewithpath)[1][1:] #gets the extension without dot
            if extension not in extension_list and extension != "":
                extension_list.append(extension)
    #print ("FUNCTION file_extension_checker : {}".format(extension_list))
    #print ("FUNCTION file_extension_checker : above list is the output of this function")            
    return extension_list            
  
def folder_creator(path):
    """Creates different folders with names of the different extensions"""

    #create a list of all the file extensions available in the current folder
    extension_list = file_extension_checker(path)
    for items in extension_list:
        try:
            os.mkdir(items.upper() + "s")
        except OSError as error:
            print(error)
    #print ("FUNCTION folder_creator : {} folders created.".format(extension_list))
    print ("FUNCTION folder_creator : Total {} new folders were created.".format(len(extension_list)))
    return (extension_list)        

def files_mover(path):
    """will move the files based on their file existensions in the now created
       new folders based on file extensions"""
    listdir = os.listdir(path)   
    mydict = {}

    #create a list of all the file extensions available in the current folder
    extension_list = file_extension_checker(path)
    for extn in extension_list:
        target = os.path.join(path, extn.upper() + "s")
        for files in listdir:
            fileswithpath = os.path.join(path, files)
            extension = os.path.splitext(files)[1][1:] #gets the extension without dot
            if extension == extn:
                try:
                    shutil.move(fileswithpath,target)
                except OSError as error:
                    print(error)
                mydict[files] = target 
    #print ("FUNCTION files_mover : {} files were moved".format(mydict))
    print ("FUNCTION files_mover : Total {} files were created.".format(len(mydict)))
    return mydict

def report():
    pass

def main():
    #first lets move all the already existing folders to the FOLDERs folder
    folder_mover(path)
    folder_creator(path)
    files_mover(path)

if __name__ == "__main__":
    main()
    print("THE END")






