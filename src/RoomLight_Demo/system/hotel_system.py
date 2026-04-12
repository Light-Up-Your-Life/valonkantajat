# System logic
import json
import os
import time
from models.models import Room, LightingProfile, LightingParameters, GuestOverride

STATE_FILE = "hotel_state.json"

MOODS = {
    "Relax":  LightingParameters(40,  2700, "Relax"),
    "Focus":  LightingParameters(80,  5000, "Focus"),
    "Night":  LightingParameters(10,  2200, "Night"),
    "Bright": LightingParameters(100, 6500, "Bright"),
}


class HotelLightingSystem:
    def __init__(self, room_count=100):
        self.rooms = [Room(i + 1) for i in range(room_count)]
        self.profiles = {}
        self.load_state()

    # --- Profile management ---

    def create_profile(self, name):
        profile = LightingProfile(name)
        self.profiles[name] = profile
        print(f"Profile '{name}' created.")
        return profile

    def add_scene_to_profile(self, profile_name, scene_name, brightness, color_temp):
        if profile_name not in self.profiles:
            print("Profile not found.")
            return
        self.profiles[profile_name].add_scene(scene_name, brightness, color_temp)
        print(f"Scene '{scene_name}' added to profile '{profile_name}'.")

    def delete_profile(self, name):
        if name not in self.profiles:
            return False
        del self.profiles[name]
        self.save_state()
        return True

    # --- Room operations ---

    def apply_profile(self, profile_name, scene_name, room_numbers):
        if profile_name not in self.profiles:
            print("Profile not found.")
            return
        profile = self.profiles[profile_name]
        if scene_name not in profile.scenes:
            print(f"Scene '{scene_name}' not found in profile '{profile_name}'.")
            return

        params = profile.scenes[scene_name]
        print("Applying profile to rooms...")
        time.sleep(1)
        for num in room_numbers:
            room = self.rooms[num - 1]
            room.profile_name = profile_name
            room.active_params = params
            room.status.last_sync_ok = True

        self.save_state()
        print("Sync complete.")

    def set_override(self, room_number, params):
        room = self.rooms[room_number - 1]
        room.override = GuestOverride(params)
        self.save_state()
        print(f"Guest override applied to room {room_number}.")

    def checkout_room(self, room_number):
        room = self.rooms[room_number - 1]
        room.override = None
        room.profile_name = None
        room.active_params = None
        self.save_state()
        print(f"Room {room_number} checked out and reset.")

    def get_rooms(self, room_filter=None):
        if room_filter is None:
            return self.rooms
        return [self.rooms[n - 1] for n in room_filter if 1 <= n <= len(self.rooms)]

    # --- Persistence ---

    def save_state(self):
        state = {
            "profiles": {name: p.to_dict() for name, p in self.profiles.items()},
            "rooms": {}
        }
        for room in self.rooms:
            if room.profile_name or room.override:
                state["rooms"][str(room.number)] = {
                    "profile_name": room.profile_name,
                    "active_params": room.active_params.to_dict() if room.active_params else None,
                    "override": room.override.to_dict() if room.override else None,
                }
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)

    def load_state(self):
        if not os.path.exists(STATE_FILE):
            return
        try:
            with open(STATE_FILE) as f:
                state = json.load(f)
            for name, profile_dict in state.get("profiles", {}).items():
                self.profiles[name] = LightingProfile.from_dict(profile_dict)
            for room_num_str, room_data in state.get("rooms", {}).items():
                room = self.rooms[int(room_num_str) - 1]
                room.profile_name = room_data.get("profile_name")
                if room_data.get("active_params"):
                    room.active_params = LightingParameters.from_dict(room_data["active_params"])
                if room_data.get("override"):
                    room.override = GuestOverride.from_dict(room_data["override"])
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Warning: Could not load saved state: {e}")
