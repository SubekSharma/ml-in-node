import sys
import requests
from io import BytesIO
from imageai.Classification import ImageClassification

# Send a GET request to the image URL
response = requests.get(sys.argv[1])

# Get the image data from the response
image_data = response.content

# Store the image data as a variable
image_variable = BytesIO(image_data)



# import os
# execution_path = os.getcwd()

# prediction = ImageClassification()
# prediction.setModelTypeAsInceptionV3()
# prediction.setModelPath('C:\\Users\\subek\\Desktop\\python-in-node\\inception_v3_google-1a9a5a14.pth')
# prediction.loadModel()

# predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "C:\\Users\\subek\\Desktop\\python-in-node\\img.jpg"), result_count=10)
# for eachPrediction, eachProbability in zip(predictions, probabilities):
#     print(eachPrediction , " : " , eachProbability)


prediction = ImageClassification()
prediction.setModelTypeAsInceptionV3() #Here i used Inception however any one could be used 

#Directly give the path where the model is stored or use above code to join paths 
prediction.setModelPath('C:\\Users\\subek\\Desktop\\python-in-node\\inception_v3_google-1a9a5a14.pth')
prediction.loadModel()

predictions, probabilities = prediction.classifyImage("C:\\Users\\subek\\Desktop\\python-in-node\\img.jpg", result_count=10)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    # print(eachPrediction , " : " , eachProbability)
    print(eachPrediction )

