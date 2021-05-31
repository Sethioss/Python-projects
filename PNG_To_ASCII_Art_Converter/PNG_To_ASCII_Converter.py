import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw

from tkinter import filedialog
import subprocess
import os

ascii_art_characters = ['  ', '  ', '..', '::', ';;', '""', '&&', '##', 'BB']
reduce_res = True
PIXEL_ON = 0
PIXEL_OFF = 255
ASCII_PATH = "ASCII_results/"
IMAGE_PATH = "Image_resources/"

def start_conversion(image_path, width_size):
    processed_path = process_url(image_path)
    
    text = add_text_file_in_registry(processed_path)
    image = add_image_to_registry(processed_path, width_size)

    pixel_to_character(image, text)

def process_url(url):
    new_url = url.replace("\\", "/")
    new_url = new_url[1:-1]
    print(new_url)
    return new_url

def get_image_name(url):
    filename = url.filename
    image_name = filename.split("/")
    
    image_name_with_format = image_name[-1].split(".")
    image_name_without_format = image_name_with_format[0:-1]

    finalName = ''
    for word in image_name_without_format:
        finalName = finalName + word
        
    return finalName
    
def add_text_file_in_registry(path):
    global ASCII_PATH
    
    im = PIL.Image.open(path)
    og_name = str(get_image_name(im))
                  
    if not os.path.exists(ASCII_PATH):
        os.makedirs(ASCII_PATH)
                  
    link = ASCII_PATH + og_name + "(ASCII)" + ".txt"
    asc_file = open(link, 'w')
    asc_file.close()
    return link

def add_image_to_registry(path, width_size):
    global IMAGE_PATH
    global reduce_res
    
    im = PIL.Image.open(path)
    size = im.size
    new_im = im
    og_name = str(get_image_name(im))

    if not os.path.exists(IMAGE_PATH):
        os.makedirs(IMAGE_PATH)
    
    im_path = IMAGE_PATH + og_name + ".png"
    new_im.save(im_path, 'PNG')

    if reduce_res:
        if(width_size != 0):
            heightRatio = im.size[0] / im.size[1]
            size = (width_size, int(im.size[1] + ((width_size - im.size[0]) / heightRatio)))

        else:  
            if(new_im.size[0] >= im.size[1]):
                heightRatio = im.size[0] / im.size[1]
                size = (150, int(im.size[1] + ((150 - im.size[0]) / heightRatio)))
            elif(new_im.size[1] > im.size[0]):
                widthRatio = im.size[1] / im.size[0]
                size = (int(im.size[0] + ((95 - im.size[1]) / widthRatio)), 95)

    im_path = "Image_resources/"+ og_name + "(Resized)" + ".png"
    new_im = im.resize(size, 0)
    #print(str(new_im.size[0]), str(new_im.size[1]))
    new_im.save(im_path, 'PNG')
    return im_path

def pixel_to_character(image_to_process, text_to_process):
    global ascii_art_characters
    global ASCII_PATH
    
    im = PIL.Image.open(image_to_process)
    pixels = im.load()
    pixelValue = 0
    
    text = open(text_to_process, 'w')
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            pixelValue = get_pixel_value(pixels[j, i])
            text.write(str(ascii_art_characters[pixelValue]))
        text.write('\n')
    text.close()

    print(text_to_process)
    
    print('Image found! Please wait while the algorithm writes your ASCII image into a png file...')
    image = text_image(text_to_process)
    image.save(ASCII_PATH + get_image_name(im).replace('(Resized)', '') + "(ASCII).png")
    os.remove(image_to_process)
    print('PNG file written! You can see the result in the "ASCII_result" folder')
    
    subprocess.Popen('explorer "ASCII_results"')   

def get_pixel_value(pixel_to_get):
    global ascii_art_characters
    
    pixel_value = int((pixel_to_get[0] + pixel_to_get[1] + pixel_to_get[2])) / 765
    pixel_value = 1 - pixel_value
    pixel_value = int(pixel_value * (len(ascii_art_characters)-1))
    
    #print(pixel_value)
    return pixel_value

def text_image(text_path, font_path=None):
    """Convert text file to a grayscale image with black characters on a white background.

    arguments:
    text_path - the content of this file will be converted to an image
    font_path - path to a font file (for example impact.ttf)
    """
    grayscale = 'L'
    # parse the file into lines
    with open(text_path) as text_file:  # can throw FileNotFoundError
        lines = tuple(l.rstrip() for l in text_file.readlines())

    # choose a font (you can see more detail in my library on github)
    large_font = 20  # get better resolution with larger size
    font_path = font_path or 'cour.ttf'  # Courier New. works in windows. linux may need more explicit path
    try:
        font = PIL.ImageFont.truetype(font_path, size=large_font)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')

    # make the background image based on the combination of font and lines
    pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
    max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
    # max height is adjusted down because it's too large visually for spacing
    test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = pt2px(font.getsize(test_string)[1])
    max_width = pt2px(font.getsize(max_width_line)[0])
    height = max_height * len(lines)  # perfect or a little oversized
    width = int(round(max_width + 40))  # a little oversized
    image = PIL.Image.new(grayscale, (width, height), color=PIXEL_OFF)
    draw = PIL.ImageDraw.Draw(image)

    # draw each line of text
    vertical_position = 5
    horizontal_position = 5
    line_spacing = int(round(max_height * 0.8))  # reduced spacing seems better
    for line in lines:
        draw.text((horizontal_position, vertical_position),
                  line, fill=PIXEL_ON, font=font)
        vertical_position += line_spacing
    # crop the text
    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    return image

def main():
    global reduce_res
    print("Input an image")
    image_path = filedialog.askopenfilename()
    user_input = ''
    
    while user_input != 'y' and user_input != 'n':
        user_input = input("Would you like a specific character length resize? (y, n) \n"+
                           "Note that there will always be a basic resize, as txt files " +
                           "only support so many characters on one line (Base resize : 510 characters per line) ")

    width_size = 0
    reduce_res = True
    if user_input == 'n':
        width_size = 510
    elif user_input == 'y':
        width_size_input = 'a'
        
        width_size_input = input("Set the width to resize the pic as (Max width : 510) ")

        if int(width_size_input) > 510:
            print("Input width is above maximum! Setting width to 510")
            width_size = 510
        else:
            width_size = int(width_size_input)
    
    start_conversion('"' + image_path + '"', width_size)

if __name__ == '__main__':
    main()
