import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_density_heatmap(file_paths, label):
    # Read data for each file and concatenate into a single DataFrame
    dfs = [pd.read_csv(file_path)[['latitude', 'longitude']] for file_path in file_paths]
    df_combined = pd.concat(dfs, axis=0)

    # Create a 2D density plot (heatmap) of vehicle positions
    plt.figure(figsize=(10, 8))
    sns.kdeplot(data=df_combined, x='longitude', y='latitude', cmap='viridis', fill=True)
    plt.title(f'Density Heatmap for Vehicle Positions ({label})')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()

# File paths for each protocol and set
file_paths_80211p = [f'80211p/=80211-sim-veh{i}-CAM.csv' for i in range(1, 21)]
file_paths_nrv2x = [f'nrv2x/=nrv2x-sim-veh{i}-CAM.csv' for i in range(1, 21)]
file_paths_cv2x = [f'cv2x/=cv2x-sim-veh{i}-CAM.csv' for i in range(1, 21)]

# Generate density heatmaps for each protocol and set
generate_density_heatmap(file_paths_80211p, '802.11p')
generate_density_heatmap(file_paths_nrv2x, 'nrv2x')
generate_density_heatmap(file_paths_cv2x, 'cv2x')
