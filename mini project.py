while(True):
    x=str(input())
    i=0
    j=0
    str1=""
    str2=""
    for i in range(0,len(x)):
        if(x[i]=="@"):
            break
        str1=str1+x[i]
    print("username:",(str1))
    for j in range(x.index("@"),len(x)):
        if(x[j] !="@"):
            str2=str2+x[j]
    print("Domain:",(str2.upper()))