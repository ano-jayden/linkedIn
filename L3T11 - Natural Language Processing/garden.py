import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# List of garden path sentences
gardenpathSentences = [
    "The old man the boat.", 
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.", 
    "That Jill is never here hurts.", 
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenising sentences and performing Named Entity Recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"Sentence: {sentence}")
    for token in doc:
        print(f"Token: {token.text}, POS: {token.pos_}, NER: {token.ent_type_ if token.ent_type_ else 'None'}")
    
    # Named Entities in the sentence
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}, Explanation: {spacy.explain(ent.label_)}")
    
    print("-" * 50)

# Example of looking up explanations for unknown entity types

entity_to_explain = "FAC"
print(f"Entity 'FAC' explained: {spacy.explain(entity_to_explain)}")

# Two Entities Explained:

# 1. Entity: "FAC" 
# Explanation: "Buildings, airports, highways, bridges, etc."
# The sentence's complicated structure may have prevented spaCy from identifying 
# the entity "FAC" in this instance. However, it would make sense if it were 
# connected to something like "the complex".

# 2. Entity: "GPE" 
# Explanation: "Countries, cities, states"
# spaCy might identify "Mississippi" as a "GPE" in the line 
# "The cotton clothing is made of grows in Mississippi."
# This makes sense given that Mississippi is a state.

