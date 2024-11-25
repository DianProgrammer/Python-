number_games = 5
count = 0
sum = 0 
sum1 = 0
sum2 = 0 
sum3 = 0  


while count < number_games:
    score = input("Please enter the score: ")
    score = int(score)
    count = count + 1
    if score ==3: 
        sum1 = count * 3
    elif score ==1:
        sum2 = count * 1
    else:
        sum3 = count * 0

sum = sum1 + sum2 + sum3
print(count , sum)


    

       
