import random
count = 1

print("I'm thing of a number betwee 1 and 20")


answer  = random.randint(1, 20)

while True:
      num = int(input("Take a guess: "))  
      if num == answer:
          break
      elif num > answer:
          print("Your guess is too high")
          count += 1
      else:
          print("Your guess is too low")
          count += 1
          
print(f"Good job! You guessed my number is {count} guesses!")