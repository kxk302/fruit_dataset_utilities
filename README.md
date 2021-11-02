# fruit dataset utilities

Fruit 360 is a dataset with 90380 images of 131 fruits and vegetables (https://www.kaggle.com/moltean/fruits).
Images are 100 pixel by 100 pixel and are RGB (color) images (3 values for each pixel). This repo contains 
utilities for creating feature vectors for the images and selecting a subset of the images for analysis. More info
about the dataset can be found in 'Fruit recognition from images using deep learning' paper (https://arxiv.org/abs/1712.00580). 

# Create and configure your virtual environment

1. Create a virtual environment via the following command:
```
python3 -m venv venv
```
2. Activate your virtual environment via the following command:
```
. ./venv/bin/activate
```
3. Install the necessary packages in your virtual environment via the following command:
```
pip3 install -r requirements.txt
```

# Creating feature vectors for images

1. Download the dataset by going to https://www.kaggle.com/moltean/fruits and clicking on Download button on top
2. Extract the downloaded zip file via the following command:
```
unzip archive.zip
```
3. Training data, Test data and a useful readme file can found in 'fruit-360_dataset/fruit-360' folder
4. There are folders containing jpeg images for each fruit/vegetable under Training/Test folders
5. To remove the whitespace in folder names, run the following commad in Training and Test folders 
```
for f in *\ *; do mv "$f" ${f// /_}; done
```
6. To create Training feature vectors, run the following command in 'fruit-360_dataset/fruit-360' folder. This 
command will create 2 files: 1) labels.json. Its a dictionary that maps the name of each fruit/vegetable folder 
under Training to a unique integer ID, 2) training.csv, feature vectors file, where each row has 
100 X 100 X 3 values of image pixels (30,000 values), integer ID of fruit/vegetable label, fruit/vegetable label 
(Name of fruit/vegetable folder), and the full image file path, for a total of 30003 columns
```
python3 feature_vector.py -d Training -f traing.tsv -l labels.json
```

7. To create Test feature vectors, run the following command in 'fruit-360_dataset/fruit-360' folder. This
command will use the labels.json file created in the previous step, and creates test.csv, Test feature vectors
file, where each row again has 100 X 100 X 3 values of image pixels (30,000 values), integer ID of 
fruit/vegetable label, fruit/vegetable label (Name of fruit/vegetable folder),  and the full image file path,
for a total of 30003 columns
```
python3 feature_vector.py -d Test -f testing.tsv -l labels.json
```

# Select a subset of images for analysis

Create a labels_subset.json file by copy labels.json file. labels.json file specifies 131 fruits/vegetables.
Creating the feature vector for all images of 131 fruits/vegetables results in very large feature vector files 
(7GB for training and 2.5 GB for testing). You can specify only the fruits/vegetables you are interested in 
labels_subset.json, and run the following commands to extract feature vector for only those fruits/vegetables. 
For the provided labels_subset.json, which includes 20 fruits/vegetables, file sizes dropped to 1.1 GB and 375 MB 
for training and testing, respectively.

To select a subset of training feature vectors, run the following command. It creates a file named train_subset.tsv
```
python3 subset.py -f training.tsv -s labels_subset.json -o training_subset.tsv
```

To select a subset of testing feature vectors, run the following command. It creates a file named test_subset.tsv
```
python3 subset.py -f testing.tsv -s labels_subset.json -o testing_subset.tsv
```
