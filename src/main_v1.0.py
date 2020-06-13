from predictors import Predictor
from suggestions import Suggestion
import numpy as np

if __name__ == "__main__":

    age = 28
    sex = 1
    height = 180
    weight = 75
    lean_factor = 0.9
    activity_factor = 1.5
    food_intake = np.array([[101, 500, 1], [102, 120, 2]])
    activity = np.array([[101, height, weight], [105, height, weight]])
    p = Predictor()
    s = Suggestion()
    suggestions, calories_requried = p.suggestions_predictor(
        age, sex, height, weight, lean_factor, activity_factor, food_intake, activity)
    # print(len(suggestions))
    # print(suggestions)
    s1 = s.exercise_suggestion(suggestions[0, 0], suggestions[0, 1])
    s2 = s.food_rec(suggestions[0, 2], calories_requried)
    print(s1)
    print(s2)

    # age = input("Age: ")
    # sex = input("Sex: ")
    # height = input("Height in centimeters: ")
    # weight = input("Weight in kilograms: ")
    # lean_factor = input("Lean factor: ")
    # activity_factor = input("Activity Factor: ")
