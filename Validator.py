import numpy as np


class Validator:

    def validateFunction(self, func):
        y = 0
        if (func == ""):
            return y, False, "Enter a function"
        if "**" in func:
            return y, False,"Invalid Function, Enter a valid function"
        try:
            z = int(func)
            return y, False,"Invalid Function, Enter a valid function"
        except:
            func = func.replace(" ", "")
            func = func.replace("X", 'x')
            func = func.replace("^", "**")
            func = func.replace("cos", "np.cos")
            func = func.replace("sin", "np.sin")
            func = func.replace("tan", "np.tan")

            x = np.linspace(-5, 5, 100)
            try:
                y = eval(func)
                return y, True, ""
            except:
                return y, False, "Invalid Function, Enter a valid function"

    def validateInputRange(self, minValue, maxValue):
        if minValue == "" or maxValue == "":
            return False, "You must enter a minimum value and maximum value for X"

        try:
            minValue = float(eval(minValue))
            maxValue = float(eval(maxValue))
        except:
            return False, "Invalid input range! Enter a valid input range"

        if (float(eval(str(minValue))) >= float(eval(str(maxValue)))):
            return False, "Invalid input range! minimum value must be smaller than maximum value"
        return True, ""
