# Image Resizer

Console script for resizing images.

# Usage
1. Install requirements `pip install -r requirements.txt`
2. Run command `python image_resize.py path_to_source [parameters]`

# Parameters description
### Mandatory parameters
- path_to_source - a path to the source file
### Optional parameters
- --width  Width of a resulting image in pixels.
- --height Height of a resulting image in pixels.
- --scale  Scale image with this coefficient. Can't be used together with --width or --height
- --output Where to save result.

If only `--width` or `--height` provided than resulting image will be resized with aspect ratio of original.

If `--output` doesn't specified than resulting image will be saved near original with adding `__WidthxHeight` to original name.

# Examples of use

Assume `pic.jpg` is a 200x100 px. jpeg file.

* Enlarge the picture by 200%
`python image_resize.py pic.jpg --scale 2`
(Resulting picture will be saved as pic__400x200.jpg)
* Reduce the picture by 70%
`python image_resize.py pic.jpg --scale 0.3`
(Resulting picture will be saved as pic__60x30.jpg)
* Resize the picture to the width = 150 px
` python image_resize.py pic.jpg --width 150`
(Resulting image will be saved as pic__150x75.jpg. Height was calculated automatically with using original image aspect ratio.)
* Transform picture into a new image with the size of 100x100 px.
```
python image_resize.py pic.jpg --width 100 --height 100
ATTENTION! Aspect ratio of the resulting image is different from the source one.
```
(Resulting picture will be saved as pic__100x100.jpg)


# Build with

* [Pillow (PIL fork)](https://pillow.readthedocs.io/)


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
