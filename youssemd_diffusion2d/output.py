import matplotlib.pyplot as plt


def create_plot(fig, u, T_cold, T_hot, time_step, dt, fig_counter):
    """Creates a single plot for a specific time step."""
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    ax.set_axis_off()
    ax.set_title(f'{time_step * dt * 1000:.1f} ms')
    return im


def output_plots(fig, im):
    """Finalizes and displays the combined plots."""
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
