prompt = "Please enter the name of city you have visated:"
prompt+= "\n(Enter 'quit' when you are finished) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
