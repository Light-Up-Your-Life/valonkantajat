# Task 4 -  Domain Model

✓Identify key concepts and relationships  
✓Text format, or a simple ASCII diagram  
Hints:
• Read your requirements — pick out the nouns
• QuickPress example (slide 21)

## Prototype Scope

Can you write "Verify that..." and end with a yes/no answer? If not, rewrite.  

| REQ‑ID | Requirement Description | Key Concepts |
|--------|--------------------------|-----------------------------------|
| 001    | When a configuration is saved, the system must apply all settings within 10 seconds | system, configurations |
| 002    | Lighting must work the same way in all rooms | lighting, rooms |
| 003    | The system must display the current lighting state of all rooms on a single screen | system, state, rooms, screen |
| 004    | The system must let staff control lighting across the property | system, staff, lighting, property |
| 008    | The system supports at least 100 rooms per setup | system, scalability |
| 010    | The system can be set up by a new user in under 10 minutes | system, installation, setup |

**Unique nouns across prototype scope:**  

system, configuration, lighting, room(s), staff, status, property

## Your Prototype Scope

Four functions most teams identified — the core of what your prototype should prove  

1. **Create a lighting profile**
   
* Define a named set of lighting parameters (brightness, color temperature, scene) that can be reused.  

2. **Apply a profile to rooms**  

* Select a profile and deploy it to one or more rooms — the "configure once, sync everywhere" promise.  

3. **View room status**
   
* See which profile each room is running, whether it's online, and whether the last sync succeeded.

4. **Guest overrides their room**
   
* A guest selects a mood from an in-room control. Their change doesn't affect other rooms. Resets on checkout.  

Functions 1+2 together = the core promise. Your prototype should prove this loop works end to end.

## Key Concepts

### Core System Concepts

- System
- Room
- Lighting
- LightingMode
- LightingStatus
- LightingPreference

### Actors
- Guest
- Staff

### Configuration Concepts
- Configuration
- Property

### Operations & Infrastructure
- Infrastructure
- Installation / Setup
- FailoverConnection

## Relationships

### Rooms & Lighting
- Room has Lighting
- Lighting has LightingStatus
- Lighting may use LightingModes

### Guests & Rooms
- Guest controls Lighting in Room
- Guest may save LightingPreferences

### Staff & System
- Staff monitors LightingStatus across Rooms
- Staff applies Configurations to Rooms

### System & Configuration
- System stores Configurations
- System applies Configurations to Rooms

### Infrastructure
- System integrates with Infrastructure
- Installation sets up System on Infrastructure

### Failover
- System has FailoverConnection

## Diagram (?)  

<img width="800" height="1000" alt="Prototype_Diagram_clean drawio" src="https://github.com/user-attachments/assets/8de30f64-be05-42b2-a24c-99a7ce3c5c26" />


## Architecture

### Architecture  

big decisions, hard to change  

* What components does the system have?  
* How do they communicate?  
* What technology? Where is data stored?  

### UI/UX Design  

what the user sees and does  

* What does using the product look like?  
* What is the interaction model?  
* How are errors communicated?  
