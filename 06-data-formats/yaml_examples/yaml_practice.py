"""
🎯 YAML Practice - Master Configuration Files!

Your mission: Learn to work with YAML, the human-friendly format for network configuration 
files, automation scripts, and infrastructure as code!

🔥 What makes this exciting?
- YAML is super readable - no quotes or brackets!
- Perfect for Ansible playbooks and automation
- Used in Docker, Kubernetes, and cloud configs  
- Network engineers love YAML for its simplicity

📚 Study the main README first to understand YAML basics!

💡 Pro Tip: YAML uses indentation (spaces) to show structure - just like Python!

⚠️  Important: You need to install PyYAML first: pip install pyyaml
"""

# Check if YAML is available
try:
    import yaml
    HAS_YAML = True
except ImportError:
    print("📦 PyYAML not installed!")
    print("💡 Install with: pip install pyyaml")
    print("🔄 YAML practice will be limited without it")
    HAS_YAML = False

def check_yaml_availability():
    """
    Check if YAML library is available and guide user if not.
    """
    if not HAS_YAML:
        print("❌ YAML library not available")
        print("📦 Install PyYAML first:")
        print("   pip install pyyaml")
        print()
        print("🤔 Want to see what YAML looks like anyway?")
        print("📖 We'll show you the structure without processing it!")
        return False
    return True

def read_network_config():
    """
    TODO: Learn to read YAML configuration files.
    
    This simulates reading network automation configs - exactly what you'll do 
    with Ansible, Docker, and infrastructure as code!
    """
    print("🔸 Reading YAML network config:")
    
    if not check_yaml_availability():
        show_yaml_example()
        return None
    
    try:
        # TODO: Open network.yaml file and load the YAML data
        # Hint: Use yaml.safe_load() to read YAML safely
        with open("06-data-formats/yaml_examples/network.yaml", "r") as f:
            config = yaml.safe_load(f)
        
        # TODO: Print basic network information
        # Show the site name from config['network']['site_name']
        print("   ✅ Loaded YAML config successfully!")

        # TODO: Print the site name
        site_name = config.get('network', {}).get('site_name')
        print(f"   📍 Site: {site_name}")

        return config
        
    except FileNotFoundError:
        print("   ❌ network.yaml file not found!")
        return None
    except yaml.YAMLError as e:
        print(f"   ❌ Invalid YAML format: {e}")
        return None
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None

def display_devices(config):
    """
    TODO: Show network devices from YAML configuration.
    
    Real scenario: Reading device lists from automation configuration files.
    """
    print("🔸 Network devices:")
    
    if not config:
        print("   ❌ No configuration data available")
        return
    
    try:
        # TODO: Loop through devices in config['devices']
        # For each device, show: hostname, type, and IP
        # Format: "🖥️  router1 - router (192.168.1.1)"
        for device in config.get('devices', []):
            hostname = device.get('hostname', 'unknown')
            device_type = device.get('type', 'unknown')
            ip = device.get('ip', 'unknown')
            print(f"   🖥️  {hostname} - {device_type} ({ip})")

        
    except Exception as e:
        print(f"   ❌ Error displaying devices: {e}")

def display_vlans(config):
    """
    TODO: Show VLAN configuration from YAML.
    
    Network scenario: Reading VLAN configs from infrastructure code files.
    """
    print("🔸 VLAN configuration:")
    
    if not config:
        print("   ❌ No configuration data available")
        return
    
    try:
        # TODO: Loop through VLANs in config['vlans']
        # For each VLAN, show: ID, name, and description
        # Format: "🔗 VLAN 10: Sales - Sales Department"
        
        for vlan in config.get('vlans', []):
            vlan_id = vlan.get('id', 'unknown')
            name = vlan.get('name', 'unknown')
            description = vlan.get('description', 'unknown')
            print(f"   🔗 VLAN {vlan_id}: {name} - {description}")
        
    except Exception as e:
        print(f"   ❌ Error displaying VLANs: {e}")

def add_new_vlan(config):
    """
    TODO: Modify YAML data and save it back.
    
    Automation scenario: Adding new VLANs to your infrastructure configuration.
    """
    print("🔸 Adding new VLAN:")
    
    if not check_yaml_availability() or not config:
        print("   ❌ Cannot modify YAML without PyYAML library and config data")
        return
    
    try:
        # TODO: Create a new VLAN dictionary
        # Include: id (30), name ("Guest"), description ("Guest Network")
        new_vlan = {
            "id": 30,
            "name": "Guest",
            "description": "Guest Network"
        }
        
        # TODO: Add the new VLAN to config['vlans']
        # Hint: Use append() method
        config['vlans'].append(new_vlan)


        # TODO: Save updated config to network_updated.yaml
        # Hint: Use yaml.dump() with default_flow_style=False and indent=2
        with open("network_updated.yaml", "w") as f:
            yaml.dump(config, f, default_flow_style=False, indent=2)


        print("   ✅ Added Guest VLAN and saved to network_updated.yaml")
        
    except Exception as e:
        print(f"   ❌ Error adding VLAN: {e}")

def show_yaml_example():
    """
    Show YAML structure even without the library installed.
    """
    print("📖 Here's what YAML looks like:")
    print()
    print("network:")
    print("  site_name: Main Office")
    print("  admin: network-team@company.com")
    print()
    print("devices:")
    print("  - hostname: router1")
    print("    ip: 192.168.1.1")
    print("    type: router")
    print("  - hostname: switch1")
    print("    ip: 192.168.1.2")
    print("    type: switch")
    print()
    print("vlans:")
    print("  - id: 10")
    print("    name: Sales")
    print("    description: Sales Department")
    print("  - id: 20")
    print("    name: IT")
    print("    description: IT Department")
    print()
    print("💡 Notice:")
    print("   • No quotes needed (usually)")
    print("   • Indentation shows structure")
    print("   • Lists use dashes (-)")
    print("   • Very human-readable!")

def yaml_tips():
    """
    Display helpful tips for working with YAML in network automation.
    """
    print("💡 YAML Pro Tips:")
    print("   • Spaces matter! Use consistent indentation (usually 2 spaces)")
    print("   • Never mix tabs and spaces - use spaces only")
    print("   • Comments start with # (great for documenting configs)")
    print("   • Perfect for Ansible playbooks and Docker configs")
    print("   • Use yaml.safe_load() to avoid security issues")
    print("   • Quotes only needed for special characters or numbers as strings")

def main():
    """
    Run all YAML practice exercises step by step.
    """
    print("=== 🎯 YAML Practice Challenge ===")
    print()
    print("Master YAML - the human-friendly config format!")
    print("=" * 50)
    print()
    
    # Step 1: Learn to read YAML files
    config = read_network_config()
    print()
    
    if HAS_YAML and config:
        # Step 2: Display device information
        display_devices(config)
        print()
        
        # Step 3: Display VLAN configuration
        display_vlans(config)
        print()
        
        # Step 4: Modify and save YAML
        add_new_vlan(config)
        print()
    else:
        print("🎓 Learn more about YAML:")
        show_yaml_example()
        print()
    
    # Bonus: Tips for success
    yaml_tips()
    print()
    
    if HAS_YAML:
        print("🎉 YAML Practice Complete!")
    else:
        print("🎯 Ready for YAML Practice!")
        print("📦 Install PyYAML and run again: pip install pyyaml")
    
    print("🚀 Next: Try XML practice to learn legacy system formats!")

if __name__ == "__main__":
    main()