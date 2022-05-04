import numpy as np


class Validator:

    def validateFunction(self, func):
        func = func.replace(" ", "")
        func = func.replace("X", 'x')
        func = func.replace("^", "**")
        x = np.linspace(-5, 5, 100)
        y = 0
        try:
            y = eval(func)
            return y, True
        except:
            return y, False

    def validateInputRange(self, minValue, maxValue):
        try:
            minValue = float(minValue)
            maxValue = float(maxValue)
        except:
            return False

        if (float(minValue) >= float(maxValue)):
            return False
        return True
