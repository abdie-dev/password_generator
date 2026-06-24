from csv import Error
from multiprocessing import Value
import random


def number_guesser():
    
    random_number = random.randint(1, 10)
    attempt = 3
    
    while attempt > 0:
        guess_number = int(input("Input your answer: "))
        print(random_number)
        
        if not guess_number:
            print("Fallback: please check your answer!!")
        try:
            if guess_number == random_number:
                print(f"Your answer is right!")
                break
            elif guess_number > random_number:
                print(f"Your asnwer is to high from the real answer")
                attempt -= 1
            elif guess_number < random_number:
                print(f"Your asnwer is to low from the real answer")
                attempt -= 1

        except ValueError as e:
            print(f"Error: please check again your answer")
    else:
        print(f"Try again later buddy")


if __name__ == "__main__":
    number_guesser()