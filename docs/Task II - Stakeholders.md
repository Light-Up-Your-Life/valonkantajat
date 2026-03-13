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
| Hotel General Manager | Decision Maker | Smooth operations, guest satisfaction scores, and cost control. A lighting system that fails is a complaint that shows up on TripAdvisor. | A vendor lock-in they can't escape, or a rollout that disrupts guests mid-stay and causes bad reviews. | "Can we deploy this without pulling my maintenance team off their normal duties?" | Budget approval, access to room inventory for pilots, sign-off on the vendor contract. |
| Chief Financial Officer | Decision Maker | Return on investment. Does the system pay for itself through energy savings, reduced maintenance, or a higher rate for premium rooms? | A investment commitment with no clear payback period, or a subscription cost that increases with every new property. | "What's the payback period and what's the cost per room at scale?" | Budget, approval for investment on pilot, review of subscription pricing. |
| Facility / Maintenance Manager | Decision Maker | Minimising unplanned maintenance calls. Every service visit for a burned bulb costs more in labor than the hardware. | A system that generates helpdesk tickets for every minor glitch, thus creating more work than it saves. | "Is system failure frequent, and how do we get alerted before a guest notices?" | Access to maintenance logs, feedback on diagnostic tools, pilot room access. |
| Chain/Hotel IT Manager | Decision Maker / Production | Network security, integration with the property management system, and not another system that breaks at 2am.| An IoT device that opens a new attack surface, or one that floods the hotel network with traffic. | "How does this integrate with our existing property management system?" | Network access, API documentation review, security sign-off. |
| Product Manager | Production / Decision Maker | Shipping a product that the hotel chain will want to renew, not only a pilot that gets quietly dropped after 6 months. | Building features nobody asked for, or shipping before the core "configure once, sync everywhere" flow is fully functional. | "Which feature is the one thing that makes them renew the contract?" | Roadmap prioritization, stakeholder interviews, success metric definition. |
| Chain Operations Director | Decision Maker | Consistency across the entire portfolio. A brand standard in lighting that applies wherever the hotel is. | A property that does not follow the lighting configuration, creating an inconsistent guest experience. | "Can we push a brand-standard lighting profile to all 200 properties from one dashboard?" | Brand standard definition, rollout mandate, chain-wide purchase agreement. |
| Installation Technician | Production | A clean, fast installation with clear documentation so they can hit 10+ rooms per day without calling support. | Inconsistent hardware batches that require different steps, or an app that requires internet access in a basement plant room. | "Does the setup work offline? We often install in areas with no signal." | Installation testing across different room types, feedback on hardware fit and tool requirements. |
| Engineering Team | Production | A clear specification that does not change in every sprint, and infrastructure that does not require heroics to deploy. | Scope creep from new hotel properties each wanting custom one-off features that fragment the codebase. |  "How do we handle per-property customisation without forking the firmware?" | Technical architecture decisions, API design, build & release ownership. |
| Hotel Guest | End User | Falling asleep in seconds, waking up refreshed, and not fumbling with confusing controls in an unfamiliar room. | Lights that will not turn off, a bright screen blinking at 3 am, or a room that feels like a tech demo instead of a retreat. | "Is there a way to just set it and forget it, like a bedtime mode?" | Real-world usage feedback, participation in UX testing. |
| Housekeeping Staff | End User | Getting in and out of rooms quickly. Every extra button they have to press is time stolen from their quota. | Lights that do not return to a normal "cleaning mode" and slow down their workflow. | "Does it reset to a bright cleaning mode when a room is marked for housekeeping?" | Workflow testing, edge case reporting (e.g. lights not resetting). |

## Stakeholder Interview Questions (Chain/Hotel IT Manager)

1. **How would a new IoT device typically get approved and connected to your network?**  

3. **How is your network segmented, do guest devices and operational systems share infrastructure?**   

5. **If we gave you full API documentation and a test device two weeks before going live, would that be enough time to do a proper security review?**  
