from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'cisco',
    'password': 'cisco',
    'secret'  : 'jazz',
    'verbose' : True,
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'admin',
    'password': 'cisco',
    'secret'  : 'jazz',
    'verbose' : True,
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'cisco',
    'password': 'cisco',
    'secret'  : 'jazz',
    'verbose' : True,
}

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]
for device in all_devices:
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    
    for n in range (100,111,2):
        print("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        #print(output) 
