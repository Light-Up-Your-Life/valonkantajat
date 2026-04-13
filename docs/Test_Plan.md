# Task 5 - Test Plan

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

- Real IoT devicec or hardware
- Network failures or real concurrency
- UI usability testing beyond basic console flows
- Security, authentication, and authorization

## System under test

## Test strategy

## Test environment

## Test items and coverage

### Lighting profile management

### Apply profile to rooms

### Room status visibility

### Guest override (local only)

### Checkout and reset

### Persistence

## Negative and edge case testing

## Risk-based testing focus

## Exit criteria

## Limitations of test plan
