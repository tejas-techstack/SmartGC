import sys
import json

import parser 


def inject_deallocation_code(input_file, output_file, json_file):
    print("Loading deallocation points from JSON file...")
    with open(json_file, 'r') as f:
        deallocation_data = json.load(f)
    print("Deallocation points loaded successfully.")

    deallocation_points = deallocation_data['deallocations']

    print("Reading original source code...")
    with open(input_file, 'r') as f:
        source_code = f.readlines()
    print("Original source code read successfully.")

    with open(output_file, 'w') as f:
        print("Injecting deallocation code...")
        for i, line in enumerate(source_code, start=1):
            f.write(line)
            #print(f"Processing line {i}...")
            for deallocation_point in deallocation_points:
                if i == deallocation_point['line_number']:
                    variable_name = deallocation_point['variable_name']
                    f.write(f'\tfree({variable_name});\n')  
                    print(f"Freeing memory for variable {variable_name} at line {i}")
        print("Deallocation code injected successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python preprocess.py input_file output_file json_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    json_file = sys.argv[3]

    parser.main(input_file, json_file)
    inject_deallocation_code(input_file, output_file, json_file)
