import numpy as np

node = hou.pwd()
geo = node.geometry()


points = geo.points()
positions = np.array([p.position() for p in points])
velocities = np.array([p.attribValue("v") for p in points]) 


centroid = np.mean(positions, axis=0)

vel_norms = np.linalg.norm(velocities, axis=1)
vel_norms[vel_norms == 0] = 1e-8 
v_hats = velocities / vel_norms[:, np.newaxis]


relative_positions = positions - centroid
deltas = np.sum(relative_positions * v_hats, axis=1)


max_abs_delta = np.max(np.abs(deltas))
if max_abs_delta == 0:
    normalized_deltas = deltas * 0
else:
    normalized_deltas = deltas / max_abs_delta

delta_attr = geo.addAttrib(hou.attribType.Point, "delta_norm", 0.0)
color_attr = geo.addAttrib(hou.attribType.Point, "Cd", (0.0, 0.0, 0.0)) 

for i, point in enumerate(points):
    delta_val = float(normalized_deltas[i])
    point.setAttribValue(delta_attr, delta_val)

  
    gray = 0.5 * (delta_val + 1.0)

    color = (1.0 - gray, 0.0, gray) 

    point.setAttribValue(color_attr, color)
