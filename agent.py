from dotenv import load_dotenv
import os
import google.genai as genai

load_dotenv()


# Use either GEMINI_API_KEY or GOOGLE_API_KEY for flexibility
API_KEY = os.getenv("GEMINI_API_KEY")


if not API_KEY:
    print("Error: GEMINI_API_KEY not set.")
    exit()



# Configure the generative AI client (google.genai)
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# --------------------------------------------
# Feature Extraction (EDA / Feature Engineering)
# --------------------------------------------

def extract_features(question):
    return {
        "num_characters": len(question),
        "num_words": len(question.split()),
        "contains_code_symbols": any(sym in question for sym in ["{", "}", "(", ")", ";"]),
        "contains_keywords": any(word in question.lower() for word in ["state", "regex", "parser", "design"])
    }

# --------------------------------------------
# Detect assignment type
# --------------------------------------------

def detect_assignment_type(question):

    q = question.lower()

    if "state machine" in q or "fsm" in q:
        return "Finite State Machine"

    if "regex" in q or "regular expression" in q:
        return "Regex"

    if "grammar" in q or "parser" in q:
        return "Parsing / Grammar"

    if "design" in q or "architecture" in q:
        return "Software Design"

    return "General Programming"


# --------------------------------------------
# Explain assignment
# --------------------------------------------

def explain_assignment(question):

    assignment_type = detect_assignment_type(question)
    features = extract_features(question)

    prompt = f"""
You are an AI Teaching Assistant helping a student understand an assignment.

Your job is to SUPPORT LEARNING, not solve the assignment.

Rules:
- Do NOT provide full solutions or final code.
- Explain what the assignment is asking.
- Break the problem into clear steps.
- Suggest how the student should approach solving it.
- Provide hints or concepts they should research.

Assignment Type:
{assignment_type}

Student Assignment:
{question}

Respond with:

1. What the assignment is asking
2. Key programming concepts involved
3. Suggested approach to solve it
4. Common mistakes students make
"""

    try:


        response = model.generate_content(prompt)
        return response.text, features

    except Exception as e:

        return f"Error contacting AI service:\n{e}", features


# --------------------------------------------
# Main Program Loop
# --------------------------------------------

print("\nAI Assignment Explainer")
print("-----------------------")

while True:

    question = input("\nPaste your assignment question (or type 'exit'): \n")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    print("\n--- Extracted Features (EDA) ---\n")

    result, features = explain_assignment(question)

    print(features)

    print("\n--- AI Model Output ---\n")

    print(result)

    print("\n--- End of Response ---\n")