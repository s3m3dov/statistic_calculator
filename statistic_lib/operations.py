import math
from collections import Counter

# OPERATIONS
#Ungrouped Data Class
class Ungrouped:
    def __init__(self):
        #Get datatype
        self.x = input(f"--Select your datatype from {dataTypes}:  ")
        self.dataType = self.x.lower()
        # Get data
        self.y = input("--Enter elements:  ")
        try:
            self.intro_data = self.y.split(", ")
            self.data = [float(_) for _ in self.intro_data]
        except:
            self.intro_data = self.y.split(" ")
            self.data = [float(_) for _ in self.intro_data]
        self.data.sort()
    # CALCULATE
    # Mean, Mode, Median, Range
    def Mean(self):
        return round(sum(self.data)/len(self.data), 3)
    def Mode(self):
        res = []
        nums = dict(Counter(self.data))
        max_count = max(nums.values())
        for num in nums.keys():
            if nums[num] == max_count:
                res.append(round(num, 3))
        if max_count == 1:
            return None
        else:
            return res
    def Median(self):
        index = int(((len(self.data)+1)/2)-1)
        if len(self.data)%2!=0:
            return round(self.data[index], 3)
        else:
            return round((self.data[index] + self.data[index + 1])/2, 3)
    def Range(self):
        return round(self.data[-1]-self.data[0], 3)
    # M.A.D, Variance, StandardDeviation, IQR
    def MAD(self):
        mmean = self.Mean()
        sumir = 0
        for numn in self.data:
            sumir += math.sqrt((numn-mmean)**2)
        return round(sumir/len(self.data), 3)
    def Variance(self):
        mmean = self.Mean()
        sumir = 0
        for numn in self.data:
            sumir += (numn-mmean)**2
        if self.dataType == "population":
            return round(sumir/len(self.data), 3)
        else:
            return round(sumir/(len(self.data)-1), 3)
    # ---
    def StandardDeviation(self):
        return round(math.sqrt(self.Variance()), 3)
    def IQR(self):
        q1th = (len(self.data)+1)/4
        q3th = ((len(self.data)+1)/4)*3
        q1 = self.data[int(q1th)-1]+(q1th-int(q1th))*(self.data[int(q1th)]-self.data[int(q1th)-1])
        q3 = self.data[int(q3th)-1]+(q3th-int(q3th))*(self.data[int(q3th)]-self.data[int(q3th)-1])
        return round(q3-q1, 3)
    # RETURN PART
    def return_sorted(self):
        return f'Sorted data:  {self.data}'
    def return_mean(self):
        return f'Mean:  {self.Mean()}'
    def return_mode(self):
        return f'Mode:  {self.Mode()}'    
    def return_median(self):
        return f'Median:  {self.Median()}'
    def return_range(self):
        return f'Range:  {self.Range()}'
    def return_mad(self):
        return f'Mean Absolute Deviation:  {self.MAD()}'
    def return_variance(self):
        return f'{self.dataType.capitalize()} Variance:  {self.Variance()}'
    def return_stdev(self):
        return f'{self.dataType.capitalize()} Standard Deviation:  {self.StandardDeviation()}'
    def return_iqr(self):
        return f'Interquartile Range:  {self.IQR()}'
    # OUTPUT
    def get_output(self):
        # Commands & Results
        #Variables
        cmds = {
            'sorted data' : self.return_sorted(),
            'mean' : self.return_mean(),
            'median' : self.return_median(),
            'mode' : self.return_mode(),
            'range' : self.return_range(),
            'mad' : self.return_mad(),
            'variance' : self.return_variance(),
            'standard deviation' : self.return_stdev(),
            'iqr' : self.return_iqr() 
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

#Multi Observation Class
class MultiObs:
    def __init__(self):
        #Get datatype
        self.x = input(f"--Select your datatype from {dataTypes}:  ")
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

#Grouped Data Class
class Grouped:
    def __init__(self):
        #Get datatype
        self.x = input(f"--Select your datatype from {dataTypes}:  ")
        self.dataType = self.x.lower()
        self.values = []
        # Get data
        self.y = input("--Enter values:  ")
        self.z = input("--Enter frequencies:  ")
        try:
            self.intro_values = self.y.split(", ")
            self.intro_freq = self.z.split(", ")
            self.freq = [float(_) for _ in self.intro_freq]
        except:
            self.intro_values = self.y.split(" ")
            self.intro_freq = self.z.split(" ")
            self.freq = [float(_) for _ in self.intro_freq]
        # Create tuples for lower and upper boundary in values
        for x in range(len(self.intro_values)):
            self.values.append(self.intro_values[x].split('-'))
            for y in range(2):
                self.values[x][y] = float(self.values[x][y])

    # CALCULATE
    # ObservationCount, CumulativeFrequencies, RelativeFrequencies, CumulativeRelativeFrequencies
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
    def RelFreq(self):
        res = []
        for i in range(1, len(self.freq)):
            temp = self.freq[i] - self.freq[i-1]
            res.append(abs(round(temp, 3)))
        return res
    def CumRelFreq(self):
        cumfreq = self.CumFreq()
        res = []
        for cfre in cumfreq:
            res.append(round(cfre/self.ObservCount(), 3))
        return res
    # Mean
    def Mean(self):
        sumir = 0
        for index in range(len(self.values)):
            midpoint = (self.values[index][0]+self.values[index][1])/2
            sumir += self.freq[index]*midpoint
        return round(sumir/self.ObservCount(), 3)
    # Mode-Modal class, Mode, Modal class
    def ModeModalClass(self):
        for x in range(len(self.freq)):
            if self.freq[x] == max(self.freq):
                return x+1
    def ModalClass(self):
        x = self.ModeModalClass()-1
        res = []
        res.append(self.values[x])
        return res[0]
    def Mode(self):
        classList = self.ModalClass()
        return (classList[0]+classList[1])/2
    # Median Class, #Median
    def MedianClass(self):
        mdth = int((self.ObservCount()+1)/2)-1
        cumfreq = self.CumFreq()
        for x in range(len(cumfreq)):
            if cumfreq[x] <= mdth <= cumfreq[x+1]:
                medianclass = x+2
        return medianclass
    def Median(self):
        mdclass = self.MedianClass() - 1
        lower = self.values[mdclass][0]
        upper = self.values[mdclass][1]
        m1obs = self.freq[mdclass-1]
        mobs = self.freq[mdclass]
        return round(  (((self.ObservCount()/2) - m1obs)/mobs)*(upper-lower) + lower , 3)
    # Variance, StandardDeviation, InterquartileRange
    def Variance(self):
        mmean = self.Mean()
        n = self.ObservCount()
        sumir = 0
        for x in range(len(self.values)):
            sumir += self.freq[x]*((self.values[x][0]+self.values[x][1])/2 - mmean)**2
        if self.dataType == "population":
            return round( sumir/n , 3)
        else:
            return round( sumir/(n-1) , 3)
    # ---
    def StandardDeviation(self):
        return round(math.sqrt(self.Variance()), 3)
    def IQR(self):
        # Variables
        cumfreq = self.CumFreq()
        # Calculate Q1
        q1th = (self.ObservCount()+1)/4
        q1thi = int(q1th)
        #Finding j1th and j1class
        for x in range(len(cumfreq)):
            if cumfreq[x] <= q1thi <= cumfreq[x+1]:
                j1tha = int(q1thi-cumfreq[x])
                j1tha_class = x+1
            if cumfreq[x] <= q1thi+1 <= cumfreq[x+1]:
                j1thb = int((q1thi+1)-cumfreq[x])
                j1thb_class = x+1
            #Calculating j1 values
        j1a = self.values[j1tha_class][0] + ((j1tha - 0.5)* ((self.values[j1tha_class][1]-self.values[j1tha_class][0]) /self.freq[j1tha_class] ) )
        j1a = round(j1a, 3)
        j1b = self.values[j1thb_class][0] + ((j1thb - 0.5)* ((self.values[j1thb_class][1]-self.values[j1thb_class][0]) /self.freq[j1thb_class] ) )
        j1b = round(j1b, 3)
        #Q1 value
        q1 = round(j1a + (q1th-q1thi)*(j1b-j1a), 3)

        # Calculate Q2
        q3th = 3*q1th
        q3thi = int(q3th)
        #Finding j1th and j1class
        for x in range(len(cumfreq)):
            if cumfreq[x] <= q3thi <= cumfreq[x+1]:
                j3tha = int(q3thi-cumfreq[x])
                j3tha_class = x+1
            if cumfreq[x] <= q3thi+1 <= cumfreq[x+1]:
                j3thb = int((q3thi+1)-cumfreq[x])
                j3thb_class = x+1
            #Calculating j1 values
        j3a = self.values[j3tha_class][0] + ((j3tha - 0.5)* ((self.values[j3tha_class][1]-self.values[j3tha_class][0]) /self.freq[j3tha_class] ) )
        j3a = round(j3a, 3)
        j3b = self.values[j3thb_class][0] + ((j3thb - 0.5)* ((self.values[j3thb_class][1]-self.values[j3thb_class][0]) /self.freq[j3thb_class] ) )
        j3b = round(j3b, 3)
        #Q1 value
        q3 = round(j3a + (q3th-q3thi)*(j3b-j3a), 3)

        return round(q3-q1, 3)
    # RETURN PART
    def return_cumfreq(self):
        return f'Cumulative Frequencies:  {self.CumFreq()}'
    def return_relfreq(self):
        return f'Relative Frequencies:  {self.RelFreq()}'
    def return_cumrelfreq(self):
        return f'Cumulative Relative Frequencies:  {self.CumRelFreq()}'   
    def return_mean(self):
        return f'Mean:  {self.Mean()}'
    def return_modal(self):
        return f'Modal Class:  {self.ModalClass()} - {self.ModeModalClass()}.class'
    def return_mode(self):
        return f'Mode:  {self.Mode()} - {self.ModeModalClass()}.class'    
    def return_median(self):
        return f'Median:  {self.Median()};  Median Class: {self.MedianClass()}.class: {self.values[self.MedianClass()-1][0]}-{self.values[self.MedianClass()-1][1]}'
    def return_variance(self):
        return f'{self.dataType.capitalize()} Variance:  {self.Variance()}'
    def return_stdev(self):
        return f'{self.dataType.capitalize()} Standard Deviation:  {self.StandardDeviation()}'
    def return_iqr(self):
        return f'Interquartile Range:  {self.IQR()}'
    # OUTPUT
    def get_output(self):
        # Commands & Results
        #Variables
        cmds = {
            'cumfreq' : self.return_cumfreq(),
            'relfreq' : self.return_relfreq(),
            'cumrelfreq' : self.return_cumrelfreq(),
            'mean' : self.return_mean(),
            'median' : self.return_median(),
            'modal class' : self.return_modal(),
            'mode' : self.return_mode(),
            'variance' : self.return_variance(),
            'standard deviation' : self.return_stdev(),
            'iqr' : self.return_iqr()
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

#VARIABLES
dataTypes = ["population", "sample"]
observType = {
    "ungrouped": Ungrouped,
    "multi observation": MultiObs,
    "grouped": Grouped
}
