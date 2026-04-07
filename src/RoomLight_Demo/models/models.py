# Data models

class LightingParameters:
    def __init__(self, brightness, color_temp, scene):
        self.brightness = brightness
        self.color_temp = color_temp
        self.scene = scene

class LightingProfile:
    def __init__(self, name, params):
        self.name = name
        self.params = params

class GuestOverride:
    def __init__(self, params):
        self.params = params

class RoomStatus:
    def __init__(self):
        self.online = True
        self.last_sync_ok = True

class Room:
    def __init__(self, number):
        self.number = number
        self.profile = None
        self.override = None
        self.status = RoomStatus()

    def current_state(self):
        if self.override:
            return("OVERRIDE", self.override.params)
        if self.profile:
            return("PROFILE", self.profile.params)
        return ("NONE", None)