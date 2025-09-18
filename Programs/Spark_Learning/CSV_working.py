import pandas as pd

# Read the CSV file in chunks
data = pd.read_csv('/Users/sg/Project/custom_2017_2020.csv', chunksize=100000)

output = pd.DataFrame()

# Process each chunk
for chunk in data:
    categories = ['Year', 'Q2']  # Specify the columns to group by
    details = chunk[categories]  # Extract the relevant columns
    details['count'] = 1  # Add a count column for aggregation

    # Summarize the chunk
    summary = details.groupby(categories).sum().reset_index()
    output = output.append(summary, ignore_index=True)  # Append the chunk summary to the output DataFrame

# Print the final result
print(output)
