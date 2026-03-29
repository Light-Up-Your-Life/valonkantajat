# Task 4 -  Domain Model

✓ Identify key concepts and relationships  
✓ Text format, or a simple ASCII diagram  

## Prototype Scope

| REQ‑ID | Requirement Description | Key Concepts |
|--------|--------------------------|-----------------------------------|
| 001    | When a configuration is saved, the system must apply all settings within 10 seconds | system, configurations |
| 002    | Lighting must work the same way in all rooms | lighting, rooms |
| 003    | The system must display the current lighting state of all rooms on a single screen | system, state, rooms, screen |
| 004    | Staff must be able to adjust lighting in any room from a control interface | system, staff, lighting, property |
| 008    | The system supports at least 100 rooms per setup | system, scalability |
| 010    | The system can be set up by a new user in under 10 minutes | system, installation, setup |

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


## Diagram

<img width="942.5" height="1240.2" alt="Prototype_Diagram_clean drawio" src="https://github.com/user-attachments/assets/c558939e-e53d-4add-90f5-dec55847132d" />

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
