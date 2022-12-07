import os
from PIL import Image
from argparse import ArgumentParser


_FORMATS = ['.jpg', '.png', '.jpeg']

class ThumbnailCreator:

    def __init__(self, args): 
        self.args = args

    def run(self):
        (command, args) = self.args
        if command.thumb_all:
            self.__thumbnail_all_images()
        elif command.thumb != None:
            self.__thumbnail_image(command.thumb)

    def __thumbnail_all_images(self):
        """creates a thumbnail of all the images in the current path"""
        count = False
        for file in os.listdir():
            file_name, extension = os.path.splitext(file)
            if extension in _FORMATS:
                count = True
                self.__create_thumbnail(file_name, extension)    
        print("⭐️⭐️⭐️ Thumbnails Created! 🍰 ⭐️⭐️⭐️" if count else "🛑 No images found 🛑")

    def __thumbnail_image(self, img_info):
        """creates a thumbnail with the sepecified name of the image"""
        if len(img_info) == 2:
            image_name = img_info[0]
            extension = img_info[1]
            for file in os.listdir():
                if file == image_name + extension:
                    self.__create_thumbnail(image_name, extension)
                    print("⭐️⭐️⭐️ Thumbnail Created! 🍰 ⭐️⭐️⭐️")
                    return
        print("🛑 Image not found in the current path 🛑")


    def __create_thumbnail(self, name = None, extension = None, width = None, heigth = None, rgb = None):
        if not os.path.exists("thumbnails"):
            os.mkdir("thumbnails")
        image = Image.open(name + extension, 'r')
        image_size = image.size
        width = image_size[0]
        height = image_size[1]
        bigside = width if width > height else height
        background = Image.new('RGB', (bigside, bigside), (56, 56, 59))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))
        background.paste(image, offset)
        background.thumbnail((100, 85))
        background.save('./thumbnails/%s-thumbnail%s' % (name, extension), quality=100, subsampling=0)


def parseArguments():
    parser = ArgumentParser()
    parser.add_argument("--thumb-all",
                        action="store_true",
                        help="💥 Create default thumbnails with all the images of the current path"
                        )
    parser.add_argument("--thumb",
                        nargs="*",
                        type=str,
                        help="💥 Create a thumbnaill with the name of the image specified. Takes: name of the image with format separated by a white space",
                        )
    return parser.parse_known_args()


def main():
    args = parseArguments()
    thumbnailCreator = ThumbnailCreator(args) 
    thumbnailCreator.run()

if __name__ == "__main__":
    main()
