
# **thumbnail-creator**

<mark>**⚠️** The command will reduce the quality of the image but this won't be a problem due to the thumbnails are small and don't require to much quality</mark>

the command will make a search throught the current directory to find all the images in the following formats:
- jpg
- png
- jpeg

The images will be transformed into thumbnails with the exact size for odoo's snippets  ( the original image isn't modified the command creates a copy )

## **Requirements 🔃**
    -pip install Pillow
    -pip install argparse

## **Usage 👷‍♂️**
---
-   *--thumb-all*
    - Run <mark>thumb-all</mark> command in a directory where you want to create your thumbnails , the command will create a folder called thumbnails where all of the images that you have in the current path will have a thumbnail.

---
-   *--thumb **< name_of_your_image> < .jpg >***
    - Run <mark>thumb < name_of_your_image > <.jpg> </mark> to specified the Image you want to create the thumbnail
    - **name_of_your_image:** the name of the file`(str)`
    - **extension:** the extension of the image (.jpg, .jpeg, .png) `(str)`
---
 ## Coming soon
-   *--thumb-custom-all **< width >** **< heigth >** **< rgb >***
    - Run <mark>thumb-custom-all < width > < heigth > < rgb > </mark> to create custom thumbnails
    - **width:** the width of the thumbnail in px `(int)`
    - **heigth** the heigth of the thumbnail in px `(int)`
    - **rgb** the background color in rgb format e.g.*255 255 255* `(int)`

---
-   *--thumb-custom **< name_of_your_image.jpg >** **< width >** **< heigth >** **< rgb >***
    - Run <mark>thumb-custom < name_of_your_image.jpg > < width > < heigth > < rgb > </mark> to create a custom thumbnails
    - **name_of_your_image.jpg:** the name of the file with it's extension (.jpg, .jpeg, .png) `(str)`
    - the other three parameters remains the same as the command above
