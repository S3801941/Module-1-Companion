"""
🚀 File Operations Practice - Your Network Automation Workshop!

Ready to learn file handling for network automation? Let's start simple and build up!

TODO: Complete each section to build a device backup system step by step.
Hint: Run the program after each TODO to see your progress!
"""

def create_device_list():
    """
    Step 1: Create a simple device inventory file
    TODO: Write device information to a text file
    """
    print("=== Creating Device Inventory ===")
    
    # TODO: Create a simple device list (hint: use a multi-line string)
    device_data = """Router-01,192.168.1.1,gig0/0-4
Switch-01,192.168.1.10,FastEthernet0/1-24  
Firewall-01,192.168.1.100,eth0-1"""
    
    filename = "devices.txt"
    
    # TODO: Write the device data to a file
    # Hint: Use 'w' mode and don't forget encoding='utf-8'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(device_data)
    
    print(f"✓ Created {filename} with device list!")


def read_device_list():
    """
    Step 2: Read the device inventory back
    TODO: Open and read the file we just created
    """
    print("\n=== Reading Device Inventory ===")
    
    filename = "devices.txt"
    
    # TODO: Read and display the file contents
    # Hint: Use 'r' mode and the 'with' statement for safe file handling
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print("Device List:\n" + content)

    print("Device list loaded successfully!")


def backup_device_config():
    """
    Step 3: Create a configuration backup
    TODO: Create a backup file with current timestamp
    """
    print("\n=== Creating Config Backup ===")
    
    # Sample router configuration
    config = """!
hostname Router-01
!
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!
interface GigabitEthernet0/1
 ip address 192.168.2.20 255.255.255.254
 no shutdown
!
interface GigabitEthernet0/2
 ip address 10.10.10.1 255.255.255.0
 no shutdown
 isis
 isis spbm 1
 isis spbm 1 circuit-type level-1
 isis enable
!
interface GigabitEthernet0/3
 ip address 10.20.20.50
 vlan 20
 no shutdown
!
interface GigabitEthernet0/4
 ip address 0.0.0.0 0.0.0.0
 shutdown
!
end"""
    
    # TODO: Create a backup filename with timestamp
    # Hint: Use datetime to create unique backup names
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"router_backup_{timestamp}.cfg"
    
    # TODO: Save the configuration to the backup file
    with open(backup_filename, 'w', encoding='utf-8') as f:
        f.write(config)
    print(f"✓ Backup saved as {backup_filename}")


def safe_file_operations():
    """
    Step 4: Handle file errors gracefully
    TODO: Add error handling to make your code bulletproof
    """
    print("\n=== Safe File Operations ===")
    
    # TODO: Try to read a file that might not exist
    # Hint: Use try/except to handle FileNotFoundError
    with open("maybe_exists.txt", 'w', encoding='utf-8') as f: 
        f.write("If you are reading this, then this file exists." \
        "\nIf you delete this file, the error handling will be triggered." \
        "\nTry deleting this file and running the program again to see the error handling in action!" \
        "\n\nGood luck!")

    test_filename = "maybe_exists.txt"
    
    # Your error handling code goes here!
    try:
        with open(test_filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print("File contents:\n" + content)
    except FileNotFoundError:
        print(f"⚠️  File not found: {test_filename}")
        print("Error handling complete!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Error handling complete!")


def main():
    """
    Your file operations workshop - run each step!
    """
    print("🚀 Welcome to File Operations Practice!\n")
    
    # Step by step file operations
    create_device_list()
    read_device_list() 
    backup_device_config()
    safe_file_operations()
    
    print("\n🎉 Great job! You're becoming a file operations expert!")
    print("\n💡 Try this: Modify the device list and run again!")


if __name__ == "__main__":
    main()