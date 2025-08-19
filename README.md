# Stylized Motion Blur in Houdini

## Overview
This project implements techniques from the [SIGGRAPH 2024 paper *“SMEAR: Stylized Motion Exaggeration with ARt-direction”*](https://research.siggraph.org) inside Houdini as a set of HDAs.  
The goal is to provide artists with a **controllable stylized motion blur** system that can generate cartoon-like “smear frames” (stretching, duplicating, and exaggerating motion) directly in Houdini.

### Key Features
- **Per-bone motion analysis** using Solver SOP + VEX.
- **Ribbon-based smear offsets** for single bones.  
- **Multi-bone weighted aggregation** for articulated figures.  
- Artist-friendly **controls for exaggeration, ribbon width, blend, and weighting**.  
- Works with **rigged characters, props, or custom animation data**.

