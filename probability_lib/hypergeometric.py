from probability_lib.comb_per import combination
# Hypergeometric Probability Distribution Class
class HyperDist:
    def __init__(self):
        self.N = int(input("--Total number of elements in the population (N):  "))
        self.S = int(input("--Number of successes in the population (S):  "))
        self.F = self.N-self.S 
        self.n = int(input("--Number of trials (n):  "))
        self.x = int(input("--Number of successes in n trials (x):  "))
        self.f = self.n-self.x
    # CALCULATE
    def Probability(self):
        return round(combination(self.S, self.x)*combination(self.F, self.f)/combination(self.N, self.n), 4)
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