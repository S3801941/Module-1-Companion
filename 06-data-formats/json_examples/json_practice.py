"""
🎯 JSON Practice - Master Network API Data!

Your mission: Learn to work with JSON, the language of modern network APIs.
Every network controller, REST API, and automation tool speaks JSON!

🔥 What makes this exciting?
- JSON is everywhere in modern networking
- APIs return JSON responses 
- Network controllers use JSON for configuration
- Automation tools love JSON data

📚 Study the main README first to understand JSON basics!

💡 Pro Tip: JSON looks like Python dictionaries and lists with quotes around everything.
"""

import json
import os

def read_device_inventory():
    """
    TODO: Learn to read JSON data from files.
    
    This simulates getting device info from a network controller API.
    Most network APIs return data in JSON format just like this!
    """
    print("🔸 Reading JSON device inventory:")
    
    try:
        # TODO: Open the devices.json file and load the JSON data
        # Hint: Use json.load() to read JSON from a file
        # Replace this comment with your code:
        with open("06-data-formats/json_examples/devices.json", "r") as file:
            data = json.load(file)
        
        # TODO: Print basic information about the network
        # Hint: Access data like a Python dictionary

            for key, value in data['network_info'].items():
                print(f"   {key}: {value}")

        # Show the site name and total device count            
        # TODO: Print site name from data['network_info']['site_name']
        # TODO: Print total devices from data['network_info']['total_devices']
        
        print(f"   Total devices: {data['network_info']['total_devices']}")
        print(f"   Site name: {data['network_info']['site_name']}")


        print("   ✅ Loaded JSON data successfully!")

    except FileNotFoundError:
        print("   ❌ devices.json file not found!")
        print("   💡 Make sure the file exists in this directory")
    except json.JSONDecodeError as e:
        print(f"   ❌ Invalid JSON format: {e}")
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")

def display_device_list():
    """
    TODO: Loop through JSON data and display each device.
    
    This teaches you how to process API responses that contain lists of devices.
    """
    print("🔸 Device inventory:")
    
    try:
        # TODO: Load the JSON data again (or better yet, modify this to accept data as parameter)
        with open("06-data-formats/json_examples/devices.json", "r") as file:
            data = json.load(file)
        
        # TODO: Loop through each device in data['devices']
        # Hint: Use a for loop to iterate through the device list
        # For each device, print: hostname, type, and location
        # Format: "🖥️  router1 - router at office"
        
        for device in data['devices']:
            print(f"🖥️   {device['hostname']} - {device['type']} at {device['location']}")
        
    except Exception as e:
        print(f"   ❌ Error displaying devices: {e}")

def find_specific_devices():
    """
    TODO: Practice filtering JSON data to find specific device types.
    
    Real-world scenario: Finding all routers in your network from an API response.
    """
    print("🔸 Finding routers:")
    
    try:
        with open("06-data-formats/json_examples/devices.json", "r") as file:
            data = json.load(file)
        
        # TODO: Create an empty list called 'routers'
        routers = []

        # TODO: Loop through all devices and find ones where type == 'router'
        # Add matching devices to the routers list
        for device in data['devices']:
            if device['type'] == 'router':
                routers.append(device)

        # TODO: Print how many routers you found
        print(f"   Found {len(routers)} routers:")  # Replace ? with actual count
        
        # TODO: Display each router's hostname and IP address
        # Format: "🔀 router1 (192.168.1.1)"
        for router in routers:
            print(f"🔀 {router['hostname']} ({router['ip']})")
        
    except Exception as e:
        print(f"   ❌ Error finding routers: {e}")
    
def add_new_device():
    """
    TODO: Learn to modify JSON data and save it back.
    
    This simulates adding a new device through a network management API.
    """
    print("🔸 Adding new device:")
    
    try:
        # TODO: Load existing data
        with open("06-data-formats/json_examples/devices.json", "r") as file:
            data = json.load(file)
        
        # TODO: Create a new device dictionary
        # Include: hostname, ip, type, location
        # Use these values: "ap1", "192.168.1.4", "access_point", "office"
        new_device = {
            "hostname": "ap1",
            "ip": "192.168.1.4",
            "type": "access_point",
            "location": "office"
        }
        
        # TODO: Add the new device to the devices list
        # Hint: Use append() method
        data['devices'].append(new_device)
        
        # TODO: Update the total device count
        # Hint: Increment data['network_info']['total_devices'] by 1
        data['network_info']['total_devices'] += 1
        
        # TODO: Save the updated data to devices_updated.json
        # Hint: Use json.dump() with indent=2 for pretty formatting
        with open("devices_updated.json", "w") as file:
            json.dump(data, file, indent=2)

        print("   ✅ Added access point and saved to devices_updated.json")
        
    except Exception as e:
        print(f"   ❌ Error adding device: {e}")

def json_tips():
    """
    Display helpful tips for working with JSON in network automation.
    """
    print("💡 JSON Pro Tips:")
    print("   • JSON is just text that looks like Python dictionaries")
    print("   • Always use double quotes, never single quotes") 
    print("   • Perfect for REST APIs and network controller responses")
    print("   • Use json.loads() for strings, json.load() for files")
    print("   • Pretty print with indent=2 for readable output")

def main():
    """
    Run all JSON practice exercises step by step.
    """
    print("=== 🎯 JSON Practice Challenge ===")
    print()
    print("Master JSON - the language of network APIs!")
    print("=" * 50)
    print()
    
    # Step 1: Learn to read JSON
    read_device_inventory()
    print()
    
    # Step 2: Display the data 
    display_device_list()
    print()
    
    # Step 3: Filter and find specific data
    find_specific_devices()
    print()
    
    # Step 4: Modify and save JSON
    add_new_device()
    print()
    
    # Bonus: Tips for success
    json_tips()
    print()
    
    print("🎉 JSON Practice Complete!")
    print("🚀 Next: Try CSV practice to learn spreadsheet data formats!")

if __name__ == "__main__":
    main()