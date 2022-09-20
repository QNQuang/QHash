import hashlib
import crypt

#Ham hash
def encodeValue(str1, typeNum):
    if typeNum=="1":
        result = hashlib.md5(str1.encode()).hexdigest()
    elif typeNum=="2":
        result = hashlib.sha1(str1.encode()).hexdigest()
    elif typeNum=="3":
        result = hashlib.sha256(str1.encode()).hexdigest()
    elif typeNum=="4":
        result = hashlib.sha512(str1.encode()).hexdigest()
        
    print(result)
    
#Ham crack hash    
def decodeValue(str1, valueHash, typeNum):  
    if typeNum=="1":
        check = hashlib.md5(str1.encode()).hexdigest()
    elif typeNum=="2":
        check = hashlib.sha1(str1.encode()).hexdigest()
    elif typeNum=="3":
        check = hashlib.sha256(str1.encode()).hexdigest()
    elif typeNum=="4":
        check = hashlib.sha512(str1.encode()).hexdigest()

    if check == valueHash:
        print(f"{str1}: is correct password")
    else:
        print("No")

#Ham menu        
def selHash(typeHash, typeNum):
    print("")
    print("-------------")
    print(typeHash)
    print("1. Hash")
    print("2. Crack Hash")
    print("Select:", end="")
    select2 = str(input())
    #Hash
    if select2=="1":
        print("-------------")
        print("1. One value")
        print("2. Many values")
        print("Select:", end="")
        select3 = str(input()) 
        #Encode mot gia tri
        if select3=="1":
            print("Input value: ", end="")
            value1 = str(input())
            print("")
            encodeValue(value1, typeNum)
        #Encode nhieu gia tri
        else:
            value2 = []
            print("Input file: ", end="")
            inFile = str(input())
            f = open(inFile, "r")
            listStr = f.read().splitlines()
            
            print("")
            for i in range(len(listStr)):
                encodeValue(listStr[i], typeNum)
    #Crack hash       
    else:
        print(f"{typeHash} value: ", end="")
        valueHash = str(input())
        
        print("Input file: ", end="")
        inFile = str(input())
        f = open(inFile, "r")
        listStr = f.read().splitlines()

        print("")
        for i in range(len(listStr)):
            decodeValue(listStr[i], valueHash, typeNum)

#===========================================================

# Main
print("")
print("-------------")
print("HASH")
print("1. MD5")
print("2. SHA1")
print("3. SHA256")
print("4. SHA512")
print("-------------")
print("HASH with SALT")
print("5. MD5")
print("6. SHA1")
print("7. SHA256")
print("8. SHA512")
print("Select:", end="")
select = str(input())

if select=="1":
    typeHash="MD5"
    typeNum="1"
    selHash(typeHash, typeNum)
elif select=="2":
    typeHash="SHA1"
    typeNum="2"
    selHash(typeHash, typeNum)
elif select=="3":
    typeHash="SHA256"
    typeNum="3"
    selHash(typeHash, typeNum)
elif select=="4":
    typeHash="SHA512"
    typeNum="4"
    selHash(typeHash, typeNum)

