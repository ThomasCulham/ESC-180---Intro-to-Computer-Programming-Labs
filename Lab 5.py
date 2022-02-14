 #Question 1:

def list1_starts_with_list2(list1, list2):
    if(len(list1)>len(list2)):
        return False
    for i in range(len(list1)):
        if(list1[i]!=list2[i]):
            return False
    return True



 #Question 2:

def match_pattern(list1, list2):

    for i in range(len(list1)-1):
        for j in range(len(list2)-1):
            if(list1[i]==list2[j] and list1[i+1]==list2[j+1]):
                return True

    return False





 #Question 3:

def repeats(L):
    L.sort()
    for i in range(len(L)-1):
        if(L[i]==L[i+1]):
            return True
    return False




 #Question 4:

 # a)

def print_matrix_dim(M):
    for i in range(len(M)):
        print(M[i])



 # b)

def mult_M_v(M, V):
    ans = M
    for i in range(len(M)):
        for j in range(len(M[0])):
            ans[i][j]=V[j]*M[i][j]
    return ans





if __name__ == '__main__':
    L=[1,2,3,4,5,6]
    M=[1,2,3,4]
    N=[2,1,3,4]
    O=[7,8,9,0]
    P=[1,1,3,4,5,6,7,8,9,0]
    T=[[1,2,3,4],
       [2,1,3,4],
       [7,8,9,0]]

    V=[1,20,3,4]
    print(list1_starts_with_list2(L,M)) #False
    print(list1_starts_with_list2(M,L)) #True
    print(list1_starts_with_list2(M,N)) #False
    print("")
    print(match_pattern(M,N)) #True
    print(match_pattern(O,L)) #False
    print(match_pattern(P,O)) #True
    print("")
    print(repeats(O)) #False
    print(repeats(P)) #True
    print("")
    print_matrix_dim(T)
    print("")
    print_matrix_dim(mult_M_v(T,V))




