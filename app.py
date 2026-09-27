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
# 2. CHATGPT-STYLE RONSARD AI DESIGN
# =============================================================================

st.markdown("""
<style>

/* ============================================================
   MAIN APP
   ============================================================ */

.stApp {
    background: var(--background-color) !important;
}

[data-testid="stAppViewContainer"] {
    background: var(--background-color) !important;
}

[data-testid="stAppViewMain"] {
    background: var(--background-color) !important;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background: var(--secondary-background-color) !important;
    border-right: 1px solid var(--border-color) !important;
}

section[data-testid="stSidebar"] * {
    color: var(--text-color) !important;
}


/* ============================================================
   TITLE
   ============================================================ */

h1 {
    font-weight: 700 !important;
    letter-spacing: -1px !important;
}


/* ============================================================
   CHAT AREA
   ============================================================ */

[data-testid="stChatMessage"] {
    border: none !important;
    background: transparent !important;
    padding-top: 14px !important;
    padding-bottom: 14px !important;
}


/* ============================================================
   USER MESSAGE
   ============================================================ */

[data-testid="stChatMessage"]:has(
    [data-testid="stChatMessageAvatar"] img[alt="user"]
) {
    background: var(--secondary-background-color) !important;
    border-radius: 18px !important;
    padding: 12px 18px !important;
    margin-left: auto !important;
    max-width: 75% !important;
    width: fit-content !important;
}


/* ============================================================
   ASSISTANT MESSAGE
   ============================================================ */

[data-testid="stChatMessage"]:has(
    [data-testid="stChatMessageAvatar"] img[alt="assistant"]
) {
    background: transparent !important;
    max-width: 100% !important;
}


/* ============================================================
   CHAT TEXT
   ============================================================ */

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] span {
    color: var(--text-color) !important;
    line-height: 1.6 !important;
}


/* ============================================================
   CHAT INPUT OUTER AREA
   ============================================================ */

[data-testid="stChatInputContainer"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding-bottom: 18px !important;
}


/* ============================================================
   CHAT INPUT BOX
   ============================================================ */

[data-testid="stChatInput"] {
    background: transparent !important;
    border: none !important;
}


/* ============================================================
   TEXT AREA
   ============================================================ */

[data-testid="stChatInput"] textarea {
    background: var(--secondary-background-color) !important;
    color: var(--text-color) !important;

    border: 1px solid var(--border-color) !important;

    border-radius: 26px !important;

    padding: 14px 55px 14px 18px !important;

    font-size: 16px !important;

    min-height: 52px !important;

    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08) !important;
}


/* ============================================================
   INPUT PLACEHOLDER
   ============================================================ */

[data-testid="stChatInput"] textarea::placeholder {
    color: var(--text-color) !important;
    opacity: 0.55 !important;
}


/* ============================================================
   INPUT FOCUS
   ============================================================ */

[data-testid="stChatInput"] textarea:focus {
    border-color: var(--border-color) !important;
    outline: none !important;
}


/* ============================================================
   SEND BUTTON
   ============================================================ */

[data-testid="stChatInput"] button {
    border-radius: 50% !important;
}


/* ============================================================
   QUICK SUGGESTION CARDS
   ============================================================ */

div.stButton > button {
    background: var(--secondary-background-color) !important;

    color: var(--text-color) !important;

    border: 1px solid var(--border-color) !important;

    border-radius: 14px !important;

    min-height: 70px !important;

    padding: 14px 16px !important;

    text-align: left !important;

    transition:
        background 0.15s ease,
        transform 0.15s ease,
        border 0.15s ease !important;
}


/* ============================================================
   CARD HOVER
   ============================================================ */

div.stButton > button:hover {
    background: var(--background-color) !important;

    border-color: var(--border-color) !important;

    transform: translateY(-1px) !important;
}


/* ============================================================
   CLEAR CHAT BUTTON
   ============================================================ */

section[data-testid="stSidebar"] div.stButton > button {
    min-height: 45px !important;

    border-radius: 10px !important;

    text-align: center !important;
}


/* ============================================================
   DIVIDERS
   ============================================================ */

hr {
    border-color: var(--border-color) !important;
}


/* ============================================================
   TOP HEADER
   ============================================================ */

header {
    background: transparent !important;
}


/* ============================================================
   HIDE STREAMLIT FOOTER
   ============================================================ */

footer {
    visibility: hidden;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 768px) {

    [data-testid="stChatMessage"] {
        padding-left: 8px !important;
        padding-right: 8px !important;
    }

    [data-testid="stChatMessage"]:has(
        [data-testid="stChatMessageAvatar"] img[alt="user"]
    ) {
        max-width: 90% !important;
    }

}

</style>
""", unsafe_allow_html=True)

# =============================================================================
# 5. CHAT MEMORY INITIALIZATION
# =============================================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

card_prompt = None


# =============================================================================
# 6. SIDEBAR MANAGEMENT
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
# 7. HELPER FUNCTIONS
# =============================================================================

def get_number(text):

    match = re.search(
        r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)",
        text
    )

    if match:
        return float(match.group())

    return None


def format_number(number):

    if number == 0:
        return "0"

    if abs(number) >= 1e15 or abs(number) < 1e-9:
        return f"{number:.9e}"

    return f"{number:.9f}".rstrip("0").rstrip(".")


# =============================================================================
# 8. DISPLAY PREVIOUS CHAT MESSAGES
# =============================================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# =============================================================================
# 9. QUICK SUGGESTION SHORTCUTS
# =============================================================================

if len(st.session_state.messages) == 0:

    st.write("---")

    st.write(
        "✨ **Quick Suggestion Shortcuts** "
        "(Click one to test instantly!)"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🏫 About École Ronsard\n"
            "Learn about curriculum & origins"
        ):
            card_prompt = "what is ecole ronsard"

        if st.button(
            "🧮 Math Squaring Engine\n"
            "Calculate values up to billions"
        ):
            card_prompt = "square 12"

    with col2:

        if st.button(
            "🎮 Minecraft Optimization Tips\n"
            "Maximize frames per second"
        ):
            card_prompt = "minecraft"

        if st.button(
            "🌍 Ask Local Cloud AI\n"
            "Test the global Llama-3 fallback brain"
        ):
            card_prompt = "explain black holes like I am five"

    st.write("---")


# =============================================================================
# 10. CHAT INPUT
# =============================================================================

typed_input = st.chat_input(
    "What do you need 💀 lol:"
)

user_input = None

if card_prompt:
    user_input = card_prompt

elif typed_input:
    user_input = typed_input


# =============================================================================
# 11. MAIN CHAT PROCESSING
# =============================================================================

if user_input:

    # -------------------------------------------------------------------------
    # DISPLAY USER MESSAGE
    # -------------------------------------------------------------------------

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    user_query = user_input.strip().lower()

    ai_response = ""


    # =========================================================================
    # ASSISTANT RESPONSE
    # =========================================================================

    with st.chat_message("assistant"):


        # =====================================================================
        # LAYER 1 — CUSTOM RESPONSES & SCHOOL KNOWLEDGE
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
                "I cannot check live weather yet, but I can answer "
                "lots of other questions!"
            )

            st.markdown(ai_response)


        elif "minecraft" in user_query:

            ai_response = (
                "Minecraft is awesome! 🎮 Performance mods such as "
                "Sodium and Lithium can help improve FPS."
            )

            st.markdown(ai_response)


        elif (
            "what is ecole ronsard" in user_query
            or "what is école ronsard" in user_query
            or "about ecole ronsard" in user_query
            or "about école ronsard" in user_query
        ):

            ai_response = (
                "École Ronsard is a bilingual French and English "
                "international school established in 2009."
            )

            st.markdown(ai_response)


        elif (
            "where is ecole ronsard" in user_query
            or "where is école ronsard" in user_query
        ):

            ai_response = (
                "École Ronsard is located at 21-23 Kinshasa Street "
                "in East Legon, Accra, Ghana."
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
            or "head" in user_query
        ):

            ai_response = (
                "The principal of École Ronsard is "
                "Marie-Patricia Agbenyeke."
            )

            st.markdown(ai_response)


        elif (
            "teachers of ecole ronsard" in user_query
            or "teachers at ecole ronsard" in user_query
        ):

            ai_response = (
                "The teachers at École Ronsard are highly qualified "
                "and experienced, dedicated to providing a nurturing "
                "environment."
            )

            st.markdown(ai_response)


        elif (
            "admission process" in user_query
            or "enrollment" in user_query
        ):

            ai_response = (
                "The admission process at École Ronsard involves "
                "an application, assessment, and interview to ensure "
                "the best fit."
            )

            st.markdown(ai_response)


        elif (
            "who are the staff in ecole ronsard" in user_query
            or "staff members" in user_query
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

            random_staff = random.sample(
                staff_members,
                3
            )

            ai_response = (
                "Here are 3 featured staff members:\n\n"
                + "\n".join(
                    [
                        f"**[{i}]** {staff}"
                        for i, staff in enumerate(
                            random_staff,
                            1
                        )
                    ]
                )
            )

            st.markdown(ai_response)


        # =====================================================================
        # LAYER 2 — CUSTOM MATH ENGINES
        # =====================================================================

        elif (
            "square" in user_query
            or "squared" in user_query
        ):

            st.caption(
                "🔹 *[Ronsard AI Squaring Engine Active]*"
            )

            target_number = get_number(user_query)

            if target_number is not None:

                try:

                    result = target_number ** 2

                    ai_response = (
                        f"**Result:** {target_number} squared = "
                        f"{format_number(result)}"
                    )

                    st.success(ai_response)

                except Exception:

                    ai_response = "❌ Value overflow error."

                    st.error(ai_response)

            else:

                ai_response = (
                    "❓ Try typing: `square 5`"
                )

                st.warning(ai_response)


        elif (
            "cube" in user_query
            or "cubed" in user_query
        ):

            st.caption(
                "🔹 *[Ronsard AI Cubing Engine Active]*"
            )

            target_number = get_number(user_query)

            if target_number is not None:

                try:

                    result = target_number ** 3

                    ai_response = (
                        f"**Result:** {target_number} cubed = "
                        f"{format_number(result)}"
                    )

                    st.success(ai_response)

                except Exception:

                    ai_response = "❌ Value overflow error."

                    st.error(ai_response)

            else:

                ai_response = (
                    "❓ Try typing: `cube 3`"
                )

                st.warning(ai_response)


        elif (
            "square root" in user_query
            or "root s" in user_query
        ):

            st.caption(
                "🔹 *[Ronsard AI Square Root Engine Active]*"
            )

            target_number = get_number(user_query)

            if target_number is not None:

                if target_number < 0:

                    ai_response = (
                        "⚠️ Scale Error: Please use positive numbers."
                    )

                    st.error(ai_response)

                else:

                    result = math.sqrt(target_number)

                    ai_response = (
                        f"**Result:** Square root of "
                        f"{target_number} = "
                        f"{format_number(result)}"
                    )

                    st.success(ai_response)

            else:

                ai_response = (
                    "❓ Try typing: `square root 16`"
                )

                st.warning(ai_response)


        # =====================================================================
        # LAYER 3 — HUGGING FACE CLOUD FALLBACK
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
                                        "You are Ronsard AI, a brilliant "
                                        "AI assistant. Give clear, helpful "
                                        "and reasonably brief answers."
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
                            .message.content
                        )

                        st.markdown(ai_response)


                    except Exception:

                        ai_response = (
                            "❌ The free cloud engine encountered "
                            "a slight error. Try hitting enter one "
                            "more time!"
                        )

                        st.error(ai_response)


            else:

                ai_response = (
                    "❌ Cloud brain unavailable. Configure your "
                    "HF_TOKEN secret on Streamlit Cloud settings!"
                )

                st.error(ai_response)


    # =========================================================================
    # SAVE ASSISTANT RESPONSE
    # =========================================================================

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })