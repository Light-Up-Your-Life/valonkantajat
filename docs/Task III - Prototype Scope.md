# Task 3 – Prototype Scope

## Task

1. Prototype description — 3–5 sentences: what does it do, who is it for, what does it prove?
2. Demonstrate — which product requirements (REQ-IDs) the prototype proves. Why?

## Prototype description  
The RoomLight prototype simulates a set of rooms and their lighting states (008). It lets a user create one lighting configuration and apply it to all rooms or selected rooms at once (001, 002, 004), demonstrating “configure once, sync everywhere.” The tool also allows viewing the lighting state of every room with a single command (003), proving that room verification can be done quickly. The prototype runs as a simple script (010) and demonstrates how the final system will support hotel staff workflows.  

## Demonstrated Product Requirements

| REQ‑ID | Requirement Description | Why the Prototype Demonstrates It |
|--------|--------------------------|-----------------------------------|
| **001** | The system must apply configurations correctly | The prototype shows consistent, repeatable behaviour when configurations are applied or room states are viewed. |
| **002** | Lighting must work the same way in all rooms | Applying one configuration to many simulated rooms demonstrates consistent behaviour across rooms. |
| **003** | The system must show staff the lighting status of all rooms | The prototype prints the current lighting state of every room in a single command. |
| **004** | The system must let staff control lighting across the property | The prototype allows updating lighting settings for any or all rooms from one central place. |
| **008** | The system should support scalability | The prototype can simulate dozens or hundreds of rooms, proving the concept works at scale. |
| **010** | The system should be easy to ~~install and~~ set up | The prototype runs from a single script, demonstrating simple setup and easy initialization. |
