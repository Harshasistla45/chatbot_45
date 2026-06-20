from groq import Groq
import os

# YOUR API KEY HERE - REPLACE THE STRING BELOW
os.environ["GROQ_API_KEY"] = "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"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

print("🚀 Groq Chatbot Started! Type 'exit' to quit")
print("💬 Ask me anything about AI, DSA, cricket, or your stupid wrist injury 😂")

while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == 'exit':
        print("👋 Bye bye Harsha! Go rest that wrist!")
        break
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful, funny assistant for Harsha, an ECE student in Bengaluru. Be sarcastic, playful, and mention cricket sometimes."},
            {"role": "user", "content": user_input}
        ],
        model="llama-3.3-70b-versatile",
    )
    
    print(f"\n🤖 Groq: {chat_completion.choices[0].message.content}")