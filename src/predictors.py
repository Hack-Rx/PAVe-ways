import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import joblib
import pickle

class Predictor():

    def obesity_predictor(self, age, sex, height, weight):

        # age_code
        if age <= 11:
            age_code = 0
        elif age > 11 and age < 18:
            age_code = 1
        elif age > 18 and age <= 22:
            age_code = 2
        elif age > 22 and age <= 27:
            age_code = 3
        elif age > 27 and age <= 33:
            age_code = 4
        elif age > 33 and age <= 40:
            age_code = 5
        elif age > 40 and age <= 66:
            age_code = 6
        if age > 66:
            age_code = 7

        # height code
        height_inch = 0.3937 * height
        if height_inch <= 60:
            height_code = 0
        elif height_inch > 60 and height_inch <= 64:
            height_code = 1
        elif height_inch > 64 and height_inch <= 66:
            height_code = 2
        elif height_inch > 66 and height_inch <= 68:
            height_code = 3
        elif height_inch > 68 and height_inch <= 70:
            height_code = 4
        elif height_inch > 70 and height_inch <= 74:
            height_code = 5
        elif height_inch > 74:
            height_code = 6

        # weight code
        weight_pound = 2.2046 * weight
        if weight_pound <= 78:
            weight_code = 0
        elif weight_pound > 78 and weight_pound <= 88:
            weight_code = 1
        elif weight_pound > 88 and weight_pound <= 98:
            weight_code = 2
        elif weight_pound > 98 and weight_pound <= 108:
            weight_code = 3
        elif weight_pound > 108 and weight_pound <= 118:
            weight_code = 4
        elif weight_pound > 118 and weight_pound <= 123:
            weight_code = 5
        elif weight_pound > 123 and weight_pound <= 128:
            weight_code = 6
        elif weight_pound > 128 and weight_pound <= 133:
            weight_code = 7
        elif weight_pound > 133 and weight_pound <= 143:
            weight_code = 8
        elif weight_pound > 143 and weight_pound <= 153:
            weight_code = 9
        elif weight_pound > 153 and weight_pound <= 163:
            weight_code = 10
        elif weight_pound > 163:
            weight_code = 11

        feature1 = np.array([age_code, sex, height_code,
                            weight_code]).reshape([1, 4])
        model1 = keras.models.load_model('../model/obesity_model.h5')
        bmi_code = model1.predict_classes(feature1)[0]

        return bmi_code


    def calories_predictor(self, food_intake, activity):

        model21 = pickle.load(open('../model/food_calorie_v1.0.pkl', 'rb'))
        model22 = pickle.load(open('../model/activity_calorie_v1.0.pkl', 'rb'))
        predict21 = model21.predict(food_intake).sum()
        predict22 = model22.predict(activity).sum()
        return predict21+predict22


    def suggestions_predictor(self, age, sex, height, weight, lean_factor, activity_factor, food_intake, activity):

        if sex == 0:
            sex_factor = 1
        else:
            sex_factor = 0.9

        bmr = weight * sex_factor * 24 * lean_factor
        calories_requried = bmr * activity_factor
        bmi_code = self.obesity_predictor(age, sex, height, weight)
        calories_intake = self.calories_predictor(food_intake, activity)

        input3 = np.array([sex_factor, age, height, weight, bmi_code, lean_factor,
                        bmr, activity_factor, calories_requried, calories_intake])
        predict_suggestion = keras.models.load_model('../model/suggestion_model_v1.1.h5')
        scalar = pickle.load(open('../model/suggestion_scaler.pkl', 'rb'))
        suggestions = predict_suggestion(scalar.transform(input3.reshape(1,-1))).numpy()

        return suggestions, calories_requried
