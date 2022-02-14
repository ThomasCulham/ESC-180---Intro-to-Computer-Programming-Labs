# Question 2 and 3

def sumOfCubes(n):
    ans=0
    for i in range(1, n+1):
        x=1
        for j in range(3):
            x*=i
        ans+=x
    return ans

def check_sum(n):
    ans=0
    for i in range(1, n+1):
        ans+=i
    ans*=ans
    return ans==sumOfCubes(n)

def check_sums_up_to_n(n):
    ans=True
    for i in range(1,n+1):
        ans*=check_sum(i)
    return ans==1

def calcPi(n):
    ans=0
    for i in range(n+1):
        pow=1
        for j in range (i):
            pow*=-1
        ans+=pow/((2*i)+1)
    return ans*4

if __name__ == '__main__':
    print (sumOfCubes(1))
    print(check_sum(3))
    print(check_sums_up_to_n(5))
    print(calcPi(100))