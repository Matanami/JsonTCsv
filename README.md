# JSON to CSV Converter

This script converts JSON data into a CSV file based on the specified keys.

## Prerequisites

- Python 3.x
- JSON file containing the data to be converted

## Usage

1. Clone the repository or download the script file.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Install the required dependencies by running the following command:
pip install csv


4. Run the script by executing the following command:
python json_to_csv_converter.py


5. Follow the prompts to enter the keys from the JSON file and the file path of the JSON file.

6. Once the conversion is complete, a CSV file named "output.csv" will be created in the same directory as the script.

## Example

Suppose you have a JSON file called "data.json" with the following structure:

```json
[
{
 "name": "John",
 "age": 25,
 "city": "New York"
},
{
 "name": "Emma",
 "age": 30,
 "city": "London"
}
]
If you want to convert this JSON data into a CSV file with the columns "name", "age", and "city", you would provide the following inputs when prompted:
Enter the keys from the JSON separated by spaces: name age city
Enter the file path for the JSON file: data.json
After the conversion is complete, a CSV file named "output.csv" will be generated, containing the following data:
name,age,city
John,25,New York
Emma,30,London
# JsonToCsv
