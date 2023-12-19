import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_cumulative_speed(file_paths):
    plt.figure(figsize=(12, 6))

    # Initialize an array to store cumulative speed values
    cumulative_speed = []

    # Get the maximum length of speed arrays
    max_length = max(len(pd.read_csv(file_path)['speed']) for file_path in file_paths)

    # Initialize an array for time
    time_array = np.linspace(0, max_length, max_length)  # Assuming a constant time step

    # Iterate over each file path
    for file_path in file_paths:
        # Read the CSV file into a DataFrame
        df_vehicle = pd.read_csv(file_path)

        # Convert timestamp to time in seconds for better readability
        df_vehicle['time'] = df_vehicle['timestamp'] / 1000  # Assuming timestamp is in milliseconds

        # Pad or truncate the speed array to match the max length
        speed_padded = np.pad(df_vehicle['speed'].values, (0, max_length - len(df_vehicle)), 'constant')

        # Add the padded speed array to the cumulative speed array
        cumulative_speed.append(speed_padded)

    # Summing up the padded speeds for each time point across all vehicles
    total_cumulative_speed = sum(cumulative_speed)

    # Plotting the cumulative speed vs time
    plt.plot(time_array, total_cumulative_speed, label='Cumulative Speed')

    plt.title('Cumulative Speed over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Cumulative Speed (m/s)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Assuming your new file paths
#file_paths = [f'80211p/=80211-sim-veh{i}-CAM.csv' for i in range(1, 21)]
file_paths = [f'nrv2x/=nrv2x-sim-veh{i}-CAM.csv' for i in range(1, 21)]
#file_paths = [f'cv2x/=cv2x-sim-veh{i}-CAM.csv' for i in range(1, 21)]
plot_cumulative_speed(file_paths)
