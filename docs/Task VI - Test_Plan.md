# Task 6 - Test Plan

## Purpose and Scope

### Purpose

The purpose of this test plant is to define how the RoomLight demo prototype would be tested to validate its core promise

> "Configure lighting once and sync it reliably across rooms, while allowing guest-level overrides that remain local and reset correctly."

The test plan focuses on logic correctness, state consistency, and end-to-end behavior, not performance or real hardware integration.

### Scope

The following prototype features are covered:

1. Create lighting profiles and scenes
2. Apply profiles to one or more rooms
3. View room status (profile, parameters, override state)
4. Guest override of room lighting
5. Reset behavior on checkout
6. Persistence of state across restarts (JSON)

### Out of scope

- Real IoT devices or hardware
- Network failures or real concurrency
- UI usability testing beyond basic console flows
- Security, authentication, and authorization

## System under test

| Component           | Description                          |
| ------------------- | ------------------------------------ |
| HotelLightingSystem | Core system logic                    |
| LightingProfile     | Named profiles with scenes           |
| LightingParameters  | Brightness, color temperature, scene |
| Room                | Represents a hotel room              |
| RoomStatus          | Online and sync status               |
| GuestOverride       | Temporay guest changes               |
| Console UI          | Manual interaction layer             |
| JSON persistence    | `hotel_state.json`                   |

## Test strategy

| Test level                    | Purpose                                         |
| ----------------------------- | ----------------------------------------------- |
| Unit testing                  | Validate individual methods and models          |
| Integration testing           | Validate interactions between system components |
| Scenario / End-to-end testing | Validate core demo flows                        |
| Negative testing              | Validate behavior with invalid input            |

Note: Test are planned, not implemented. If implemented `pytest` would be the preferred framework.

## Test environment

- Language: Python 3.x
- Execution: local console
- Persistence: JSON file (`hotel_state.json`)
- Data: in-memory objects + mock persistence
- No external dependencies

## Test items and coverage

### Lighting profile management

#### TCP01: Create lighting profile

- Requirement: System can create reusable profiles
- Method: `create_profile(name)`
- Precondition: System initialized
- Steps:
  - Create profile "Summer"
- Expected result:
  - Profile exists in `system.profiles`
  - No scenes initially

#### TCP02: Add scene to profile

- Method: `delete_profile(name)`
- Expected result:
  - Profile removed
  - State saved correctly

### Apply profile to rooms

#### TCA01: Apply profile to multiple rooms

- Requirement: Configure once, sync everywhere
- Method: `apply_profile(profile, scene, rooms)`
- Steps:
  - Apply profile "Summer" / "Relax" to rooms 1-10
- Expected result:
  - All selected rooms have:
    - `profile_name` = "Summer"
    - `active_params` set correctly
    - `last_sync_ok` = True

#### TCA02: Apply profile to all rooms

- Input: "`all`"
- Expected result:
  - Every room receives identical parameters

#### TCA03: Invalid profile or scene

- Expected result:
  - No crash
  - Clear error message
  - No state corruption

### Room status visibility

#### TCS01: View room state (profile applied)

- Method: `Room.current_state()`
- Expected result:
  - State = "`PROFILE`"
  - Parameters shown correctly

#### TCS02: View room with no configuration

- Expected result:
  - State = "`NONE`"

### Guest override (local only)

#### TCG01: Apply guest override

- Method: `set_override(room, params)`
- Steps:
  - Apply "Night" mood to room 5
- Expected result:
  - Room 5 state = "`OVERRIDE`"
  - Other rooms unchanged
  - Profile remains intact

#### TCG02: Override does not modify profile

- Expected result:
  - Profile parameters unchanged
  - Only room override active

### Checkout and reset

#### TCC01: Checkout clears override

- Method: `checkout_room(room)`
- Expected result:
  - Override cleared
  - Active profile cleared
  - Room state resets to "`NONE`"

### Persistence

#### TCPS01: Save and reload state

- Steps:
  - Apply profiles and overrides
  - Restart system
- Expected result:
  - Profiles restored
  - Room states restored
  - Overrides restored correctly

#### TCPS02: Corrupted JSON file

- Expected result:
  - Warning printed
  - System starts with clean state
  - No crash

## Negative and edge case testing

| Case                     | Expected behavior             |
| ------------------------ | ----------------------------- |
| Invalid room number      | Graceful failure              |
| Empty profile            | Cannot apply                  |
| Override without profile | Allowed                       |
| Duplicate profile name   | Overwrites or rejects cleanly |
| Large room selection     | Still consistent              |

## Risk-based testing focus

### High-risk areas:

- Applying profile to many rooms
- Override leaking to other rooms
- Incorrect reset on checkout
- State inconsistency after reload

These areas should have the highest test priority.

## Exit criteria

The RoomLight demo is considered test-ready when:

- All core flows execute without errors
- Core promise (create -> apply -> view -> override -> reset) works
- No crashes in invalid input
- State persistence behaves predictably

## Limitations of test plan

- Tests are not automated
- Timing (`sleep`) not validated
- No concurrency testing
- Console UI not usability-tested

These limitations are acceptable for a demo-level prototype
