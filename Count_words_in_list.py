x=['ahmed','omar','soliman','tamer']
count=0
for i in x:
    for u in i:
        if u.isalpha():
            count+=1
    print(f'word is {i}, letters is {count}')
    count=0
