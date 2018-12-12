while(1):
    entrada = input()
    if not entrada:
        break
    i, j = map(int, entrada.split())
    maior = 0
    for n in range(i,j+1):
        cl=0
        while 1:
            cl+=1
            if n==1: break
            if n%2==0:
                n = n // 2
            else:
                n = 3 * n + 1
        if(cl>maior):
            maior = cl
    print(f"{i} {j} {maior}")