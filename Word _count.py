word=input('write your word')
count=0
for letters in word:
    if letters.isalpha:
        count+=1
print(count)
