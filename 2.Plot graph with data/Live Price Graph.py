import pandas
import matplotlib.pyplot as plt
import matplotlib.animation as pltanimation
from matplotlib import style

#Creates graph to be drawn
style.use("dark_background")
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)

def animate(i):
    csv = pandas.read_csv("Price and time.csv")
    y = csv.iloc[1:, 2].values
    x = list(range(1, len(y)+1))
    ax1.clear()
    ax1.plot(x, y)
    ax1.set_title("S & P 500")

#Draws and refreshes graph based on data from PriceTimeCSV file
ani = pltanimation.FuncAnimation(fig, animate, interval = 1000)
plt.show()
