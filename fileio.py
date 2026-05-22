#f=open("io.py","r")
with open("io.py") as f:
    data=f.readline()
    d=chr(data)
    print(d)

f.close()
f2=open("Writingsample.txt","w")
f2.write(bin(ascii(set(data))))
f2.close()
