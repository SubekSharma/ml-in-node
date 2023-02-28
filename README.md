link to folder with photos

install library: deep-image-search

// const imgModule = require("deep-image-search")

- path to folder containing photos
- provide photos to be indexed (so that results are fast)

- module.recommendPhotos(pathToPhoto or arrayOfIndex, numberOfSimilarPhotos)

const photos = [
'https://www.cloudinary.com/gcsandesh/photogalaxy/firstPhoto.jpg',
'https://www.cloudinary.com/gcsandesh/photogalaxy/firstPhoto.jpg',
'https://www.cloudinary.com/gcsandesh/photogalaxy/firstPhoto.jpg',
'https://www.cloudinary.com/gcsandesh/photogalaxy/firstPhoto.jpg',
'https://www.cloudinary.com/gcsandesh/photogalaxy/firstPhoto.jpg',
'https://www.cloudinary.com/gcsandesh/photogalaxy/firstPhoto.jpg',
'https://www.cloudinary.com/gcsandesh/photogalaxy/firstPhoto.jpg'
]

imgModule.recommendPhotos(photos[0], 10);

recommendPhotos(pathToPhoto or arrayOfIndex, numberOfSimilarPhotos){
    //
}