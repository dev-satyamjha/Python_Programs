def factors(n):
    factor = []
    for i in range(1, n+1):
        if n%i==0:
            factor.append(i)
    return factor
num = int(input("Enter number: "))
print("Factors are : ", factors(num))
    
