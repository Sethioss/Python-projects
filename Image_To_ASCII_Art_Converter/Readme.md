# Image file to ASCII art converter

------------------------------------------------------------------------

/!\If the program doesn't launch, you might need to install the PIL library /!\

This simple tool allows you to convert any image file into an ASCII art of the said image in two formats. A .txt file for copypasting, and a .png file for sending or uploading as an image.  

## Usage  

Upon launching the program, choose an image to convert into ASCII art. The original image will be copied in two folders created in the program's directory if they don't exist already. The "Image_resources" folder stores the original image and serves as a temporary holder for a resized version of the picture, while the ASCII art txt and png file outputs will be stored within the "ASCII_results" folder.

## Resizing

The program will ask you if you want a specific size to resize your image to. Since each character is written in a set of two to keep accurate proportions in the txt file, this size corresponds to half the number of characters per line in the .txt file.  
If you choose "No", the image will be automatically resized to the maximum number a .txt can have on a single lin, which corresponds to 510 (2*510 = 1020 characters, the maximum being 1024).  
If you choose "Yes", a number between 1 and 510 will be needed from the user. The image will proportionally be resized to fit the width provided by the user.  

Keep in mind that a larger width will increase the final output's precision, but also the png file's generation time and size.

## Examples

All images have been converted using the maximum width (The ASCII art txt and png files are available in the source project)  
All images belong to their respective owners

![Angel_Dust](https://user-images.githubusercontent.com/55959375/120187318-edd18d80-c214-11eb-9acb-ec7d18fedc0b.png)
![Angel_Dust(ASCII)](https://user-images.githubusercontent.com/55959375/120187471-1eb1c280-c215-11eb-9cff-bce40b4ed9f4.png)
![Final-Space](https://user-images.githubusercontent.com/55959375/120187535-325d2900-c215-11eb-971b-85066c96f8cf.png)
![Final-Space(ASCII)](https://user-images.githubusercontent.com/55959375/120187655-5f114080-c215-11eb-9386-d0bdb64e391f.png)
![Oz](https://user-images.githubusercontent.com/55959375/120188445-6c7afa80-c216-11eb-9717-4f1ea216d866.png)
![Oz(ASCII)](https://user-images.githubusercontent.com/55959375/120188687-b368f000-c216-11eb-8ee7-cf73b88c2753.png)



