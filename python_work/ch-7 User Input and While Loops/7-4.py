prompt = "\n Please enter a pizza topping:"
prompt += "\nEnter 'quit' when you are finished. :"

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"I will the {message.title()} topping.")


prompt = "\nWhat do you want for toppings?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    topping = input(prompt)
    if topping != 'quit'
        print(f"I'll add {topping.title()} to your pizza.")
    else:
        break

