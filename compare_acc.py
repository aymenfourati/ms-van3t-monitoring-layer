import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_comparison(file_paths_set1, file_paths_set2, file_paths_set3, label_set1, label_set2, label_set3):
    plt.figure(figsize=(12, 6))

    # Function to calculate cumulative values for a given set of file paths
    def calculate_cumulative_values(file_paths):
        cumulative_values = []

        # Get the maximum length of speed/acceleration arrays
        max_length = max(len(pd.read_csv(file_path)['acceleration']) for file_path in file_paths)

        # Initialize an array for time
        time_array = np.linspace(0, max_length, max_length)  # Assuming a constant time step

        # Iterate over each file path
        for file_path in file_paths:
            # Read the CSV file into a DataFrame
            df_vehicle = pd.read_csv(file_path)

            # Convert timestamp to time in seconds for better readability
            df_vehicle['time'] = df_vehicle['timestamp'] / 1000  # Assuming timestamp is in milliseconds

            # Pad or truncate the acceleration array to match the max length
            values_padded = np.pad(df_vehicle['acceleration'].values, (0, max_length - len(df_vehicle)), 'constant')

            # Add the padded array to the cumulative values array
            cumulative_values.append(values_padded)

        # Summing up the padded values for each time point across all vehicles
        total_cumulative_values = sum(cumulative_values)

        return time_array, total_cumulative_values

    # Calculate cumulative values for each set
    time_set1, cumulative_acceleration_set1 = calculate_cumulative_values(file_paths_set1)
    time_set2, cumulative_acceleration_set2 = calculate_cumulative_values(file_paths_set2)
    time_set3, cumulative_acceleration_set3 = calculate_cumulative_values(file_paths_set3)

    # Plotting the cumulative acceleration vs time for each set
    #plt.plot(time_set1, cumulative_acceleration_set1, label=label_set1 + ' Acceleration')
    plt.plot(time_set2, cumulative_acceleration_set2, label=label_set2 + ' Acceleration')
    plt.plot(time_set3, cumulative_acceleration_set3, label=label_set3 + ' Acceleration')

    plt.title('Cumulative Acceleration Comparison over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Cumulative Acceleration (m/s^2)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Assuming your new file paths and labels
file_paths_set1 = [f'80211p/=80211-sim-veh{i}-CAM.csv' for i in range(1, 21)]
file_paths_set2 = [f'nrv2x/=nrv2x-sim-veh{i}-CAM.csv' for i in range(1, 21)]
file_paths_set3 = [f'cv2x/=cv2x-sim-veh{i}-CAM.csv' for i in range(1, 21)]

plot_comparison(file_paths_set1, file_paths_set2, file_paths_set3, 'Set 1', 'Set 2', 'Set 3')
