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
| Chief Financial Officer | Decision Maker | Return on investment. Does the system pay for itself through energy savings, reduced maintenance, or a higher rate for premium rooms? | "We roll out across multiple properties and eighteen months later the net saving is zero. I can't take a break even to the board." | "What's the payback period and what's the cost per room at scale?" | Budget, approval for investment on pilot, review of subscription pricing. |
| Facility / Maintenance Manager | Decision Maker | Minimising unplanned maintenance calls. Every service visit for a burned bulb costs more in labor than the hardware. | "A guest calls at 23:00 because a light won't turn off. I spend 20 minutes on a software issue I don't understand and end up moving the guest to another room on a Friday night." | "Is system failure frequent, and how do we get alerted before a guest notices?" | Access to maintenance logs, feedback on diagnostic tools, pilot room access. |
| Chain/Hotel IT Manager | Decision Maker / Production | Network security, integration with the property management system, and not another system that breaks at 2am.| "Every new connected device is a new attack surface." "I've explained a network breach to our GM once. I don't want to do it again over a smart bulb with a default password." | "How does this integrate with our existing property management system?" | Network access, API documentation review, security sign-off. |
| Product Manager | Production / Decision Maker | Shipping a product that the hotel chain will want to buy, not only a pilot that gets dropped after 6 months. | "We'll spend six months building the perfect multi-property sync dashboard, then do the first real customer interview and find out the GM just wanted a single button that sets the whole hotel to night mode. We optimised the wrong thing." | "Which feature is the one thing that makes them sign the contract?" | Roadmap prioritization, stakeholder interviews, success metric definition. |
| Chain Operations Director | Decision Maker | Consistency across the entire portfolio. A brand standard in lighting that applies wherever the hotel is. | "We're locked into one vendor for every light in every room across our properties. If they get acquired or change their pricing, I have no leverage and no exit." | "Can we push a brand-standard lighting profile to all properties from one dashboard?" | Brand standard definition, rollout mandate, chain-wide purchase agreement. |
| Installation Technician | Production | A clean, fast installation with clear documentation so they can hit 10+ rooms per day without calling support. | "I'm in the basement with no signal, three hours into a 40-room day, and the app needs connectivity to register a device." | "If a device won't pair, am I able to fix it without external support?" | Installation testing across different room types, feedback on hardware fit and tool requirements. |
| Engineering Team | Production | A clear specification that does not change in every sprint, and infrastructure that does not require heroics to deploy. | Scope creep from new hotel properties each wanting custom one-off features that fragment the codebase. |  "How do we handle per-property customisation without forking the firmware?" | Technical architecture decisions, API design, build & release ownership. |
| Hotel Guest | End User | Falling asleep in seconds, waking up refreshed, and not fumbling with confusing controls in an unfamiliar room. | "I just want to turn my room lights on and off." "I don't want to spend my trip learning how to use a light controller remote." | "Is there a way to just set it and forget it?" | Participation in User Experience (UX) testing. |
| Housekeeping Staff | End User | Getting in and out of rooms quickly. Every extra button they have to press is time stolen from their quota. | "If I walk into a room stuck in 'romantic dinner' mode from the last guest and can't reset it, that's ten minutes gone. Do that twice and I'm behind for the whole shift." | "Does it reset to a bright cleaning mode when a room is marked for housekeeping?" | Workflow testing, edge case reporting (e.g. lights not resetting). |

## Stakeholder Interview Questions (Chain/Hotel IT Manager)

1. **How would a new IoT device typically get approved and connected to your network?**  

3. **How is your network segmented, do guest devices and operational systems share infrastructure?**   

5. **If we gave you full API documentation and a test device two weeks before going live, would that be enough time to do a proper security review?**  
