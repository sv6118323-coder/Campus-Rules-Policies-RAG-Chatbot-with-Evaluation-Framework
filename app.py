# app.py
# This file creates the visual chat interface using Gradio

import gradio as gr
from chatbot import ask_chatbot  # imports our updated function from chatbot.py

# -------------------------------------------------------
# 🆕 UPDATED chat() FUNCTION
# Now receives both answer + evaluation scores from chatbot.py
# Formats and appends the score panel to the answer
# -------------------------------------------------------
def chat(message, history):
    # Handle new Gradio version (sends message as dict)
    if isinstance(message, dict):
        message = message.get("text", "")

    # Build conversation history for context
    conversation_history = []
    for entry in history:
        if entry["role"] == "user":
            conversation_history.append({
                "role": "user",
                "content": entry["content"]
            })
        else:
            conversation_history.append({
                "role": "assistant",
                "content": entry["content"]
            })

    # ✅ ask_chatbot now returns (answer, eval_scores)
    answer, eval_scores = ask_chatbot(message, conversation_history)

    # --- 🆕 Format the evaluation scores as a readable panel ---
    # This appends a score card below every answer in the chat
    eval_display = f"""

---
📊 **Evaluation Report**
| Metric | Score & Reason |
|--------|---------------|
| 🎯 Faithfulness | {eval_scores['faithfulness']} |
| 🔍 Relevance | {eval_scores['relevance']} |
| 💡 Confidence | {eval_scores['confidence']} |
| ⚠️ Hallucination | {eval_scores['hallucination']} |
"""

    # Combine answer + evaluation panel
    full_response = answer + eval_display

    return full_response


# -------------------------------------------------------
# CREATE THE INTERFACE
# ✅ UPDATED: description now mentions evaluation feature
# -------------------------------------------------------
demo = gr.ChatInterface(
    fn=chat,
    title="🏫 Campus Rules & Policies Chatbot",
    description="""Ask me anything about campus rules, attendance, exams, library, hostel, or fees!
    
📊 **Evaluation Framework Active** — Every answer is automatically scored for Faithfulness, Relevance, and Confidence.""",
    examples=[
        "What is the minimum attendance required?",
        "What are the library borrowing rules?",
        "Can I use my phone in the exam hall?",
        "What time is hostel curfew?",
        "What is the fine for late fee payment?"
    ],
)

# -------------------------------------------------------
# LAUNCH THE APP
# -------------------------------------------------------
if __name__ == "__main__":
    print("🚀 Launching chatbot with Evaluation Framework...")
    print("📌 Open your browser and go to: http://localhost:7860")
    demo.launch(debug=True)
