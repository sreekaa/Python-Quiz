score = 0
print("Welcome to the General Knowledge Quiz!")
print("Answer all 10 questions. Each correct answer gives 1 point.\n")

questions = [
    {"q": "1. What is the capital of Australia?", 
     "options": ["a) Sydney", "b) Melbourne", "c) Canberra", "d) Brisbane"], "ans": "c"},
     
    {"q": "2. Who wrote the play 'Romeo and Juliet'?", 
     "options": ["a) Charles Dickens", "b) William Shakespeare", "c) Jane Austen", "d) Mark Twain"], "ans": "b"},
     
    {"q": "3. Which planet is known as the Red Planet?", 
     "options": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"], "ans": "b"},
     
    {"q": "4. What is the largest ocean on Earth?", 
     "options": ["a) Atlantic Ocean", "b) Indian Ocean", "c) Arctic Ocean", "d) Pacific Ocean"], "ans": "d"},
     
    {"q": "5. Who is known as the Father of Computers?", 
     "options": ["a) Alan Turing", "b) Bill Gates", "c) Charles Babbage", "d) Tim Berners-Lee"], "ans": "c"},
     
    {"q": "6. In which country were the Olympic Games originated?", 
     "options": ["a) Italy", "b) Greece", "c) Egypt", "d) China"], "ans": "b"},
     
    {"q": "7. Which gas do plants absorb from the atmosphere?", 
     "options": ["a) Oxygen", "b) Nitrogen", "c) Carbon Dioxide", "d) Hydrogen"], "ans": "c"},
     
    {"q": "8. What is H2O commonly known as?", 
     "options": ["a) Oxygen", "b) Salt", "c) Water", "d) Hydrogen Peroxide"], "ans": "c"},
     
    {"q": "9. How many continents are there on Earth?", 
     "options": ["a) 5", "b) 6", "c) 7", "d) 8"], "ans": "c"},
     
    {"q": "10. Who painted the Mona Lisa?", 
     "options": ["a) Pablo Picasso", "b) Vincent Van Gogh", "c) Leonardo da Vinci", "d) Michelangelo"], "ans": "c"},
]

for q in questions:
    print(q["q"])
    for option in q["options"]:
        print(option)
    ans = input("Your answer: ").lower()
    if ans == q["ans"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['ans']})\n")

print(f"You scored {score} out of 10.")
if score == 10:
    print("Perfect score! Excellent work.")
elif score >= 7:
    print("Great job!")
elif score >= 5:
    print("Good attempt, keep learning.")
else:
    print("Don't give up, try again.")
