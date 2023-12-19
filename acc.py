import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_system_acceleration(file_paths):
    plt.figure(figsize=(12, 6))

    # Initialize an array to store system acceleration values
    system_acceleration = []

    # Get the maximum length of acceleration arrays
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
        acceleration_padded = np.pad(df_vehicle['acceleration'].values, (0, max_length - len(df_vehicle)), 'constant')

        # Add the padded acceleration array to the system acceleration array
        system_acceleration.append(acceleration_padded)

    # Summing up the padded accelerations for each time point across all vehicles
    total_system_acceleration = sum(system_acceleration)

    # Plotting the system acceleration vs time
    plt.plot(time_array, total_system_acceleration, label='System Acceleration')

    plt.title('System Acceleration over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('System Acceleration (m/s^2)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Assuming your new file paths
#file_paths = [f'80211p/=80211-sim-veh{i}-CAM.csv' for i in range(1, 21)]
file_paths = [f'nrv2x/=nrv2x-sim-veh{i}-CAM.csv' for i in range(1, 21)]
#file_paths = [f'cv2x/=cv2x-sim-veh{i}-CAM.csv' for i in range(1, 21)]
plot_system_acceleration(file_paths)


