import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Berlin", "C. Madrid", "D. Rome"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. Jane Austen", "C. William Shakespeare", "D. Mark Twain"],
        "answer": "C"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["A. 90", "B. 95", "C. 100", "D. 105"],
        "answer": "C"
    },
    {
        "question": "Which animal is known as the king of the jungle?",
        "options": ["A. Tiger", "B. Elephant", "C. Bear", "D. Wolf"],
        "answer": None  # rigged
    },
    {
        "question": "Which element has the chemical symbol O?",
        "options": ["A. Oxygen", "B. Gold", "C. Iron", "D. Helium"],
        "answer": "A"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Van Gogh", "B. Picasso", "C. Da Vinci", "D. Rembrandt"],
        "answer": "C"
    },
    {
        "question": "What is the tallest mountain on Earth?",
        "options": ["A. K2", "B. Everest", "C. Kilimanjaro", "D. Denali"],
        "answer": "B"
    },
    {
        "question": "How many continents are there?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "What color are aircraft black boxes?",
        "options": ["A. Black", "B. Red", "C. Yellow", "D. White"],
        "answer": None  # rigged
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["A. Won", "B. Yen", "C. Yuan", "D. Ringgit"],
        "answer": "B"
    },
    {
        "question": "In which year did WW2 end?",
        "options": ["A. 1942", "B. 1945", "C. 1948", "D. 1950"],
        "answer": "B"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {
        "question": "Which country invented pizza?",
        "options": ["A. France", "B. USA", "C. Germany", "D. China"],
        "answer": None  # rigged
    },
    {
        "question": "What is H2O commonly known as?",
        "options": ["A. Water", "B. Salt", "C. Sugar", "D. Oxygen"],
        "answer": "A"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["A. Toronto", "B. Vancouver", "C. Montreal", "D. Ottawa"],
        "answer": "D"
    },
    {
        "question": "Who discovered gravity?",
        "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Darwin"],
        "answer": "A"
    },
    {
        "question": "Which gas do plants absorb?",
        "options": ["A. Oxygen", "B. Hydrogen", "C. Nitrogen", "D. Helium"],
        "answer": None  # rigged
    }
]

def play_game():
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQ{i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if q['answer'] is None:
            print("Unlucky! skill issue get better!")
        elif answer == q['answer']:
            print("✅ Correct! lucky one bet u wont get it next time")
            score += 1
        else:
            print("❌ Wrong! skill issue")

    print("\nGame Over!")
    print(f"Score: {score}/20")
    print(f"Percentage: {(score / 20) * 100:.2f}%")

if __name__ == "__main__":
    play_game()

