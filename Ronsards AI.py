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

elif "what is ecole ronsard" in question or "about ecole ronsard" in question:
    print("École Ronsard is a leading bilingual (French and English) international school established in 2009, offering a holistic education from Creche up to Secondary levels.")

elif "where is ecole ronsard" in question or "location" in question:
    print("École Ronsard is located at 21-23 Kinshasa Street in East Legon, Accra, Ghana!")

elif "accreditation" in question or "curriculum" in question:
    print("The school holds dual accreditation from Cambridge International (for English, Math, and Science) and LabelFrancÉducation (for the French stream).")

elif "principal" in question or "head" in question:
    print("The principal of École Ronsard is Marie-Patricia Agbenyeke.")

elif "campuses" in question:
    print("École Ronsard has two vibrant campuses: one dedicated entirely to the Nursery program, and the other for Primary and Secondary levels.")

elif "What is 2+2" in question:
    print("4")

# --- NURSERY TO YEAR 3 TOPICS ---
elif "counting" in question or "number recognition" in question:
    print("\n👶 [Nursery Math]: Counting means naming numbers in order up to 20, and recognizing how the symbols 1 to 20 look.")

elif "shapes" in question:
    print("\n👶 [Nursery Math]: Basic shapes include flat 2D shapes: Circles (round), Squares (4 equal sides), and Triangles (3 sides).")

elif "multiplication" in question or "times tables" in question:
    print("\n🎒 [Primary Math]: Multiplication is repeated addition. For example, 3 x 5 means adding 3 five times (3+3+3+3+3 = 15).")


# --- YEARS 4 TO 6 TOPICS ---
elif "fraction" in question or "decimal" in question:
    print("\n📈 [Upper Primary Math]: A fraction represents a part of a whole (like 1/2 of a pizza). A decimal does the same using a point (like 0.5).")

elif "area" in question or "perimeter" in question:
    print("\n📈 [Upper Primary Math]: Perimeter is the total distance around the outside of a shape. Area is the total space inside the shape.")


# --- YEARS 7 TO 9 TOPICS (Cambridge Checkpoint) ---
elif "algebra" in question or "solve for x" in question:
    print("\n📐 [Lower Secondary Math]: Algebra uses letters (variables) to stand for missing numbers. If x + 5 = 12, then x must be 7.")

elif "pythagorean" in question or "triangle rule" in question:
    print("\n📐 [Lower Secondary Math]: The Pythagorean Theorem states that in a right-angled triangle, a² + b² = c² (where c is the longest side).")


# --- YEAR 10 TOPICS (Cambridge IGCSE) ---
elif "quadratic" in question:
    print("\n🧠 [Year 10 IGCSE Math]: A quadratic equation contains a squared variable, looking like ax² + bx + c = 0. It usually has two answers.")

elif "trigonometry" in question or "sine" in question or "cosine" in question:
    print("\n🧠 [Year 10 IGCSE Math]: Trigonometry studies triangle sides and angles. Remember SOH-CAH-TOA to find Sine, Cosine, and Tangent!")

elif "probability" in question:
    print("\n🧠 [Year 10 IGCSE Math]: Probability measures how likely an event is to happen, calculated as: (Desired Outcomes) / (Total Outcomes).")

# --- AUTOMATIC MATH ENGINE (Handles 0.000000001 to 100,000,000) ---
elif any(op in question for op in ["+", "-", "*", "/", "add", "subtract", "multiply", "divide"]):
    print("\n🧮 [Ronsard AI Calculator Active]")
    try:
        # 1. Clean the words out of the sentence to find the numbers
        words = question.replace("what is", "").replace("by", "").split()
        numbers = []
        operation = None
        
        # Identify the math symbols or words
        for word in words:
            if word in ["+", "add"]: operation = "+"
            elif word in ["-", "subtract", "minus"]: operation = "-"
            elif word in ["*", "multiply", "times"]: operation = "*"
            elif word in ["/", "divide"]: operation = "/"
            else:
                try:
                    numbers.append(float(word))
                except ValueError:
                    continue # Skip normal text words

        if len(numbers) >= 2 and operation:
            num1, num2 = numbers[0], numbers[1]
            
            # 2. Enforce your specific scale boundary constraints
            MIN_VAL, MAX_VAL = 0.0000000000000000000000000000000001, 10000000000000000000000000000000000.0
            if not (MIN_VAL <= abs(num1) <= MAX_VAL) or not (MIN_VAL <= abs(num2) <= MAX_VAL):
                print(f"⚠️ Scale Error: Please use numbers between {MIN_VAL} and {MAX_VAL:,}.")
            else:
                # 3. Process the arithmetic operations securely
                if operation == "+": result = num1 + num2
                elif operation == "-": result = num1 - num2
                elif operation == "*": result = num1 * num2
                elif operation == "/":
                    if num2 == 0:
                        print("❌ Math Error: Cannot divide by zero.")
                        result = None
                    else: result = num1 / num2
                
                if result is not None:
                    # Formats up to 9 decimal places without trailing zeros
                    print(f"➡️ Result: {result:.9f}".rstrip('0').rstrip('.'))
        else:
            print("❓ I detected a math request, but couldn't parse the numbers clearly. Example: '5.2 + 100'")
            
    except Exception:
          print("❌ Could not compute. Please ensure your format is correct.")

        # --- SQUARING ENGINE (Handles numbers from 0.000000001 to 100,000,000) ---
elif "square" in question or "squared" in question:
    print("\n🧮 [Ronsard AI Squaring Engine Active]")
    try:
        # 1. Clean words out of the sentence to find the single number
        words = question.replace("what is", "").replace("square", "").replace("squared", "").split()
        
        target_number = None
        for word in words:
            try:
                target_number = float(word)
                break  # Stop at the first number we find
            except ValueError:
                continue

        if target_number is not None:
            # 2. Enforce your scale constraints
            MIN_VAL, MAX_VAL = 0.0000000000000000000000000000000001, 10000000000000000000000000000000000.0
            if not (MIN_VAL <= abs(target_number) <= MAX_VAL):
                print(f"⚠️ Scale Error: Please use numbers between {MIN_VAL} and {MAX_VAL:,}.")
            else:
                # 3. Calculate the square (number multiplied by itself)
                result = target_number ** 2
                # Formats up to 9 decimal places cleanly
                print(f"➡️ Result: {target_number} squared = {result:.9f}".rstrip('0').rstrip('.'))
        else:
            print("❓ I didn't catch the number. Try typing: 'square 5' or '9 squared'")
            
    except Exception:
        print("❌ Could not compute. Please check your text format.")

# --- SQUARING ENGINE (Handles numbers from 0.000000001 to 100,000,000) ---
elif "square" in question or "squared" in question:
    print("\n🧮 [Ronsard AI Squaring Engine Active]")
    try:
        # 1. Clean words out of the sentence to find the single number
        words = question.replace("what is", "").replace("square", "").replace("squared", "").split()
        
        target_number = None
        for word in words:
            try:
                target_number = float(word)
                break  # Stop at the first number we find
            except ValueError:
                continue

        if target_number is not None:
            # 2. Enforce your scale constraints
            MIN_VAL, MAX_VAL = 0.0000000000000000000000000000000001, 10000000000000000000000000000000000.0
            if not (MIN_VAL <= abs(target_number) <= MAX_VAL):
                print(f"⚠️ Scale Error: Please use numbers between {MIN_VAL} and {MAX_VAL:,}.")
            else:
                # 3. Calculate the square (number multiplied by itself)
                result = target_number ** 2
                # Formats up to 9 decimal places cleanly
                print(f"➡️ Result: {target_number} squared = {result:.9f}".rstrip('0').rstrip('.'))
        else:
            print("❓ I didn't catch the number. Try typing: 'square 5' or '9 squared'")
            
    except Exception:
        print("❌ Could not compute. Please check your text format.")

# --- SQUARING ENGINE (Handles numbers from 0.000000001 to 100,000,000) ---
elif "square" in question or "squared" in question:
    print("\n🧮 [Ronsard AI Squaring Engine Active]")
    try:
        # 1. Clean words out of the sentence to find the single number
        words = question.replace("what is", "").replace("square", "").replace("squared", "").split()
        
        target_number = None
        for word in words:
            try:
                target_number = float(word)
                break  # Stop at the first number we find
            except ValueError:
                continue

        if target_number is not None:
            # 2. Enforce your scale constraints
            MIN_VAL, MAX_VAL = 0.0000000000000000000000000000000001,  10000000000000000000000000000000000.0
            if not (MIN_VAL <= abs(target_number) <= MAX_VAL):
                print(f"⚠️ Scale Error: Please use numbers between {MIN_VAL} and {MAX_VAL:,}.")
            else:
                # 3. Calculate the square (number multiplied by itself)
                result = target_number ** 2
                # Formats up to 9 decimal places cleanly
                print(f"➡️ Result: {target_number} squared = {result:.9f}".rstrip('0').rstrip('.'))
        else:
            print("❓ I didn't catch the number. Try typing: 'square 5' or '9 squared'")
            
    except Exception:
        print("❌ Could not compute. Please check your text format.")

# --- SQUARING ENGINE (Handles numbers from 0.000000001 to 100,000,000) ---
elif "square" in question or "squared" in question:
    print("\n🧮 [Ronsard AI Squaring Engine Active]")
    try:
        # 1. Clean words out of the sentence to find the single number
        words = question.replace("what is", "").replace("square", "").replace("squared", "").split()
        
        target_number = None
        for word in words:
            try:
                target_number = float(word)
                break  # Stop at the first number we find
            except ValueError:
                continue

        if target_number is not None:
            # 2. Enforce your scale constraints
            MIN_VAL, MAX_VAL = 0.0000000000000000000000000000000001,  10000000000000000000000000000000000.0
            if not (MIN_VAL <= abs(target_number) <= MAX_VAL):
                print(f"⚠️ Scale Error: Please use numbers between {MIN_VAL} and {MAX_VAL:,}.")
            else:
                # 3. Calculate the square (number multiplied by itself)
                result = target_number ** 2
                # Formats up to 9 decimal places cleanly
                print(f"➡️ Result: {target_number} squared = {result:.9f}".rstrip('0').rstrip('.'))
        else:
            print("❓ I didn't catch the number. Try typing: 'square 5' or '9 squared'")
            
    except Exception:
        print("❌ Could not compute. Please check your text format.")
 
 # --- CUBING ENGINE (Handles numbers from 0.000000001 to 100,000,000) ---
elif "cube" in question or "cubed" in question:
    print("\n🧮 [Ronsard AI Cubing Engine Active]")
    try:
        # 1. Clean words out of the sentence to find the single number
        words = question.replace("what is", "").replace("cube", "").replace("cubed", "").split()
        
        target_number = None
        for word in words:
            try:
                target_number = float(word)
                break  # Stop at the first number we find
            except ValueError:
                continue

        if target_number is not None:
            # 2. Enforce your scale constraints
            MIN_VAL, MAX_VAL = 0.0000000000000000000000000000000001, 10000000000000000000000000000000000.0
            if not (MIN_VAL <= abs(target_number) <= MAX_VAL):
                print(f"⚠️ Scale Error: Please use numbers between {MIN_VAL} and {MAX_VAL:,}.")
            else:
                # 3. Calculate the cube (number ** 3)
                result = target_number ** 3
                # Formats up to 9 decimal places cleanly
                print(f"➡️ Result: {target_number} cubed = {result:.9f}".rstrip('0').rstrip('.'))
        else:
            print("❓ I didn't catch the number. Try typing: 'cube 3' or '5 cubed'")
            
    except Exception:
        print("❌ Could not compute. Please check your text format.")

# --- SQUARE ROOT ENGINE (Handles numbers up to 100,000,000) ---
elif "root s" in question:
    print("\n🧮 [Ronsard AI Square Root Engine Active]")
    try:
        # Clean words out to find the number
        words = question.replace("what is", "").replace("the", "").replace("square root of", "").replace("square root", "").split()
        target_number = None
        for word in words:
            try:
                target_number = float(word)
                break
            except ValueError:
                continue

        if target_number is not None:
            MIN_VAL, MAX_VAL = 0.0000000000000000000000000000000001, 10000000000000000000000000000000000.0
            if not (MIN_VAL <= target_number <= MAX_VAL):
                print(f"⚠️ Scale Error: Please use positive numbers between {MIN_VAL} and {MAX_VAL:,}.")
            else:
                # Calculate square root using exponent 0.5
                result = target_number ** 0.5
                print(f"➡️ Result: Square root of {target_number} = {result:.9f}".rstrip('0').rstrip('.'))
        else:
            print("❓ I didn't catch the number. Try typing: 'square root of 16' or 'square root 9'")
    except Exception:
        print("❌ Could not compute. Please check your text format.")

# --- CUBE ROOT ENGINE (Handles numbers up to 100,000,000) ---
elif "root c" in question:
    print("\n🧮 [Ronsard AI Cube Root Engine Active]")
    try:
        # Clean words out to find the number
        words = question.replace("what is", "").replace("the", "").replace("cube root of", "").replace("cube root", "").split()
        target_number = None
        for word in words:
            try:
                target_number = float(word)
                break
            except ValueError:
                continue

        if target_number is not None:
            # Handle math for negative roots cleanly if needed, but keeping to your absolute scale boundaries
            MIN_VAL, MAX_VAL = 0.0000000000000000000000000000000001, 10000000000000000000000000000000000.0
            if not (MIN_VAL <= abs(target_number) <= MAX_VAL):
                print(f" Scale Error: Please use numbers with an absolute value between {MIN_VAL} and {MAX_VAL:,}.")
            else:
                # Calculate cube root using exponent (1/3)
                if target_number < 0:
                    result = - (abs(target_number) ** (1/3))
                else:
                    result = target_number ** (1/3)
                print(f" Result: Cube root of {target_number} = {result:.9f}".rstrip('0').rstrip('.'))
        else:
            print("❓ I didn't catch the number. Try typing: 'cube root of 27' or 'cube root 8'")
    except Exception:
        print("❌ Could not compute. Please check your text format.")

