
from numpy import *





#Problem 1:

def  print_matrix(M_lol):
    print(array(M_lol))



#Problem 2:

def get_lead_ind(row):
    for i in range(len(row)):
        if(row[i]!=0):
            return i
    return len(row)



#Problem 3:

def get_row_to_swap(M, start_i):
    ind=get_lead_ind(M[start_i])
    ans=start_i
    for i in range(start_i, len(M)):
        if(get_lead_ind(M[i])<ind):
            ans=i
    return ans



#Problem 4:

def add_rows_coefs(r1, c1, r2, c2):
    ans=[0]*len(r1)
    for i in range(len(r1)):
        ans[i]=(r1[i]*c1)+(r2[i]*c2)
    return ans



#Problem 5:

def eliminate(M, row_to_sub, best_lead_ind):
    n=M[row_to_sub][best_lead_ind]
    for i in range(row_to_sub+1,len(M)):
        c=M[i][best_lead_ind]/n
        for j in range(len(M[i])):
            M[i][j]=M[i][j]-c*M[row_to_sub][j]



#Problem 6:

def forward_step(M):
    for i in range(len(M)):
        s=get_row_to_swap(M,i)
        if(i!=s):
            c=M[i].copy()
            M[i]=M[s]
            M[s]=c

    for i in range(len(M)):
        l=get_lead_ind(M[i])
        eliminate(M,i,l)



#Problem 7:

def backward_step(M):
    for i in range(1,len(M)):
        l=get_lead_ind(M[i])
        v=M[i][l]
        for j in range(0,i):
            c=-M[j][l]/v
            M[j]=add_rows_coefs(M[j],1,M[i],c)
    print_matrix(M)
    print()
    for i in range(len(M)):
        v=M[i][get_lead_ind(M[i])]
        for j in range(len(M[i])):
            M[i][j]=M[i][j]/v




#Problem 8:

def solve(M,b):
    for i in range(len(M)):
        M[i].append(b[i])
    print(M)
    forward_step(M)
    backward_step(M)
    print(M)
    print()
    ans=[0]*len(b)
    for i in range(len(b)):
        ans[i]=M[i][-1]
    return ans







if __name__ == '__main__':
    M = array([[1.,-2.,3.,22.],[3.,10.,1.,314.],[1.,5.,3.,92.]])
    print_matrix(M)
    print()
    #print(get_lead_ind(M[1]))
    #print(get_row_to_swap(M,0))
    #print(add_rows_coefs(M[0],1,M[2],1))
    #eliminate(M,0,0)
    #print_matrix(M)
    forward_step(M)
    print_matrix(M)
    print()
    backward_step(M)
    print_matrix(M)
    print()
    print("-----------------------------------------------------------------------")
    print()




    M = array([[1,-2,3],[3,10,1],[1,5,3]])
    x = array([105,10,-12])
    b = dot(M,x)
    M=M.tolist()
    b=b.tolist()
    print(solve(M,b))







