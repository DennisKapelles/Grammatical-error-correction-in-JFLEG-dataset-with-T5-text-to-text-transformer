from datasets import load_dataset

from transformers import T5ForConditionalGeneration, T5Tokenizer

from nltk.translate.gleu_score import corpus_gleu

# Load the pre-trained T5 model and tokenizer
model_name = "t5-base"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Load the JFLEG test dataset
dataset = load_dataset("jfleg", split='test[:]')

# Function to generate predictions
def generate_predictions(model, tokenizer, sentences):
    predictions = []
    for sentence in sentences:
        input_text = "grammar: " + sentence
        input_ids = tokenizer.encode(input_text, return_tensors="pt")
        outputs = model.generate(input_ids)
        prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
        predictions.append(prediction)
    return predictions

# Get the list of sentences from the test dataset
sentences = dataset["sentence"]

# Generate predictions
predictions = generate_predictions(model, tokenizer, sentences)

# Generate predictions
predictions = generate_predictions(model, tokenizer, sentences)

# Function to preprocess references
def preprocess_references(corrections):
    references = []
    for correction_set in corrections:
        # Each correction set is a list of corrected sentences
        formatted_references = [correction.split() for correction in correction_set if correction.strip() != ""]
        references.append(formatted_references)
    return references

# Preprocess references and predictions
references = preprocess_references(dataset["corrections"])
predictions = [pred.split() for pred in predictions]

# Calculate the GLEU score
gleu_score = corpus_gleu(references, predictions)
print(f"GLEU Score: {gleu_score:.4f}")