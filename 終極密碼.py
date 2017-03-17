ans = eval(input())
max = 100
min = 1

while True :
    print('%d<?<%d'%(min,max) )
    guess = eval(input())
    if guess >=100 or guess <= 0 :
        print ('Invalid number.')
    elif guess > ans :
        max = guess
        print('wrong answer, guess smaller')
        continue
    elif guess < ans :
        min = guess
        print('Wrong answe, guess larger')
        continue 
    elif guess == ans :
        print('bingo answer is %d'%(ans))
        break
    
