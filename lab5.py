numbers = [12, 7, 5, 8, 10, 3, 14, 9]

with open("ededler.txt", "w") as f:
    for num in numbers:
        f.write(str(num) + "\n")

even_numbers = []
with open("ededler.txt", "r") as f:
    for line in f:
        number = int(line.strip())
        if number % 2 == 0:
            even_numbers.append(number)

with open("cut_ededler.txt", "w") as f:
    for num in even_numbers:
        f.write(str(num) + "\n")

sum_even = sum(even_numbers)
print("Cüt ədədlərin cəmi:", sum_even)
