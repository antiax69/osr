from django.db import models
from django.conf import settings
from osr.static.python.storage import OverwriteStorage

#https://djangosnippets.org/snippets/10597/
import cv2
from PIL import Image, ExifTags
import numpy as np
from osr.static.python.board3 import border

# Create your models here.

class SudokuModel (models.Model):
    image = models.ImageField(upload_to='uploads/', storage=OverwriteStorage(), blank=True)

    def save(self):
        image = Image.open(self.image)
        #try:
            #image=Image.open(filepath)
        #    for orientation in ExifTags.TAGS.keys():
        #        if ExifTags.TAGS[orientation]=='Orientation':
        #            break
        #    exif=dict(image._getexif().items())

        #    if exif[orientation] == 3:
        #        image=image.rotate(180, expand=True)
        #    elif exif[orientation] == 6:
        #        image=image.rotate(270, expand=True)
        #    elif exif[orientation] == 8:
        #        image=image.rotate(90, expand=True)
            #image.save(filepath)
            #image.close()

        #except (AttributeError, KeyError, IndexError):
            # cases: image don't have getexif
        #    pass
        im_opencv = np.array(image)
        #cv2.imwrite(settings.MEDIA_ROOT + "/image_uploaded.jpg", im_opencv)
        #cv2.putText(im_opencv,"Hello World!!!", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
        #cv2.imwrite(settings.MEDIA_ROOT + "/output.png", im_opencv)
        cv2.imwrite(settings.MEDIA_ROOT + "board_border.jpg", border(im_opencv))

        super(SudokuModel,self).save()


    def __str__(self):
        return self.name
