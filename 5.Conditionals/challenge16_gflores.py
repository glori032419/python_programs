print("\t\t\tWelcome to the Shipping Accounts Program.")

users=["Eramom","footea","davisv","papinukt","allenj"]
users=str.title(input("Hello, what is your username: ").swapcase())

if 'Eramom' in users:
    print("SI")
    print(f"Hello {users}. Welcome back to your account.")


else:
    'b' not in users
    print("Sorry, you do not have an account with us. Goodbye.")

print("Current shipping prices are as follows: ")

print("\tShipping orders 0 to 100:    $5.10 each")
print("\tShipping orders 100 to 500:  $5.00 each")
print("\tShipping orders 500 to 1000: $4.94 each")
print("\tShipping orders over 1000:   $4.80 each")

cost1=4.80
cost2=4.94
cost3=5.00
cost4=5.10

order=float(input("How many items would you like to ship: "))
if order<1000:
    print(f"To ship {order} items it will cost you ${str(order * cost1)} at ${cost1} per item.")
elif order>100 and order<500:
    print(f"To ship {order} items it will cost you ${str(order * cost3)} at ${cost3} per item.")
elif order>500 and order<1000:
    print(f"To ship {order} items it will cost you ${str(order * cost2)} at ${cost2} per item.")
elif order>0 and order<100:
    print(f"To ship {order} items it will cost you ${str(order * cost4)} at ${cost4} per item.")
  
cuestion=input("Would you like to place this order (yes/no): ")

if cuestion=='yes':
    order=float(input("How many items would you like to ship: "))
    if order<1000:
     print(f"To ship {order} items it will cost you ${str(order * cost1)} at ${cost1} per item.")
elif order>100 and order<500:
    print(f"To ship {order} items it will cost you ${str(order * cost3)} at ${cost3} per item.")
elif order>500 and order<1000:
    print(f"To ship {order} items it will cost you ${str(order * cost2)} at ${cost2} per item.")
elif order>0 and order<100:
    print(f"To ship {order} items it will cost you ${str(order * cost4)} at ${cost4} per item.")
  
else:
    cuestion=='no'
    print("Okay, no order is being placed at this time.")