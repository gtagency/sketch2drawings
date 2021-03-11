# The following script process all images in a folder, detect edges and save them as new images
import cv2
import os
import os.path
import numpy as np
import pathlib


def auto_canny(image, sigma=0.33):
    # Compute the median of the single channel pixel intensities
    v = np.median(image)

    # Apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # Return the edged image
    return edged


def main():
    print(cv2.__version__)
    imageDir = pathlib.Path(__file__).parent.parent.joinpath('images', 'resized')  # Specify your path here
    image_path_list = []
    valid_image_extensions = [".jpg", ".jpeg", ".png"]  # Specify your valid extensions here
    valid_image_extensions = [item.lower() for item in valid_image_extensions]

    for file in os.listdir(imageDir):
        extension = os.path.splitext(file)[1]
        if extension.lower() not in valid_image_extensions:
            continue
        image_path_list.append(os.path.join(imageDir, file))

    for imagePath in image_path_list:
        print(imagePath)
        # read the img
        img = cv2.imread(imagePath, 0)
        if img is None:
            continue

        # Detect edges
        edges = auto_canny(img)

        # Revert white and balck
        newEdges = cv2.bitwise_not(edges)

        # Save output image in the edges folder (requires folder named resized!)
        path = imagePath.replace('resized', 'edges')
        cv2.imwrite(path, newEdges)


if __name__ == '__main__':
    main()
