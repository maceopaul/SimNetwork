from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'cisco',
    'password': 'cisco',
    'secret'  : 'jazz',
    'verbose' : True,
}


net_connect = ConnectHandler(**iosv_l2)
#net_connect.find_prompt()
#output = net_connect.send_command('enable')
#output = net_connect.send_command('jazz')
#print(output)

output = net_connect.send_command('show ip int brief')
print(output)

#output = net_connect.send_command('conf terminal')

net_connect.enable()
config_commands = ['int loop 2', 'ip address 2.2.2.2 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range (100,111,2):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output) 
