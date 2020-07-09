from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
    'verbose' : True,
}
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
    'verbose' : True,
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
    'verbose' : True,
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.74',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
    'verbose' : True,
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.75',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
    'verbose' : True,
}

with open('iosv_l2_config1') as file:
    lines = file.read().splitlines()
print(lines)

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_config_set(lines)
