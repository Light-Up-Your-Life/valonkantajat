# Task 4 -  Domain Model

✓Identify key concepts and relationships  
✓Text format, or a simple ASCII diagram  
Hints:
• Read your requirements — pick out the nouns
• QuickPress example (slide 21)

| REQ-ID | Requirement Description | Key Concepts |
|--------|------------------------|--------------|
| 001    | The system must apply configurations correctly | system, configurations |
| 002    | Lighting must work the same way in all rooms | lighting, rooms |
| 003    | The system must show staff the lighting status of all rooms | system, staff, lighting status, rooms |
| 004    | The system must let staff control lighting across the property | system, staff, lighting, property |
| 005    | The system must integrate with existing infrastructure | system, infrastructure |
| 006    | The system must allow guests to adjust room lighting | system, guests, room, lighting |
| 007    | The system must comply with data protection standards | system, data, protection standards |
| 008    | The system should support scalability | system, scalability |
| 009    | The system should have a failover connection | system, failover connection |
| 010    | The system should be easy to install and set up | system, installation, setup |
| 011    | The user interface should load quickly | user interface, loading |
| 012    | The system could support different lighting modes | system, lighting modes |
| 013    | Guests could save personal lighting preferences | guests, personal lighting preferences |

## Summary:  
- System  
- Lighting  
- Rooms  
- Staff / Guests  
- Preference / Status / Modes  
- Infrastructure / Installation / setup

## Prototype Scope

Can you write "Verify that..." and end with a yes/no answer? If not, rewrite.  

| REQ‑ID | Requirement Description | Key Concepts |
|--------|--------------------------|-----------------------------------|
| 001    | The system must apply configurations correctly | system, configurations |
| 002    | Lighting must work the same way in all rooms | lighting, rooms |
| 003    | The system must show staff the lighting status of all rooms | system, staff, lighting status, rooms |
| 004    | The system must let staff control lighting across the property | system, staff, lighting, property |
| 008    | The system should support scalability | system, scalability |
| 010    | The system should be easy to install and set up | system, installation, setup |

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

## Relationships  


## Diagram (?)  
