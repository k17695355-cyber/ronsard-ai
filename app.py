import streamlit as st

# 1. Page Configuration (Website Title)
st.set_page_config(page_title="Ronsard AI", page_icon="🤖")
st.title("🤖 Ronsard AI Chatbot")
st.write("Ask me about École Ronsard, Minecraft, or math equations!")

# 2. Web Input Box
user_question = st.text_input("Type your question here:", placeholder="e.g., What is the square root of 64?")

# 3. Process the question when the user presses Enter or types something
if user_question:
    question = user_question.lower()
    
    # --- GREETINGS ---
    if "hello" in question or "hi" in question:
        st.success("Hello there! How can I help you today?")
        
    # --- ECOLE RONSARD FACTS ---
    elif "what is ecole ronsard" in question or "about ecole ronsard" in question:
        st.info("École Ronsard is a leading bilingual (French and English) international school established in 2009 in East Legon, Accra, Ghana.")
        
    elif "where is ecole ronsard" in question or "location" in question:
        st.info("École Ronsard is located at 21-23 Kinshasa Street in East Legon, Accra, Ghana!")

    # --- MINECRAFT ---
    elif "minecraft" in question:
        st.warning("Minecraft is awesome! Make sure to install performance mods like Sodium or OptiFine for the best FPS.")

    # --- MATH: SQUARE ROOT ENGINE ---
    elif "square root" in question:
        try:
            words = question.replace("square root of", "").replace("square root", "").split()
            target_number = None
            for word in words:
                try: target_number = float(word); break
                except ValueError: continue
            
            if target_number is not None:
                if target_number < 0:
                    st.error("⚠️ Scale Error: Please use positive numbers.")
                else:
                    result = target_number ** 0.5
                    st.success(f"➡️ Result: Square root of {target_number} = {result:.9f}".rstrip('0').rstrip('.'))
            else:
                st.error("❓ Couldn't parse the number. Try: 'square root 16'")
        except Exception:
            st.error("❌ Error calculating.")

    # --- MATH: CUBE ROOT ENGINE ---
    elif "cube root" in question:
        try:
            words = question.replace("cube root of", "").replace("cube root", "").split()
            target_number = None
            for word in words:
                try: target_number = float(word); break
                except ValueError: continue
            
            if target_number is not None:
                result = target_number ** (1/3) if target_number >= 0 else - (abs(target_number) ** (1/3))
                st.success(f"➡️ Result: Cube root of {target_number} = {result:.9f}".rstrip('0').rstrip('.'))
            else:
                st.error("❓ Try typing: 'cube root of 27'")
        except Exception:
            st.error("❌ Error calculating.")

    # --- MATH: SQUARING ENGINE ---
    elif "square" in question or "squared" in question:
        try:
            words = question.replace("square", "").replace("squared", "").split()
            target_number = None
            for word in words:
                try: target_number = float(word); break
                except ValueError: continue

            if target_number is not None:
                result = target_number ** 2
                st.success(f"➡️ Result: {target_number} squared = {result:.9f}".rstrip('0').rstrip('.'))
        except Exception:
            st.error("❌ Error calculating.")

    # --- MATH: CUBING ENGINE ---
    elif "cube" in question or "cubed" in question:
        try:
            words = question.replace("cube", "").replace("cubed", "").split()
            target_number = None
            for word in words:
                try: target_number = float(word); break
                except ValueError: continue

            if target_number is not None:
                result = target_number ** 3
                st.success(f"➡️ Result: {target_number} cubed = {result:.9f}".rstrip('0').rstrip('.'))
        except Exception:
            st.error("❌ Error calculating.")

    # --- FALLBACK ---
    else:
        st.error("I'm sorry, I don't know the answer to that question yet.")
