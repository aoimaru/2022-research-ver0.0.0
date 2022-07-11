import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# test data
x = np.linspace(-5, 5, 100)
ys = np.ones(shape=(6, len(x))) * np.nan
ys[0] = 1
ys[1] = 1 + x
ys[2] = 1 + x + x**2 / 2
ys[3] = 1 + x + x**2 / 2 + x**3 / 6
ys[4] = 1 + x + x**2 / 2 + x**3 / 6 + x**4 / 24
ys[5] = 1 + x + x**2 / 2 + x**3 / 6 + x**4 / 24 + x**5 / 120

# plot
fig = plt.figure()
gs = gridspec.GridSpec(nrows=2, ncols=3, figure=fig)
for i in range(2):
    for j in range(3):
        ax = fig.add_subplot(gs[i, j])
        ax.plot(x, ys[3 * i + j], color='C0', zorder=5)
        ax.plot(x, np.exp(x), color='darkgray', linestyle='dashed', zorder=4)
        ax.set_title('plot ({}, {})'.format(i, j))
fig.tight_layout()

# save
# fig.savefig('multiple_plot2.jpg', dpi=600)
fig.show()