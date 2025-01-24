

# Machine-Learning-Models

Must use Jupiyter Notebook to run these projects

## 1 Linear Regression Model with Singel Variable

This notebook is designed to **predict house prices based on their areas** using a method called **linear regression**. It starts by importing the necessary libraries and loading a dataset that includes house areas and their prices. The data is cleaned by removing any rows with missing values. Then, it sets up a linear regression model, which is a simple way to find the relationship between two variables—in this case, the area of the house and its price. The model is trained using the existing data, and it then predicts prices for the given house areas. These predicted prices are added as a new column in the dataset. Finally, the actual and predicted prices are plotted on a graph to visually show how well the model's predictions match the real prices.

You can use this model for your practice and understanding by cloning the repositoy or downloading the model.


## 2 Linear Regression Model with Multiple Variables

This notebook is designed to **predict house prices based on multiple factors** using a method called **linear regression**. It starts by importing the necessary libraries and loading a dataset that includes house areas, number of bedrooms, age of the houses, and their prices. The data is cleaned by removing any rows with missing values. Then, it sets up a linear regression model, which is a method to find the relationship between multiple variables—in this case, the area of the house, number of bedrooms, age of the person, and its price. The model is trained using the existing data, and it then predicts prices based on other three variables. These predicted prices are added as a new column in the dataset. 

You can use this model for your practice and understanding by cloning the repositoy or downloading the model.


## 3 Gradient Descending Model

This script uses a method called gradient descent to find the best line that predicts values based on given data points. It starts by importing the NumPy library and defining the Gradient_Descent function. This function begins with the slope (m) and intercept (b) set to zero and updates them to reduce the error between the predicted and actual values. The learning rate is set to 0.08, and the function runs for 5000 steps. In each step, the script calculates the predicted values, finds the error, and adjusts m and b to make the error smaller. The updated values and error are printed in each step. At the end, the script shows how this process works with a simple example dataset, predicting values based on a small set of x and y coordinates.

You can use this model for your practice and understanding by cloning the repositoy or downloading the model.


## 4 One Hot Encoding

The notebook "One Hot Encoding.ipynb" is the demonstration for predicting the house prices using linear regression in Python, with a focus on using **dummy variables** and **one-hot encoding** to handle categorical data. 

The notebook starts by importing necessary libraries (Pandas and NumPy) and loading a dataset called "homeprices2.csv" into a DataFrame. It then creates dummy variables for the categorical column 'town' using pd.get_dummies(), concatenates these dummy variables back to the original DataFrame, and drops the original 'town' column and one of the dummy variable columns to avoid the dummy variable trap. After preparing the data, it uses Scikit-Learn's LinearRegression to train a model on the predictors and target variable ('price'). The notebook concludes by making predictions with the trained model and evaluating its performance using the score method.

You can use this model for your practice and understanding by cloning the repositoy or downloading the model.


## 5 Train Test Split

The Jupyter notebook **Test Train Split.ipynb** shows how to build a simple machine learning model to predict car prices using the car's mileage and age. It starts by loading the car prices data and then visualizes how mileage and age affect the price with scatter plots. The **main focus of the notebook is to show how to use the train_test_split method from scikit-learn** to divide the data into training and test sets. This method helps in separating the data so that some of it is used to train the model, and the rest is used to test how well the model performs. After splitting the data, the notebook trains a linear regression model on the training data, makes predictions on the test data, and then checks the accuracy of the model. This step-by-step process is a practical way to learn how to prepare data and build a predictive model.

You can use this model for your practice and understanding by cloning the repositoy or downloading the model.





















