# For multiple rmsd files in a folder this script calculates the mean and Standard deviation and export it as tsv file

import numpy as np
import os
import pandas as pd

def calculate_stats(filename):
    x, y = np.loadtxt(filename, comments=["@", "#"], unpack=True)
    mean_y = np.mean(y)
    std_dev_y = np.std(y)
    return mean_y, std_dev_y

def main():
    folder_path = 'mds'
    output_dir = 'output'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    stats_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.xvg'):
            file_path = os.path.join(folder_path, filename)
            mean_y, std_dev_y = calculate_stats(file_path)
            stats_data.append([filename[:-4], mean_y, std_dev_y])

    # Create a pandas DataFrame from the statistics data
    columns = ["File Name", "Mean", "Standard Deviation"]
    stats_df = pd.DataFrame(stats_data, columns=columns)

    # Save the statistics as a TSV file
    output_path = os.path.join(output_dir, "statistics.tsv")
    stats_df.to_csv(output_path, sep='\t', index=False)

if __name__ == "__main__":
    main()

