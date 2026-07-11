import json
import csv

def txt_to_json(txt_file, json_file):
    # Example of converting simple text to json
    data = {'lines': []}
    try:
        with open(txt_file, 'r') as f:
            data['lines'] = [line.strip() for line in f.readlines()]
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        print('Conversion successful!')
    except FileNotFoundError:
        print('Sample file not found. Create a sample.txt to test.')

if __name__ == '__main__':
    txt_to_json('sample.txt', 'output.json')