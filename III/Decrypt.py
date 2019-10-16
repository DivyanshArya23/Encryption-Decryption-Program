#Program To Decrypt a File:
#-------------------------------------------------------------
from os import system
from time import sleep

print "Loading program into Memory",
for i in range(15):
        print '.',
        sleep(0.15)

print "\nReading Encrypted File",
for i in range(15):
        print '.',
        sleep(0.02)

print "\nReading Support File",
for i in range(15):
        print '.',
        sleep(0.02)

print "\nDecrypting Data",
for i in range(10):
        print '.',
        sleep(0.5)
#-------------------------------------------------------------

#function to convert binary into decimal
def deci(n):
    st=str(n)
    st=st[::-1]
    num=0
    for i in range(len(st)):
        num+=int(st[i])*(2**i)
    return num

#loading file into memory
fr=open('Encrypted.txt','r')
s1=fr.read()

fr.close()
info=open('Support.txt','r')
INFO=info.read()
info.close()
fw=open('Decrypted.txt','w')

#---------------------------
SD=[]
for i in INFO:
    if i!=',':
        SD.append(i)

SUM=0
for i in SD:
    a=SUM
    SUM+=int(i)
    b=SUM
    fw.write(chr(int(deci(s1[a:b]))))
fw.close()
    
print "CODE DECRYPTED"
sleep(3)
quit()
