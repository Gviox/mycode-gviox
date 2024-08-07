import trivia_data
import html

trivia = trivia_data.trivia

def trivia(trivia):
    print(html.unescape(trivia["question"])) 

    answers = trivia["incorrect"] + [trivia["correct"]]

trivia(trivia)    


