import pandas as pd
import os

# Read the original Excel file in xlsx format
file_path = 'file_path.xlsx'  # replace with your actual file path
df = pd.read_excel(file_path)

# Clean column names by removing leading and trailing whitespaces
df.columns = df.columns.str.strip()

# Sort the data based on 'cname'
df_sorted = df.sort_values(by='cname')

# Extract unique courses from the sorted DataFrame
unique_courses = df_sorted['cname'].unique()

# Create separate Excel files for each course
output_directory = 'output_path_on_system'  # replace with your desired directory
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist

for course in unique_courses:
    # Replace invalid characters in the course name
    sanitized_course_name = course.replace('/', '_')

    course_data = df_sorted[df_sorted['cname'] == course]
    output_file_path = os.path.join(output_directory, f'{sanitized_course_name}_records.xlsx')

    course_data.to_excel(output_file_path, index=False)
    print(f'Saved {output_file_path}')

print('Process completed successfully.')
