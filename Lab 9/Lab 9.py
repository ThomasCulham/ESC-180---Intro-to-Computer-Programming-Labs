


























def word_counts(word,words):
    ans=0
    for w in words:
        if(w==word):
            ans+=1
    return ans



def top10(L):
    newL=L.copy()
    newL.sort(reverse=True)
    ans=[]
    for i in range(0,10):
        ans.append(newL[i])
    print(ans)
    return ans



def top10words(words):
    ans=[]
    sim_words = []
    for w in words:
        if w not in sim_words:
            sim_words.append(w)

    wordCount={}
    for w in sim_words:
        wordCount[w]=word_counts(w,words)

    Lcount=top10(list(wordCount.values()))

    for key in wordCount:
        for n in Lcount:
            if(wordCount[key]==n):
                ans.append(key)
                Lcount.remove(n)
                break
    return ans







if __name__ == '__main__':

    words=open("Notes_Underground.txt", encoding="latin-1").read().split()
    book=open("Pride and Prejudice.txt", encoding="latin-1").read().split()
    print(top10words(book))













