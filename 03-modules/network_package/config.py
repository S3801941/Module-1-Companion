def router_config():
    """
    Returns a dictionary containing router configuration details.
    """
    return {
        "hostname": "Router1",
        "interfaces": {
            "GigabitEthernet0/0": {"ip": "192.168.1.1"},
            "GigabitEthernet0/1": {"ip": "192.168.2 .1"}
        },
        "routing_protocol": "OSPF"
    }

def switch_config():
    """
    Returns a dictionary containing switch configuration details.
    """
    return {
        "hostname": "Switch1",
        "interfaces": {
            "FastEthernet0/1": {"vlan": 10},
            "FastEthernet0/2": {"vlan": 20}
        },
        "spanning_tree": True
    }