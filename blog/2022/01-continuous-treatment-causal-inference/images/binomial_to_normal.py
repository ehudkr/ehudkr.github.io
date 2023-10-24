import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# fig, ax = plt.subplots()
# # xdata, ydata = [], []
# # ln, = ax.plot([], [])
# ax.set(xlim=(-10, 10), ylim=(0, 2))
#
#
# def init():
#     ax.set_xlim(-10, 10)
#     ax.set_ylim(0, 2)
#     return ln,
#
#
# def update(frame):
#     x, y = generate_ith_frame(frame)
#     xdata.append(x)
#     ydata.append(y)
#     ln.set_data(xdata, ydata)
#     return ln,
#
#
# def generate_frames():
#     data = []
#     p = 0.5
#     N = [2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 75, 100, 200]
#     for n in N:
#         x = np.arange(stats.binom.ppf(0.01, n, p), stats.binom.ppf(0.99, n, p))
#         y = stats.binom(n, p).pmf(x)
#         data.append((x, y))
#     return data
#
#
# def generate_ith_frame(i):
#     p = 0.5
#     N = [2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 75, 100, 200]
#
#     n = N[i]
#     x = np.arange(stats.binom.ppf(0.01, n, p), stats.binom.ppf(0.99, n, p))
#     y = stats.binom(n, p).pmf(x)
#     return x, y
#
#
# # frames = generate_frames()
#
# ani = FuncAnimation(
#     fig,
#     update,
#     frames=list(range(14)),
#     init_func=init,
#     blit=True
# )
# plt.show()



# fig, ax = plt.subplots()
# ax.set(xlim=(-10, 10), ylim=(0, 2))
#
#
# def generate_frames():
#     data = []
#     p = 0.5
#     N = [2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 75, 100, 200]
#     for n in N:
#         x = np.arange(stats.binom.ppf(0.01, n, p), stats.binom.ppf(0.99, n, p))
#         y = stats.binom(n, p).pmf(x)
#         data.append((x, y))
#     return data
#
#
# frames = generate_frames()
# # ydata = np.row_stack((d[1] for d in frames))
# # xdata = np.row_stack((d[0] for d in frames))
# # line = ax.plot(xdata[0, :], ydata[0, :], color='k', lw=2)[0]
# line = ax.bar(frames[0][0], frames[0][1], color='k', lw=2)[0]
#
#
# def animate(i):
#     # line.set_x(frames[i][0])
#     # line.set_height(frames[i][1])
#     # line.set_y(frames[i][1])
#     ax.clear()
#     ax.set(xlim=(0, 20), ylim=(0, 1))
#     ax.bar(frames[i][0], frames[i][1], color='k', lw=2)[0]
#
#
# anim = FuncAnimation(
#     fig,
#     animate,
#     interval=100,
#     # frames=ydata.shape[0] - 1,
#     frames=len(frames) - 1,
#     # blit=True
# )
# plt.draw()
# plt.show()



fig, ax = plt.subplots()

rng = np.random.RandomState(0)
data = rng.normal(size=1000000)
N = [
    2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 75, 100, 150, 200,
    "kde", "kde", "kde", "kde", "kde", "kde", "kde", "kde",  # Freeze continuous frames
]

hist_params = dict(
    color='k',
    lw=2,
    density=True,
)

hist = ax.hist(data, bins=2, **hist_params)[0]
xlim = ax.get_xlim()


def animate(i):
    ax.clear()
    if i != "kde":
        ax.hist(data, bins=i, **hist_params)[0]
        if i >= 20:
            ax.set_ylim(0, 0.42)
        ax.text(
            0.85, 0.9,
            f'$n={i}$',
            # ha="right",
            transform=ax.transAxes,
            # color="white" if i == 2 else "black",
        )
    else:
        x = np.arange(-6, 6, 0.01)
        y = stats.norm.pdf(x)
        ax.plot(x, y, color='k', lw=2)
        ax.fill_between(x, 0, y, color='k')
        ax.set_ylim(0, ax.get_ylim()[1])
        ax.set_xlim(xlim)
        ax.set_ylim(0, 0.42)
        # ax.xaxis.set_major_locator(plt.MaxNLocator(5))


anim = FuncAnimation(
    fig,
    animate,
    interval=200,
    frames=N,
    # blit=True
)
# plt.draw()
# plt.show()
anim.save('binomial_to_normal.gif', writer='imagemagick', fps=4)

