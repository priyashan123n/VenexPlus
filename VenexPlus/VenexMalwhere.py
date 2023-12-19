#importing libraryis
import subprocess as shell
import os
from colorama import Fore, Style, init
from pathlib import Path
from lib.venexEncrypt import Vencrypt,VencryptF

init(autoreset=True)





#underdarkMod
class underdark():

    def listfile_dir(command="c:/ -f -d"):

        command = command.split(" ")
        flags = command[1:].__str__()
        #to do fiter ls by control panel

        p = Path(command[0]) # using pathlib lybrary
        output = ""
        for dir_file in p.iterdir():
            
            if "-f" in flags and "-d" in flags:
                
                output +=  "--Files & Derectory--> " + str(dir_file)[len(command[0 - 1]):] + "\n\n"
                #to do in cotrol print("")

            elif "-f" in flags:
                if dir_file.is_file():
                    output += "--------Files--------> " + str(dir_file)[len(command[0 - 1]):] + "\n\n"
                    #to do in cotrol print("")

            elif "-d" in flags:
                if dir_file.is_dir():
                    output += "------Derectory------> " + str(dir_file)[len(command[0 - 1]):] + "\n\n"
                    #to do in cotrol print("")
            
            else:
                output = "invalid command syntax Error \\ / *\n\n"
                break
        
        return output[:-2]
    
    def readfile(fileName):
        p = Path(fileName)
        try:
            with p.open() as f:
                return f.read()
        except:
            return "This file is using another program"
        
    def file_size(fileName):
        p = Path(fileName)
        if not p.is_dir():
            size = p.stat().st_size
            return str((size/1024)/1024) + " Mb"
        else:
            return  Fore.RED + "Sory we are under the cunstruction we cann't calculate derectory size is this time but comming zoon. are you programmer or can you add it in to venexplus go to htttps://github.com/priyashan123n/venexPlus/venexPlusv1.0_code and edite venexPlusmal.py file line 53 under else: statement thank you"
    

    def isfilein(fileName):
        p = Path(fileName).exists()
        if p == True:
            return f"{fileName} is in this derectory"
        else:
            return f"{fileName} is not this derectory : find Another derectory"



    def encrypt(victim):

        victim = victim.split(" ")
        victimFileOrText = victim[0]
        flags = [1] or "-t"
        #to do filter encrypt by c panel

        if flags == "-f":
            key = VencryptF.encrypt(victimFileOrText)
            return key
        else:
            key = Vencrypt.genarateKey()
            obj = Vencrypt(key)
            encrypted = obj.encrypt(victimFileOrText)
            return key," ",encrypted
        

    def decrypt(key,victim):

        victim = victim.split(" ")
        victimFileOrText = victim[0]
        flags = [1] or "-t"
        #to do filter encrypt by c panel

        if flags == "-f":
            VencryptF.decrypt(key,victimFileOrText)
        else:
            obj = Vencrypt(key)
            decrypted = obj.decrypt(victimFileOrText)
            return decrypted
        


# key = Vencrypt.genarateKey("L")



# file = open("d.png","rb").read()
# file = str(file)

# print(file)

# encrypted = obj.encrypt(file)
# encrypted = encrypted.encode()

# vict = open("d.png","wb")
# vict.write(encrypted)



# file = open("d.png","r").read()

# decrypted = obj.decrypt(file)
# decrypted = decrypted.encode()

# wfile = open("d.png","wb")
# wfile.write(decrypted)


#end underdark clas

# x = underdark.readfile_dir("c:/ -f") to do ls command
# print(x)
        
# f = "C:\\Users\\xenoneS\\Desktop\\hacker101.txt"
# x = underdark.readfile(f)  to do read command
# print(x)

# x = underdark.file_size("C:\\Users\\xenoneS\\Desktop\\Programs") #to do size command
# print(x)

# x = underdark.isfilein("vednex.py") #to do isfilein command
# print(x)
    
# x =underdark.lastmodify("c:\\Users\\xenoneS\\Desktop\\venex_code\\a")
# print(x)

