from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

def classify(text_blocks):
    named_entities = []

    for block in text_blocks:
        named_entities.append(get_named_entities(block))

    return named_entities

def get_named_entities(string):
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    ner_results = nlp(string)

    threshold = 0.9
    entities = []

    for item in ner_results:
        #if item['score'] >= threshold:
            text = item['word']
            if item['entity'].startswith('B-'):
                entities.append(text)
            elif item['entity'].startswith('I-') and len(entities) > 0:
                entities[-1] += ' ' + text

    for index, entity in enumerate(entities):
        entities[index] = entity.replace(' ##', '')

    return entities