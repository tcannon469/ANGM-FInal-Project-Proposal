# 🕹️ Mini Python Platformer  
*A simple 2D platformer built with Python + Pygame*

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Pygame](https://img.shields.io/badge/pygame-2.5-orange)

---

## 📌 Overview

This project is a **fully animated mini side-scrolling platformer** made using **Python** and **Pygame**.  
It includes:

- Animated player (idle, run, jump, fall)
- Grass/dirt auto-tiling terrain
- Multi-level support
- Collision physics
- Smooth side-scrolling camera
- “You Win” end screen
- Clean, expandable code structure

This project is great for beginners learning game development with Pygame or for experimenting with your own assets and levels.

---

## 🎮 Features

- ✔️ Smooth player movement + jump physics  
- ✔️ Sprite animation system  
- ✔️ Automatic tile selection (grass, dirt, edges, middle)  
- ✔️ Level maps defined in simple text format  
- ✔️ Camera following the player  
- ✔️ Easily expandable for enemies, items, checkpoints and more  

---

## 📂 Folder Structure

```text
project-root/
│
├── assets/
│   ├── player/
│   │   ├── idle.png
│   │   ├── run1.png
│   │   ├── run2.png
│   │   ├── jump.png
│   │   ├── fall.png
│   │   └── player_cheer1.png
│   │
│   └── tiles/
│       ├── grass_single.png
│       ├── grass_block_left.png
│       ├── grass_block_middle.png
│       ├── grass_block_right.png
│       └── dirt.png
│
├── src/
│   ├── main.py
│   ├── levelmaps.py
│   └── (your other modules)
│
└── README.md

```
## 🔧 Installation
 
### 1. Install Python

Make sure you have Python 3.10+ installed.

Download from: https://www.python.org/downloads/

### 2. Install Pygame

In a terminal (or command prompt):
```
pip install pygame
```

### 3. Run the Game  
From inside the `src` folder:
```bash
python main.py
```

## 🎮 Controls
Left / A – Move left  
Right / D – Move right  
Up / W / Space – Jump  
Esc – Quit

## 🧱 Level Maps (levelmaps.py)
Levels are defined as lists of text rows:
```python
LEVEL_MAPS = [
    [
        "............................",
        "............................",
        "...P.............XXX........",
        ".............XXXXXXXX.......",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]
]
```

Legend:  
X → Solid block  
P → Player start  
. → Empty space

## 🎨 Player Animations
Player graphics obtained from : 
    **Kenney Platformer Art Characters** — https://kenney.nl/assets  
     Licensed under **CC0 (Public Domain)** 
     
Player animation frames must exist in `assets/player/`:
  

```text
idle.png
run1.png
run2.png
jump.png
fall.png
player_cheer1.png (optional)
```

States: 
The player has 4 animation states:
 - idle  
 - run  
 - jump  
 - fall  

The game loads, scales, and flips these automatically.

## 🌿 Tile System
Tile graphics obtained from:  
   **Kenney Platformer Art Extended TileSet** — https://kenney.nl/assets  
   Licensed under **CC0 (Public Domain)** 

Tile artwork loaded from `assets/tiles/`:

```text
grass_single.png
grass_block_left.png
grass_block_middle.png
grass_block_right.png
dirt.png
```

Tile logic:  
Each tile in the map is a 32×32 block (TILE_SIZE = 32).
For each 'X' in the level:
- If no tile above → draw grass  
- Else → draw dirt  

Grass type depends on neighbors:  
```
| Left neighbor | Right neighbor | Tile used          |
| ------------- | -------------- | ------------------ |
| none          | none           | grass_single       |
| none          | yes            | grass_block_left   |
| yes           | yes            | grass_block_middle |
| yes           | none           | grass_block_right  |
```
This produces natural-looking platforms without manually placing edge tiles.

## 🧠 Camera System
Camera centers on the player:
```python
camera_x = player.rect.centerx - WIDTH // 2
```

Clamped so the world doesn’t scroll too far.

All objects are drawn with:
```python
draw_x = tile.x - camera_x
```
The x-position of tiles and player is shifted by -camera_x
This makes the world appear to scroll while the player moves

## 🏆 Final Victory Screen
After the final level, the game shows:
- Sky background  
- Ground platform  
- player_cheer1.png (scaled up)  
- “YOU WIN!” text  
Waits for key press before closing.

## 🧩 Main Components (Summary)
✔ Player class  
Handles: Input, Physics, Collision, Animation, Drawing

✔ Level builder  
Creates tiles from 'X' and determines player start 'P'.

✔ Tile renderer  
Decides grass/dirt tiles using neighbor rules.

✔ Camera helper  
Centers the view and applies scrolling.

✔ Main loop  
Initializes pygame, Loads assets, Runs game, Switches levels, Shows final screen

## 🚀 Possible Extensions
Collectibles and coins  
Enemies with simple AI  
Music and sound effects  
Parallax backgrounds  
Checkpoints and lives  
HUD (score, health)  
Level editor

## 📜 License
MIT License (recommended). Add a LICENSE file in the repo.
