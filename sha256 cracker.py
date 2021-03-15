import os
import hashlib
os.system("clear")
print("hash cracker kimeerteam")
n=input("hash:").encode()
print("""
[1] a,A,b,B,c,C,... 
[2] numbers
[3] a,A,b,B,c,C,... with numbers
[4] a,A,b,B,c,C,... with symbols
[5] a,A,b,B,c,C,... with numbers and symbols
[6] Your word list :)
""")
loop=True
a=input(" Number Of Option:")
if a=="1":
    lib=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
if a=="2":
    lib=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
if a=="3":
    lib=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
if a=="4":
    lib=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ', '!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
if a=="5":
    lib=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ', '!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
if a=="6":
    file=open(input("Your file name:"),"r")
    lib=file.read()
    lib=lib.split("\n")
    loop=False
i=1
while True:
    build="import hashlib,sys\nimport base64\n"
    build+="p="+str(n)+"\n"
    build+="lib="+str(lib)+"\n"
    build+="ub=1\n"
    tab=""
    for j in range(i):
        build+=tab+"for a"+str(j)+" in lib:\n"
        tab+="   "
    out=""
    for k in range(i):
        out+="a"+str(k)+"+"
    build+=tab+"if hashlib.sha256(("+out[:len(out)-1]+").encode()).hexdigest()==p.decode():\n"
    prog=tab+"b=str(ub)+' of '+str(len(lib)**"+str(i)+")\n"+tab+"sys.stdout.write('\b'*len(b))\n"+tab+"sys.stdout.flush()\n"+tab+"sys.stdout.write(b)\n"+tab+"ub+=1"
    tab+="   "
    build+=tab+"sys.stdout.write('\b'*len(b))\n"+tab+"print('Found--> '+"+out[:len(out)-1]+"+len(b)*' '"+")\n"+tab+"exit()\n"
    build+=prog
    print(i)
    exec(build)
    print()
    i+=1
    if loop==False:
        break
print("NOT FOUND!")
