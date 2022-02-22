def fib(N):
    F = []
    f_0 = 0
    F.append(f_0)
    f_1 = 1
    F.append(f_1)
    f_2 = 1
    F.append(f_2)
    for i in range(N):
        f_n = f_1 + f_2
        f_1 = f_2
        f_2 = f_n
        F.append(f_n)
    print(F)
    
if __name__ == '__main__':
    fib(30)
   
