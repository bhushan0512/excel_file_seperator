# Data Sorting and Excel File Generation

## Overview

This Python script reads an Excel file containing course-related data, sorts the data based on the course name, and generates separate Excel files for each course. The generated files are named after the course and saved in a specified directory.

## Features

- **Sorting:** The script sorts the course data based on the course name.
- **File Generation:** It creates individual Excel files for each course.
- **Filename Sanitization:** Handles invalid characters in course names for filenames.

## Requirements

- Python 3.x
- pandas library (`pip install pandas`)
- openpyxl library (`pip install openpyxl`)

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
2. **Install the required libraries:**

   ```bash
   pip install pandas openpyxl
3. **Run the script:**

   ```bash
   pip install pandas openpyxl
  Replace **your_script_name.py** with the actual name of your Python script.

4. **Check the 'outputs' directory for the generated Excel files.**

## Configuration
- **Input File:** Make sure to replace /path/to/your/list.xlsx with the path to your actual Excel file.
- **Output Directory:** You can customize the output_directory variable in the script to specify where the generated files should be saved.
## Notes
- The script handles potential issues such as invalid characters in course names for filenames.
## Feedback
**- If you encounter any issues or have suggestions for improvement, feel free to create an issue or pull request.**
