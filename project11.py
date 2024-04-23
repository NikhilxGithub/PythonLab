def papersizes(i,n,l,b):
    if n !=0:
        print(f'A{i}:L={int(l)}B={int(b)}')
        newb=l/2
        newl=b
        n-=1
        i+=1
        papersizes(i,n,newl,newb)

papersizes(0,7,1189,841)