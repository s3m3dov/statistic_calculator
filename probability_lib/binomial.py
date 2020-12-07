import math
from probability_lib.comb_per import combination
# Binomial Probability Distribution Class
class BinomialDist:
    def __init__(self):
        self.n = int(input("--Total number of trials (n):  "))
        self.p = float(input("--Probability of success (p):  "))
        if self.p > 1:
            print("--Probability of success can't be greater than 1")
            self.p = float(input("--Probability of success (p):  "))
        self.q = 1-self.p
        self.x = input("--Enter number of success in (n) trials or press 'ENTER' for empty:  ")
        if self.x == "":
            self.x = None
        else:
            self.x = int(self.x)
            self.f = self.n - self.x
    # CALCULATE
    def Probability(self):
        try:
            return round(combination(self.n, self.x)*(self.p**self.x)*(self.q**self.f), 3)
        except:
            return None
    def Mean(self):
        return round(self.n*self.p, 3)
    def StandardDeviation(self):
        return round(math.sqrt(self.n*self.p*self.q), 3)
    # RETURN PART
    def return_probability(self):
        return f'Probability:  {self.Probability()}'
    def return_mean(self):
        return f'Mean:  {self.Mean()}'
    def return_stdev(self):
        return f'Standard Deviation:  {self.StandardDeviation()}'
    # OUTPUT
    def get_output(self):
        # Commands & Results
        #Variables
        cmds = {
            'probability' : self.return_probability(),
            'mean' : self.return_mean(),
            'standard deviation' : self.return_stdev(),
        } 
        # Print part
        print("------------------------------------------------------------------------\n------------------------------------------------------------------------")
        for cmd in cmds:
            print(cmds[cmd])