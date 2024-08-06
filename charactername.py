# Save a user's input to the variable char_name from the following question:
# Which character do you want to know about? (Starlord, Mystique, Hulk)

def main():
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)")

#Save a user's input to the variable char_stat from the following question:
# What statistic do you want to know about? (real name, powers, archenemy)
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")

    marvelchars= {
    "Starlord":
      {"real name": "peter quill",
     "powers": "dance moves",
     "archenemy": "Thanos"},

    "Mystique":
     {"real name": "raven darkholme",
      "powers": "shape shifter",
      "archenemy": "Professor X"},

    "Hulk":
      {"real name": "bruce banner",
      "powers": "super strength",
      "archenemy": "adrenaline"}
             }


    print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}")

main()
