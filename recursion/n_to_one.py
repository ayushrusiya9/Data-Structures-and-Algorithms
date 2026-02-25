class Solution:
    """"
    this class is using to write a one to n programe. 
    """
    def printNumber(self, currentNumber):
        if currentNumber < 1:
            return
        
        self.printNumber(currentNumber - 1)

        print(currentNumber,end=" ")
    
if __name__ == "__main__":
    sol = Solution()
    n = 10
    sol.printNumber(n)
