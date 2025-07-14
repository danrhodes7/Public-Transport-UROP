import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.spatial import KDTree
import pandas as pd
import math
import matplotlib.ticker as mticker

def meters_to_degrees(radius_meters, lat_deg=51.5):
    meters_per_deg_lat = 111000  
    meters_per_deg_lon = 111000 * math.cos(math.radians(lat_deg))
    radius_deg_lat = radius_meters / meters_per_deg_lat
    return radius_deg_lat

filename = r"C:\Users\dan12\OneDrive\Documents\trains project\stations2.csv"
df = pd.read_csv(filename)

df = df[df['Zone'].isin(range(11))]

df = df[df['x'] >= -0.65]
points = df[['x', 'y']].values
tree = KDTree(points)

margin = 0.01
xmin, ymin = points.min(axis=0) - margin
xmax, ymax = points.max(axis=0) + margin

grid_resolution = 200  
xgrid = np.linspace(xmin, xmax, grid_resolution)
ygrid = np.linspace(ymin, ymax, grid_resolution)
xx, yy = np.meshgrid(xgrid, ygrid)
grid_points = np.vstack([xx.ravel(), yy.ravel()]).T

def compute_density(radius_meters):
    radius_deg = meters_to_degrees(radius_meters)
    counts = np.array([len(tree.query_ball_point(p, radius_deg)) for p in grid_points])
    return counts.reshape((grid_resolution, grid_resolution))

init_radius_metres = 500

fig, ax = plt.subplots(figsize=(10, 10))
plt.subplots_adjust(bottom=0.25)

density = compute_density(init_radius_metres)

fixed_vmin = 0
fixed_vmax = 16

heatmap = ax.imshow(density, extent=(xmin, xmax, ymin, ymax), origin='lower', cmap='viridis', vmin=fixed_vmin, vmax=fixed_vmax)
cbar = plt.colorbar(heatmap, ax=ax)
cbar.set_label("Stations within radius")

cbar.ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%d'))

ax.set_title(f"Station Density Heatmap (radius = {init_radius_metres} m)")
ax.set_xlabel("Longitude (degrees)")
ax.set_ylabel("Latitude (degrees)")

ax_radius = plt.axes([0.25, 0.1, 0.5, 0.03])
slider = Slider(ax_radius, 'Radius (meters)', 100, 2000, valinit=init_radius_metres, valstep=50)

def update(val):
    radius = slider.val
    new_density = compute_density(radius)
    heatmap.set_data(new_density)
    ax.set_title(f"Station Density Heatmap (radius = {radius})")
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()
