import datetime
time = datetime.datetime.now()
print("Date/Time: " + str(time) + "\n")
print ("Welcome to Nemo☕Cafe!\n")

name = input ("What's your name, sir?\n")

if name == "mohtady" or name == "nehal":
  location = input("Are you home or out side?\n")
  if location == "home":
    print("Then, Get Out!")
    exit()
  else:
    print("Then, Don't come back!")
    exit()
  
else:
  print ("Hello " + name + ", thank you so much for coming here today\n")

menu = "espresso \nnescafe \nblack Coffee"

order = input ("What would you like to have today? This is our menu: \n" + menu + "\n")

if order == "espresso":
  price = 4
elif order == "nescafe":
  price = 3
elif order == "black coffee":
  price = 2
else:
  print ("Sorry, we don't have this drink on our menu.")
  exit()

print (order + "! Nice Choice. Your order will be done in a minute \n")

quantity = input("How many cups would you like?\n")

total = price * int(quantity)
print("\nOk, here is your drink.")
print("The total is: $" + str(total))
print("hint:say the total to pay me")
money = input()
if money == str(total):
  print("Thank you, have a nice day!")
else:
  print("Wrong! \nhint:write the total to pay me")
  money_1 = input()
  if money_1 == str(total):
    print("Thank you, have a nice day!")
  else:
    print("You are annoying \nGet Out!")
    exit()