import sys
from DeepImageSearch import SearchImage

# for searching, you need to give the image path and the number of the similar image you want
print(SearchImage().get_similar_images(sys.argv[1], int(sys.argv[2])))
