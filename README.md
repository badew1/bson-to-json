# BSON to JSON Converter

This project provides a Python script that automates the conversion of `.bson` files to `.json` files. It extracts data from a specified ZIP file, converts all BSON files to JSON format, and combines the JSON files into a single output file.

## Features

- **Unzip Support Data**: Extracts the contents of a specified ZIP file.
- **BSON to JSON Conversion**: Converts `.bson` files to `.json` format using `bsondump`.
- **Combine JSON Files**: Merges multiple JSON files into one comprehensive JSON file.

## Requirements

- **Python**: Version 3.6 or higher.
- **MongoDB Tools**: `bsondump` utility must be installed. Download from [MongoDB Database Tools](https://www.mongodb.com/try/download/database-tools).

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/bson-to-json-converter.git
    cd bson-to-json-converter
    ```

2. **Install Required Python Packages**:
    ```bash
    pip install pymongo
    ```

3. **Ensure MongoDB Tools are Installed**:
    - Download and install MongoDB tools from [MongoDB Tools](https://www.mongodb.com/try/download/database-tools).
    - Ensure `bsondump` is available in your system's PATH.

## Usage

1. **Prepare Your ZIP File**:
    - Create a ZIP file containing your `.bson` files and name it as desired.
    - Place this ZIP file in an accessible directory.

2. **Run the Script with Command-Line Arguments**:
    ```bash
    python convert.py /path/to/your/support_data.zip -o output.json
    ```
    - Replace `/path/to/your/support_data.zip` with the actual path to your ZIP file.
    - Use the `-o` option to specify the output file name (defaults to `output.json` if not provided).

3. **Example Commands**:
    ```bash
    # Basic usage with default output file name
    python convert.py ./support_data.zip

    # Specify a custom output file name
    python convert.py ./support_data.zip -o combined_output.json
    ```

4. **Output**:
    - The script creates a combined JSON file (default: `output.json`) in the current directory, containing the data from all `.bson` files in the ZIP.