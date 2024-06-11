import spacy
from beautifultable import BeautifulTable

if __name__ == '__main__':
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(
        "Brexanolone may increase the excretion rate of Aminophylline which could result in a U.K lower serum level and potentially a reduction in efficacy.")

    table = BeautifulTable()

    table.columns.header = ['Token', 'POS', 'TAG', 'Dep', 'Shape', 'is_alpha', 'is_stop']
    for token in doc:
        table.rows.append([token, token.pos_, token.tag_, token.dep_, token.shape, token.is_alpha, token.is_stop])

    print(table)
