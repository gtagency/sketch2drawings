# sketch2drawings
Repo for the sketch2drawings project group for spring 2021

## How to train sketch2drawings??
#### Big Overview Steps
1. Download data from [this kaggle dataset](https://www.kaggle.com/shanmukh05/anime-names-and-image-generation)
2. Prepare/Preprocess the data
3. Train the model
4. Test the model
5. Export the model??

<hr>

### After Downloading Data
Create a folder called original and edges under images so that the directory looks like this
```
.
├── README.md
├── docker
│        └── Dockerfile
├── images
│        └── original
│        └── edges
│        └── resized
│        └── combined
```

Move the images (only, no folders) to images/original

We will
1. Resize all images into 256 x 256
2. Detect edges to get the "sketch"
3. Combine input images and target images
4. Split combined images into train and val set

### Install dependencies
Install all the dependencies
```bash
pip3 install -r requirements.txt
```

Warning: Python version must be at max 3.6! I spent too much time trying to do with Python 3.8 `D:`

While I did it manually with Conda, you could probably try this after creating a virtual environment
```bash
conda install --file requirements.txt
```

### Resizing Operation
After putting all the images into the original folder, run

```bash
python preprocessing/process.py --input_dir images/original --operation resize --output_dir images/resized
```

This operation took me about 25 minutes to run. When finished, we should see a folder called resize with 256 x 256 images

### Detect Edges Using Canny
We used Canny to detect edges. Navigate to the folder with process in it and then run process.py

```bash
cd preprocessing
python edge_detection.py
```

### Combine Operation
```bash
python preprocessing/process.py --input_dir images/resized --b_dir images/blank --operation combine --output_dir images/combined
```

### Split Operation
```bash
python preprocessing/split.py --dir images/combined
```

TODO
Write stuff about actually training