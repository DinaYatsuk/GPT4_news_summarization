import g4f
import sys
import csv
from multiprocessing import Pool

def read_csv(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row['text'])
    return data


def get_gpt(prompt: str) -> str:
    while True:
        try:
            response = g4f.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
            )
            break
        except:
            print(".", end='')
    print("")
    return response

def process_text(text):
    cleaned_text = text.replace('"', '\\')
    prompt = (f"""создай заголовок на русском языке, состоящий не более, чем из 10 слов, на основе следующего текста: {cleaned_text}. 
    Выведи только заголовок без каких-либо добавлений, знаков или эмоджи.""")
    response = get_gpt(prompt)
    print(str(response) + "\nDIXI.")
    return response


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Необходимо ввести в cmd: python script.py <csv_file>")
        sys.exit(1)

    responses = []
    csv_file_path = sys.argv[1]
    texts = read_csv(csv_file_path)

    with Pool(processes=30) as pool:
        responses = pool.map(process_text, texts)


    with open('output_responses.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Заголовок'])
        for response in responses:
            writer.writerow([response])
        pbar.update()

