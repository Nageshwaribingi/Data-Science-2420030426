#correcting inconsistent formats
import pandas as pd

#sample dataset
df = pd.DataFrame({
    'Date': ['2025-01-05', '05/01/2025', 'Jan 5,2025', '2025.01.05']
})

print("Original dataset (with inconsistent date formats):")
print(df)

#convert all dates to standard ISO format (YYYY-MM-DD)
df['Date'] = pd.to_datetime(df['Date'],errors='coerce').dt.strftime('%Y-%m-%d')

print("\nDataset after correcting date formats:")
print(df)