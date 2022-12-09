
# **Thumbnail-creator**

<mark>**⚠️** The command will reduce the quality of the image but this won't be a problem due to the thumbnails are small and don't require to much quality</mark>

the command will make a search throught the current directory to find all the images or the image in the following formats:
- jpg
- png
- jpeg

The images will be transformed into thumbnails with the exact size for odoo's snippets  ( the original image isn't modified the command creates a copy )

## **Requirements 🔃**
    -pip install Pillow
    -pip install argparse

## **Usage 👷‍♂️**
it's recommended to create an alias to the path where you are going to save the thumbnail_creator.py file.

e.g.
| Location    | alias |
| ----------- | ----------- |
| ~/Personal/thumbnail_creator.py      | alias thumbnail="python3  ~/Personal/thumbnail_creator.py"       |
---
-   *your_alias --thumb-all*
    - Run <mark>thumb-all</mark> command in a directory where you want to create your thumbnails , the command will create a folder called thumbnails where all of the images that you have in the current path will have a thumbnail.

---
-   *your_alias --thumb **< name_of_your_image> < .jpg >***
    - Run <mark>thumb < name_of_your_image > <.jpg> </mark> to specified the Image you want to create the thumbnail
    - **name_of_your_image:** the name of the file`(str)`
    - **extension:** the extension of the image (.jpg, .jpeg, .png) `(str)`
