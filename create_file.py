import pandas as pd
from datetime import datetime

# Generate today's date in the format 'YYYY-MM-DD'
today_date = datetime.today().strftime('%Y-%m-%d')

# File name with today's date
filename = f"{today_date}.csv"

# Example data to save (you can replace this with your actual data)
data = {
    'Column1': [1, 2, 3],
    'Column2': ['A', 'B', 'C']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file in the current folder
df.to_csv(filename, index=False)

print(f"File '{filename}' created and saved in the current folder.")
