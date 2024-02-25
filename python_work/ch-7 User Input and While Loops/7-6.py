#1,3 solution
prompt = "\nWhat are your toppings?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(f"I'll add your {message} toppings.")


#2 solution
prompt = "\nPlease enter a pizza topping:"
prompt += "\nEnter 'quit' when you are finished. :"

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"I will add the {message.title()} topping.")


