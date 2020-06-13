# Calorie Intake Recommendation and Tracking
Although food packaging comes with calorie labels, it is not very convenient for people to refer. Therefore, we propose a DEEP LEARNING based
calorie tracking model to monitor people’s daily calorie intake. Based on an internally calculated parameter, our model also suggests
the users, appropriate food, and relevant exercises. Along with this, we have a food-label tracker as well, which will suggest the user if a particular food item is fit for consumption or not. 

## Mind Map

![mind map_page-0001](https://user-images.githubusercontent.com/57681462/84494924-ee051000-acc7-11ea-8002-406ca78bba20.jpg)


## Process Flow

![block diagram1](https://user-images.githubusercontent.com/57681462/84495028-20167200-acc8-11ea-91ca-4f9a76cfdf4e.png)


### DL-1: Obesity_Model
DL-1 takes physical attributes such as Age, Gender, Height and Weight as the training features and gives user's health state as the output.
In this model, the output is coded as: 
0: Underweight,
1: Healthy,
2: Overweight,
3: Obese. 

Dataset source: https://www.kaggle.com/freego1/bmi-data


### DL-2: Calorie_Model
DL-2 consists of two models, namely, food calorie model and activity calorie model. First model predicts the calorie intake value on consumption of given food, while the latter predicts calories burnt amount based on physical activity done (like walking, running, etc.).However, model was trained for limited data for prototype ,data can be expanded afterwards. Subtracting calorie intake and burnt data will give calorie consumed value.

Dataset_activity source: https://www.health.harvard.edu/diet-and-weight-loss/calories-burned-in-30-minutes-of-leisure-and-routine-activities

Dataset_food source: Kaggle, https://www.calories.info/food/, https://docs.google.com/spreadsheets/d/1snqE6leDkZlL61qQ4g-vUmiFjizJyN1OCVAhwWWKSm4/edit#gid=2024304766


### DL-3: Suggestions_model
DL-3 takes inputs from both DL-1 and DL-3 along with user's physical parameters. This model suggests healthy food and excercises like running and walking based on the calories intake.
