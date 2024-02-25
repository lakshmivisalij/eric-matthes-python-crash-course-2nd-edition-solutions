# 7-8. Deli

sandwich_orders = ['Tuna', 'Potato', 'Tomato', 'Cucumber']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made are: ")
for sandwich in finished_sandwiches:
    print(sandwich)
