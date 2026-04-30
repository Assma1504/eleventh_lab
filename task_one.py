from pathlib import Path
from PIL import Image, ImageFilter


currentPath = Path('filters')
folderFiltredImages = Path('Filtred_images')

if not folderFiltredImages.exists():

    folderFiltredImages.mkdir()

else:

    for item in currentPath.iterdir():

        myImg = Image.open(item)
        filtredImage = myImg.filter(ImageFilter.CONTOUR)
        filtredImage.save(folderFiltredImages / f'filtredImage{item.name}.jpg')
        myImg.close()




        # print(f"filtredImage{item.name}")
