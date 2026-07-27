import numpy as np
import matplotlib.pyplot as plt

def fleche(ax, z, couleur, label=None):
    """créer Z comme une fleche partant de l'origine"""
    ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=couleur, lw=2))
    if label:
        ax.text(z.real * 1.08, z.imag * 1.08, label, color=couleur)

def prepare_axes(ax, lim=1.5):
    ax.set_aspect("equal")
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim)
    ax.axhline(0, color="gray", lw=0.5); ax.axvline(0, color="gray", lw=0.5)
    ax.grid(True, alpha=0.3)
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(t), np.sin(t), color="lightgray", lw=1)  # cercle unité

fig, ax = plt.subplots(figsize=(6, 6))
prepare_axes(ax)

z0 = 0.6+0.8j
for theta in [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]:

    z_turn = z0 * (np.exp(1j*theta))
    fleche(ax, z_turn, "teal")
    print(abs(z_turn))
plt.show()

