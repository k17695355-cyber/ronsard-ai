

# 1. Ask the user for a question
question = input("Ask me a question: ").lower()

# 2. Check the question and give the correct answer
if "hello" in question or "hi" in question:
    print("Hello there! How can I help you today?")

elif "your name" in question:
    print("I am a simple Python chatbot built in VS Code!")

elif "weather" in question:
    print("I can't check the live weather yet, but it looks like a great day to code!")

elif "minecraft" in question:
    print("Minecraft is awesome! Make sure to install performance mods like Sodium or OptiFine for the best FPS.")

# 3. Fallback if the program doesn't understand
else:
    print("I'm sorry, I don't know the answer to that question yet.")

elif "Where is Ecole Ronsard located" in question:
    print("Ecole Ronsard is located at East Legon")

# A dictionary matching keywords to general facts
facts = {
    "earth": "The Earth is the third planet from the Sun and the only known planet to support life.",
    "water": "Water is made of two hydrogen atoms and one oxygen atom (H2O). It covers about 71% of Earth's surface.",
    "speed of light": "The speed of light is about 186,282 miles per second (299,792 kilometers per second).",
    "dinosaur": "Dinosaurs went extinct about 66 million years ago, likely due to a massive asteroid impact.",
    "python": "Python is a high-level programming language created by Guido van Rossum and released in 1991."
}

# Ask the user what they want to know
query = input("What general topic do you want to know about? ").lower()

# Search for the keyword in our facts database
found = False
for keyword, answer in facts.items():
    if keyword in query:
        print(f"\nFact: {answer}")
        found = True
        break

if not found:
    print("\nI don't have information on that topic yet. Try asking about 'Earth', 'Water', or 'Speed of Light'.")
 # 1. This is your database of facts. 
# You can add as many as you want using the format "keyword": "the actual fact"
facts_database = {
    "capital of France": "The capital of France is Paris.",
    "tallest mountain": "Mount Everest is the tallest mountain above sea level, reaching 8,848 meters.",
    "human bones": "An adult human has 206 bones, while a newborn baby has around 270.",
    "honey": "Honey never spoils. You can theoretically eat 3,000-year-old Egyptian tomb honey.",
    "gravity": "Sir Isaac Newton discovered gravity when he saw an apple fall in his orchard."
}

print("--- General Knowledge Bot is Ready! ---")
print("Type 'exit' at any time to close the program.\n")

# 2. This keeps the program running in a loop
while True:
    # Ask the user for a question
    user_input = input("Ask a question or enter a topic: ").lower()
    
    # Check if the user wants to stop the program
    if user_input == "exit":
        print("Goodbye!")
        break
        
    # This variable tracks whether we found a match in our facts
    matched_fact = False
    
    # 3. Look through every fact in your database
    for keyword, fact_content in facts_database.items():
        if keyword.lower() in user_input:
            print(f"\n💡 FACT: {fact_content}\n")
            matched_fact = True
            break # Stop looking once we find a match
            
    # 4. If the loop finished and found nothing, tell the user
    if not matched_fact:
        print("\n❌ I don't have a fact about that in my database yet.\n")
