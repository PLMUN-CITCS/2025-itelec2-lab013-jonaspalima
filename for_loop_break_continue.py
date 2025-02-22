numbers = list(range(1, 11))  # Create a list from 1 to 10

for num in numbers:
    if num == 3:
        continue  # Skip the rest of this iteration when num is 3

    if num == 7:
        break  # Exit the loop completely when num is 7

    print(num)  # Print the number if it's not skipped or breaking the loop

