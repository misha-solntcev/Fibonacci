def fib(N):
    F = []
    f_0 = 0
    f_1 = 1
    f_2 = f_0 + f_1
    f_3 = f_2 + f_1
    F.append(f_0)
    F.append(f_1)
    F.append(f_2)
    F.append(f_3)
    for n in range(N-3):
        f_n = f_2 + f_3
        f_2 = f_3
        f_3 = f_n
        F.append(f_n)
    print(F)
    
if __name__ == '__main__':
    fib(20)
   
