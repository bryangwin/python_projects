import random

computer_choice = f"{random.randint(1, 3)} {random.randint(1, 3)}"
print(f"The computer chooses {computer_choice}")

row, col = map(int, computer_choice.split())

print(row, col)