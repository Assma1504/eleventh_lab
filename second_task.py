from PIL import Image, ImageFilter
from pathlib import Path


currentPath = Path('filters')
folderFiltredImages = Path('Filtred_images')
listSuffixes = [".png", ".jpg"]


for item in currentPath.iterdir():
    if item.suffix in listSuffixes:
        myImg = Image.open(item)
        filtredImage = myImg.filter(ImageFilter.CONTOUR)
        filtredImage.save(folderFiltredImages / f'filtredImage{item.name}.jpg')
        myImg.close()
else:
        print("Thers is no file to edit")
