import argparse
import os
from PIL import Image


def create_parser():
    arguments_parser = argparse.ArgumentParser(description='Image resize utility')
    arguments_parser.add_argument('path')
    arguments_parser.add_argument('--width', nargs='?', type=image_size_type, help='Width of a resulting image.')
    arguments_parser.add_argument('--height', nargs='?', type=image_size_type, help='Height of a resulting image.')
    arguments_parser.add_argument('--scale', nargs='?', type=float, help='Scale image with this coefficient.')
    arguments_parser.add_argument('--output', nargs='?', help='Where to save result.')
    return arguments_parser


def image_size_type(x):
    x = int(x)
    if x <= 0:
        raise argparse.ArgumentTypeError('The size can\'t be an 0 or a negative number')
    return x


def process_image(image, params):
    if params.height or params.width:
        return resize_image(image, params.width, params.height)
    if params.scale:
        return scale_image(image, params.scale)


def scale_image(image, scale_coeff):
    result_width, result_height = (round(x * scale_coeff) for x in image.size)
    return image.resize((result_width, result_height), resample=Image.LANCZOS)


def resize_image(image, result_width, result_height):
    source_width, source_height = image.size
    if result_width and result_height:
        if round(source_width/source_height, 2) != round(result_width/result_height, 2):
            print('WARNING! Aspect ratio of the resulting image is different from the source one.')
    elif result_width:
        result_height = round((result_width/source_width) * source_height)
    elif result_height:
        result_width = round((result_height/source_height) * source_width)
    return image.resize((result_width, result_height), resample=Image.LANCZOS)


def save_image(image, params):
    if image is None:
        return
    base, tail = os.path.split(params.path)
    if not params.output:
        file_name, file_extension = os.path.splitext(tail)
        tail = '{name}__{i[0]}x{i[1]}{ext}'.format(name=file_name, i=image.size, ext=file_extension)
    save_to = os.path.join(base, tail)
    image.save(save_to)


if __name__ == '__main__':
    parser = create_parser()
    parameters = parser.parse_args()
    if parameters.scale and (parameters.height or parameters.width):
        parser.error('Parameter --scale can\'t be used together with --width or --height.')
    try:
        with Image.open(parameters.path) as source_image:
            result_image = process_image(source_image, parameters)
    except OSError:
        parser.error('{} is not a valid file'.format(parameters.path))

    try:
        save_image(result_image, parameters)
    except OSError:
        parser.error('Can\'t save resulting file to {}'.format(parameters.output))
