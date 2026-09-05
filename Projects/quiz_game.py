# #   Python Quiz Game

questions = ("Which planet is known as the Red Planet?",
             "Who wrote Romeo and Juliet?",
             "What is the largest ocean on Earth?",
             "What is the chemical symbol for gold?",
             "Which is the fastest land animal?")

options = (("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),
           ("A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Jane Austen"),
           ("A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"),
           ("A. Ag", "B. Fe", "C. Au", "D. Cu"),
           ("A. Lion", "B. Cheetah", "C. Horse", "D. Leopard"))

answers = ("B",
           "A",
           "C",
           "C",
           "B")
correct_answers = ("Mars",
                   "William Shakespeare",
                   "Pacific Ocean",
                   "Au",
                   "Cheetah")
guesses = []

score = 0

question_num = 0

for question in questions:
    print("---------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if answers[question_num] == guess:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{(correct_answers[question_num])} is the correct answer ")
    question_num += 1
