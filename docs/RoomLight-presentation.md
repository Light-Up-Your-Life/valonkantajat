# RoomLight Presentation  

## Problem & value  
- Hotels typically use one lighting setup for all rooms  
- Guests have different preferences  
- Staff need centralized control  
- RoomLight allows configuring lighting once and syncing everywhere  
- Guests can override lighting locally  
- Overrides reset correctly  

**Core Promise**  
> Configure lighting once and sync it to all rooms  

---

## Scope & Requirements  
**In Scope**  
- Create lighting profiles  
- Apply profiles to multiple rooms  
- View room status  
- Guest override  
- Reset on checkout  

**Out of Scope**  
- Real IoT hardware  
- Network failures 
- Security  

**Key Requirements**  
- Consistent behavior across rooms  
- Centralized control  
- Local overrides  
- Reset on checkout  
- Supports at least 100 rooms  

---

## Architecture & SW Design

**Main Components**  

**Design decisions**  

---

## Test Plan  
**Test Levels**  
- Unit testing  
- Integration testing  
- End-to-end testing  
- Negative testing  

**High-Risk Areas**  
- Multi-room configuration sync  
- Override isolation  
- Checkout reset  
- Persistence reload  

**Exit Criteria**  
- No crashes  
- Core flow works  
- Consistent state  
- Overrides remain local  

---

## Demo  
**Demo Steps**  
1. Create lighting profile  
2. Apply profile to all rooms  
3. Show room status  
4. Apply guest override to one room  
5. Verify other rooms unchanged  
6. Checkout reset  
7. Restart system (persistence)  

**What This Demonstrates**  
- Configure once  
- Sync everywhere  
- Local override  
- Reset on checkout  
- State persistence  

---

## What we learned  
**Technical Learnings**  
- Requirement-driven design  

**Project Learnings**  
- Importance of scope limitation  
- Prototype vs production differences  





