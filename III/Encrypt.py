#Program To Encrypt a File:
#-------------------------------------------------------------
from os import system
from time import sleep

print "Loading program into Memory",
for i in range(15):
        print '.',
        sleep(0.15)

print "\nReading Code File",
for i in range(15):
        print '.',
        sleep(0.02)

print "\nEncrypting Data",
for i in range(10):
        print '.',
        sleep(0.5)
#-------------------------------------------------------------
#function to convert decimal into binary
def binary(n):
    sum=0
    rem=0
    t=1
    while n!=0:
        rem=n%2
        n/=2
        sum+=(t*rem)
        t*=10
    return sum

#loading files into memory
fr=open('Code.txt','r')
s1=fr.read()
fr.close()
fw=open('Encrypted.txt','w')
info=open('Support.txt','w')

for i in s1:
    bina=binary(ord(i))
    lenbin=len(str(bina))
    fw.write(str(bina))
    info.write(str(lenbin)+',')
info.close()
fw.close()
print "CODE ENCRYPTED"
sleep(3)
quit()
