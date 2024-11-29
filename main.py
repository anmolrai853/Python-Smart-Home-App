# File: main.py

class SmartPlug:
    def __init__(self, cons_rate):
        self.switched_on = False
        self.cons_rate = cons_rate

    def toggle_switch(self):
        self.switched_on = not self.switched_on

    def set_cons_rate(self, rate):
        if 0 <= rate <= 150:
            self.cons_rate = rate
        else:
            raise ValueError("Invalid consumption rate, must be between 0 and 150.")

    def get_cons_rate(self):
        return self.cons_rate

    def get_switch(self):
        return "on" if self.switched_on else "off"

    def __str__(self):
        return f"Smart Plug | Status: {self.get_switch()}, Consumption Rate: {self.get_cons_rate()}"


class SmartDoorbell:
    def __init__(self, ring_mode=False):
        self.ringMode = bool(ring_mode)
        self.switched_on = False

    def toggle_switch(self):
        self.switched_on = not self.switched_on

    def get_switch(self):
        return "on" if self.switched_on else "off"

    def get_mode(self):
        return "on" if self.ringMode else "off"

    def set_mode(self, mode):
        if isinstance(mode, bool):
            self.ringMode = mode
        else:
            raise ValueError("Invalid mode, must be True or False.")

    def __str__(self):
        return f"Smart Doorbell | Status: {self.get_switch()}, Ring Mode: {self.get_mode()}"


class SmartHome:
    def __init__(self):
        self.devices = []

    def get_devices(self):
        return self.devices

    def get_device_at(self, index):
        if 0 <= index < len(self.devices):
            return self.devices[index]
        else:
            raise IndexError("Invalid index for devices.")

    def remove_device_at(self, index):
        if 0 <= index < len(self.devices):
            self.devices.pop(index)
        else:
            raise IndexError("Invalid index for devices.")

    def add_device(self, device):
        if isinstance(device, (SmartPlug, SmartDoorbell)):
            self.devices.append(device)
        else:
            raise TypeError("Invalid device type. Must be SmartPlug or SmartDoorbell.")

    def toggle_switch(self, index):
        if 0 <= index < len(self.devices):
            self.devices[index].toggle_switch()
        else:
            raise IndexError("Invalid index for devices.")

    def turn_on_all(self):
        for device in self.devices:
            device.switched_on = True

    def turn_off_all(self):
        for device in self.devices:
            device.switched_on = False

    def __str__(self):
        output = "Smart Home contains:\n"
        for device in self.devices:
            output += f" - {device}\n"
        return output
