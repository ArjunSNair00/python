import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))
ax.set_ylim(-1.5, 1.5)
ax.set_title('Moving Sine Wave')

# Animation function
def update(frame):
    y = np.sin(x + frame * 0.1)  # Phase shift
    line.set_ydata(y)
    return line,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=np.arange(0, 200), interval=50, blit=True
)

plt.show()
