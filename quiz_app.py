def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) Ernest Hemingway"],
            "answer": "A"
        }
    ]

    score = 0   # score = 0 initializes the score variable to keep track of the user's score throughout the quiz

    for index, q in enumerate(questions):
        print(f"Question {index + 1}: {q['question']}")   # prints the current question number and the question text
        for option in q["options"]:  # 
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ")
        print(user_answer.strip().upper(), q["answer"][0])   #
        
        '''if user_answer == q["answer"][0]:
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")'''

    print(f"Your final score is: {score}/{len(questions)}")  # 

run_quiz()    