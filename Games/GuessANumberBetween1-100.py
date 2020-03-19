import random
# Module implements the Mersenne Twister random
# number generator.


# Create a number guessing game, gives users a certain ammount of guesses
#  if the guess is higher than the  number let use know 
# that they  should guess lower, if  number is higher than guess ,
#  let user know that they need to guess lower
# if guess == number  let user know they have won, if user run out of guesses , 
# let user know that they have lost 



print('Guess the number that is between 1 - 100, You have 6 Guesses, Good Luck!')
randomNumber = random.randint(1,100)
guesses = 0
while guesses < 6:
    guess = int(input())

    if guess == randomNumber:
        print('Congratulations you won!')
        break
    elif guess < randomNumber:
        print(' its lower than',guess)
    else:
        print(' its higher than', guess)
    guesses +=1
    print('you haves ', 6 - guesses, 'guesses left')

    if guesses >= 6:
        print("You lost, better luck next time")





