---

# Falling Objects Game  
## CS110 B1 Final Project - Fall 2024  

## Team Members  

**Dylan Guthrie**  

---

## Project Description  

Our project is a **Falling Objects Game**, an interactive and fast-paced game where players control a character using arrow keys to dodge objects falling from the sky. The goal is to avoid collisions while earning points based on survival time. The game includes escalating difficulty as objects fall faster over time, adding to the challenge. Key features include:

- **Dynamic gameplay**: Objects increase speed and variety over time.  
- **Interactive controls**: Smooth movement with arrow keys for precise dodging.  
- **Score tracking**: Points are awarded based on survival duration, with a high-score feature.  
- **Power-ups**: Optional shields or speed boosts for extra excitement.  
- **Unique design**: Vibrant visuals and engaging sound effects enhance the gaming experience.  

This game is designed to provide an engaging and competitive experience for players of all skill levels.  

---

## GUI Design  

### Initial Design  

![initial gui](https://ibb.co/Smqj6pk)  

### Final Design  

![final gui](assets/finalgui.jpg)  

---

## Program Design  

### Features  

1. **Player Movement**: Arrow key controls for smooth navigation.  
2. **Falling Objects**: Randomized objects with varying speeds and sizes.  
3. **Score System**: Tracks survival time and displays high scores.  
4. **Difficulty Progression**: Gradual increase in object speed and frequency.  
5. **Power-Ups**: Optional items for added excitement, such as shields or temporary speed boosts.  
6. **Data Persistence**: Saves high scores to a file for future sessions.  

### Classes  

- **Player**: Manages the character's position, movement, and collision detection.  
- **FallingObject**: Represents objects falling from the sky, with attributes like speed and type.  
- **Game**: Oversees the game logic, including difficulty scaling and score tracking.  
- **GUIManager**: Handles rendering of the game screen and updates based on user interaction.  
- **DataHandler**: Manages saving and loading of high scores from a file.  

---

## Acceptance Test Plan (ATP)  

| **Step**                     | **Procedure**                           | **Expected Results**                                |  
|-------------------------------|-----------------------------------------|---------------------------------------------------|  
| 1. Launch the game            | Run the program                        | Main window opens with character and objects visible |  
| 2. Move the character         | Use arrow keys to move left/right       | Character responds smoothly to inputs             |  
| 3. Objects fall               | Start the game                         | Objects fall from the top of the screen           |  
| 4. Avoid collision            | Move character to avoid objects         | No collision; game continues                      |  
| 5. Collision detection        | Let the character collide with an object | Collision ends game and shows the final score     |  
| 6. Score updates              | Survive as long as possible            | Score increases based on survival time            |  
| 7. High score saving          | Close and reopen the game              | High score is retained and displayed              |  

---
