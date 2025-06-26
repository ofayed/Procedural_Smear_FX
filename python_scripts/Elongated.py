import numpy as np
node = hou.pwd()
geo = node.geometry()


inputs = [node.inputs()[i].geometry() for i in range(4)]
num_points = len(inputs[0].points())

delta_attr = geo.findPointAttrib("delta_norm")
delta_norms = np.array([p.attribValue(delta_attr) for p in geo.points()])
beta_max = 1.0  
betas = delta_norms * beta_max


new_positions = []

# Catmull-Rom helper
def catmull_rom(p0, p1, p2, p3, t):
    """C-R spline interpolation"""
    t2 = t * t
    t3 = t2 * t
    return 0.5 * ((2 * p1) +
                  (-p0 + p2) * t +
                  (2*p0 - 5*p1 + 4*p2 - p3) * t2 +
                  (-p0 + 3*p1 - 3*p2 + p3) * t3)

for i in range(num_points):
    beta = betas[i]
    frame_offset = int(np.floor(beta))
    t = beta - frame_offset

  
    f0 = np.clip(frame_offset + 0, 0, 3)
    f1 = np.clip(frame_offset + 1, 0, 3)
    f2 = np.clip(frame_offset + 2, 0, 3)
    f3 = np.clip(frame_offset + 3, 0, 3)

    p0 = np.array(inputs[f0].points()[i].position())
    p1 = np.array(inputs[f1].points()[i].position())
    p2 = np.array(inputs[f2].points()[i].position())
    p3 = np.array(inputs[f3].points()[i].position())

    new_pos = catmull_rom(p0, p1, p2, p3, t)
    new_positions.append(new_pos)

for i, point in enumerate(geo.points()):
    point.setPosition(hou.Vector3(new_positions[i]))
