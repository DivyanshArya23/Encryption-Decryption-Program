#Program to Encrypt a file:
print "1.Encrypt\n2.View Code\n--------------------------------------------"
choice=input("Enter Your Choice:")
if choice==1:
    fr=open("Code.txt","r")
    fw=open("Encrypted.txt","w")
    s=fr.read()
    n=0
    for i in s:
        r=n%255
        a=chr(ord(i)+r)
        fw.write(a)
        n+=1
    fr.close()
    fw.close()
    print "Code Encrypted."
elif choice==2:
    password=""
    password=raw_input("Enter Password:")
    if password=="15047":
        print'''---------------------\nCODE:\n
fr=open("Code.txt","r")
fw=open("Encrypted.txt","w")
s=fr.read()
n=0
for i in s:
    r=n%255
    a=chr(ord(i)+r)
    fw.write(a)
    n+=1
fr.close()
fw.close()
print "Code Encrypted."
'''
    else:
        print "Invalid Password"
    input()
