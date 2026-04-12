# Data models

class LightingParameters:
    def __init__(self, brightness, color_temp, scene):
        self.brightness = brightness
        self.color_temp = color_temp
        self.scene = scene

    def to_dict(self):
        return {"brightness": self.brightness, "color_temp": self.color_temp, "scene": self.scene}

    @classmethod
    def from_dict(cls, d):
        return cls(d["brightness"], d["color_temp"], d["scene"])


class LightingProfile:
    def __init__(self, name):
        self.name = name
        self.scenes = {}  # scene_name -> LightingParameters

    def add_scene(self, scene_name, brightness, color_temp):
        self.scenes[scene_name] = LightingParameters(brightness, color_temp, scene_name)

    def to_dict(self):
        return {
            "name": self.name,
            "scenes": {name: params.to_dict() for name, params in self.scenes.items()}
        }

    @classmethod
    def from_dict(cls, d):
        profile = cls(d["name"])
        for scene_name, params_dict in d["scenes"].items():
            profile.scenes[scene_name] = LightingParameters.from_dict(params_dict)
        return profile


class GuestOverride:
    def __init__(self, params):
        self.params = params

    def to_dict(self):
        return self.params.to_dict()

    @classmethod
    def from_dict(cls, d):
        return cls(LightingParameters.from_dict(d))


class RoomStatus:
    def __init__(self):
        self.online = True
        self.last_sync_ok = True


class Room:
    def __init__(self, number):
        self.number = number
        self.profile_name = None
        self.active_params = None  # LightingParameters currently applied
        self.override = None
        self.status = RoomStatus()

    def current_state(self):
        if self.override:
            return ("OVERRIDE", self.override.params)
        if self.active_params:
            return ("PROFILE", self.active_params)
        return ("NONE", None)
