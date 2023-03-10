import sys
import requests
from io import BytesIO
from DeepImageSearch import SearchImage

# Send a GET request to the image URL
response = requests.get(sys.argv[1])

# Get the image data from the response
image_data = response.content

# Store the image data as a variable
image_variable = BytesIO(image_data)


print(SearchImage().get_similar_images(
    image_variable, number_of_images=int(sys.argv[2])))
