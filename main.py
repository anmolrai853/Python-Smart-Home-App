class SmartPlug:
    # Class representing a smart plug

    def __init__(self, cons_rate):
        # Constructor to initialize the SmartPlug instance
        self.switched_on = False
        self.cons_rate = cons_rate

    def toggle_switch(self):
        # Method to toggle the switch state
        self.switched_on = not self.switched_on

    def set_cons_rate(self, rate):
        # Method to set the consumption rate with input validation
        if 0 <= rate <= 150:
            self.cons_rate = rate
        else:
            print("Invalid consumption rate, has to be between 0 - 150.")

    def get_cons_rate(self):
        # Method to get the consumption rate
        return self.cons_rate

    def get_switch(self):
        # Method to get the switch state
        if not self.switched_on:
            power = "off"
        else:
            power = "on"
        return power

    def __str__(self):
        # String representation of the SmartPlug instance
        return f"Smart Plug| status: {self.get_switch()}, consumption rate: {self.get_cons_rate()}"

# Function to test SmartPlug functionality
def test_smart_plug():
    smart_plug = SmartPlug(45)
    smart_plug.toggle_switch()
    print(smart_plug.get_switch())
    print(smart_plug.get_cons_rate())
    print(smart_plug)


class SmartDoorbell:
    # Class representing a smart doorbell

    def __init__(self, ring_mode=False):
        # Constructor to initialize the SmartDoorbell instance
        self.ringMode = bool(ring_mode)
        self.switched_on = False

    def toggle_switch(self):
        # Method to toggle the switch state
        self.switched_on = not self.switched_on

    def get_switch(self):
        # Method to get the switch state
        return "on" if self.switched_on else "off"

    def get_mode(self):
        # Method to get the doorbell mode
        return "on" if self.ringMode else "off"

    def set_mode(self, modes=None):
        # Method to set the doorbell mode with input validation
        if isinstance(modes, bool):
            self.ringMode = modes
        else:
            print("not a valid mode")

    def __str__(self):
        # String representation of the SmartDoorbell instance
        return f"SmartDoorBell| status: {self.get_switch()}, Ring mode: {self.get_mode()}"

# Function to test SmartDoorbell functionality
def test_device():
    device = SmartDoorbell()
    device.toggle_switch()
    print(device.get_switch())
    device.set_mode(True)
    print(device)

#test_device()

class SmartHome:

    def __init__(self):
        # Constructor to initialize the SmartHome instance
        self.devices = []

    def get_devices(self):
        # Method to get all devices
        return self.devices

    def get_device_at(self, index):
        # Method to get device at a particular index
        return self.devices[index]

    def remove_device_at(self, index):
        # Method to remove device at a particular index
        self.devices.remove(self.devices[index])

    def add_device(self, device):
        # Method to add a device
        self.devices.append(device)

    def toggle_switch(self, index):
        # Method to toggle the switch of a device at a particular index
        self.devices[index].toggle_switch()

    def turn_on_all(self):
        # Method to turn on all devices
        for i in range(len(self.devices)):
            self.devices[i].switched_on = True

    def turn_off_all(self):
        # Method to turn off all devices
        for i in range(len(self.devices)):
            self.devices[i].switched_on = False

    def __str__(self):
        # String representation of the SmartHome instance
        output = "smart home contains: \n"
        for device in self.devices:
            output += str(device) + "\n"
        return output

# Function to test SmartHome functionality
def test_smart_home():
    smarthome = SmartHome()

    plug1 = SmartPlug(45)
    plug2 = SmartPlug(45)
    smart_doorbell = SmartDoorbell()
    plug1.toggle_switch()
    plug1.set_cons_rate(150)
    plug2.set_cons_rate(25)
    smart_doorbell.set_mode(True)
    smarthome.add_device(plug1)
    smarthome.add_device(plug2)
    smarthome.add_device(smart_doorbell)
    smarthome.toggle_switch(1)
    print(smarthome)
    smarthome.turn_on_all()
    print(smarthome)
    smarthome.remove_device_at(0)
    print(smarthome)

#test_smart_home()
