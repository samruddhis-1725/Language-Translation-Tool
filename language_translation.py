from deep_translator import GoogleTranslator

def translate_text(text, target_language="hi"):
    try:
        result = GoogleTranslator(
            source="auto",
            target=target_language
        ).translate(text)
        return result
    except Exception:
        return "Translation service is temporarily unavailable."

print("LANGUAGE TRANSLATION TOOL")
print("1. Hindi")
print("2. Marathi")
print("3. French")

choice = input("Choose target language (1/2/3): ")

languages = {
    "1": "hi",
    "2": "mr",
    "3": "fr"
}

if choice in languages:
    text = input("Enter text to translate: ")
    print("Translation:", translate_text(text, languages[choice]))
else:
    print("Invalid choice.")
