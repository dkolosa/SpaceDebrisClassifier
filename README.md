# Space Debris Classifier and Debris Prediction

Imported a space debris dataset from star-track.org listing all of the tracked space objects around Earth. 
Used a Random Forest Regressor model to predict the decay date of various objects and optimizing its 
hyperparameters using grid search cross validation to achieve a training a test accuracy of 98% and 68%, 
respectively. Also implemented a nearest neighbors classifier to predict an object’s radar cross-section 
resulting in a training and test accuracy of 70% and 68%, respectively.

## Requirements
python > 3
pandas
sklearn
jypyter-notebook

## Usage
All data exploration, model training, and results are found in SPclassifier.ipynb
