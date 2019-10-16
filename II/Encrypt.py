#Program to encrypt a file:

#-----------------------------------------------------------------------
fr=open("Code.txt","r")
s=fr.read()
fr.close()
fw=open("Encrypted.txt","w")
fw.write(s)
fw.close()
#----------------------------------
def encrypt(level):
    fr=open("Encrypted.txt","r")
    s=fr.read()
    fr.close()
    fw=open("Encrypted.txt","w")
    n=0
    for i in s:
        r=n%255
        r*=level
        a=chr((ord(i)+r)%255)
        fw.write(a)
        n+=1
    
    fw.close()
#----------------------------------
print "1.Encrypt\n2.View Code\n--------------------------------------------"
choice=input("Enter Your Choice:")
if choice==1:
#----------------------------------
    level=input("Enter Level Of Encryption:")

    for z in range(level):
        encrypt(z)
        
    print "Code Encrypted."
#-----------------------------------------------------------------------
elif choice==2:
    password=""
    password=raw_input("Enter Password:")
    if password=="15047":
        print'''---------------------\nCODE:\n
#-----------------------------------------------------------------------
fr=open("Code.txt","r")
s=fr.read()
fr.close()
fw=open("Encrypted.txt","w")
fw.write(s)
fw.close()
#----------------------------------
def encrypt(level):
    fr=open("Encrypted.txt","r")
    s=fr.read()
    fr.close()
    fw=open("Encrypted.txt","w")
    n=0
    for i in s:
        r=n%255
        r*=level
        a=chr((ord(i)+r)%255)
        fw.write(a)
        n+=1
    
    fw.close()
#----------------------------------
print "1.Encrypt\n2.View Code\n--------------------------------------------"
choice=input("Enter Your Choice:")
if choice==1:
#----------------------------------
    level=input("Enter Level Of Encryption:")

    for z in range(level):
        encrypt(z)
        
    print "Code Encrypted."
#-----------------------------------------------------------------------
'''
    else:
        print "Invalid Password"
    input()
