import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('eeg_data.csv', header=None)  # Assuming no header row in the CSV file

# Calculate the start index for the middle 1000 rows
start_index = (len(df) - 250) // 2

# Extract the middle 1000 rows and reset the index
df_middle = df.iloc[start_index:start_index+250].reset_index(drop=True)

# Generate time values in milliseconds based on the index of the DataFrame
time_ms = df_middle.index  # Assuming the index represents time in samples

# Extract data columns excluding the first column
data = df_middle.iloc[:, :15]  # Assuming data columns start from index 0 to 14

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
for col in data.columns:
    plt.plot(time_ms, data[col], label=f'Channel {col+1}')

# Add labels and legend
plt.xlabel('Time (samples)')
plt.ylabel('Amplitude')
plt.title('EEG Data (Middle 1000 Rows)')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
