import numpy as np
import pandas as pd

class Suggestion:

    def roundoff(self, x, base):
        return int(base * round(float(x)/base))

    def exercise_suggestion(self, walk_day,run_day):
        
        self.walk_min = self.roundoff((walk_day*24*60),15)
        self.run_min = self.roundoff((run_day*24*60),15)
        
        if self.walk_min<=0.01: self.walk_min=30
        if self.run_min<=0.1: self.run_min=0
        
        self.suggestions = "Walk for " + str(self.walk_min) + " minutes and run for " + str(self.run_min) + " minutes"
        # print("Walk for", int(arr[0]), "minutes and run for" , int(arr[1]) , "minutes")
        return self.suggestions
    
    def food_rec(self, ratio, calc_req):

        data= pd.read_csv('../datasets/fruits_v0.2.csv', delimiter=',',header=0, index_col=0, skipinitialspace=True)
        data = data.to_numpy()
        self.ratio = ratio
        self.calc_req = calc_req
        calc_need = self.ratio * self.calc_req
        
        food_b = round((data[1,1] * 0.4 * calc_need)/data[1,4])
        food_o = round((data[3,1] * 0.2 * calc_need)/data[3,4])
        food_p = self.roundoff((data[4,1] * 0.2 * calc_need)/data[4,4], 50)
        food_g = self.roundoff((data[2,1] * 0.2 * calc_need)/data[2,4], 50)

        self.suggestions = "Banana: " + str(food_b) + " units, " + "Orange: " + str(food_o) + " units, " + "Papaya: " + str(food_p) + " grams & "\
              + "Grapes: " + str(food_g) + " grams"
        
        return self.suggestions