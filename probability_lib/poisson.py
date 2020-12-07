from math import exp, factorial
# Poisson Probability Distribution Class
class PoissonDist:
    def __init__(self):
        self.L = int(input("--The mean number of occurences in the in the interval (lambda):  "))
        self.x = int(input("--Number of successes in n trials (x):  "))
    # CALCULATE
    def Probability(self):
        return round((self.L**self.x)*exp(-self.L)/factorial(self.x), 4)
    # RETURN PART
    def return_probability(self):
        return f'Probability:  {self.Probability()}'
    # OUTPUT
    def get_output(self):
        # Commands & Results
        #Variables
        cmds = {
            'probability' : self.return_probability()
        } 
        
        # Print part
        print("------------------------------------------------------------------------\n------------------------------------------------------------------------")
        for cmd in cmds:
            print(cmds[cmd])