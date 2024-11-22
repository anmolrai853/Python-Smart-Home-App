from main import *
from tkinter import *
from tkinter import simpledialog
#UP2246915
def setup_home():
    # Creating an instance of SmartHome
    smart_home = SmartHome()

    print("Welcome to Smart Home Setup!")

    # Loop to allow the user to add five devices
    for i in range(5):
        print(f"\nAdding device {i + 1}:")

        # Prompting the user for the device type
        device_type = input("(Not case sensitive)Enter device type (SmartPlug(1)/SmartDoorbell(2)): ").strip().lower()

        # Validating the input device type
        while device_type not in ['1', '2']:
            print("Invalid device type. Please enter either 'SmartPlug' or 'SmartDoorbell'.")
            device_type = input("Enter device type (SmartPlug(1)/SmartDoorbell(2): ").strip().lower()

        # Prompting the user for the consumption rate for SmartPlug devices
        if device_type == '1':
            consumption_rate = int(input("Enter consumption rate for SmartPlug (0-150): "))
            while not 0 <= consumption_rate <= 150:
                print("Invalid consumption rate. Please enter a value between 0 and 150.")
                consumption_rate = int(input("Enter consumption rate for SmartPlug (0-150): "))
            device = SmartPlug(consumption_rate)
        else:
            ring_mode_input = input("Enter ring mode (True or False): ").strip().lower()

            # Validate the input
            while ring_mode_input not in ['true', 'false']:
                print("Invalid ring mode. Please enter either 'True' or 'False'.")
                ring_mode_input = input("Enter ring mode (True or False): ").strip().lower()

            ring_mode = ring_mode_input == 'true'
            device = SmartDoorbell(ring_mode)

        # Adding the device to the SmartHome
        smart_home.add_device(device)

    return smart_home


class SmartHomeSystem:
    def __init__(self, home):
        self.window = Tk()
        self.window.geometry("630x430")
        self.window.title("Smart Home")
        self.window.configure(bg="grey")
        self.main_frame = Frame(self.window)
        self.main_frame.grid(row=0,
                            column=0,
                            padx=5,
                            pady=5
                            )

        self.home = home

    def run(self):
        self.create_widget()
        self.window.mainloop()

    def create_widget(self):
        # presents the devices in the tk window
        row_inc = 0
        self.device_buttons = []

        for device in self.home.get_devices():
            device_info = device
            row_inc += 1
            label_device = Label(self.main_frame, text=device_info)
            label_device.grid(
                row=row_inc,
                column=0,
                padx=10,
                pady=10
            )

            button_toggle = Button(self.main_frame, text="Toggle", height=2, width=10, command=lambda d=device: self.toggle_device(d))
            button_toggle.grid(
                row=row_inc,
                column=1,
                padx=5,
                pady=10
            )

            button_edit = Button(self.main_frame, text="Edit", height=2, width=10, command=lambda d=device: self.edit_device(d))
            button_edit.grid(
                row=row_inc,
                column=2,
                padx=5,
                pady=10
            )

            button_delete = Button(self.main_frame, text="Delete", height=2, width=10, command=lambda d=device: self.delete_device(d))
            button_delete.grid(
                row=row_inc,
                column=3,
                padx=10,
                pady=10
            )

            self.device_buttons.append((button_toggle, button_edit, button_delete))

        # button
        button_turn_on_all = Button(self.main_frame, text="Turn All On", height=2, width=20, command=self.turn_on_all, bg="grey", bd=2)
        button_turn_on_all.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        button_add = Button(self.main_frame, text="Add", height=2, width=20, command=self.add_device, bg="grey", bd=2)
        button_add.grid(
            row=6,
            column=0,
            padx=5,
            pady=5
        )

        button_turn_off_all = Button(self.main_frame, text="Turn All Off", height=2, width=20, command=self.turn_off_all, bg="grey", bd=2)
        button_turn_off_all.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
        )

    def turn_on_all(self):
        self.home.turn_on_all()
        self.update_gui()

    def turn_off_all(self):
        self.home.turn_off_all()
        self.update_gui()

    def toggle_device(self, device):
        device.toggle_switch()
        self.update_gui()

    def edit_device(self, device):
        # Open a new window to edit device attributes
        # Here you can implement the code to open a new window for editing device attributes
        pass

    def delete_device(self, device):
        self.home.remove_device(device)
        self.update_gui()

    def add_device(self):
        device_type = simpledialog.askstring("Add Device", "Enter device type (SmartPlug/Custom):")
        if device_type.lower() == 'smartplug':
            consumption_rate = simpledialog.askinteger("Add Device", "Enter consumption rate for SmartPlug (0-150):")
            device = SmartPlug(consumption_rate)
        else:
            # Here you can implement the code to add a custom smart device
            device = None
        if device:
            self.home.add_device(device)
            self.update_gui()

    def update_gui(self):
        for i, device in enumerate(self.home.get_devices()):
            self.device_buttons[i][0].config(text="On" if device.get_switch() == "on" else "Off")
            # Update other labels/buttons if necessary


def main():
    home = setup_home()
    smart_home_system = SmartHomeSystem(home)
    smart_home_system.run()


main()
