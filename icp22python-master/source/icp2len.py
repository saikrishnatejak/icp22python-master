with open("C:/Users/vmred/Documents/text/maa.txt","r") as f:
    for line in f:
     data1 =line.strip()
     data=line.strip().split()
    print(data1,len(data))


