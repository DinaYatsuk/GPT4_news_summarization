# Text-to-Title-Generator-using-GPT-4
This Python script utilizes the GPT-4 model from the g4f library to generate titles in Russian language based on input texts provided in a CSV file.
The titles are generated by prompting the model with a specific format and extracting the generated titles.

## Prerequisites
- Python 3.x
- Required Python libraries:
  - g4f
  - tqdm
  - multiprocessing
## Usage
- Ensure you have installed the required libraries. 
- Clone or download the script gpt.py into your local environment.
- Prepare a CSV file containing a column named "text" which includes the input texts for which you want to generate titles.
- Run the script from the command line with the following command:
``` python
python script.py <path_to_csv_file>```

The script will generate titles for each text in the CSV file and save the results in a new CSV file named output_responses.csv.
