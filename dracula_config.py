from collections import Counter

# open file in read mode
with open("dracula.txt", "r") as file:
   vampire_count = 0 
   for line in file:
        if "vampire" in line.lower():
            print(line.strip())
            vampire_count += line.lower().count("vampire")

print(f"vampire count is: {vampire_count}")


