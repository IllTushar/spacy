import spacy

if __name__ == '__main__':
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(
        "Brexanolone may increase the excretion rate of Aminophylline which could result in a U.K lower serum level and potentially a reduction in efficacy.")
    for token in doc:
        print(token.text)
