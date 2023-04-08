# Neuropathic Pain Heatmap Generator

This is a python script to generate clustermap (complex heatmap) for annotated samples using SCRAP pipeline. For more information about SCRAP, visit SCRAP at https://github.com/Meffert-Lab/SCRAP.

## How to run

You would need the following packages to run this python script.

- Python 3
- Pandas
- Seaborn
- Scipy
- Matplotlib


### 1. Create a folder name data

Put all your sample folders into this data folder.
Folder structure as follow:

```
├── main.py
├── data
│   ├── sample1
│   │   ├── peaks.bed.mouse.annotation.txt
│   ├── sample2
│   │   ├── peaks.bed.mouse.annotation.txt
│   ├── sample3
│   │   ├── peaks.bed.mouse.annotation.txt
```


### 2. Install all the necessary pacakges listed above. 

You can try running it and see which ones you are missing. ```pip3 install <package name>```

```
python3 main.py
```


### 3. If you have all the pacakges. Run the script.

```
python3 main.py
```

After you run the script, a pdf file ```heatmap.pdf``` will be generated.

