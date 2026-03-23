# Task 3 – Prototype Scope

## Task

1. Prototype description — 3–5 sentences: what does it do, who is it for, what does it prove?
2. Demonstrate — which product requirements (REQ-IDs) the prototype proves. Why?

## Prototype description  
The RoomLight prototype demonstrates the system’s consistency, reliability, and scalability for hotel staff. It shows that lighting behaves the same in all tested (?) rooms (001), operates reliably (002), can handle multiple rooms (003), and is easy to install (004) for non-technical users. The prototype proves that the system meets key operational requirements and supports staff efficiency and room verification.  

The RoomLight prototype simulates a set of rooms and their lighting states. It lets a user create one lighting configuration and apply it to all rooms or selected rooms at once, demonstrating “configure once, sync everywhere.” The tool also allows viewing the lighting state of every room with a single command, proving that room verification can be done quickly. This proof‑of‑concept demonstrates how the final system will support hotel staff workflows.  

## Demonstrated Product Requirements

| REQ‑ID | Requirement Description | Why the Prototype Demonstrates It |
|--------|--------------------------|-----------------------------------|
| **001** | The system must apply configurations correctly | The prototype shows consistent, repeatable behaviour when configurations are applied or room states are viewed. |
| **002** | Lighting must work the same way in all rooms | Applying one configuration to many simulated rooms demonstrates consistent behaviour across rooms. |
| **003** | The system must show staff the lighting status of all rooms | The prototype prints the current lighting state of every room in a single command. |
| **004** | The system must let staff control lighting across the property | The prototype allows updating lighting settings for any or all rooms from one central place. |
| **008** | The system should support scalability | The prototype can simulate dozens or hundreds of rooms, proving the concept works at scale. |
| **010** | The system should be easy to ~~install and~~ set up | The prototype runs from a single script, demonstrating simple setup and easy initialization. |
