import random

print("Welcome to the random number guessing game :) " )
print("You have 5 attempts to win!" )

def guess_number():
    random_number = random.randint(1,25)
    guess = None
    attempts = 5 
    while guess != random_number and attempts > 0 :
        guess = int(input("Guess a number between 1 and 25: " ))
        if guess < random_number:
            print("Guess is too low! " )
            attempts -= 1
            print("Number of attempts remaining: " + str(attempts))

        elif guess > random_number:
            print("Guess is too high! " )
            attempts -= 1
            print(attempts)
              
        else:
            print("Congratulations that is the correct number!" )

    else:
        if attempts == 0:
            print("You have ran out of attempts, you lose! D: " )
        else:
            print("You have guessed the number in " + str(attempts) + " attempts. " 
                  "the number was " + str(random_number) )
            

            
                
if __name__ =="__main__":
    guess_number()       
        