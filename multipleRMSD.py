# this script will take all the files in the directory and create the graph; you can tweek it to do for certain files by specifying the names.

import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns

def plot_volume(filename):
    x, y = np.loadtxt(filename, comments=["@", "#"], unpack=True)
    return x, y

# Define a custom color cycle for the plots
custom_palette = sns.color_palette("tab20", n_colors=20)

def main():
    folder_path = 'mds'
    output_dir = 'plots'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for idx, filename in enumerate(os.listdir(folder_path)):
    #for filename in os.listdir(folder_path):
        if filename.endswith('.xvg'):
            file_path = os.path.join(folder_path, filename)
            x, y = plot_volume(file_path)

            plt.plot(x, y, color=custom_palette[idx % len(custom_palette)], label=filename[:-4])

    plt.xlabel("time (ps)")
    plt.ylabel("RMSD (nm)")
    plt.legend()
    #plt.savefig(os.path.join(output_dir, "combined_volume.png"), format="png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()

