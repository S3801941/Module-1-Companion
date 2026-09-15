"""
🎯 Module Practice - Build Your First Reusable Network Tools!

Your mission: Master Python modules by creating your own network automation toolkit.
Learn to write once, use everywhere, and organize code like a pro!

📚 STUDY THE README FIRST! It explains modules and imports with clear examples.
"""

# ====================================================================
# PART 1: CREATE YOUR FIRST MODULE (my_network_tools.py)
# ====================================================================

# TODO: Before running this script, create a new file called 'my_network_tools.py' 
# in the same directory as this file. Put these functions in it:
#
# def ping_device(ip_address):
#     """Simulate pinging a network device."""
#     print(f"🔍 Pinging {ip_address}...")
#     print(f"✅ {ip_address} is reachable!")
#     return True
#
# def get_device_info(hostname):
#     """Get basic device information."""
#     print(f"📋 Getting info for {hostname}:")
#     info = {
#         "hostname": hostname,
#         "status": "online",
#         "uptime": "5 days, 2 hours", 
#         "interfaces": 24
#     }
#     for key, value in info.items():
#         print(f"   {key}: {value}")
#     return info
#
# def configure_vlan(switch_name, vlan_id, vlan_name):
#     """Configure a VLAN on a switch."""
#     print(f"🔧 Configuring VLAN on {switch_name}:")
#     print(f"   VLAN {vlan_id}: {vlan_name}")
#     print(f"✅ VLAN {vlan_id} configured successfully!")
#     return True

print("=== 🎯 Module Practice Challenge ===\n")

# ====================================================================
# PART 2: BASIC IMPORTS - Using Your Module
# ====================================================================

print("2️⃣ Testing Basic Module Imports:")

try:
    # TODO: Uncomment this line after creating my_network_tools.py
    import my_network_tools
    
    # TODO: Use your module functions (uncomment after creating the module)
    print("\n🔸 Using import module_name style:")
    my_network_tools.ping_device("192.168.1.1")
    my_network_tools.get_device_info("CORE-SWITCH-01")
    

    
except ImportError:
    print("❌ Could not import my_network_tools module!")
    print("💡 Create the file 'my_network_tools.py' with the functions shown above.")

print()

# ====================================================================
# PART 3: SPECIFIC IMPORTS - Import Individual Functions
# ====================================================================

print("3️⃣ Testing Specific Function Imports:")

try:
    # TODO: Uncomment these lines after creating my_network_tools.py
    from my_network_tools import ping_device, configure_vlan
    
    # TODO: Use imported functions directly (uncomment after creating module)
    print("\n🔸 Using from module import function style:")
    ping_device("10.0.1.1")  # No module name needed!
    configure_vlan("ACCESS-SW1", 10, "Sales_VLAN")
    
except ImportError:
    print("❌ Could not import specific functions!")
    print("💡 Make sure my_network_tools.py exists with the required functions.")

print()

# ====================================================================
# PART 4: IMPORT WITH ALIASES - Shorter Names
# ====================================================================

print("4️⃣ Testing Import Aliases:")

try:
    # TODO: Uncomment these lines after creating my_network_tools.py
    import my_network_tools as tools  # Shorter name!
    from my_network_tools import get_device_info as get_info
    
    # TODO: Use aliased imports (uncomment after creating module)
    print("\n🔸 Using aliases for shorter names:")
    tools.ping_device("172.16.1.1")
    get_info("BORDER-ROUTER")
    
except ImportError:
    print("❌ Could not import with aliases!")
    print("💡 Create my_network_tools.py first.")

print()

# ====================================================================
# PART 5: BUILT-IN MODULE PRACTICE - Python Standard Library
# ====================================================================

print("5️⃣ Practice with Built-in Python Modules:")

# TODO: Import some useful built-in modules
import datetime
import random
import json

print("\n🔸 Using built-in Python modules:")

# Using datetime module
current_time = datetime.datetime.now()
print(f"📅 Current time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Using random module  
random_ip = f"192.168.1.{random.randint(1, 254)}"
print(f"🎲 Random IP for testing: {random_ip}")

# Using json module
device_data = {
    "hostname": "TEST-DEVICE",
    "ip": random_ip,
    "vendor": "Cisco",
    "model": "2960X"
}
json_string = json.dumps(device_data, indent=2)
print(f"📄 Device data as JSON:\n{json_string}")

print()

# ====================================================================
# PART 6: CREATE A SIMPLE PACKAGE (Advanced Challenge)
# ====================================================================

print("6️⃣ Package Creation Challenge (ADVANCED):")
print()
print("🎯 BONUS CHALLENGE - Create Your First Package!")
print("Once you master basic modules, try this advanced challenge:")
print()
print("1. Create a new folder called 'network_package'")
print("2. Inside that folder, create these files:")
print("   📁 network_package/")
print("   ├── 📄 __init__.py  (can be empty for now)")  
print("   ├── 📄 devices.py   (put device-related functions here)")
print("   └── 📄 config.py    (put configuration functions here)")
print()
print("3. Try importing from your package:")
print("   from network_package import devices")
print("   from network_package.config import backup_config")
print()

# ====================================================================
# PART 7: REAL-WORLD SIMULATION
# ====================================================================

print("7️⃣ Real-World Module Usage Simulation:")

def simulate_network_automation():
    """
    Simulate how modules are used in real network automation.
    
    TODO: Modify this after creating your my_network_tools.py
    """
    print("\n🔸 Professional Network Automation Workflow:")
    
    devices = [
        {"name": "CORE-R1", "ip": "10.0.0.1"},
        {"name": "DIST-SW1", "ip": "10.0.0.2"}, 
        {"name": "ACCESS-SW1", "ip": "10.0.0.3"}
    ]
    
    print(f"📋 Processing {len(devices)} network devices...")
    
    for device in devices:
        print(f"\n🔧 Working on {device['name']}:")
        
        # TODO: Uncomment these lines after creating my_network_tools.py
        # This is how professionals use modules!
        
        # Step 1: Test connectivity
        # if my_network_tools.ping_device(device['ip']):
        #     # Step 2: Get device information  
        #     my_network_tools.get_device_info(device['name'])
        #     print(f"   ✅ {device['name']} processed successfully!")
        # else:
        #     print(f"   ❌ {device['name']} unreachable!")
        
        print(f"   ⏳ Would process {device['name']} with your module functions...")
    
    print("\n🎉 Automation complete! This is the power of reusable modules!")

simulate_network_automation()

print("\n" + "="*60)
print("🎯 COMPLETION CHECKLIST:")
print("="*60)
print("To complete this module challenge:")
print()
print("✅ 1. Create 'my_network_tools.py' with the functions shown above")
print("✅ 2. Run this script again to see imports in action")  
print("✅ 3. Experiment with different import styles")
print("✅ 4. Try the bonus package creation challenge")
print("✅ 5. Understand how modules prevent code duplication")
print()
print("💡 KEY INSIGHT: Modules let you write code once and use it everywhere!")
print("💡 This is how professional network automation is built!")
print()
print("🚀 Next steps after mastering modules:")
print("   • Learn about third-party packages (pip install)")
print("   • Explore popular network automation modules (netmiko, napalm)")
print("   • Build your own network automation library!")