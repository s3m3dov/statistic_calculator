import math
from collections import Counter
#Ungrouped Data Class
class Ungrouped:
    def __init__(self):
        #Get datatype
        self.x = input(f"--Is data type [population] or [sample]?:  ")
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