import spacy

if __name__ == '__main__':
    nlp = spacy.load("en_core_web_sm")
    text = '''
    Brexanolone may increase the excretion rate of Aminophylline which could result in a lower serum level and potentially a reduction in efficacy.
    Carbamazepine may increase the Change in thyroid function activities of Brexanolone.
    Brexanolone may increase the excretion rate of Mercaptopurine which could result in a lower serum level and potentially a reduction in efficacy.
    '''
    doc = nlp(text)

    print(list(doc.sents))
    print(len(list(doc.sents)))
