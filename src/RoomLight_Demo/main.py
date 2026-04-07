# Main
from system.hotel_system import HotelLightingSystem, MOODS
from ui.console_ui import parse_room_selection

def main():
    system = HotelLightingSystem()

    while True:
        print("\n--- Hotel Lighting Demo ---")
        print("1. Create a lighting profile")
        print("2. Apply profile to rooms")
        print("3. Show all room statuses")
        print("4. Guest override (mood)")
        print("5. Clear override (checkout)")
        print("6. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
                    name = input("Profile name: ")
                    brightness = int(input("Brightness (0-100): "))
                    temp = int(input("Color temperature (2000-6500): "))
                    scene = input("Scene name: ")
                    system.create_profile(name, brightness, temp, scene)

        elif choice == "2":
            profile = input("Profile name: ")
            rooms = input("Room numbers (e.g., 1-10, 15, 20-30 or 'all'): ")
            room_list = parse_room_selection(rooms, len(system.rooms))
            system.apply_profile(profile, room_list)

        elif choice == "3":
            system.show_all_rooms()

        elif choice == "4":
            room = int(input("Guest room number: "))
            if room < 1 or room > len(system.rooms):
                print("Invalid room.")
                continue

            print("Available moods:", ", ".join(MOODS.keys()))
            mood = input("Select mood: ").strip()

            if mood in MOODS:
                system.set_override(room, MOODS[mood])
            else:
                print("Invalid mood.")

        elif choice == "5":
            room = int(input("Room number: "))
            system.clear_override(room)

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()