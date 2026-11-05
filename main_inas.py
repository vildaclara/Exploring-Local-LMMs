import ollama
import csv
import time

def add_to_csv(filename, row, new=False):
    mode = 'w' if new else 'a+'
    with (open(filename, mode=mode, newline='', encoding='utf-8')) as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(row)


models = ["llama3.2:1b", "qwen2.5:0.5b"]
prompt = "How many letters are in the word banana? Answer with only the number."

add_to_csv("results.csv", ["Model", "Prompt", "Response", "Seconds"], new=True)

for model in models:
    start = time.time()
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    seconds = round(time.time() - start, 2)
    print(model)
    print(response['message']['content'])

    add_to_csv("results.csv", [model, prompt, response['message']['content'], seconds])