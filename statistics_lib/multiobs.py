import math
#Multi Observation Class
class MultiObs:
    def __init__(self):
        #Get datatype
        self.x = input(f"--Is data type [population] or [sample]?:  ")
        self.dataType = self.x.lower()
        # Get data
        self.y = input("--Enter values:  ")
        self.z = input("--Enter frequencies:  ")
        try:
            self.intro_values = self.y.split(", ")
            self.values = [float(_) for _ in self.intro_values]
            self.intro_freq = self.z.split(", ")
            self.freq = [float(_) for _ in self.intro_freq]
        except:
            self.intro_values = self.y.split(" ")
            self.values = [float(_) for _ in self.intro_values]
            self.intro_freq = self.z.split(" ")
            self.freq = [float(_) for _ in self.intro_freq]
    # CALCULATE
    # ObservationCount, CumulativeFrequencies
    def ObservCount(self):
        sumir = 0
        for fre in self.freq:
            sumir += fre
        return round(sumir, 3)
    def CumFreq(self):
        temp_sumir = 0
        res = []
        for fre in self.freq:
            temp_sumir += fre
            res.append(round(temp_sumir, 3))
        return res
    # Mean, Mode, Median
    def Mean(self):
        sumir = 0
        for x in range(len(self.values)):
            sumir += self.freq[x]*self.values[x]
        return round(sumir/self.ObservCount(), 3)
    def Mode(self):
        res = []
        for x in range(len(self.freq)):
            if self.freq[x] == max(self.freq):
                res.append(round(self.values[x], 3))
        return res
    def Median(self):
        mdth = int((self.ObservCount()+1)/2)-1
        cumfreq = self.CumFreq()
        for x in range(len(cumfreq)):
            if cumfreq[x] <= mdth <= cumfreq[x+1]:
                class1 = x+1
            if cumfreq[x] <= mdth+1 <= cumfreq[x+1]:
                class2 = x+1
        return round((self.values[class1]+self.values[class2])/2, 3)
    # Variance, StandardDeviation
    def Variance(self):
        mmean = self.Mean()
        n = self.ObservCount()
        sumir = 0
        for x in range(len(self.values)):
            sumir += self.freq[x]*(self.values[x]**2)
        if self.dataType == "population":
            return round( (sumir/n)-mmean**2 , 3)
        else:
            return round( (sumir-(n*(mmean**2)))/(n-1) , 3)
    # ---
    def StandardDeviation(self):
        return round(math.sqrt(self.Variance()), 3)
    # RETURN PART
    def return_mean(self):
        return f'Mean:  {self.Mean()}'
    def return_mode(self):
        return f'Mode:  {self.Mode()}'    
    def return_median(self):
        return f'Median:  {self.Median()}'
    def return_variance(self):
        return f'{self.dataType.capitalize()} Variance:  {self.Variance()}'
    def return_stdev(self):
        return f'{self.dataType.capitalize()} Standard Deviation:  {self.StandardDeviation()}'
    # OUTPUT
    def get_output(self):
        # Commands & Results
        #Variables
        cmds = {
            'mean' : self.return_mean(),
            'median' : self.return_median(),
            'mode' : self.return_mode(),
            'variance' : self.return_variance(),
            'standard deviation' : self.return_stdev(),
        } 
        # Get commands
        z = input(f"--We can find these: {list(cmds.keys())}.\n--Please, write like 'example, example, ...' or press ENTER for calculating all:  ")
        if z=="":
            commands = cmds.keys()
        else:
            commands = z.split(", ")
            for i in range(len(commands)):
                commands[i] = commands[i].lower()
            for i in range(len(commands)):
                if commands[i] not in cmds:
                    commands[i] = input(f"--{commands[i]} is not specified as operation. Please, correct it carefully:  ")
        # Print part
        print("------------------------------------------------------------------------\n------------------------------------------------------------------------")
        for cmd in cmds:
            print(cmds[cmd])