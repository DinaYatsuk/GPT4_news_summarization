# GPT Title Generator

This repository contains a Python script that utilizes GPT-4 to generate concise Russian titles (up to 10 words) based on the input text from a CSV file. The project uses the `g4f` library for GPT communication and supports multiprocessing for efficient processing.

## Features

- **CSV Input Handling**: Reads a list of text entries from a CSV file.
- **Title Generation**: Creates titles in Russian using GPT-4 based on the input text.
- **Parallel Processing**: Leverages multiprocessing to process multiple text entries simultaneously, speeding up the title generation process.
- **CSV Output**: Saves the generated titles to an output CSV file.

## File Description

### `gpt.py`
The main script that performs the following tasks:
- **`read_csv(file_path)`**: Reads text entries from a specified CSV file.
- **`get_gpt(prompt)`**: Communicates with GPT-4 to generate a response based on a prompt.
- **`process_text(text)`**: Cleans input text and generates a title using GPT-4.
- **Main Execution**:
  - Reads input from a CSV file provided via command-line arguments.
  - Processes the input text in parallel using a multiprocessing pool.
  - Saves the generated titles to `output_responses.csv`.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/gpt-title-generator.git
   cd gpt-title-generator
   ```

2. **Install dependencies**:
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

   **Dependencies**:
   - `g4f`
   - `multiprocessing`
   - `csv`

3. **API Configuration**:
   Ensure that the `g4f` library is configured to communicate with GPT-4.

## Usage

1. **Prepare the input CSV file**:
   The CSV file should have a column named `text` containing the text entries for which titles need to be generated.

2. **Run the script**:
   Execute the script with the input CSV file as a command-line argument:
   ```bash
   python gpt.py <input_csv_file>
   ```

   Example:
   ```bash
   python gpt.py input_texts.csv
   ```

3. **Output**:
   The generated titles will be saved in `output_responses.csv` in the current directory, with a column named `Заголовок`.

## Notes

- **Error Handling**: The script retries GPT calls in case of errors, ensuring robust execution.
- **Language Support**: Titles are generated in Russian, as specified in the prompts.
- **Efficiency**: The script uses multiprocessing to handle large input files efficiently.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or improvements.
