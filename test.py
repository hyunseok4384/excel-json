
list = []
vk_lists={'use': 'vmotion', 'subnet': '255.255.255.0', 'ip': '10.33.2.103', 'vlan': '[15]', 'pgname': 'VLAN15-AutoVmotion-01'}
list.append(vk_lists)
vk_lists={'use': 'monitor', 'subnet': '255.255.255.0', 'ip': '192.168.124.103', 'vlan': '[129]', 'pgname': 'VLAN129-AutoMonitor-01'}
list.append(vk_lists)
print(list)
list = []
print("list : ", list)
