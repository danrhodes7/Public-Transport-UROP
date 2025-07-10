import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from stations import line_station_orders
from stations import line_colors

for line, color in line_colors.items():
    if line == "Walking":
        linestyle = '--'

filename = r"C:\Users\dan12\OneDrive\Documents\trains project\stations.csv"
df = pd.read_csv(filename)

G = nx.MultiGraph()
pos = {}

for _, row in df.iterrows():
    station = row['NAME']
    G.add_node(station)
    pos[station] = (round(row['x'], 4), round(row['y'], 4))

for line, station_data in line_station_orders.items():
    branches = station_data if isinstance(station_data[0], list) else [station_data]
    
    for branch in branches:
        for i in range(len(branch) - 1):
            G.add_edge(branch[i], branch[i + 1], line=line, time=2)

plt.figure(figsize=(15, 15))
nx.draw_networkx_nodes(G, pos, node_color='lightgrey', node_size=10)
# nx.draw_networkx_labels(G, pos, font_size=3)

def draw_offset_edges(G, pos, line, color, offset_distance=0.001):
    drawn = set()
    edge_dict = {}

    for u, v, d in G.edges(data=True):
        key = tuple(sorted((u, v)))
        edge_dict.setdefault(key, []).append(d['line'])

    for u, v, d in G.edges(data=True):
        if d.get('line') != line:
            continue

        key = tuple(sorted((u, v)))
        lines_on_edge = edge_dict[key]
        index = lines_on_edge.index(line)
        total = len(lines_on_edge)

        x1, y1 = pos[u]
        x2, y2 = pos[v]

        dx = x2 - x1
        dy = y2 - y1

        length = np.hypot(dx, dy)
        if length == 0:
            continue  
        perp_dx = -dy / length
        perp_dy = dx / length

        shift = (index - (total - 1) / 2) * offset_distance
        offset = (perp_dx * shift, perp_dy * shift)

        start = (x1 + offset[0], y1 + offset[1])
        end = (x2 + offset[0], y2 + offset[1])

        plt.plot([start[0], end[0]], [start[1], end[1]], color=color, linewidth=1.5, zorder=1)

for line, color in line_colors.items():
    draw_offset_edges(G, pos, line, color)


plt.title("Underground Stations Graph")
plt.axis('off')
plt.show()
