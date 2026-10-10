from difflib import get_close_matches

faqs = {
"what is python": "Python is a programming language.",
"what is ai": "AI means Artificial Intelligence.",
"what is machine learning": "Machine learning helps computers learn from data.",
"what is your name": "I am a College FAQ Chatbot.",
"what is data science": "Data science uses data to find useful information.",
"what is cse": "CSE stands for Computer Science Engineering."
}

print("COLLEGE FAQ CHATBOT")
question = input("Ask your question: ").lower().strip()
matches = get_close_matches(question, faqs.keys(), n=1, cutoff=0.4)

if matches:
print("Chatbot:", faqs[matches[0]])
else:
print("Chatbot: Sorry, I don't know that answer yet.")
Ye past karye hai na phele
