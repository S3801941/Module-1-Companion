# my_network_tools.py
# This module contains basic network utility functions for practice.

def ping_device(ip_address):
    """Simulate pinging a network device."""
    print(f"🔍 Pinging {ip_address}...")
    print(f"✅ {ip_address} is reachable!")
    return True

def get_device_info(hostname):
    """Get basic device information."""
    print(f"📋 Getting info for {hostname}:")
    info = {
        "hostname": hostname,
        "status": "online",
        "uptime": "5 days, 2 hours", 
        "interfaces": 24
    }
    for key, value in info.items():
        print(f"   {key}: {value}")
    return info

def configure_vlan(switch_name, vlan_id, vlan_name):
    """Configure a VLAN on a switch."""
    print(f"🔧 Configuring VLAN on {switch_name}:")
    print(f"   VLAN {vlan_id}: {vlan_name}")
    print(f"✅ VLAN {vlan_id} configured successfully!")
    return True
