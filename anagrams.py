#sorted(x) gives the sorted list of elements
#sorted(x,reverse=True) give the sorted list in descending order
#sorted(x,key=len) to sort based on length

#ANAGRAMS DISCUSSION

def anagram_checker():
  str1=input()
  str2=input()
  if sorted(str1.replace(" ", "").lower())==sorted(str2.replace(" ", "").lower()):
    return 1
  else:
    return 0
 
print(anagram_checker(),end="")
