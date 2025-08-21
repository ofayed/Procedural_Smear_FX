# Stylized Motion Blur in Houdini

## Overview
This project implements techniques from the [SIGGRAPH 2024 paper *“SMEAR: Stylized Motion Exaggeration with ARt-direction”*](https://research.siggraph.org) inside Houdini as a set of HDAs.  
The goal is to provide artists with a **controllable stylized motion blur** system that can generate cartoon-like “smear frames” (stretching, duplicating, and exaggerating motion) directly in Houdini.

## Thesis
This project is part of my thesis research on **Stylized Motion Blur Houdini Digital Asset**.  
The full thesis paper is included in this repository and can be accessed here:

📄 [Read the Thesis Paper](Thesis_Paper.pdf)

### Key Features
- **Per-bone motion analysis** using Solver SOP + VEX.
- **Ribbon-based smear offsets** for single bones.  
- **Multi-bone weighted aggregation** for articulated figures.  
- Artist-friendly **controls for exaggeration, ribbon width, blend, and weighting**.  
- Works with **rigged characters, props, or custom animation data**.

## Available Effects

This HDA provides multiple stylized motion effects inspired by traditional 2D animation smear frames and FX animation.  
Each effect can be enabled independently or combined for more complex results.

### 1. Smear Effect
Creates an **exaggerated motion blur** by stretching the geometry along its motion path.  
Instead of a camera-based blur, this generates **cartoon-like elongated shapes** that mimic hand-drawn smear frames.  
Useful for:
- Fast action sequences (e.g., sword swings, punches).
- Stylizing character animation to feel more “2D-like.”

### 2. Trail Lines
Generates **drawn-like motion trails** that follow or lead the animation.  
Artists can control whether trails:
- **Follow** the motion (classic afterimage smear).  
- **Lead** the motion (anticipation/exaggeration).  
- Or do **both** simultaneously.  
These trails can be tuned for length, opacity, and thickness.

### 3. Animation Copies
Creates **multiple offset copies of the animation** to mimic the look of **2D animation motion blur**.  
Instead of a smooth smear, this produces **“frame stutter” style echoes**, like when 2D animators draw several copies of a character’s limb in different positions.  
Perfect for:
- Punchy stylized hits.
- Retro anime-style effects.

### 4. Smoke / Dust Simulation
Built-in **pyro solver** and **POP networks** create stylized smoke or dust bursts that trigger from motion.  
This can be driven by speed or impact, letting you add:
- Dust puffs when characters land.  
- Smoke trails following fast-moving objects.  
- Cartoon-style secondary motion effects.

### 5. Energy Particle Simulation
Generates a **particle-based “energy aura” effect** that comes with a preset material for rendering.  
Particles can be shaped, colored, and stylized to resemble:  
- Energy trails / power-up effects.  
- Magical aura bursts.  
- Stylized lightning or glowing streaks.  

## Installation

This project contains two separate HDAs, each packaged in its own folder.  
You can use either HDA individually or both together, depending on the effect you want.

### Steps
1. **Clone or download** this repository:
2. Import the HDA into Houdini : File → Import → Houdini Digital Asset and then choose the one or both of the .hdanc
3. Follow the walkthrough videos for help
- 🎥 [Characters HDA Walkthrough](Demos/Character_Demo.MOV)  
- 🎥 [Regular Objects HDA Walkthrough](Demos/Object_Demo.MOV) 
## Demo

👉 [Watch the demo video](Demos/Example_Renders.MOV)

## 3D Model Credits

The demo scenes and walkthroughs use publicly available 3D models.  
All rights belong to their respective creators.  

- [Mixamo](https://www.mixamo.com/) – Source for all 3D character rigs and animations used in the demo videos.  
- [Apple Model](https://www.fab.com/listings/34d0ab78-7287-4d36-954e-c3461231e3a8) – via Fab.com.  
- [Toy Rocket Model](https://www.fab.com/listings/b8be6c85-2d54-47cf-9010-7b3e9de0b33a) – via Fab.com.  
- [Magic Wand Model](https://www.fab.com/listings/0711299c-ca45-4315-8cb1-08592c77de62) – via Fab.com.  
- [Basketball Model](https://www.fab.com/listings/be7c485f-bd36-4313-97c5-1f1d8e6ac48f) – via Fab.com.  

