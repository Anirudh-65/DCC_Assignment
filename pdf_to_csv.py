import fitz
import csv
import pandas as pd

doc = fitz.open("Political_Party_Data.pdf")  # Open document
all_df_data = []  # List to store DataFrames from all tables

for i in range(len(doc)):
    page = doc[i]  # Get the ith page of the document
    tabs = page.find_tables()  # Locate and extract any tables on page

    if tabs:  # At least one table found?
        table_data = tabs[0].extract()  # Extract content of first table
        df = pd.DataFrame(table_data[1:], columns=table_data[0])  # Create DataFrame from table data
        print(df)
        all_df_data.append(df)  # Append DataFrame to the list

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(all_df_data, ignore_index=True)

# Write the combined DataFrame to a CSV file
combined_df.to_csv("political_party.csv", index=False)

# Write combined table content to the CSV file
with open("political_party.csv", "a", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    for row in table_data:
        csv_writer.writerow(row)