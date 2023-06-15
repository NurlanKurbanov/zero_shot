import pandas as pd
import googletrans

translator = googletrans.Translator()

docs = ['bar_text.xlsx', 'bar_reddit.xlsx',
        'depr_reddit.xlsx', 'depr_text.xlsx',
        'okr_reddit.xlsx', 'okr_text_clear.xlsx',
        'rpp_reddit.xlsx', 'rpp_text.xlsx',
        'shiz_reddit.xlsx', 'shiz_text.xlsx'
        ]

len_docs = len(docs)

for i, doc in enumerate(docs):
    print(f'docs {i+1}/{len_docs}')
    df = pd.read_excel(doc)

    texts = list(df['text'])
    labels = list(df['label'])
    len_texts = len(texts)
    trans_texts = []
    trans_labels = []
    for j, (text, label) in enumerate(zip(texts, labels)):
        if (j+1) % 30 == 0:
            print(f"                    text {j+1}/{len_texts}")
        tr_text = translator.translate(text, src='ru', dest='en').text
        tr_label = translator.translate(label, src='ru', dest='en').text

        trans_texts.append(tr_text)
        trans_labels.append(tr_label)

    df['text_tr'] = trans_texts
    df['label_tr'] = trans_labels

    df.to_excel('tr_' + doc, index=False)

