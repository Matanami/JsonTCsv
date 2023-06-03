import json
import csv

def converter(path, keys):
    try:
        with open(path, 'r') as f:
            data = json.load(f)

        output_rows = []
        output_rows.append(keys)

        for obj in data:
            row = [str(obj.get(key, "")) for key in keys]
            output_rows.append(row)

        with open('output.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(output_rows)

        print("Conversion successful. CSV file created: output.csv")

    except Exception as ex:
        print(f'Error: {str(ex)}')

if __name__ == "__main__":
    key_input = input("Enter the keys from the JSON separated by spaces: ")
    key_list = key_input.split()

    file_path = input("Enter the file path for the JSON file: ")
    converter(file_path, key_list)
