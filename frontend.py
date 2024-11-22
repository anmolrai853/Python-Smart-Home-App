
from main import SmartHome, SmartPlug, SmartDoorbell
from tkinter import Tk, Frame, Label, Button, simpledialog, messagebox


def setup_home():
    """Initializes the SmartHome system with up to 5 devices added by user input."""
    smart_home = SmartHome()
    print("Welcome to Smart Home Setup!")

    for i in range(5):
        print(f"\nAdding device {i + 1}:")
        while True:
            try:
                device_type = input("Enter device type (1 for SmartPlug, 2 for SmartDoorbell): ").strip()
                if device_type not in ['1', '2']:
                    raise ValueError("Invalid device type. Enter 1 or 2.")
                break
            except ValueError as e:
                print(e)

        if device_type == '1':
            consumption_rate = get_valid_input("Enter consumption rate for SmartPlug (0-150): ", int, 0, 150)
            device = SmartPlug(consumption_rate)
        else:
            ring_mode = get_valid_input("Enter ring mode (True/False): ", bool)
            device = SmartDoorbell(ring_mode == 'true')

        smart_home.add_device(device)
    return smart_home


def get_valid_input(prompt, expected_type, min_val=None, max_val=None):
    """Prompts user for valid input of a specific type within optional bounds."""
    while True:
        try:
            value = input(prompt).strip().lower()
            if expected_type == bool:
                if value not in ['true', 'false']:
                    raise ValueError("Invalid input. Enter 'True' or 'False'.")
                return value == 'true'
            elif expected_type == int:
                value = int(value)
                if min_val is not None and not (min_val <= value <= max_val):
                    raise ValueError(f"Value must be between {min_val} and {max_val}.")
                return value
        except ValueError as e:
            print(e)


class SmartHomeSystem:
    def __init__(self, home):
        self.home = home
        self.window = Tk()
        self.window.title("Smart Home System")
        self.window.geometry("600x400")
        self.window.configure(bg="lightgrey")
        self.main_frame = Frame(self.window, bg="lightgrey")
        self.main_frame.pack(padx=10, pady=10)

    def run(self):
        """Runs the Tkinter main loop after setting up the GUI."""
        self.update_gui()
        self.window.mainloop()

    def update_gui(self):
        """Refreshes the GUI layout to reflect the current state of the SmartHome."""
        # Clear existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Display devices
        for i, device in enumerate(self.home.get_devices()):
            Label(self.main_frame, text=str(device), bg="lightgrey", fg="black").grid(row=i, column=0, padx=5, pady=5)

            Button(self.main_frame, text="Toggle", command=lambda idx=i: self.toggle_device(idx)).grid(row=i, column=1)
            Button(self.main_frame, text="Edit", command=lambda idx=i: self.edit_device(idx)).grid(row=i, column=2)
            Button(self.main_frame, text="Delete", command=lambda idx=i: self.delete_device(idx)).grid(row=i, column=3)

        # Add control buttons
        Button(self.main_frame, text="Add Device", command=self.add_device, bg="darkblue", fg="white").grid(
            row=len(self.home.get_devices()) + 1, column=0, pady=10)
        Button(self.main_frame, text="Turn All On", command=self.turn_on_all, bg="green", fg="white").grid(
            row=len(self.home.get_devices()) + 2, column=0, pady=10)
        Button(self.main_frame, text="Turn All Off", command=self.turn_off_all, bg="red", fg="white").grid(
            row=len(self.home.get_devices()) + 2, column=1, pady=10)

    def toggle_device(self, index):
        """Toggles the switch state of the device at the given index."""
        self.home.toggle_switch(index)
        self.update_gui()

    def edit_device(self, index):
        """Edits the attributes of a device at the given index."""
        device = self.home.get_device_at(index)

        if isinstance(device, SmartPlug):
            new_rate = simpledialog.askinteger("Edit SmartPlug", "Enter new consumption rate (0-150):")
            if new_rate is not None:
                try:
                    device.set_cons_rate(new_rate)
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
        elif isinstance(device, SmartDoorbell):
            new_mode = simpledialog.askstring("Edit SmartDoorbell", "Enter new ring mode (True/False):")
            if new_mode is not None and new_mode.lower() in ['true', 'false']:
                device.set_mode(new_mode.lower() == 'true')
        self.update_gui()

    def delete_device(self, index):
        """Removes the device at the given index."""
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this device?"):
            try:
                self.home.remove_device_at(index)
            except IndexError as e:
                messagebox.showerror("Error", str(e))
            self.update_gui()

    def add_device(self):
        """Adds a new device to the SmartHome."""
        device_type = simpledialog.askstring("Add Device", "Enter device type (SmartPlug/SmartDoorbell):")
        if device_type is not None:
            device_type = device_type.strip().lower()

            if device_type == "smartplug":
                consumption_rate = simpledialog.askinteger("Add SmartPlug", "Enter consumption rate (0-150):")
                if consumption_rate is not None:
                    try:
                        self.home.add_device(SmartPlug(consumption_rate))
                    except ValueError as e:
                        messagebox.showerror("Error", str(e))
            elif device_type == "smartdoorbell":
                ring_mode = simpledialog.askstring("Add SmartDoorbell", "Enter ring mode (True/False):")
                if ring_mode is not None and ring_mode.lower() in ['true', 'false']:
                    self.home.add_device(SmartDoorbell(ring_mode.lower() == 'true'))
            else:
                messagebox.showwarning("Invalid Input", "Device type must be SmartPlug or SmartDoorbell.")
            self.update_gui()

    def turn_on_all(self):
        """Turns on all devices in the SmartHome."""
        self.home.turn_on_all()
        self.update_gui()

    def turn_off_all(self):
        """Turns off all devices in the SmartHome."""
        self.home.turn_off_all()
        self.update_gui()


def main():
    """Main entry point for the application."""
    home = setup_home()
    system = SmartHomeSystem(home)
    system.run()


if __name__ == "__main__":
    main()
