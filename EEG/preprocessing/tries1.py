import mne
import matplotlib.pyplot as plt

# Specify the path to the FIF file
fif_file_path = "fif/20240215-160931-Epoc X-raw.fif"

# Read the FIF file
raw = mne.io.read_raw_fif(fif_file_path, preload=True)

# Print basic information about the data
print("Information about the FIF file:")
print("Number of channels:", len(raw.info['ch_names']))
print("Sampling rate:", raw.info['sfreq'])
print("Channel names:", raw.info['ch_names'])
print("Channel types:", raw.get_channel_types())

# More detailed information can be accessed through the `info` attribute
print("\nFull information about the FIF file:")
print(raw.info)


# Define the positions of the electrodes in the standard 10-20 system
montage = mne.channels.make_standard_montage('standard_1005')

# Set the montage for the raw data
raw.set_montage(montage)

# Plot the sensor locations to verify the montage
raw.plot_sensors(show_names=True) 
raw.plot(
    duration=7.0,
    n_channels=len(raw.ch_names),
    scalings='auto'
)

plt.show()