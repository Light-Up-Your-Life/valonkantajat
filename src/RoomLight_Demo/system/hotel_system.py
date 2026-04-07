# System logic
import time
from models.models import Room, LightingProfile, LightingParameters, GuestOverride

class HotelLightingSystem:
    def __init__(self, room_count = 100):
        self.rooms = [Room(i + 1) for i in range(room_count)]
        self.profiles = {}

        # Add built-in mood profiles for staff
        for mood_name, params in MOODS.items():
            self.profiles[mood_name] = LightingProfile(mood_name, params)
    
    def create_profile(self, name, brightness, color_temp, scene):
        params = LightingParameters(brightness, color_temp, scene)
        profile = LightingProfile(name, params)
        self.profiles[name] = profile
        print(f"Profile '{name}' created.")
    
    def apply_profile(self, profile_name, room_numbers):
        if profile_name not in self.profiles:
            print("Profile not found.")
            return
    
        profile = self.profiles[profile_name]
        print("Applying profile to rooms...")
        time.sleep(1)

        for num in room_numbers:
            room = self.rooms[num -1]
            room.profile = profile
            room.status.last_sync_ok = True
        
        print("Sync complete.")

    def set_override(self, room_number, params):
        room = self.rooms[room_number -1]
        room.override = GuestOverride(params)
        print(f"Guest override applied to room {room_number}.")
    
    def clear_override(self, room_number):
        room = self.rooms[room_number - 1]
        room.override = None
        print(f"Override cleared for room {room_number}.")

    def show_all_rooms(self):
        print("\nRoom | State     | Bright | Temp | Scene | Override?")
        print("--------------------------------------------------------")
        for r in self.rooms:
            state, params = r.current_state()
            if params:
                print(f"{r.number:4} | {state:9} | {params.brightness:6} | "
                      f"{params.color_temp:4} | {params.scene:5} | "
                      f"{'Yes' if r.override else 'No'}")
            else:
                print(f"{r.number:4} | NONE      |   -    |   -  |   -   | No")
        print()

# Moods

MOODS = {
    "Relax": LightingParameters(40, 2700, "Relax"),
    "Focus": LightingParameters(80, 5000, "Focus"),
    "Night": LightingParameters(10, 2200, "Night"),
    "Bright": LightingParameters(100, 6500, "Bright")
}
