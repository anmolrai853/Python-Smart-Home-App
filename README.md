# Python-Smart-Home-App
The Smart Home Controller is a Python-based application designed to manage various smart home devices such as smart plugs and doorbells. This app allows you to turn on or turn off devices, manage their settings, and monitor their current states.

Key Features:
Smart Plug Control: Easily toggle your smart plug on/off and set its consumption rate.
Smart Doorbell Control: Toggle the doorbell's state and manage its "ring mode."
Centralized Smart Home Management: Add, remove, and control all devices in a centralized smart home system.
Classes & Functionality:
SmartPlug
The SmartPlug class simulates a smart plug with the ability to toggle its power state and adjust its consumption rate. You can:

Toggle the power state (on/off).
Set a consumption rate between 0 and 150 Watts.
Get the current consumption rate and power status.
python
Copy code
plug = SmartPlug(45)
plug.toggle_switch()  # Turns the plug on or off
plug.set_cons_rate(150)  # Set consumption rate to 150
plug.get_cons_rate()  # Returns the consumption rate
print(plug)  # Outputs: Smart Plug| status: on, consumption rate: 150
SmartDoorbell
The SmartDoorbell class represents a smart doorbell with a toggleable power state and customizable "ring mode." Features include:

Toggle the power state (on/off).
Set and get the ring mode (active or inactive).
python
Copy code
doorbell = SmartDoorbell()
doorbell.toggle_switch()  # Turns the doorbell on or off
doorbell.set_mode(True)  # Activates the ring mode
print(doorbell)  # Outputs: SmartDoorBell| status: on, Ring mode: on
SmartHome
The SmartHome class manages a collection of devices, allowing you to control and monitor them as a whole:

Add, remove, and list devices in your home.
Toggle device states individually or turn all devices on or off at once.
python
Copy code
home = SmartHome()
plug1 = SmartPlug(45)
plug2 = SmartPlug(50)
doorbell = SmartDoorbell()

home.add_device(plug1)
home.add_device(plug2)
home.add_device(doorbell)

home.toggle_switch(0)  # Toggle plug1 on or off
home.turn_on_all()  # Turns all devices on
print(home)  # Displays the current status of all devices in the home
Installation
Prerequisites:
Python 3.x
Required Python libraries (as specified in requirements.txt)
Steps to Install:
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/smart-home-controller.git
Navigate to the project directory:

bash
Copy code
cd smart-home-controller
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your devices by configuring the app and integrating them via the SmartPlug and SmartDoorbell classes.

Example Usage:
python
Copy code
# Initialize a smart home system
smarthome = SmartHome()

# Create devices
plug1 = SmartPlug(45)
plug2 = SmartPlug(25)
doorbell = SmartDoorbell()

# Add devices to the home
smarthome.add_device(plug1)
smarthome.add_device(plug2)
smarthome.add_device(doorbell)

# Toggle device states
smarthome.toggle_switch(1)  # Toggle the second smart plug

# Turn on all devices
smarthome.turn_on_all()

# Remove a device
smarthome.remove_device_at(0)

# Print the current state of the smart home
print(smarthome)
