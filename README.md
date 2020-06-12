# Calorie Intake Recommendation and Tracking
Although food packaging comes with calorie labels, it is not very convenient for people to refer. Therefore, we propose a DEEP LEARNING based
calorie tracking model to monitor people’s daily calorie intake. Based on an internally calculated parameter, our model also suggests
the users, appropriate food, and relevant exercises. Along with this, we have a food-label tracker as well, which will suggest the user if a particular food item is fit for consumption or not. 

## Mind Map

![mind map_page-0001](https://user-images.githubusercontent.com/57681462/84494924-ee051000-acc7-11ea-8002-406ca78bba20.jpg)

## Process Flow

![block diagram1](https://user-images.githubusercontent.com/57681462/84495028-20167200-acc8-11ea-91ca-4f9a76cfdf4e.png)

### DL-1
DL-1 takes physical attributes such as Age, Gender, Height and Weight as the training features and gives user's health state as the output.
In this model, the output is coded as: 
0: Underweight,
1: Healthy,
2: Overweight,
3: Obese. 

Dataset source: https://www.kaggle.com/freego1/bmi-data

