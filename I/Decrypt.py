#Program to Decrypt a file:
print "1.Decrypt\n2.View Code\n--------------------------------------------"
choice=input("Enter Your Choice:")
if choice==1:
    fr=open("Encrypted.txt","r")
    fw=open("Decrypted.txt","w")
    s=fr.read()
    n=0
    for i in s:
        r=n%255
        a=chr(ord(i)-r)
        fw.write(a)
        n+=1
    fr.close()
    fw.close()
    print "Code Decrypted."
elif choice==2:
    password=""
    password=raw_input("Enter Password:")
    if password=="15047":
        print'''---------------------\nCODE:\n
fr=open("Code.txt","r")
fw=open("Decrypted.txt","w")
s=fr.read()
n=0
for i in s:
    r=n%255
    a=chr(ord(i)-r)
    fw.write(a)
    n+=1
fr.close()
fw.close()
print "Code Decrypted."
'''
    else:
        print "Invalid Password"
    input()
