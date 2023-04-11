import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

rootdir = './data'
dataframes = []

# Go through each sample folder within data directory and locate /peaks.bed.mouse.annotation.txt

for folder in os.listdir(rootdir):
    directory = os.path.join(rootdir, folder)
    if (os.path.isdir(directory)):
        file = directory + '/peaks.bed.mouse.annotation.txt'

        # Read the data file and extract columns: Chromosomes, MicroRNA, Reads, mRNA,  Location (intergenic?)
        
        df = pd.read_csv(file, sep="\t", header=None, usecols=[0, 3, 4, 9, 10], names=[
                         "chromosome", "microRNA", "reads", "targetGene", "location"])

        # Filter data with intergenic location and drop the column

        df = df[df['location'] != 'intergenic'].drop(columns=['location'])

        # Add column to indicate with sample the data is from
        df['sample'] = folder

        # Append to the dataframe list
        dataframes.append(df)


# Combine all the samples into one dataframe
concated = pd.concat(dataframes)


heatmap_data = pd.pivot_table(concated, values='reads',
                              index=['chromosome', 'targetGene', 'microRNA'],
                              columns='sample').fillna(0)

# generate heatmap data into csv
# heatmap_data.to_csv('heatmap_data.csv')

# set font size
# plt.rcParams.update({'font.size': 2})

# set color scale
colors = [[0, '#333333'],
          [.1, '#F5D5CE'],
          [.5, '#F57656'],
          [.75, '#F5542C'],
          [1, '#F53200']]
cmap = LinearSegmentedColormap.from_list('', colors)


# generate clustermap
clustermap = sns.clustermap(heatmap_data, cmap=cmap, yticklabels=True)

# Adjust color scale position
clustermap.fig.subplots_adjust(right=0.7)
clustermap.ax_cbar.set_position((0.8, .2, .03, .4))
clustermap.ax_heatmap.set_yticklabels(clustermap.ax_heatmap.get_yticklabels(), fontsize=2)
# save file as pdf.
plt.savefig('heatmap.pdf', dpi=1000)

# plt.show()
