from googletrans import Translator

def translate_to_english(text):
    """
    Translates given text from any language to English.
    
    Args:
        text (str): Text to translate in any language
    
    Returns:
        str: Translated text in English
        str: Source language code (e.g., 'es' for Spanish)
    """
    try:
        # Initialize the translator
        translator = Translator()
        
        # Detect the language and translate to English
        translation = translator.translate(text, dest='en')
        
        return translation.text, translation.src
    except Exception as e:
        return f"Translation error: {str(e)}", None

def main():
    # Example usage
    while True:
        # Get input from user
        text = input("\nEnter text to translate (or 'q' to quit): ")
        
        # Check if user wants to quit
        if text.lower() == 'q':
            print("Goodbye!")
            break
        
        # Translate the text
        translated_text, source_lang = translate_to_english(text)
        
        # Print results
        if source_lang:
            print(f"\nSource language: {source_lang}")
            print(f"Translation: {translated_text}")
        else:
            print(translated_text)  # This would be the error message

if __name__ == "__main__":
    main()