class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def __init__(self,elements):
        self.__elements = elements
        
    def computeDifference(self):
        maxDiff = 0
        for i in range(len(self.__elements)-1):
            for j in range(i+1, len(self.__elements)):
                diff = abs(self.__elements[i] - self.__elements[j])
                if diff > maxDiff:
                    maxDiff = diff
        self.maximumDifference = maxDiff
