import spacy

def handler(event, context):
    doc = nlp(event['text'])
    response = [
        {
            'text': ent.text,
            'label': ent.label_,
            'start': ent.start_char,
            'end': ent.end_char
        }
        for ent in doc.ents
        
    ]
    return response

model = 'en_core_web_sm-2.2.5'
m_path = f"/opt/{model}/{model.split('-')[0]}/{model}"
nlp = spacy.load(m_path)