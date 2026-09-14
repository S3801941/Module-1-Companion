"""
🚀 Function Basics Practice - Your Network Automation Toolkit!

Ready to put what you learned in the README into action? 
Let's build the 4 types of functions you just learned about!

Remember from the README:
1. Basic Functions - Simple functions with parameters
2. Default Values - Smart defaults for network settings  
3. Multiple Arguments (*args) - Handle many devices at once
4. Keyword Arguments (**kwargs) - Flexible configuration

TODO: Complete each function using what you learned in the README.
Hint: If you get stuck, go back and review the examples in the README!
"""

def connect_device(hostname, username):
    """
    Step 1: Basic Function (from README section 1)
    TODO: Create a function that simulates connecting to a network device
    This is like the connect_device(hostname) example in your README!
    """
    # TODO: Print a connection message using the hostname and username
    # Example: "Connecting to Router-01 as admin..."
    
    print(f"Connecting to {hostname} as {username}")


    # TODO: Return True to indicate successful connection
    # Hint: Just like the README example, use print() and return
    
    return True


def configure_interface(device_name, interface, ip_address, subnet_mask="255.255.255.0"):
    """
    Step 2: Function with Default Values (from README section 2)
    TODO: Configure a network interface with smart defaults
    This is exactly like the configure_interface example in your README!
    """
    # TODO: Print configuration details
    # Show device name, interface, IP address, and subnet mask
    # Example: "Configuring GigE0/1 on Router-01: 192.168.1.1/255.255.255.0"
    
    print("Device, Interface, and IP Configuration:" \
          f"\nDevice: {device_name}" \
          f"\nInterface: {interface}" \
          f"\nIP Address: {ip_address}" \
          f"\nSubnet Mask: {subnet_mask}")
    
    # TODO: Notice how subnet_mask already has a default value of "255.255.255.0"
    # This means if someone doesn't provide a mask, it uses /24 automatically!
    
    print(f"✓ Interface {interface} configured on {device_name}")


def create_vlan(switch_name, vlan_id, vlan_name="Data", ports=None):
    """
    Step 3: Function with default values and optional lists
    TODO: Create a VLAN with flexible parameters
    """
    # TODO: Handle the case where no ports are provided
    # Hint: Use 'if ports is None: ports = []'
    
    if ports is None:
        ports = []



    # TODO: Print VLAN creation details
    # Include switch name, VLAN ID, VLAN name, and number of ports
    
    print(f"Configuring Vlan on switch {switch_name}:" \
        f"\nVLAN ID: {vlan_id}" \
        f"\nVLAN Name: {vlan_name}" \
        f"\nPorts: {ports}")

    print(f"✓ VLAN {vlan_id} created on {switch_name}")


def configure_multiple_devices(*device_names):
    """
    Step 4: Multiple Arguments - *args (from README section 3)
    TODO: Configure multiple devices at once
    This uses *args just like the README example with configure_multiple_devices(*devices)!
    """
    print(f"Configuring {len(device_names)} devices...")
    
    # TODO: Loop through each device name
    # Print a configuration message for each device
    
    for device in device_names:
        print(f"Configuring device: {device}")

    # Hint: The README shows 'for device in devices:' - do the same with device_names
    
    print("✓ All devices configured!")


def setup_network(**network_settings):
    """
    Step 5: Keyword Arguments - **kwargs (from README section 4)
    TODO: Set up network with flexible configuration options
    This uses **kwargs exactly like the setup_network example in your README!
    """
    print("Setting up network with these options:")
    
    # TODO: Loop through the network settings and print each one
    # Hint: The README shows 'for setting, value in settings.items():' - copy that pattern!
    
    for setting, value in network_settings.items():
        print(f"{setting}: {value}")

    print("✓ Network setup complete!")


def main():
    """
    Test your functions here!
    """
    print("🚀 Welcome to Function Basics Practice!\n")
    
    # Test your functions
    print("=== Testing Basic Function ===")
    connect_device("Router-01", "admin")
    
    print("\n=== Testing Default Parameters ===")
    configure_interface("Switch-01", "GigE0/1", "192.168.1.10")
    print()
    configure_interface("Router-02", "GigE0/0", "10.0.0.1", "255.255.0.0")
    
    print("\n=== Testing Optional Parameters ===")
    create_vlan("Switch-01", 100, "Sales", ["Fa0/1", "Fa0/2"])
    print()
    create_vlan("Switch-02", 200)  # Uses default name
    print()
    create_vlan("Switch-03", 30, "Management", ["Fa0/3", "Fa0/4", "Fa0/5"])    

    
    print("\n=== Testing Multiple Arguments ===")
    configure_multiple_devices("Router-01", "Router-02", "Switch-01")
    
    print("\n=== Testing Keyword Arguments ===")
    setup_network(domain="company.com", dns="8.8.8.8", gateway="192.168.1.1")
    
    print("\n🎉 Great job! You're building useful network functions!")
    print("\n💡 Try this: Add your own function to backup device configs!")


if __name__ == "__main__":
    main()