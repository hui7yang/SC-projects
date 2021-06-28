"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
-----------------------------------------------
Author: Hui-Chi Yang

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values
    """
    dist = ((red-pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)**(1/2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_red = 0
    total_green = 0
    total_blue = 0
    pixel_num = 0

    for pixel in pixels:
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue
        pixel_num += 1

    avg = [total_red/pixel_num, total_green/pixel_num, total_blue/pixel_num]
    return avg


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    rgb_avg = get_average(pixels)
    pixel_dist_list = []

    for pixel in pixels:
        pixel_dist = get_pixel_dist(pixel, rgb_avg[0], rgb_avg[1], rgb_avg[2])
        pixel_dist_list.append(pixel_dist)

    # mark the order as the best pixel
    order = 0

    # assign a random variable in pixel_dist_list as the one who has the minimal distance
    min_dist = pixel_dist_list[0]
    for i in range(len(pixel_dist_list)):
        if pixel_dist_list[i] < min_dist:
            min_dist = pixel_dist_list[i]
            order = i
    return pixels[order]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    pixel_list = []
    for x in range(width):  # (assign variable that changes the least as first for-loop)
        for y in range(height):
            for img in images:
                # get each img's pixel at the same coordinate and add to pixel_list
                pixel = img.get_pixel(x, y)
                pixel_list.append(pixel)
            # find the best pixel
            best_pixel = get_best_pixel(pixel_list)
            # get the pixel in result(a blank image)
            result_pixel = result.get_pixel(x, y)
            # replace result_pixel with the best pixel got in img
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue
            # clear the list and go on to compare the best pixel in next cycle
            pixel_list = []

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
