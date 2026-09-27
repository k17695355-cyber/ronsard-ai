import os
import random
import math
import re
import streamlit as st
from openai import OpenAI

# =============================================================================
# 1. PAGE CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title="Ronsard AI",
    page_icon="🤖",
    layout="centered"
)

# =============================================================================
# 2. DYNAMIC THEME
# =============================================================================

st.markdown("""
<style>

@media (prefers-color-scheme: dark) {
    :root {
        --bg-core: #000000;
        --bg-secondary: #121212;
        --text-core: #ffffff;
        --border-core: #2d2d2d;
        --btn-hover: #1f1f1f;
    }
}

@media (prefers-color-scheme: light) {
    :root {
        --bg-core: #ffffff;
        --bg-secondary: #f4f4f4;
        --text-core: #000000;
        --border-core: #e0e0e0;
        --btn-hover: #eaeaea;
    }
}

html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewMain"] {
    background-color: var(--bg-core) !important;
    color: var(--text-core) !important;
}

section[data-testid="stSidebar"] {
    background-color: var(--bg-secondary) !important;
    border-right: 1px solid var(--border-core) !important;
}

section[data-testid="stSidebar"] * {
    color: var(--text-core) !important;
}

h1, h2, h3, h4, h5, h6, p, span, label, li {
    color: var(--text-core) !important;
}

[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
}

[data-testid="stChatMessage"]:has(
    [data-testid="stChatMessageAvatar"] img[alt="user"]
) {
    background-color: var(--bg-secondary) !important;
    color: var(--text-core) !important;
    border-radius: 18px !important;
    padding: 12px 18px !important;
    margin-left: auto !important;
    max-width: 75% !important;
    width: fit-content !important;
    border: 1px solid var(--border-core) !important;
}

[data-testid="stChatMessage"]:has(
    [data-testid="stChatMessageAvatar"] img[alt="assistant"]
) {
    background-color: transparent !important;
    color: var(--text-core) !important;
    max-width: 100% !important;
}

div[data-testid="stChatInputContainer"],
div[data-testid="stChatInputContainer"] > div {
    background-color: var(--bg-core) !important;
    border: none !important;
    box-shadow: none !important;
}

[data-testid="stChatInput"] textarea {
    background-color: var(--bg-secondary) !important;
    color: var(--text-core) !important;
    border: 1px solid var(--border-core) !important;
    border-radius: 26px !important;
    padding: 14px 55px 14px 18px !important;
    font-size: 16px !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: var(--text-core) !important;
    opacity: 0.55 !important;
}

div.stButton > button {
    background-color: var(--bg-secondary) !important;
    color: var(--text-core) !important;
    border: 1px solid var(--border-core) !important;
    border-radius: 14px !important;
    min-height: 70px !important;
    padding: 14px 16px !important;
    text-align: left !important;
    width: 100% !important;
    transition: all 0.15s ease !important;
}

div.stButton > button:hover {
    background-color: var(--btn-hover) !important;
}

section[data-testid="stSidebar"] div.stButton > button {
    min-height: 45px !important;
    text-align: center !important;
}

hr {
    border-color: var(--border-core) !important;
}

header {
    background: transparent !important;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =============================================================================
# 3. HUGGING FACE CLOUD API
# =============================================================================

HF_TOKEN = os.environ.get("HF_TOKEN")
client = None

if HF_TOKEN:
    try:
        client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=HF_TOKEN
        )
    except Exception:
        client = None

# =============================================================================
# 4. BRAND HEADER
# =============================================================================

st.markdown(
    """
    <div style="
        text-align: center;
        padding-top: 25px;
        padding-bottom: 20px;
    ">
        <h1 style="font-size: 30px; margin-bottom: 5px;">
            🤖 Ronsard AI
        </h1>

        <p style="opacity: 0.6; font-size: 15px;">
            Your intelligent knowledge hub
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =============================================================================
# 5. SESSION STATE
# =============================================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

card_prompt = None

# =============================================================================
# 6. SIDEBAR
# =============================================================================

with st.sidebar:

    st.header("⚙️ Chatbot Settings")

    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    st.write("---")

    st.caption(
        "Powered by Ronsard Core v3 & Hugging Face Cloud"
    )

# =============================================================================
# 7. MATH FUNCTIONS
# =============================================================================

def get_numbers(text):
    matches = re.findall(
        r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)",
        text
    )

    return [float(number) for number in matches]


def format_number(number):

    if number == 0:
        return "0"

    if abs(number) >= 1e15 or abs(number) < 1e-9:
        return f"{number:.9e}"

    return f"{number:.9f}".rstrip("0").rstrip(".")


# =============================================================================
# 8. DISPLAY OLD MESSAGES
# =============================================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =============================================================================
# 9. QUICK SUGGESTIONS
# =============================================================================

if len(st.session_state.messages) == 0:

    st.write("---")

    st.write("✨ **Quick Suggestion Shortcuts**")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🏫 About École Ronsard\nLearn about curriculum & origins"
        ):
            card_prompt = "what is ecole ronsard"

        if st.button(
            "🧮 Math Squaring Engine\nCalculate values up to billions"
        ):
            card_prompt = "square 12"

    with col2:

        if st.button(
            "🎮 Minecraft Optimization Tips\nMaximize frames per second"
        ):
            card_prompt = "minecraft"

        if st.button(
            "🌍 Ask Local Cloud AI\nTest the Llama-3 fallback brain"
        ):
            card_prompt = "explain black holes like I am five"

    st.write("---")

# =============================================================================
# 10. CHAT INPUT
# =============================================================================

typed_input = st.chat_input("What do you need 💀 lol?")

user_input = card_prompt if card_prompt else typed_input

# =============================================================================
# 11. MAIN CHAT SYSTEM
# =============================================================================

if user_input:

    # -------------------------------------------------------------------------
    # SHOW USER MESSAGE
    # -------------------------------------------------------------------------

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    user_query = user_input.strip().lower()

    ai_response = ""

    # -------------------------------------------------------------------------
    # ASSISTANT RESPONSE
    # -------------------------------------------------------------------------

    with st.chat_message("assistant"):

        # =====================================================================
        # LAYER 1 — BASIC INFORMATION
        # =====================================================================

        if user_query in ["hello", "hi", "hey"]:

            ai_response = (
                "Hello there! 👋 How can I help you today?"
            )

            st.markdown(ai_response)

        elif (
            "your name" in user_query
            or "who are you" in user_query
        ):

            ai_response = (
                "I am Ronsard AI, a custom chatbot built in Python! 🤖"
            )

            st.markdown(ai_response)

        elif "weather" in user_query:

            ai_response = (
                "I cannot check live weather yet, "
                "but it looks like a great day to code! ☀️"
            )

            st.markdown(ai_response)

        # =====================================================================
        # MINECRAFT
        # =====================================================================

        elif "minecraft" in user_query:

            ai_response = (
                "Minecraft is awesome! 🎮\n\n"
                "Performance mods such as Sodium and Lithium "
                "can help improve FPS."
            )

            st.markdown(ai_response)

        # =====================================================================
        # ÉCOLE RONSARD
        # =====================================================================

        elif (
            "what is ecole ronsard" in user_query
            or "what is école ronsard" in user_query
            or "about ecole ronsard" in user_query
            or "about école ronsard" in user_query
        ):

            ai_response = (
                "École Ronsard is a bilingual French and English "
                "international school established in 2009, offering "
                "education from Nursery through Secondary."
            )

            st.markdown(ai_response)

        elif (
            "where is ecole ronsard" in user_query
            or "where is école ronsard" in user_query
            or user_query == "location"
        ):

            ai_response = (
                "École Ronsard is located at "
                "21-23 Kinshasa Street in East Legon, Accra, Ghana."
            )

            st.markdown(ai_response)

        elif (
            "accreditation" in user_query
            or "curriculum" in user_query
        ):

            ai_response = (
                "École Ronsard offers Cambridge International "
                "and LabelFrancÉducation programmes."
            )

            st.markdown(ai_response)

        elif (
            "principal" in user_query
            or "head teacher" in user_query
            or "head of school" in user_query
        ):

            ai_response = (
                "The principal of École Ronsard is "
                "Marie-Patricia Agbenyeke."
            )

            st.markdown(ai_response)

        elif (
            "campuses" in user_query
            or "campus" in user_query
        ):

            ai_response = (
                "École Ronsard has two campuses: one dedicated "
                "to Nursery and another for Primary and Secondary students."
            )

            st.markdown(ai_response)

        elif (
            "teachers of ecole ronsard" in user_query
            or "teachers at ecole ronsard" in user_query
            or "teachers at école ronsard" in user_query
        ):

            ai_response = (
                "The teachers at École Ronsard are qualified and "
                "experienced educators dedicated to a nurturing environment."
            )

            st.markdown(ai_response)

        elif (
            "admission process" in user_query
            or "enrollment" in user_query
            or "admission" in user_query
        ):

            ai_response = (
                "The admission process involves an application, "
                "assessment and interview."
            )

            st.markdown(ai_response)

        elif (
            "who are the staff in ecole ronsard" in user_query
            or "staff members" in user_query
            or "ronsard staff" in user_query
        ):

            staff_members = [
                "Mrs Jane Doe",
                "Mr Jeffery",
                "Mr Edem",
                "Mrs Pearl",
                "Mrs Agbenyeke",
                "Mrs Christene",
                "Mr Divine",
                "Mrs Authur"
            ]

            random_staff = random.sample(staff_members, 3)

            ai_response = (
                "Here are 3 featured staff members:\n\n"
                + "\n".join(
                    [
                        f"**[{i}]** {staff}"
                        for i, staff in enumerate(random_staff, 1)
                    ]
                )
            )

            st.markdown(ai_response)

        # =====================================================================
        # LAYER 1B — SCHOOL COURSE DETAILS
        # =====================================================================

        elif (
            "counting" in user_query
            or "number recognition" in user_query
        ):

            ai_response = (
                "[Nursery Math] Counting means naming numbers "
                "in order and recognising what numbers look like."
            )

            st.markdown(ai_response)

        elif "shapes" in user_query:

            ai_response = (
                "[Nursery Math] Basic 2D shapes include "
                "circles, squares and triangles."
            )

            st.markdown(ai_response)

        elif (
            "multiplication" in user_query
            or "times tables" in user_query
        ):

            ai_response = (
                "[Primary Math] Multiplication is repeated addition. "
                "For example, 3 × 5 = 15."
            )

            st.markdown(ai_response)

        elif (
            "fraction" in user_query
            or "fractions" in user_query
            or "decimal" in user_query
            or "decimals" in user_query
        ):

            ai_response = (
                "[Upper Primary Math] A fraction represents part "
                "of a whole. A decimal can represent the same value "
                "using a decimal point."
            )

            st.markdown(ai_response)

        elif (
            "area" in user_query
            or "perimeter" in user_query
        ):

            ai_response = (
                "[Upper Primary Math] Perimeter is the distance "
                "around a shape. Area is the space inside a shape."
            )

            st.markdown(ai_response)

        elif (
            "algebra" in user_query
            or "solve for x" in user_query
        ):

            ai_response = (
                "[Lower Secondary Math] Algebra uses letters to "
                "represent unknown numbers. For example, "
                "if x + 5 = 12, x = 7."
            )

            st.markdown(ai_response)

        elif (
            "pythagorean" in user_query
            or "pythagorean theorem" in user_query
            or "triangle rule" in user_query
        ):

            ai_response = (
                "[Lower Secondary Math] The Pythagorean Theorem "
                "states that a² + b² = c² in a right-angled triangle."
            )

            st.markdown(ai_response)

        elif "quadratic" in user_query:

            ai_response = (
                "[Year 10 IGCSE Math] A quadratic equation contains "
                "a squared variable, such as ax² + bx + c = 0."
            )

            st.markdown(ai_response)

        elif (
            "trigonometry" in user_query
            or "sine" in user_query
            or "cosine" in user_query
            or "tangent" in user_query
        ):

            ai_response = (
                "[Year 10 IGCSE Math] Trigonometry studies the "
                "relationship between angles and sides of triangles. "
                "SOH-CAH-TOA is commonly used."
            )

            st.markdown(ai_response)

        elif "probability" in user_query:

            ai_response = (
                "[Year 10 IGCSE Math] Probability measures how "
                "likely an event is to happen."
            )

            st.markdown(ai_response)

        # =====================================================================
        # LAYER 2 — SQUARE ROOT
        # =====================================================================

        elif (
            "square root" in user_query
            or "sqrt" in user_query
        ):

            st.caption(
                "🔹 *[Ronsard AI Square Root Engine Active]*"
            )

            numbers = get_numbers(user_query)

            if not numbers:

                ai_response = (
                    "❓ I didn't catch the number. "
                    "Try: square root of 16"
                )

                st.warning(ai_response)

            else:

                number = numbers[0]

                if number < 0:

                    ai_response = (
                        "❌ A real square root cannot be "
                        "calculated for a negative number."
                    )

                    st.error(ai_response)

                else:

                    result = math.sqrt(number)

                    ai_response = (
                        f"➡️ Result: √{format_number(number)} = "
                        f"{format_number(result)}"
                    )

                    st.success(ai_response)

        # =====================================================================
        # LAYER 2 — CUBE ROOT
        # =====================================================================

        elif (
            "cube root" in user_query
            or "cbrt" in user_query
        ):

            st.caption(
                "🔹 *[Ronsard AI Cube Root Engine Active]*"
            )

            numbers = get_numbers(user_query)

            if not numbers:

                ai_response = (
                    "❓ I didn't catch the number. "
                    "Try: cube root of 27"
                )

                st.warning(ai_response)

            else:

                number = numbers[0]

                if number < 0:
                    result = -((-number) ** (1 / 3))
                else:
                    result = number ** (1 / 3)

                ai_response = (
                    f"➡️ Result: ∛{format_number(number)} = "
                    f"{format_number(result)}"
                )

                st.success(ai_response)

        # =====================================================================
        # LAYER 2 — SQUARE
        # =====================================================================

        elif (
            "square" in user_query
            or "squared" in user_query
        ):

            st.caption(
                "🔹 *[Ronsard AI Squaring Engine Active]*"
            )

            numbers = get_numbers(user_query)

            if not numbers:

                ai_response = (
                    "❓ I didn't catch the number. "
                    "Try: square 5"
                )

                st.warning(ai_response)

            else:

                number = numbers[0]

                result = number ** 2

                ai_response = (
                    f"➡️ Result: {format_number(number)}² = "
                    f"{format_number(result)}"
                )

                st.success(ai_response)

        # =====================================================================
        # LAYER 2 — CUBE
        # =====================================================================

        elif (
            "cube" in user_query
            or "cubed" in user_query
        ):

            st.caption(
                "🔹 *[Ronsard AI Cubing Engine Active]*"
            )

            numbers = get_numbers(user_query)

            if not numbers:

                ai_response = (
                    "❓ I didn't catch the number. "
                    "Try: cube 3"
                )

                st.warning(ai_response)

            else:

                number = numbers[0]

                result = number ** 3

                ai_response = (
                    f"➡️ Result: {format_number(number)}³ = "
                    f"{format_number(result)}"
                )

                st.success(ai_response)

        # =====================================================================
        # LAYER 2 — BASIC CALCULATOR
        # =====================================================================

        elif any(
            op in user_query
            for op in ["+", "-", "*", "/"]
        ):

            st.caption(
                "🔹 *[Ronsard AI Calculator Active]*"
            )

            numbers = get_numbers(user_query)

            if len(numbers) < 2:

                ai_response = (
                    "❓ I couldn't find two numbers. "
                    "Try: 25 + 17"
                )

                st.warning(ai_response)

            else:

                num1 = numbers[0]
                num2 = numbers[1]

                if "+" in user_query:

                    result = num1 + num2
                    symbol = "+"

                elif "*" in user_query:

                    result = num1 * num2
                    symbol = "×"

                elif "/" in user_query:

                    symbol = "÷"

                    if num2 == 0:

                        ai_response = (
                            "❌ You cannot divide by zero."
                        )

                        st.error(ai_response)

                        result = None

                    else:

                        result = num1 / num2

                elif "-" in user_query:

                    result = num1 - num2
                    symbol = "-"

                else:

                    result = None
                    symbol = "?"

                if result is not None:

                    ai_response = (
                        f"➡️ Result: "
                        f"{format_number(num1)} {symbol} "
                        f"{format_number(num2)} = "
                        f"{format_number(result)}"
                    )

                    st.success(ai_response)

        # =====================================================================
        # 2 + 2
        # =====================================================================

        elif user_query.replace(" ", "") == "2+2":

            ai_response = "4"

            st.markdown(ai_response)

        # =====================================================================
        # EXIT
        # =====================================================================

        elif user_query in ["exit", "quit", "bye"]:

            ai_response = (
                "Ronsard AI: Goodbye! 👋"
            )

            st.markdown(ai_response)

        # =====================================================================
        # LAYER 3 — HUGGING FACE AI FALLBACK
        # =====================================================================

        else:

            if client is not None:

                with st.spinner(
                    "Searching cosmic database..."
                ):

                    try:

                        response = client.chat.completions.create(
                            model="meta-llama/Meta-Llama-3-8B-Instruct",

                            messages=[
                                {
                                    "role": "system",
                                    "content": (
                                        "You are Ronsard AI, a helpful "
                                        "AI assistant. Give clear, "
                                        "friendly and brief answers."
                                    )
                                },
                                {
                                    "role": "user",
                                    "content": user_input
                                }
                            ],

                            max_tokens=500
                        )

                        ai_response = (
                            response.choices[0]
                            .message
                            .content
                        )

                        st.markdown(ai_response)

                    except Exception as error:

                        ai_response = (
                            "❌ The cloud AI encountered an error. "
                            "Please try again."
                        )

                        st.error(ai_response)

            else:

                ai_response = (
                    "❌ Cloud brain unavailable.\n\n"
                    "Please configure your **HF_TOKEN** secret "
                    "in your Streamlit Cloud settings."
                )

                st.error(ai_response)

    # =========================================================================
    # SAVE ASSISTANT RESPONSE
    # =========================================================================

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    # =========================================================================
    # REFRESH
    # =========================================================================

    st.rerun()