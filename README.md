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
project-root/
│
├─ assets/
│   ├─ player/
│   │    idle.png
│   │    run1.png
│   │    run2.png
│   │    jump.png
│   │    fall.png
│   │    player_cheer1.png
│   │
│   └─ tiles/
│        grass_single.png
│        grass_block_left.png
│        grass_block_middle.png
│        grass_block_right.png
│        dirt.png
│
├─ src/
│    main.py
│    levelmaps.py
│    (your other modules)
│
└─ README.md



---

## 🔧 Installation

### **1. Install Python**
This game works on **Python 3.10+**.

Download: https://www.python.org/downloads/

### **2. Install Pygame**
Open a terminal or command prompt:

```sh
pip install pygame

## 🔧 Installation

### **1. Install Python**
This game works on **Python 3.10+**.

Download: https://www.python.org/downloads/

### **2. Install Pygame**
Open a terminal or command prompt:

```sh
pip install pygame
Run the game

Inside the src folder:

python main.py

🧱 How Levels Work

Levels are stored in levelmaps.py like this:

LEVEL_MAPS = [
    [
        "............................",
        "............................",
        "...P.............XXX........",
        ".............XXXXXXXX.......",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ],
]


"X" = solid tile

"P" = player spawn point

"." = empty space

You can create as many levels as you want.

🎨 Player Animation System

The player supports 4 animation states:

idle

run

jump

fall

The files required inside assets/player/:

idle.png
run1.png
run2.png
jump.png
fall.png


(Optional final level reward)

player_cheer1.png

🌿 Tile System

Terrain is automatically selected using neighbor logic:

Tile	Used When
grass_single	No tile left or right
grass_left	No tile to the left
grass_middle	Tiles on both sides
grass_right	No tile to the right
dirt	Tile has another tile above it

This creates natural-looking platforms without placing individual tile types manually.

🧠 How the Camera Works

The camera follows the player:

camera_x = player.centerx - (WIDTH // 2)


The value is clamped so the camera never scrolls too far left or right.

🏆 Final Win Screen

At the end of the last level, the game displays a “You Win” screen with:

Sky background

Player cheer animation

Big text with drop shadow

Triggered after the last level.

🚀 Future Improvements

Ideas you can easily add:

Coins or collectibles

Enemies and patrol AI

Sound effects + music

HUD (lives, score)

Parallax backgrounds

Level transition animations

Game menus

📜 License

This project is released under the MIT License, meaning you are free to modify, share, and use it in your own games.

🤝 Contributing

Pull requests and new ideas are welcome!
If you'd like help expanding the game, feel free to open an issue.
