# Space Debris Classifier and Debris Prediction

Imported a space debris dataset from star-track.org listing all of the tracked space objects around Earth. 
Used a Random Forest Regressor model to predict the decay date of various objects and optimizing its 
hyperparameters using grid search cross validation to achieve an accuracy of 75%. Also implemented a nearest neighbors classifier to predict an object’s radar cross-section 
resulting in an accuracy of 70% and 68%, respectively.

## Requirements
python > 3

pandas

sklearn

jypyter-notebook

## Usage
The implementation for this repository is found in [`SPclassifier.ipynb`](https://github.com/dkolosa/SpaceDebrisClassifier/blob/master/SPclassifier.ipynb)
