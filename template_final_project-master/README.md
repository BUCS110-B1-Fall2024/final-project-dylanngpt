
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Productivity App >>
## CS110 B1 Final Project  << Fall 2024 >>

## Team Members

 Dylan Guthrie 

***

## Project Description

 Project Description
Our project is a Productivity App designed to help users enhance focus and manage stress. The app combines a focus timer, task checklist, goal tracking, and stress-relief features to create a streamlined tool for organization and mental well-being. Key features include:

A Focus Timer with customizable durations for productivity.
A Daily Checklist to organize tasks and track completion.
Goal Tracking, including both mini and big goals, for progress monitoring.
A Breathing Timer with sound guidance to promote relaxation and reduce stress.
This app aims to provide an intuitive, user-friendly interface with efficient functionality to support better mental health and productivity.

 

***    

## GUI Design

### Initial Design

![initial gui]((https://ibb.co/Smqj6pk)
### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Focus Timer with customizable intervals.
2. Daily Checklist with task addition/removal.
3 . Mini Goals and Big Goals tracking.
 4.Breathing Timer with guided audio cues.
5. Progress-saving functionality to retain user data across sessions.

### Classes

Timer: Handles focus timer and breathing timer functionality.
Checklist: Manages daily tasks, including adding, removing, and marking tasks as complete.
Goals: Tracks mini and big goals with the ability to update progress.
GUIManager: Controls the graphical user interface and user interaction.
DataHandler: Manages data saving and loading for task and goal persistence.

ATP


Step	                      Procedure	        Expected Results
1	Launch the app	          Main window       opens with all elements visible
2	Set a focus timer	          Timer           starts countdown correctly
3	Add a daily task	          Task             appears in the checklist
4	Mark a task complete	      Task              marked as done with visual update
5	Add a goal	                Goal             is displayed in the goals section
6	Use the breathing timer	    Timer             counts correctly with sound cues
7	Close and reopen the app	  Data           is saved and restored correctly
