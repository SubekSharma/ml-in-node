from imageai.Classification import ImageClassification

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
prediction.setModelTypeAsInceptionV3()
prediction.setModelPath('C:\\Users\\subek\\Desktop\\python-in-node\\inception_v3_google-1a9a5a14.pth')
prediction.loadModel()

predictions, probabilities = prediction.classifyImage("C:\\Users\\subek\\Desktop\\python-in-node\\img.jpg", result_count=10)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)

