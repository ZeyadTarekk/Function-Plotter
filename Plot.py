from tkinter import messagebox
from Validator import *
import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, minValue, maxValue, func):
        self.minValue = minValue
        self.maxValue = maxValue
        self.func = func
        # self.root = root

    def finalPlot(self, x, y):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x, y, 'b', label="F(X)=" + self.func)
        plt.xlabel("X")
        plt.ylabel("F(X)")
        plt.legend(loc='upper left')
        plt.show()

    def plot(self):
        valid = Validator()
        x = 0
        y, flag, errorMessage = valid.validateFunction(self.func)
        if not flag:
            messagebox.showinfo(
                title='Error!',
                message=errorMessage
            )
            return
        else:
            flag, errorMessage = valid.validateInputRange(self.minValue, self.maxValue)
            if not flag:
                messagebox.showinfo(
                    title='Error!',
                    message=errorMessage
                )
                return
            else:
                x = np.linspace(float(eval(self.minValue)), float(eval(self.maxValue)), 100)
                self.finalPlot(x, y)
