import matplotlib.pyplot as plt


class RealtimePlot:
    def __init__(self, title='', x_label='', y_label=''):
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        self.axes.set_title(title)
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)
        self.x_data = []
        self.y_data = []
        self.plot, = self.axes.plot(self.x_data, self.y_data)
        self.figure.show()

    def add(self, x, y):
        self.x_data.append(x)
        self.y_data.append(y)
        self.plot.set_data(self.x_data, self.y_data)
        self.axes.relim()
        self.axes.autoscale_view()
        self.figure.canvas.draw()
