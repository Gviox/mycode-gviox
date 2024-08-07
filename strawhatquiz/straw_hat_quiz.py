import quiz_data
from collections import Counter

questions = quiz_data.questions

#This will be used to hav us start at the first question
question_num = 0

#this will collect the users answers needs to start as an empty array first
answers = []

# this is for the amount of times a character appears in the selected answer
character_counts = Counter()

def quiz_questions(questions):
    global question_num, answers, character_counts

    #display question
    for question in questions:
        print("Enter a number that cooresponds with your answer.")
        print(question["question"])

    #display all choices
        for index, choice in enumerate(question["choices"], 1):
            print(f"{index}.{choice['text']}")

    #account for user input
        while True:
            try:
                 user_input = int(input("Choose your answer: ")) - 1
                 if 0 <= user_input < len(question["choices"]):
                     selected_choice = question["choices"][user_input]
                     answers.append(user_input + 1)# append the selected number instead of text

                     # count the character associated with the selected choice
                     character_counts.update(selected_choice["characters"])
                     break
                 else:
                     print("Invalid choice. Please choose a number from the list")
            except ValueError:
                print("Invalid input. Please enter a number.")

    #increment through the questions by one
        question_num += 1

quiz_questions(questions)

# find the most common character
most_common_character = character_counts.most_common(1)[0][0]

# message at the end of quiz telling you which pirate you would be like
print(f"You would be {most_common_character} from the Straw Hat Pirates")
