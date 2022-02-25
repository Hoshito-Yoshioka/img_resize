# img_resize
This file takes multiple file paths and resizes them all at once.
When saving the resized image, add "_resized(img_size)" to the file name.

You can change the destination path, the name of the directory where the image will be saved, the length of the sides of the square, and the value to be added to the file name.

Things to keep in mind when using this file as is:

1.The value of the variable (img_size) is set to 500, so it will resize the image file to a 500x500 square.
  You can change this value to make any square you want.
  If you want to resize the image to a rectangle with different horizontal and vertical lengths, change the img.resize property.
  
2.It is necessary to create the directory for retrieving the image in advance.If you do, please change the path to the destination file.
  You do not need to create a directory to save the images.
  
3.Versions
  Python --3.9.1
  Pillow --9.0.1
