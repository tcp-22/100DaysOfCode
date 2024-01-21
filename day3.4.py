print("Welcome to Rollercoaster Ticket Machine")

height = int(input("How tall are you in cm? "))

bill = 0

if height > 120:
  print("Great, you can ride!")

  age = int(input("How old are you? "))

  if age < 12:
    bill = 5 
    print("You need to pay $5.")
  elif age <= 18:  
    bill = 7
    print("You need to pay $7.")
  else:
    bill = 12
    print("You need to pay $12.")
  
  photo = input("Would you like a photo? (y/n) ")

  if photo == "y":
    bill += 3 
    print(f"Your total bill is ${bill}")

else:
  print("Sorry, you are not tall enough to ride.")