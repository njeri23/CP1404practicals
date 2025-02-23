name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
name_from_file = file.read().strip()
file.close()
print(f"Hi {name_from_file}!")

with open("numbers.txt", "r") as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())
print(num1 + num2)  # Output should be 59

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(total)
