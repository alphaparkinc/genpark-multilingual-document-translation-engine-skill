from client import DocumentTranslatorClient

def main():
    client = DocumentTranslatorClient()
    res = client.translate_doc(text='Hello World', target_lang='ES')
    print(f"Result for translated_text: {res['translated_text']}")

if __name__ == "__main__":
    main()
