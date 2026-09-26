import os
import random
import math
import streamlit as st
from openai import OpenAI


# =============================================================================
# 1. PAGE CONFIGURATION + DARK CHATGPT-STYLE THEME
# =============================================================================

st.set_page_config(
    page_title="Ronsard AI",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>

.stApp,
div[data-testid="stAppViewMain"] {
    background-color: #171717 !important;
    color: #ececec !important;
}

section[data-testid="stSidebar"] {
    background-color: #212121 !important;
    border-right: 1px solid #2f2f2f !important;
}

div[data-testid="stChatInputContainer"] {
    background-color: transparent !important;
    border: none !important;
}

div[data-testid="stChatInput"] textarea {
    background-color: #2f2f2f !important;
    color: #ececec !important;
    border: 1px solid #424242 !important;
    border-radius: 28px !important;
    padding-left: 15px !important;
}

div[data-testid="stChatMessage"]:has(
    div[data-testid="stChatMessageAvatar"] img[alt="user"]
) {
    background-color: #2f2f2f !important;
    border-radius: 20px !important;
    padding: 12px !important;
    margin-bottom: 12px !important;
    max-width: 80%;
    margin-left: auto;
}

div[data-testid="stChatMessage"]:has(
    div[data-testid="stChatMessageAvatar"] img[alt="assistant"]
) {
    background-color: transparent !important;
    padding: 12px !important;
    margin-bottom: 12px !important;
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
# 2. HUGGING FACE CONNECTION
# =============================================================================

HF_TOKEN = os.environ.get("HF_TOKEN")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN if HF_TOKEN else "hf_placeholder"
)


# =============================================================================
# 3. TITLE
# =============================================================================

st.title("🤖 Ronsard AI Chatbot")
st.write("Welcome to the infinite knowledge hub. Ask me anything!")


# =============================================================================
# 4. CHAT MEMORY
# =============================================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =============================================================================
# 5. SIDEBAR
# =============================================================================

with st.sidebar:

    st.header("⚙️ Chatbot Settings")

    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    st.write("---")

    st.caption("Powered by Ronsard Core v2 & Hugging Face Cloud")


# =============================================================================
# 6. DISPLAY PREVIOUS MESSAGES
# =============================================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# =============================================================================
# 7. CHAT INPUT
# =============================================================================

if user_input := st.chat_input("What do you need 💀 lol:"):

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    user_query = user_input.strip().lower()

    ai_response = ""


    # =========================================================================
    # 8. ASSISTANT RESPONSE
    # =========================================================================

    with st.chat_message("assistant"):


        # =====================================================================
        # LAYER 1 — CUSTOM RESPONSES
        # =====================================================================

        if "hello" in user_query or "hi" in user_query:

            ai_response = "Hello there! How can I help you today?"
            st.markdown(ai_response)


        elif "your name" in user_query:

            ai_response = (
                "I am Ronsard AI, a custom chatbot built in VS Code!"
            )
            st.markdown(ai_response)


        elif "weather" in user_query:

            ai_response = (
                "I can't check the live weather yet, "
                "but it looks like a great day to code!"
            )
            st.markdown(ai_response)


        elif "minecraft" in user_query:

            ai_response = (
                "Minecraft is awesome! Make sure to install performance "
                "mods like Sodium, Lithium, or OptiFine for the best FPS."
            )
            st.markdown(ai_response)


        elif (
            "what is ecole ronsard" in user_query
            or "about ecole ronsard" in user_query
        ):

            ai_response = (
                "École Ronsard is a leading bilingual (French and English) "
                "international school established in 2009, offering a "
                "holistic education."
            )
            st.markdown(ai_response)


        elif (
            "where is ecole ronsard" in user_query
            or "location" in user_query
        ):

            ai_response = (
                "École Ronsard is located at 21-23 Kinshasa Street "
                "in East Legon, Accra, Ghana!"
            )
            st.markdown(ai_response)


        elif (
            "accreditation" in user_query
            or "curriculum" in user_query
        ):

            ai_response = (
                "The school holds dual accreditation from Cambridge "
                "International (for English, Math, and Science) "
                "and LabelFrancÉducation."
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
                "and challenging learning environment."
            )
            st.markdown(ai_response)


        elif (
            "admission process" in user_query
            or "enrollment" in user_query
        ):

            ai_response = (
                "The admission process at École Ronsard involves "
                "an application, assessment, and interview to ensure "
                "the best fit for the student."
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
        # LAYER 2 — MATH ENGINE: SQUARE
        # =====================================================================

        elif "square" in user_query or "squared" in user_query:

            st.caption("🔹 [Ronsard AI Squaring Engine Active]")

            try:

                words = (
                    user_query
                    .replace("what is", "")
                    .replace("square", "")
                    .replace("squared", "")
                    .split()
                )

                target_number = next(
                    (
                        float(word)
                        for word in words
                        if word.replace(".", "", 1).isdigit()
                        or (
                            word.startswith("-")
                            and word[1:].replace(".", "", 1).isdigit()
                        )
                    ),
                    None
                )

                if target_number is not None:

                    result = target_number ** 2

                    ai_response = (
                        f"**Result:** {target_number} squared = "
                        f"{result:.9f}"
                    ).rstrip("0").rstrip(".")

                    st.success(ai_response)

                else:

                    ai_response = (
                        "❓ I didn't catch the number. "
                        "Try typing: `square 5`"
                    )

                    st.warning(ai_response)

            except Exception:

                ai_response = (
                    "❌ Could not compute. "
                    "Please check your text format."
                )

                st.error(ai_response)


        # =====================================================================
        # LAYER 3 — MATH ENGINE: CUBE
        # =====================================================================

        elif "cube" in user_query or "cubed" in user_query:

            st.caption("🔹 [Ronsard AI Cubing Engine Active]")

            try:

                words = (
                    user_query
                    .replace("what is", "")
                    .replace("cube", "")
                    .replace("cubed", "")
                    .split()
                )

                target_number = next(
                    (
                        float(word)
                        for word in words
                        if word.replace(".", "", 1).isdigit()
                        or (
                            word.startswith("-")
                            and word[1:].replace(".", "", 1).isdigit()
                        )
                    ),
                    None
                )

                if target_number is not None:

                    result = target_number ** 3

                    ai_response = (
                        f"**Result:** {target_number} cubed = "
                        f"{result:.9f}"
                    ).rstrip("0").rstrip(".")

                    st.success(ai_response)

                else:

                    ai_response = (
                        "❓ I didn't catch the number. "
                        "Try typing: `cube 3`"
                    )

                    st.warning(ai_response)

            except Exception:

                ai_response = (
                    "❌ Could not compute. "
                    "Please check your text format."
                )

                st.error(ai_response)


        # =====================================================================
        # LAYER 4 — MATH ENGINE: SQUARE ROOT
        # =====================================================================

        elif (
            "square root" in user_query
            or "root" in user_query
        ):

            st.caption("🔹 [Ronsard AI Square Root Engine Active]")

            try:

                words = (
                    user_query
                    .replace("what is", "")
                    .replace("the", "")
                    .replace("square root of", "")
                    .replace("square root", "")
                    .replace("root", "")
                    .split()
                )

                target_number = next(
                    (
                        float(word)
                        for word in words
                        if word.replace(".", "", 1).isdigit()
                    ),
                    None
                )

                if target_number is not None:

                    if target_number < 0:

                        ai_response = (
                            "⚠️ Scale Error: "
                            "Please use positive numbers."
                        )

                        st.error(ai_response)

                    else:

                        result = math.sqrt(target_number)

                        ai_response = (
                            f"**Result:** Square root of "
                            f"{target_number} = {result:.9f}"
                        ).rstrip("0").rstrip(".")

                        st.success(ai_response)

                else:

                    ai_response = (
                        "❓ I didn't catch the number. "
                        "Try typing: `square root of 16`"
                    )

                    st.warning(ai_response)

            except Exception:

                ai_response = (
                    "❌ Could not compute. "
                    "Please check your text format."
                )

                st.error(ai_response)


        # =====================================================================
        # LAYER 5 — AI FALLBACK
        # =====================================================================

        else:

            with st.spinner("Searching cosmic database..."):

                try:

                    response = client.chat.completions.create(

                        model="meta-llama/Llama-3.1-8B-Instruct",

                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are Ronsard AI, a helpful AI "
                                    "assistant. Give clear, accurate, "
                                    "friendly answers. Keep answers "
                                    "reasonably brief."
                                )
                            },
                            {
                                "role": "user",
                                "content": user_input
                            }
                        ],

                        max_tokens=500
                    )

                    ai_response = response.choices[0].message.content

                    st.markdown(ai_response)

                except Exception as e:

                    ai_response = (
                        "❌ The free cloud AI engine encountered "
                        "an error.\n\n"
                        "Make sure your HF_TOKEN is configured correctly."
                    )

                    st.error(ai_response)


    # =========================================================================
    # 9. SAVE ASSISTANT MESSAGE
    # =========================================================================

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })