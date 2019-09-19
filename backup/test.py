dic = {'lab': {'vsphere': {'vcenter': {'pw': 'Mrn_nttcom!!1', 'vmname': 'AUTO-VC-TEST1', 'user': 'administrator@vsphere.local', 'mgmt': {'ip': '10.33.1.8', 'subnet': '255.255.255.0'}}, 'topology': {'dc': {'clusters': [{'members': [{'mgmt': '10.33.1.10'}], 'name': 'Auto-Cluster01'}, {'members': [], 'name': 'Auto-Cluster02'}], 'name': 'AutoDataCenter01', 'vDS': {'PortGroup': [{'name': 'VLAN3-Common-MGMT', 'vlan': '3', 'use': 'common-mgmt'}, {'name': 'VLAN10-MGMT', 'vlan': '10', 'use': 'mgmt'}, {'name': 'VLAN15-vMotion', 'vlan': '15', 'use': 'vmotion'}, {'name': 'VLAN3-Common-VM', 'vlan': '3', 'use': 'common-vm'}, {'name': 'VLAN11-Auto01', 'vlan': '11', 'use': 'vm'}, {'name': 'VLAN12-Auto02', 'vlan': '12', 'use': 'vm'}, {'name': 'VLAN13-Auto03', 'vlan': '13', 'use': 'vm'}, {'name': 'VLAN10-MGMT-VM', 'vlan': '10', 'use': 'vmmgmt'}, {'name': 'VLAN129-Monitor', 'vlan': '129', 'use': 'monitor'}], 'name': 'Auto-vDS01'}}}, 'host': [{'hostname': 'mrn-cus001a-hk1.mrn.local', 'portgroup': {'name': 'VLAN10-Mgmt-VM-vSS', 'vlan': '10'}, 'mgmt': {'ip': '10.33.1.10', 'subnet': '255.255.255.0'}, 'addvk': [{'ip': '10.33.2.100', 'subnet': '255.255.255.0', 'pgname': 'VLAN15-AutovMotion-01', 'vlan': '15', 'use': 'vmotion'}, {'ip': '192.168.124.100', 'subnet': '255.255.255.0', 'pgname': 'VLAN129-AutoMonitor-01', 'vlan': '129', 'use': 'monitor'}], 'pw': 'Mrn_nttcom!!1', 'user': 'root'}]}}}
print(dic)
print("--------------------------------------------------------------------")
esxis = dic["lab"]["vsphere"]["host"]

for i in esxis:
    print(i["addvk"][0]["pgname"])