from django.db import models

from io import BytesIO
from django.core.files import File
from PIL import Image
from collections import Counter
from django.core.files.images import ImageFile

# Create your models here.

# models.py 

def getColors(image):
    contrast = 10000
    img = Image.open(image)
    img = img.convert('RGB')
    pixel_list = list(img.getdata())
    count_list = Counter(pixel_list).most_common(contrast)
    mode_list = []

    for index, mode in enumerate(count_list):
	    if index % (contrast//5) == 0:
               mode_list.append(mode[0])

    Palette = Image.new('RGB', (500,500))

    for i in range (0,5):

        for x in range(0+(i*100),100*(i+1)):

            for y in range(0,500):
                   
                Palette.putpixel((x,y), mode_list[i])

    paletteIO= BytesIO()
    Palette.save(paletteIO, 'JPEG', quality=85)
    paletteFile = ImageFile(paletteIO, name="palette.jpg")
    return(paletteFile)


class processImage(models.Model):

    name = models.CharField(max_length=50) 
    Choose_Image= models.ImageField(upload_to='images/')
    palette = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):

        self.palette = getColors(self.Choose_Image)
        super().save(*args, **kwargs)





