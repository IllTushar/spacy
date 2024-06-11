import spacy

if __name__ == '__main__':
    nlp = spacy.load("en_core_web_sm")
    text = 'I was played'
    doc = nlp(text)

    for token in doc:
        print(token.text, token.lemma_)
