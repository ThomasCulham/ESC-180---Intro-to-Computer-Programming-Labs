




# Question 2:

def dict_to_str(d):
    k=[]
    v=[]
    for i in d.keys():
        k.append(str(i))
        v.append(str(d[i]))
    ans=""
    for i in range(len(k)):
        ans += k[i] + ", " + v[i] + "\n"
    return ans






# Question 3:

def dict_to_str_sorted(d):
    k=[]
    v=[]
    for i in d.keys():
        k.append(i)
        v.append(d[i])


    while(i<len(k)-1):
        if(k[i]>k[i+1]):
            mem=k[i]
            k[i]=k[i+1]
            k[i+1]=mem
            mem=v[i]
            v[i]=k[i+1]
            v[i+1]=mem
            i=(-1)
        i+=1



    ans={}

    for i in range(len(k)):
        ans[k[i]]=v[i]
    return dict_to_str(ans)





#Question 4a) !!!!!!!do others later. It will help with project 3!!!!!!!!

def to_dictionary(words):
    word=words.readlines()
    w=[]
    v=[[]]

    for i in range(len(word)):
        last=0
        vv=[]
        str=""
        word[i]=word[i].rstrip()
        v.append([])
        for j in range(len(word[i])):
            if(word[i][j]==" " and word[i][j-1]==" "):
                w.append(word[i][1:j-2])
                last=j+1
            if(word[i][j]==" " and word[i][j-1]!=" "and word[i][j+1]!=" "):
                v[i].append(word[i][last:j-1])
    ans={}

    for i in range(len(w)):
        ans[w[i]]=v[i]
    return ans



















if __name__ == '__main__':

    #Question 1:

    f = open("test.txt")
    lines=f.readlines()
    for i in lines:
        i=i.rstrip()
        if(i.lower().count('lol')>0):
            print(i)
    f.close()



    d={15:2, 7:4, 6:6, 2:8}
    print(dict_to_str(d))
    print(dict_to_str_sorted(d))


    words=open("words.txt")

    dictionary=to_dictionary(words)
    print(dict_to_str(dictionary))









