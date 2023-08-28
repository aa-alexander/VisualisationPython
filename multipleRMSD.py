import matplotlib.pyplot as plt
import numpy as np
import os

def plot_volume(filename):
    x, y = np.loadtxt(filename, comments=["@", "#"], unpack=True)
    return x, y

def main():
  #path for the directories
    folder_path = 'mds'
    output_dir = 'plots'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(folder_path):
        if filename.endswith('.xvg'):
            file_path = os.path.join(folder_path, filename)
            x, y = plot_volume(file_path)

            plt.plot(x, y, label=filename)

    plt.xlabel("time (ps)")
    plt.ylabel("RMSD (nm)")
    plt.legend()
    plt.savefig(os.path.join(output_dir, "combined_volume.png"), format="png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()

