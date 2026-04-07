# Console

def parse_room_selection(text, max_room):
    text = text.strip().lower()
    if text == "all":
        return list(range(1, max_room + 1))

    rooms = []
    parts = text.split(",")
    for part in parts:
        part = part.strip()
        if "-" in part:
            start, end = part.split("-")
            start, end = int(start), int(end)
            rooms.extend(range(start, end + 1))
        else:
            rooms.append(int(part))
    return rooms