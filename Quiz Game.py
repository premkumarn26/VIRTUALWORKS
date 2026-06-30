Quiz Game:

# Quiz Game in Python

def quiz_game():
    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": ["A. Chennai", "B. New Delhi", "C. Mumbai", "D. Kolkata"],
            "answer": "B"
        },
        {
            "question": "2. Which language is mainly used for Data Science?",
            "options": ["A. Python", "B. HTML", "C. CSS", "D. XML"],
            "answer": "A"
        },
        {
            "question": "3. Who is known as the Father of Computers?",
            "options": ["A. Alan Turing", "B. Charles Babbage", "C. Bill Gates", "D. Steve Jobs"],
            "answer": "B"
        },
        {
            "question": "4. Which symbol is used to define a comment in Python?",
            "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
            "answer": "C"
        },
        {
            "question": "5. Which data type is used to store True or False values?",
            "options": ["A. int", "B. string", "C. float", "D. bool"],
            "answer": "D"
        }
    ]

    score = 0

    print("===================================")
    print("      WELCOME TO THE QUIZ GAME")
    print("===================================")

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer is {q['answer']}.")

    total = len(questions)
    percentage = (score / total) * 100

    print("\n===================================")
    print("          QUIZ COMPLETED")
    print("===================================")
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent! ")
    elif percentage >= 60:
        print("Good Job! ")
    elif percentage >= 40:
        print("Average. Keep Practicing!")
    else:
        print("Needs Improvement. Try Again!")

# Run the quiz
quiz_game()

Output:

===================================
      WELCOME TO THE QUIZ GAME
===================================

1. What is the capital of India?
A. Chennai
B. New Delhi
C. Mumbai
D. Kolkata
Enter your answer (A/B/C/D): B
 Correct!

2. Which language is mainly used for Data Science?
A. Python
B. HTML
C. CSS
D. XML
Enter your answer (A/B/C/D): A
 Correct!

3. Who is known as the Father of Computers?
A. Alan Turing
B. Charles Babbage
C. Bill Gates
D. Steve Jobs
Enter your answer (A/B/C/D): B
 Correct!

4. Which symbol is used to define a comment in Python?
A. //
B. <!-- -->
C. #
D. **
Enter your answer (A/B/C/D): C
 Correct!

5. Which data type is used to store True or False values?
A. int
B. string
C. float
D. bool
Enter your answer (A/B/C/D): D
 Correct!

===================================
          QUIZ COMPLETED
===================================
Score: 5/5
Percentage: 100.00%
Excellent!