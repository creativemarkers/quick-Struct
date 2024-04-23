import argparse
import os

def directoryChecker(folderPath)->str:
    if folderPath == None:
        print("No Directory given...defaulting to current Directory")
        userChose = False
        while userChose == False:
            userChoice = input("Type (Y/n) to continue...")
            userChoice.lower()
            if userChoice == 'y':
                return os.getcwd()
            elif userChoice == 'n':
                print("exiting...")
                exit()
            else:
                print("incorrect input")
    else:
        """
        check valid path
        """
        if os.path.exists(folderPath):
            print("Directory chosen:", folderPath)
            return folderPath
        else:
            print("Directory given not found")
            exit()

def checkForFileExtension(fileName:str):
    #writing my own algo for fun! this can be accomplished with a built in method
    for i, char in enumerate(fileName):
        if char == '.' and i != 0:
            #print(fileName[i:])
            return fileName[i:]
    return None
            
def scanFolderforExtensions(folderPath:str)->list:
    fileExtensions = set()
    with os.scandir(folderPath) as items:
        for item in items:
            fileExtension = checkForFileExtension(item.name)
            if fileExtension != None and fileExtension not in fileExtensions:
                fileExtensions.add(fileExtension)

    return fileExtensions

def main():

    """
    get file directory from command line
    warn user about what the command line is going to do, and this could break your programs/operating systems
    an arg for file extensions to ignore
    scan the directory for all present file extensions
    create a log of where everything was before
    create folders for appropriate files
    move items into said folders
    print report of the files moved
    """
    
    progName = "Fernando's Directory Organizer"
    parserDescrip = "Organizes Directories"
    parserEpilog = "Don't koof too hard"

    parser=argparse.ArgumentParser(prog=progName,description=parserDescrip, epilog=parserEpilog)

    parser.add_argument('-d','--directory',type=str, help="specificies directory, if not, program will default to using the directory command was used in")

    parser.add_argument('-t', '--test',action='store_true', help="test arg")
    
    args = parser.parse_args()

    print("flag:", args.test)
 
    workingDir = directoryChecker(args.directory)
    #print(workingDir)
    fileExtensions = scanFolderforExtensions(workingDir)
    print(fileExtensions)

if __name__ == "__main__":
    main()