import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt


def proyectarPts(T, wz, b=None):
    assert T.shape == (2, 2)  # chequeo de matriz 2x2
    assert T.shape[1] == wz.shape[0]  # multiplicacion matricial valida
    xy = None
    if b is not None:
        xy = T @ wz
        xy = np.xy + b
    else:
        ############### Insert code here!! ######################3
        xy = T @ wz
    ############### Insert code here!! ######################3
    return xy


def aplicar_transformacion(T: ndarray, wz: ndarray, traslacion: int = None):
    if T.shape[1] == wz.shape[0]:
        xy = T @ wz
        if traslacion:
            xy += traslacion


def dibujar_plano(T, wz, titulo="", b=None):
    # transformar los puntos de entrada usando T
    xy = proyectarPts(T, wz, b)
    if xy is None:
        print("No fue implementada correctamente la proyeccion de coordenadas")
        return
    # calcular los limites para ambos plots
    minlim = np.min(np.concatenate((wz, xy), 1), axis=1)
    maxlim = np.max(np.concatenate((wz, xy), 1), axis=1)

    bump = [
        np.max(((maxlim[0] - minlim[0]) * 0.05, 0.1)),
        np.max(((maxlim[1] - minlim[1]) * 0.05, 0.1)),
    ]
    limits = [
        [minlim[0] - bump[0], maxlim[0] + bump[0]],
        [minlim[1] - bump[1], maxlim[1] + bump[1]],
    ]

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(titulo)
    grid_plot(ax1, wz, limits, "w", "z")
    grid_plot(ax2, xy, limits, "x", "y")


def grid_plot(ax, ab, limits, a_label, b_label):
    ax.plot(ab[0, :], ab[1, :], ".")
    ax.set(
        aspect="equal", xlim=limits[0], ylim=limits[1], xlabel=a_label, ylabel=b_label
    )
