import os
import subprocess
import json
import zipfile
import shutil
import argparse

def create_temp_directory():
    temp_dir = 'temp_support_data'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    return temp_dir

def ensure_db_content_directory(base_dir):
    db_content_path = os.path.join(base_dir, 'db-content')
    os.makedirs(db_content_path)
    return db_content_path

def unzip_support_data(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def find_bson_files(directory):
    bson_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.bson'):
                bson_files.append(os.path.join(root, file))
    return bson_files

def bson_to_json(bson_file):
    json_data = []
    cmd = ['bsondump', bson_file]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
        output_lines = result.stdout.decode('utf-8').splitlines()
        for line in output_lines:
            json_data.append(json.loads(line))
    except subprocess.CalledProcessError as e:
        print(f"Error converting {bson_file} to JSON: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    return json_data

def combine_json_data(json_data_list, output_file):
    combined_data = []
    for data in json_data_list:
        if isinstance(data, list):
            combined_data.extend(data)
    
    with open(output_file, 'w') as f:
        json.dump(combined_data, f, indent=4)

    print(f"Output JSON file saved to: {os.path.abspath(output_file)}")


def main():
    parser = argparse.ArgumentParser(description='Convert BSON files to JSON.')
    parser.add_argument('zip_file', type=str, help='Path to the support data ZIP file')
    parser.add_argument('-o', '--output', type=str, default='output.json', help='Output JSON file name (default: output.json)')

    args = parser.parse_args()

    support_data_zip = args.zip_file
    output_json = args.output

    temp_dir = create_temp_directory()
    db_content_path = ensure_db_content_directory(temp_dir)

    try:
        unzip_support_data(support_data_zip, temp_dir)
        
        db_content_path = os.path.join(temp_dir, 'db-content')  

        bson_files = find_bson_files(db_content_path)
        if not bson_files:
            print("No BSON files found in the specified directory.")
            return

        json_data_list = []
        for bson_file in bson_files:
            json_data = bson_to_json(bson_file)
            if json_data:
                json_data_list.append(json_data)

        if not json_data_list:
            print("No JSON data was generated.")
            return

        combine_json_data(json_data_list, output_json)
    finally:
        shutil.rmtree(temp_dir)

if __name__ == '__main__':
    main()
