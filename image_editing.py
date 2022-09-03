from PIL import Image
import io

def convert_to_BW(image_object):
    """ Converts image from color to black & white
    - Takes an image object
    - Returns a file object """
    image = Image.open(image_object)
    image = image.convert("L")
    b = io.BytesIO()
    image.save(b, "JPEG")
    # image.show()
    b.seek(0)
    return b
