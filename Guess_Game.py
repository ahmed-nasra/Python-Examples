import random
secret_number= random.randint(1,20)
tries=0
max_tries=6
print('welcome to guessing number game')
print( 'i have selcted a number between 1:20')
print( f'you have {max_tries} tries to win')
while tries< max_tries:
    guess=int(input('guess the number'))
    tries+=1
    if guess < secret_number:
        print('too low')
    elif guess > secret_number:
        print('too high')
    else:
        print(f'congrats! you win after {tries} and the secret number is {secret_number}')
        break
else:
    print(f'you lost!! you have reached all tries and the secrert number was {secret_number}')
