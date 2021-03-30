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

If you have conda installed, you can also try this
1. Create virtual environment named sketch2drawings
```bash
conda create -n "sketch2drawings" python=3.6.0
```

2. Activate conda environment
```bash
conda activate sketch2drawings
```

3. Install OpenCV and Tensorflow v1.4.1 (since numpy is already installed)
```bash
conda install opencv-python
pip install tensorflow==1.4.1
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
Navigate back to the root directory with `cd ..`. Now run the combine operation with
```bash
python preprocessing/process.py --input_dir images/resized --b_dir images/edges --operation combine --output_dir images/combined
```

This operation took me about 30 minutes to run. The script will skip over files that already exist, so you can pause the operation and resume later.

### Split Operation
Generate train/validation splits
```bash
python preprocessing/split.py --dir images/combined
```

### Training
Hopefully you have a GPU because if you train on CPU you will definitely be waiting for a bit.
```bash
python pix2pix.py --mode train --output_dir s2d_train --max_epochs 200 --input_dir images/combined/train --which_direction BtoA --ngf 32 --ndf 32
```

Maybe try changing `--ngf 32` and `--ndf32` to 64 to see how well it does, but it takes more computation

If you have Docker installed, you can use the Docker image to train without having to install the correct version of Tensorflow

```bash
# Train the model with docker
python dockrun.py python pix2pix.py \
      --mode train \
      --output_dir s2d_train \
      --max_epochs 200 \
      --input_dir images/combined/train \
      --which_direction BtoA
```