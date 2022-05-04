from tkinter import *
from Plot import *


class GUI:
    def __init__(self):
        root = Tk()
        root.title("Function Plotter")
        root.geometry("800x500")
        root.resizable(False, False)
        mainLabel = Label(root, text="Function Plotter", font="Helvetica 26 bold italic")
        mainLabel.place(x=275, y=10)
        self.tipsScreen(root)
        self.fx = self.functionLabelFrame(root)
        self.minVal, self.maxVal = self.rangeLabelFrame(root)
        self.plotButton(root)
        root.mainloop()

    # Function responsible for building the frame of the function
    def functionLabelFrame(self, root):
        lfFunction = LabelFrame(root, text=' Enter a Valid Function', font="Helvetica 20 italic",padx=10)
        lfFunction.place(x=50, y=70)
        fxLabel = Label(lfFunction, text="F(X) = ", font="Helvetica 16")
        fxLabel.pack(side=LEFT, pady=20, padx=10)
        entryFunction = Entry(lfFunction, width=20, font="Helvetica 16")
        entryFunction.pack(side=LEFT, pady=20, padx=10)
        return entryFunction

    # Function responsible for building the frame of the range
    def rangeLabelFrame(self, root):
        lfRange = LabelFrame(root, text=' Enter a Valid Range', font="Helvetica 20 italic",padx=10)
        lfRange.place(x=50, y=222)
        minLabel = Label(lfRange, text="Min = ", font="Helvetica 16")
        minLabel.pack(side=LEFT, pady=20, padx=2)
        entryMin = Entry(lfRange, width=9, font="Helvetica 16")
        entryMin.pack(side=LEFT, pady=20)

        maxLabel = Label(lfRange, text="Max = ", font="Helvetica 16")
        maxLabel.pack(side=LEFT, pady=20, padx=2)
        entryMax = Entry(lfRange, width=8, font="Helvetica 16")
        entryMax.pack(side=LEFT, pady=20, padx=5)
        return entryMin, entryMax

    # Function responsible for building the plot button
    def plotButton(self, root):
        button = Button(root, text="Plot", command=self.getInputsAndPlot,bg="#DADADA",width=10, font="Helvetica 20")
        button.place(x=320, y=400)

    # Utility Function responsible for taking the input fields and plot the figure
    def getInputsAndPlot(self):
        plotObj = Plot(self.minVal.get(), self.maxVal.get(), self.fx.get())
        plotObj.plot()

    # Function responsible for building the tips part
    def tipsScreen(self, root):
        lfTips = LabelFrame(root, text='Some tips', font="Helvetica 20 italic",pady=20)
        lfTips.place(x=450, y=70)

        tip2Label = Label(lfTips, text="The following operators are", font="Helvetica 16")
        tip2Label.pack(padx=10)

        tip3Label = Label(lfTips, text="supported:  + - / * ^", font="Helvetica 16")
        tip3Label.pack()

        tip1Label = Label(lfTips, text="Valid function is like: 5*x^3 + 2*x", font="Helvetica 16")
        tip1Label.pack(pady=20, padx=10)

        tip4Label = Label(lfTips, text="You can use sin,cos and tan ", font="Helvetica 16")
        tip4Label.pack(padx=10)

        tip5Label = Label(lfTips, text="in this form: cos(x),sin(x)..", font="Helvetica 16")
        tip5Label.pack()
