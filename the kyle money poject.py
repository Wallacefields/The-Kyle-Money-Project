from openai import OpenAI
import time

# OPENAI Client setup
client = OpenAI(api_key="")

def get_gpt_message(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[GPT ERROR]: {e}"

questions = [
    # Easy
    {"question": "What color is the sky on a clear day?", "options": ["A. Green", "B. Red", "C. Blue", "D. Purple"], "answer": "C"},
    {"question": "Which animal barks?", "options": ["A. Cat", "B. Dog", "C. Cow", "D. Horse"], "answer": "B"},
    {"question": "What is 2 + 2?", "options": ["A. 3", "B. 4", "C. 5", "D. 6"], "answer": "B"},
    {"question": "Which fruit is yellow and curved?", "options": ["A. Apple", "B. Banana", "C. Cherry", "D. Grape"], "answer": "B"},
    {"question": "What do cows drink?", "options": ["A. Orange Juice", "B. Soda", "C. Lemonade", "D. Coffee"], "answer": None},  # rigged
    
    # Medium
    {"question": "Who was the first president of the USA?", "options": ["A. Lincoln", "B. Washington", "C. Adams", "D. Roosevelt"], "answer": "B"},
    {"question": "Which planet has rings?", "options": ["A. Mars", "B. Saturn", "C. Earth", "D. Venus"], "answer": "B"},
    {"question": "How many continents are there?", "options": ["A. 6", "B. 5", "C. 7", "D. 8"], "answer": "C"},
    {"question": "Which gas do plants absorb?", "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Helium"], "answer": "C"},
    {"question": "Is fire hot or cold?", "options": ["A. Cold", "B. Lukewarm", "C. Room Temperature", "D. Frozen"], "answer": None},  # rigged

    # Hard
    {"question": "What is the derivative of sin(x)?", "options": ["A. cos(x)", "B. -cos(x)", "C. tan(x)", "D. -sin(x)"], "answer": "A"},
    {"question": "Which element has the atomic number 79?", "options": ["A. Silver", "B. Gold", "C. Copper", "D. Platinum"], "answer": "B"},
    {"question": "In what year did WW1 begin?", "options": ["A. 1912", "B. 1914", "C. 1916", "D. 1918"], "answer": "B"},
    {"question": "Who developed the general theory of relativity?", "options": ["A. Newton", "B. Bohr", "C. Einstein", "D. Feynman"], "answer": "C"},
    {"question": "What is 1 divided by 0?", "options": ["A. 0", "B. 1", "C. Infinity", "D. 100"], "answer": None},  # rigged

    # Very Hard
    {"question": "What is Schrödinger's cat paradox about?", "options": ["A. Space", "B. Time", "C. Quantum Superposition", "D. Thermodynamics"], "answer": "C"},
    {"question": "What language is spoken in Brazil?", "options": ["A. Spanish", "B. Portuguese", "C. French", "D. English"], "answer": "B"},
    {"question": "Which organelle is known as the powerhouse of the cell?", "options": ["A. Ribosome", "B. Nucleus", "C. Mitochondria", "D. Golgi body"], "answer": "C"},
    {"question": "Which number is both a cube and a square?", "options": ["A. 64", "B. 36", "C. 100", "D. 25"], "answer": "A"},
    {"question": "What is 5 times 0?", "options": ["A. 0.1", "B. 1", "C. 5", "D. 10"], "answer": None}  # rigged
]

def play_game():
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQ{i + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        # Send motivational prompt
        motivation = get_gpt_message("Write a motivational one-liner for a trivia player.")
        print(f"\n✨ GPT says: {motivation}")

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if q['answer'] is None:
            print("Skill Issue! get a life")
        elif answer == q['answer']:
            print("LUCKY U WONT GET THAT NEXT TIME")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer was: {q['answer']} GET  BETTER")

        time.sleep(0.5)

    print("\n🧾 Game Over!")
    print(f"🏁 Final Score: {score}/20")
    print(f"📊 Percentage: {(score / 20) * 100:.2f}%")

if __name__ == "__main__":
    play_game()
