from happytransformer import HappyTextToText

happy_tt = HappyTextToText("T5", "t5-base")

from datasets import load_dataset

train_dataset = load_dataset("jfleg", split='validation[:]')

eval_dataset = load_dataset("jfleg", split='test[:]')

import csv

def generate_csv(csv_path, dataset):
    with open(csv_path, 'w', newline='') as csvfile:
        our_csv = csv.writer(csvfile)
        our_csv.writerow(["input", "target"])
        for sent in dataset:
            # Adding the task's prefix to input
            input_text = "grammar: " + sent["sentence"]
            for correction in sent["corrections"]:
                # a few of the cases contain blank strings.
                if input_text and correction:
                    our_csv.writerow([input_text, correction])

generate_csv("train.csv", train_dataset)
# generate_csv("eval.csv", eval_dataset)

# generate_csv("train.csv", train_dataset)
generate_csv("eval.csv", eval_dataset)


from happytransformer import TTTrainArgs

import tracemalloc

# Start monitoring memory usage
tracemalloc.start()

args = TTTrainArgs(batch_size=8, num_train_epochs=3)

# Train the model with error handling
try:
    happy_tt.train("train.csv", args=args)
except OverflowError as e:
    print(f"OverflowError encountered: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Display memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 10**6}MB; Peak: {peak / 10**6}MB")
tracemalloc.stop()

after_result = happy_tt.eval("eval.csv")

print("After loss: ", after_result.loss)

# Function to generate predictions
def generate_predictions(model, sentences):
    predictions = []
    for sentence in sentences:
        input_text = "grammar: " + sentence
        result = model.generate_text(input_text)
        prediction = result.text
        predictions.append(prediction)
    return predictions

# Get the list of sentences from the test dataset
sentences = eval_dataset["sentence"]

# Generate predictions
predictions = generate_predictions(happy_tt, sentences)

from nltk.translate.gleu_score import corpus_gleu

# Calculate the GLEU score
gleu_score = corpus_gleu(references, predictions)
print(f"GLEU Score: {gleu_score:.4f}")