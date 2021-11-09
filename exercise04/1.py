with open("1.txt","r") as f:
    data=f.readlines()
    for i in range(len(data)):
        data[i]=str(data[i]).replace("\n","")
f.close()
with open("3.txt","w") as f:
    for i in range(len(data)):
        f.writelines(str(bin(int(data[i],16))[2:])+"\n")





f.close()

