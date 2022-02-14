import urllib.request





def numResults(key):
    key=key.replace(" ","%20")
    link= "http://search.yahoo.com/search;_ylt=A0oG7l7PeB5P3G0AKASl87UF?p="+ key
    f = urllib.request.urlopen(link)
    source = f.read().decode("utf-8")
    f.close()
    ind=source.find("results</span></div></div></li></ol></div></div><div")
    i=1
    while (source[ind-i]!=">"):
        i+=1
    ans=source[ind-i+1:ind-1:1]
    ans=ans.replace(",","")
    return int(ans)




def choose_variant(v):
    if(numResults(v[0])<numResults(v[1])):
        return v[1]
    elif(numResults(v[0])>numResults(v[1])):
        return v[0]
    else:
        return "Both " + v[0] + " and " + v[1] + " work!!"







if __name__ == '__main__':
    print(numResults("engineering science"))
    print(choose_variant(["five-year anniversary", "fifth anniversary"]))
































