
import math

#Question 1:

def sum_nums(L):
  s = 0
  for num in L:
    s += num

  return s


def count_evens(L):
  ans = 0
  for num in L:

      if num%2==0:
          ans += 1

  return ans



#Question 2:

def listToString(L):
    ans = "["
    for num in L[:-1]:
      ans = ans + str(num) + ", "
    return ans + str(L[len(L)-1]) + "]"



#Question 3:

def lists_are_the_same(L1, L2):
    if(len(L1)!=len(L2)):
        return False

    for i in range(0,len(L1)):
        if L1[i]!=L2[i]:
            return False
    return True



#Question 4:

def simplify_fraction(n, m):
    max=0
    factor=1
    if n<m :
        max=n+1
    else:
        max=m+1

    for i in range(2,max):
        if(n%i==0 and m%i==0):
            factor = i

    n/=factor
    m/=factor
    print(str(n)+"/"+str(m))



#Question 5:

def calcPi(n):
    ans=0
    for i in range(n+1):
        pow=1
        for j in range (i):
            pow*=-1
        ans+=pow/((2*i)+1)
    return ans*4



def sig_fig_pi(n):

    if(n==1):
        return 2

    step=1

    while(1==1):

        if( int((calcPi(step)*10**(n-1))) == int((math.pi*10**(n-1)))):
            return step
            break
        step+=1





#Question 6:

def Euclids(a,b):
    if(a<b):
        l=b
        s=a
    else:
        l=a
        s=b
    carry = l%s
    if(carry==0):
        return l
    else:
        return Euclids(s,carry)





if __name__ == '__main__':
    L=[1,2,3,4,5,6,7,8,10,200]
    S=[1,2,3]
    T=[1,2,3]
    V=[2,3,1]
    print(sum_nums(L))
    print(count_evens(L))
    print(listToString(L))
    print(lists_are_the_same(L,S))
    print(lists_are_the_same(S,T))
    print(lists_are_the_same(T,V))
    simplify_fraction(4,8)
    print(sig_fig_pi(3))
    print(sig_fig_pi(2))
    print(sig_fig_pi(1))
    print(Euclids(2322,654))






