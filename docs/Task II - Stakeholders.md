# Task 2 – Stakeholders

- Create a stakeholder map for RoomLight  
- Identify stakeholders, place on Power-Impact grid  
- Walk through the 4 questions per stakeholder  
- Prepare 3-5 interview questions for a RoomLight stakeholder  

## Power-Impact Matrix  



![Power-Impact Matrix](https://github.com/user-attachments/assets/a7b24e1a-a949-4dc0-9c2e-dbb036642fa6)

## Stakeholders  
| Stakeholder | Role | What matters most? | What keeps me up at night? | Key question? | What do we need from them? |
|-------------|------|----------------------------|-------------------------------|----------------------------------|-----------------------------|
| Hotel General Manager | Decision Maker | Smooth operations, guest satisfaction scores, and cost control. A lighting system that fails leads to complaints on TripAdvisor. | "If the lights stop working, that's my problem, not the vendor's." "I can't have another quarter like the last system rollout." | "Can we deploy this without pulling my maintenance team off their normal duties?" | Budget approval, access to room inventory for pilots, sign-off on the vendor contract. |
| Chief Financial Officer | Decision Maker | Return on investment. Does the system pay for itself through energy savings and reduced maintenance? | "We're locked into one vendor for every light in every room. If they get acquired or change their pricing, I have no leverage and no exit." | "What's the payback period and what's the cost per room at scale?" | Budget, approval for investment on pilot, review of subscription pricing. |
| Facility Manager | Decision Maker | Minimising unplanned maintenance calls. Every service visit for a burned bulb costs more in labor than the hardware. | "A guest calls at 23:00 because a light won't turn off. I spend 20 minutes on a software issue I don't understand and end up moving the guest to another room on a Friday night." | "Is system failure frequent, and how do we get alerted before a guest notices?" | Access to maintenance logs, feedback on diagnostic tools, pilot room access. |
| Hotel IT Manager | Decision Maker / Production | Network security, integration with the property management system, and not another system that breaks at 2am.| "Every new connected device is a new attack surface." "I've explained a network breach to our GM once. I don't want to do it again over a smart bulb with a default password." | "How does this integrate with our existing property management system?" | Network access, API documentation review, security sign-off. |
| Product Manager | Production / Decision Maker | Shipping a product that the hotel chain will want to buy, not only a pilot that gets dropped after 6 months. | "We'll spend six months building the perfect multi-property sync dashboard, then do the first real customer interview and find out the GM just wanted a single button that sets the whole hotel to night mode. We optimised the wrong thing." | "Which feature is the one thing that makes them sign the contract?" | Roadmap prioritization, stakeholder interviews, success metric definition. |
| Installation Technician | Production | A clean, fast installation with clear documentation so they can hit 10+ rooms per day without calling support. | "I'm three hours into a 40-room day and the app times out trying to reach the server every time I move to a new room." | "If a device won't pair, am I able to fix it without external support?" | Installation testing across different room types, feedback on hardware fit and tool requirements. |
| Engineering Team | Production | A clear specification that does not change in every sprint, and infrastructure that allows easy deploment. | "We have one codebase today. If we start accommodating per-property variations, every release has to be tested against every configuration. We'll spend more time on QA than on building anything new." | "How do we give properties enough flexibility to feel in control without ever giving them enough rope to break the system?" | Technical architecture decisions, API design, build & release ownership. |
| Hotel Guest | End User | Falling asleep in seconds, waking up refreshed, and not fumbling with confusing controls in an unfamiliar room. | "I just want to turn my room lights on and off." "I don't want to spend my trip learning how to use a light controller remote." | "Is there a way to just set it and forget it?" | Participation in User Experience (UX) testing. |
| Housekeeping Staff | End User | Getting in and out of rooms quickly. Every extra button they have to press is time stolen from their quota. | "If I walk into a room stuck in 'romantic dinner' mode from the last guest and can't reset it, that's ten minutes gone. Do that twice and I'm behind for the whole shift." | "Does it reset to a bright cleaning mode when a room is marked for housekeeping?" | Workflow testing, edge case reporting (e.g. lights not resetting). |

## How does this shape the product?

| Stakeholder | Concern | Requirement Direction |
|---|---|---|
| Product Manager | "We never measured the return" | Built-in usage analytics, energy savings reporting, auto-generated summary per property |
| Chief Financial Officer | "The net saving is basically zero" | Energy consumption reporting, maintenance call volume tracking |
| Hotel General Manager | "A failed system shows up on TripAdvisor" | Fault tolerance, guest-invisible failure recovery, guaranteed uptime commitment |
| Hotel General Manager | "Another painful rollout" | Phased deployment tooling, zero-downtime updates, rollback capability |
| Hotel IT Manager | "Every device is a new attack surface" | VLAN isolation, no default credentials |
| Hotel IT Manager | "Another system that breaks at 02:00" | Local-first operation, offline resilience, remote diagnostic access |
| Engineering Team | "Dozens of firmware forks" | Single configurable firmware, profile-based customisation, no per-property code branches |
| Engineering Team | "Six-week release cycle" | Over-the-air update system, staged rollout by property, automated regression testing |
| Installation Tech | "I'm on a different network than the devices and I can't get IT on the phone." | Full offline commissioning mode, local device pairing over Bluetooth, queued sync |
| Installation Tech | "I need to prove every room is working" | Per-room commissioning report, green/red status per device |
| Facility Manager | "I'm troubleshooting software at night" | Remote diagnostics, plain-language fault descriptions, front desk escalation flow |
| Facility Manager | "I won't know until a guest complains" | Predictive failure alerts, proactive maintenance notifications |
| Hotel Guest | "I can't figure out how to turn off the lights" | Discoverable in-room controls, one-tap scene presets, no learning curve |
| Hotel Guest | "A blinking LED prevents me from sleeping" | Status lights off by default in sleep scenes, zero ambient light emission at night |
| Housekeeping | "Stuck in romantic dinner mode" | Auto-reset to cleaning scene on property management system checkout trigger, hard override button in room |
| Housekeeping | "Ten minutes lost per room" | Scene reset in under 5 seconds, no manual intervention required |

## Stakeholder Interview Questions (Chain/Hotel IT Manager)

**1.** How would a new IoT device typically get approved and connected to your network?  

**2.** How is your network segmented, do guest devices and operational systems share infrastructure?  

**3.** If we gave you full API documentation and a test device two weeks before going live, would that be enough time to do a proper security review?  
