import random
import math
import re


# =============================================================================
# RONSARD AI - NORMAL PYTHON CHATBOT
# =============================================================================

print("=" * 50)
print("🤖 RONSARD AI")
print("=" * 50)
print("Type 'exit' to close the chatbot.")
print()


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_numbers(text):
    """Find numbers in the user's question."""

    matches = re.findall(
        r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)",
        text
    )

    return [float(number) for number in matches]


def format_number(number):
    """Format numbers neatly."""

    if number == 0:
        return "0"

    if abs(number) >= 1e15 or abs(number) < 1e-9:
        return f"{number:.9e}"

    return f"{number:.9f}".rstrip("0").rstrip(".")


# =============================================================================
# MAIN CHAT LOOP
# =============================================================================

while True:

    question = input("\nAsk me a question: ").strip().lower()


    # -------------------------------------------------------------------------
    # EXIT
    # -------------------------------------------------------------------------

    if question in ["exit", "quit", "bye"]:
        print("Ronsard AI: Goodbye! 👋")
        break


    # -------------------------------------------------------------------------
    # BASIC QUESTIONS
    # -------------------------------------------------------------------------

    if "hello" in question or "hi" in question or "hey" in question:

        print("Hello there! 👋 How can I help you today?")


    elif "your name" in question or "who are you" in question:

        print(
            "I am Ronsard AI, a simple Python chatbot "
            "built in VS Code! 🤖"
        )


    elif "weather" in question:

        print(
            "I cannot check live weather yet, "
            "but it looks like a great day to code!"
        )


    elif "minecraft" in question:

        print(
            "Minecraft is awesome! 🎮 "
            "Performance mods such as Sodium and Lithium "
            "can help improve FPS."
        )


    # -------------------------------------------------------------------------
    # ÉCOLE RONSARD
    # -------------------------------------------------------------------------

    elif (
        "what is ecole ronsard" in question
        or "what is école ronsard" in question
        or "about ecole ronsard" in question
        or "about école ronsard" in question
    ):

        print(
            "École Ronsard is a bilingual French and English "
            "international school established in 2009, "
            "offering education from Nursery through Secondary."
        )


    elif (
        "where is ecole ronsard" in question
        or "where is école ronsard" in question
        or "location" in question
    ):

        print(
            "École Ronsard is located at "
            "21-23 Kinshasa Street in East Legon, Accra, Ghana."
        )


    elif (
        "accreditation" in question
        or "curriculum" in question
    ):

        print(
            "École Ronsard offers Cambridge International "
            "and LabelFrancÉducation programmes."
        )


    elif (
        "principal" in question
        or "head teacher" in question
        or "head of school" in question
    ):

        print(
            "The principal of École Ronsard is "
            "Marie-Patricia Agbenyeke."
        )


    elif (
        "campuses" in question
        or "campus" in question
    ):

        print(
            "École Ronsard has two campuses: "
            "one dedicated to Nursery and another for "
            "Primary and Secondary students."
        )


    elif (
        "teachers of ecole ronsard" in question
        or "teachers at ecole ronsard" in question
        or "teachers at école ronsard" in question
    ):

        print(
            "The teachers at École Ronsard are qualified "
            "and experienced educators."
        )


    elif (
        "admission process" in question
        or "enrollment" in question
        or "admission" in question
    ):

        print(
            "The admission process involves an application, "
            "assessment and interview."
        )


    elif (
        "who are the staff in ecole ronsard" in question
        or "staff members" in question
        or "ronsard staff" in question
    ):

        staff_members = [
            "Mrs Jane Doe",
            "Mr Jeffery",
            "Mr Edem",
            "Mrs Pearl",
            "Mrs. Agbenyeke",
            "Mrs Christene",
            "Mr. Divine",
            "Mrs. Authur"
        ]

        random_staff = random.sample(staff_members, 3)

        print("Here are 3 featured staff members:")

        for i, staff in enumerate(random_staff, 1):
            print(f"  [{i}] {staff}")


    # -------------------------------------------------------------------------
    # NURSERY - YEAR 3
    # -------------------------------------------------------------------------

    elif (
        "counting" in question
        or "number recognition" in question
    ):

        print(
            "[Nursery Math] Counting means naming numbers "
            "in order and recognising what numbers look like."
        )


    elif "shapes" in question:

        print(
            "[Nursery Math] Basic 2D shapes include circles, "
            "squares and triangles."
        )


    elif (
        "multiplication" in question
        or "times tables" in question
    ):

        print(
            "[Primary Math] Multiplication is repeated addition. "
            "For example, 3 × 5 = 15."
        )


    # -------------------------------------------------------------------------
    # YEARS 4 - 6
    # -------------------------------------------------------------------------

    elif (
        "fraction" in question
        or "fractions" in question
        or "decimal" in question
        or "decimals" in question
    ):

        print(
            "[Upper Primary Math] A fraction represents part of "
            "a whole. A decimal can represent the same value "
            "using a decimal point."
        )


    elif (
        "area" in question
        or "perimeter" in question
    ):

        print(
            "[Upper Primary Math] Perimeter is the distance "
            "around a shape. Area is the space inside a shape."
        )


    # -------------------------------------------------------------------------
    # YEARS 7 - 9
    # -------------------------------------------------------------------------

    elif (
        "algebra" in question
        or "solve for x" in question
    ):

        print(
            "[Lower Secondary Math] Algebra uses letters "
            "to represent unknown numbers. For example, "
            "if x + 5 = 12, x = 7."
        )


    elif (
        "pythagorean" in question
        or "pythagorean theorem" in question
        or "triangle rule" in question
    ):

        print(
            "[Lower Secondary Math] The Pythagorean Theorem "
            "states that a² + b² = c² in a right-angled triangle."
        )


    # -------------------------------------------------------------------------
    # YEAR 10 / IGCSE
    # -------------------------------------------------------------------------

    elif "quadratic" in question:

        print(
            "[Year 10 IGCSE Math] A quadratic equation contains "
            "a squared variable, such as ax² + bx + c = 0."
        )


    elif (
        "trigonometry" in question
        or "sine" in question
        or "cosine" in question
        or "tangent" in question
    ):

        print(
            "[Year 10 IGCSE Math] Trigonometry studies the "
            "relationship between angles and sides of triangles. "
            "SOH-CAH-TOA is commonly used for right-angled triangles."
        )


    elif "probability" in question:

        print(
            "[Year 10 IGCSE Math] Probability measures how likely "
            "an event is to happen."
        )


    # -------------------------------------------------------------------------
    # SQUARE ROOT
    # IMPORTANT: THIS COMES BEFORE SQUARE
    # -------------------------------------------------------------------------

    elif (
        "square root" in question
        or "sqrt" in question
    ):

        print("\n🧮 [Ronsard AI Square Root Engine Active]")

        numbers = get_numbers(question)

        if not numbers:

            print(
                "❓ I didn't catch the number. "
                "Try: square root of 16"
            )

        else:

            number = numbers[0]

            if number < 0:

                print(
                    "❌ A real square root cannot be calculated "
                    "for a negative number."
                )

            else:

                result = math.sqrt(number)

                print(
                    f"➡️ Result: √{format_number(number)} "
                    f"= {format_number(result)}"
                )


    # -------------------------------------------------------------------------
    # CUBE ROOT
    # IMPORTANT: THIS COMES BEFORE CUBE
    # -------------------------------------------------------------------------

    elif (
        "cube root" in question
        or "cbrt" in question
    ):

        print("\n🧮 [Ronsard AI Cube Root Engine Active]")

        numbers = get_numbers(question)

        if not numbers:

            print(
                "❓ I didn't catch the number. "
                "Try: cube root of 27"
            )

        else:

            number = numbers[0]

            if number < 0:
                result = -abs(number) ** (1 / 3)
            else:
                result = number ** (1 / 3)

            print(
                f"➡️ Result: ∛{format_number(number)} "
                f"= {format_number(result)}"
            )


    # -------------------------------------------------------------------------
    # SQUARE
    # -------------------------------------------------------------------------

    elif (
        "square" in question
        or "squared" in question
    ):

        print("\n🧮 [Ronsard AI Squaring Engine Active]")

        numbers = get_numbers(question)

        if not numbers:

            print(
                "❓ I didn't catch the number. "
                "Try: square 5"
            )

        else:

            number = numbers[0]
            result = number ** 2

            print(
                f"➡️ Result: "
                f"{format_number(number)}² = "
                f"{format_number(result)}"
            )


    # -------------------------------------------------------------------------
    # CUBE
    # -------------------------------------------------------------------------

    elif (
        "cube" in question
        or "cubed" in question
    ):

        print("\n🧮 [Ronsard AI Cubing Engine Active]")

        numbers = get_numbers(question)

        if not numbers:

            print(
                "❓ I didn't catch the number. "
                "Try: cube 3"
            )

        else:

            number = numbers[0]
            result = number ** 3

            print(
                f"➡️ Result: "
                f"{format_number(number)}³ = "
                f"{format_number(result)}"
            )


    # -------------------------------------------------------------------------
    # NORMAL MATH
    # -------------------------------------------------------------------------

    elif any(
        operator in question
        for operator in ["+", "-", "*", "/"]
    ):

        print("\n🧮 [Ronsard AI Calculator Active]")

        numbers = get_numbers(question)

        if len(numbers) < 2:

            print(
                "❓ I couldn't find two numbers. "
                "Try: 25 + 17"
            )

        else:

            num1 = numbers[0]
            num2 = numbers[1]

            if "+" in question:

                result = num1 + num2
                symbol = "+"

            elif "*" in question:

                result = num1 * num2
                symbol = "×"

            elif "/" in question:

                symbol = "÷"

                if num2 == 0:

                    print("❌ You cannot divide by zero.")
                    result = None

                else:

                    result = num1 / num2

            elif "-" in question:

                result = num1 - num2
                symbol = "-"

            else:

                result = None
                symbol = "?"


            if result is not None:

                print(
                    f"➡️ Result: "
                    f"{format_number(num1)} "
                    f"{symbol} "
                    f"{format_number(num2)} = "
                    f"{format_number(result)}"
                )


    # -------------------------------------------------------------------------
    # 2 + 2
    # -------------------------------------------------------------------------

    elif (
        "what is 2+2" in question
        or "what is 2 + 2" in question
        or question == "2+2"
        or question == "2 + 2"
    ):

        print("4")


    # -------------------------------------------------------------------------
    # UNKNOWN QUESTION
    # -------------------------------------------------------------------------

    else:

        print(
            "🤖 I don't know that yet! "
            "Try asking me about École Ronsard, maths, "
            "Minecraft, or one of my other topics."
        )