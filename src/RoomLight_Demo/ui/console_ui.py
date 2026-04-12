# Console
from system.hotel_system import HotelLightingSystem, MOODS


def parse_room_selection(text, max_room):
    text = text.strip().lower()
    if text == "all":
        return list(range(1, max_room + 1))
    rooms = []
    for part in text.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-")
            rooms.extend(range(int(start), int(end) + 1))
        else:
            rooms.append(int(part))
    return rooms


def print_profiles(profiles):
    if not profiles:
        print("No profiles created.")
        return
    print("\nProfiles:")
    for name, profile in profiles.items():
        if profile.scenes:
            print(f"  {name}:")
            for scene_name, params in profile.scenes.items():
                print(f"    - {scene_name}: brightness={params.brightness}, temp={params.color_temp}")
        else:
            print(f"  {name}: (no scenes)")
    print()


def print_rooms(rooms):
    print("\nRoom | State     | Bright | Temp | Scene | Override?")
    print("--------------------------------------------------------")
    for r in rooms:
        state, params = r.current_state()
        if params:
            print(f"{r.number:4} | {state:9} | {params.brightness:6} | "
                  f"{params.color_temp:4} | {params.scene:5} | "
                  f"{'Yes' if r.override else 'No'}")
        else:
            print(f"{r.number:4} | NONE      |   -    |   -  |   -   | No")
    print()


def manage_profiles(system):
    while True:
        print("\n--- Manage Profiles ---")
        print("1. List profiles")
        print("2. Create profile")
        print("3. Delete profile")
        print("4. Back")

        choice = input("Select an option: ").strip()

        if choice == "1":
            print_profiles(system.profiles)

        elif choice == "2":
            name = input("Profile name: ").strip()
            system.create_profile(name)
            print("Add scenes to the profile (press Enter with no name to finish).")
            while True:
                scene_name = input("  Scene name: ").strip()
                if not scene_name:
                    break
                brightness = int(input("  Brightness (0-100): "))
                temp = int(input("  Color temperature (2000-6500): "))
                system.add_scene_to_profile(name, scene_name, brightness, temp)
            system.save_state()

        elif choice == "3":
            print_profiles(system.profiles)
            if not system.profiles:
                continue
            name = input("Profile name to delete: ").strip()
            if system.delete_profile(name):
                print(f"Profile '{name}' deleted.")
            else:
                print("Profile not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def run_console():
    system = HotelLightingSystem()

    while True:
        print("\n--- Hotel Lighting Demo ---")
        print("1. Manage profiles")
        print("2. Apply profile to rooms")
        print("3. Show room statuses")
        print("4. Guest override (mood)")
        print("5. Checkout (clear room)")
        print("6. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            manage_profiles(system)

        elif choice == "2":
            print_profiles(system.profiles)
            if not system.profiles:
                continue
            profile_name = input("Profile name: ").strip()
            if profile_name not in system.profiles:
                print("Profile not found.")
                continue
            profile = system.profiles[profile_name]
            if not profile.scenes:
                print("Profile has no scenes. Add scenes first via Manage profiles.")
                continue
            print("Available scenes:", ", ".join(profile.scenes.keys()))
            scene_name = input("Scene name: ").strip()
            rooms_input = input("Room numbers (e.g., 1-10, 15, 20-30 or 'all'): ")
            room_list = parse_room_selection(rooms_input, len(system.rooms))
            system.apply_profile(profile_name, scene_name, room_list)

        elif choice == "3":
            filter_input = input("Show (all / room number / range e.g. 1-10): ").strip().lower()
            if not filter_input or filter_input == "all":
                print_rooms(system.get_rooms())
            else:
                room_list = parse_room_selection(filter_input, len(system.rooms))
                print_rooms(system.get_rooms(room_list))

        elif choice == "4":
            room = int(input("Guest room number: "))
            print("Available moods:", ", ".join(MOODS.keys()))
            mood = input("Select mood: ").strip()
            if mood in MOODS:
                system.set_override(room, MOODS[mood])
            else:
                print("Invalid mood.")

        elif choice == "5":
            room = int(input("Room number: "))
            system.checkout_room(room)

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")
