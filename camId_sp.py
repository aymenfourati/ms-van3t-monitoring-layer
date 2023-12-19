import pandas as pd
import matplotlib.pyplot as plt

def plot_trajectory(file_paths, label):
    # Read data for each file and concatenate into a single DataFrame
    dfs = [pd.read_csv(file_path)[['latitude', 'longitude', 'camId']] for file_path in file_paths]
    df_combined = pd.concat(dfs, axis=0)

    # Plot trajectories of vehicles
    plt.figure(figsize=(12, 8))

    for vehicle_id, group in df_combined.groupby('camId'):
        plt.plot(group['longitude'], group['latitude'], label=f'camId {vehicle_id}', marker='o', markersize=4)

    plt.title(f'Trajectory Visualization ({label})')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.show()

# File paths for each protocol and set
file_paths_80211p = [f'80211p/=80211-sim-veh{i}-CAM.csv' for i in range(1, 21)]
file_paths_nrv2x = [f'nrv2x/=nrv2x-sim-veh{i}-CAM.csv' for i in range(1, 21)]
file_paths_cv2x = [f'cv2x/=cv2x-sim-veh{i}-CAM.csv' for i in range(1, 21)]

# Plot trajectories for each protocol and set
plot_trajectory(file_paths_80211p, '802.11p')
plot_trajectory(file_paths_nrv2x, 'nrv2x')
plot_trajectory(file_paths_cv2x, 'cv2x')
