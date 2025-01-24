a = "aaaaa"
l1 = [0]*256
for i in range(len(a)):
    l1[ord(a[i])]+=1
for i in range(256):
    if l1[i]>0:
        print(chr(i),l1[i])



