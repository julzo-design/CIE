import pandas as pd
import csv

# Load and inspect the uploaded RPT file content to determine its structure.
#file_path = '/mnt/data/Displacement_Small_Structure_2MN_Force.rpt'

files = ['Displacement_Long_Structure_1MN_Force','Displacement_Long_Structure_2MN_Force','Displacement_Small_Structure_1MN_Force','Displacement_Small_Structure_2MN_Force',]
system_class = "class_0_perfect_structure" ## class_1_imperfect_structure or class_0_perfect_structure

for filename in files:

    file_path = f'../{system_class}/{filename}.rpt'

    # Read and display a sample of the content
    with open(file_path, 'r') as file:
        rpt_content = file.readlines()


    # Define the output CSV file path
    csv_file_path = f"../{system_class}_csv/{filename}.csv"

    # Parse the header lines to construct column names
    header_lines = rpt_content[1:3]
    data_lines = rpt_content[4:]

    # Clean and split the header lines
    header = " ".join(line.strip() for line in header_lines).split()

    lines = []
    for line in header_lines:
        line = line.strip().split('  ')
        lines.append(line)

    lines[1] = [entry for entry in lines[1] if entry != '']
    del lines[1][0]

    form_header= []
    form_header.append('TimeStamp')
    for i in range(len(lines[0])):
        form_header.append(lines[0][i] + lines[1][i])

    # Parse the data lines
    data = []
    for line in data_lines:
        if line.strip():  # Skip empty lines
            data.append(line.split())

    # Write the data to a CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(form_header)  # Write the header
        writer.writerows(data)   # Write the data

#csv_file_path