import mne
import pandas as pd

# Load the raw EEG data from the FIF file
raw = mne.io.read_raw_fif('fif/20240215-160931-Epoc X-raw.fif', preload=True)

# Extract the EEG data as a numpy array
eeg_data = raw.get_data()

# Convert the EEG data to a pandas DataFrame
df = pd.DataFrame(eeg_data.T, columns=raw.ch_names)

# Save the DataFrame to a CSV file
df.to_csv('eeg_data.csv', index=False)
