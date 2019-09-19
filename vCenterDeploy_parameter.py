#pip install simplejson
#pip install openpyxl
#pip install xlrd
#pip install xlwt
#pip install pandas

Format = {
    "__version": "1.2.0",
    "__comments": "Sample template to deploy a vCenter Server Appliance with an embedded Platform Services Controller on an ESXi host.",
    "target.vcsa": {
        "appliance": {
            "deployment.network": "VM Network",
            "deployment.option": "small",
            "name": "Embedded-vCenter-Server-Appliance",
            "thin.disk.mode": "true"
        },
        "esxi": {
            "hostname": "<FQDN or IP address of the ESXi host on which to deploy the new appliance>",
            "username": "root",
            "password": "<Password of the ESXi host root user>",
            "datastore": "<ESXi host datastore>"
        },
        "network": {
            "hostname": "<Optional. FQDN or IP address for the appliance. Remove this if using dhcp.>",
            "ip.family": "ipv4",
            "mode": "static",
            "ip": "<Optional. Static IP address. Remove this if using dhcp.>",
            "dns.servers": [
                "<Optional. DNS Server IP Address. Remove this if using dhcp.>"
            ],
            "prefix": "<Optional. The value must be from 0 to 32. Remove this if using dhcp.>",
            "gateway": "<Optional. Gateway IP address. Remove this if using dhcp.>"
        },
        "os": {
            "password": "<Appliance root password; refer to --template-help for password policy>",
            "ssh.enable": "true"
        },
        "sso": {
            "password": "<vCenter Single Sign-On administrator password; refer to --template-help for password policy>",
            "domain-name": "vsphere.local",
            "site-name": "<vCenter Single Sign-On site name>"
        }
    }
}

import simplejson as js
import pandas as pd

df = pd.read_excel(r"C:\parameter\vCenter_Auto_parameter.xlsx",headers=0,index_col=0,sheet_name=["ESXi_Info","vCenter_Info"])
ESXi_df = df["ESXi_Info"]
vCenter_df = df["vCenter_Info"]
print(ESXi_df)
print("------------------------------------------------")
"""
                                     Value
Item
Target_ESXi      mrn-cus001a-hk1.mrn.local
ESXi_User                             root
ESXi_Passeord                Mrn_nttcom!!1
Deploy_Netowork        mrn_Management_Port
DataStore                       datastore1
"""
#print(Format["target.vcsa"]["esxi"]["password"])#<Password of the ESXi host root user>
#print("------------------------------------------------")
#print(df.index)
#print(df.columns)
#print("------------------------------------------------")
#print(df.loc["Target_ESXi"].values)
print("------------------------------------------------")
Format["target.vcsa"]["esxi"]["hostname"]="".join(ESXi_df.loc["Target_ESXi"].values)
Format["target.vcsa"]["esxi"]["username"]="".join(ESXi_df.loc["ESXi_User"].values)
Format["target.vcsa"]["esxi"]["password"]="".join(ESXi_df.loc["ESXi_Passeord"].values)
Format["target.vcsa"]["esxi"]["datastore"]="".join(ESXi_df.loc["DataStore"].values)
print(Format["target.vcsa"]["esxi"])
print("------------------------------------------------")
i_prefix = vCenter_df.loc["Prefix"].values
prefix = "".join(map(lambda x : str(x),i_prefix))
print("prefix : ", prefix)
Format["target.vcsa"]["appliance"]["deployment.network"]="".join(ESXi_df.loc["Deploy_Netowork"].values)
Format["target.vcsa"]["appliance"]["deployment.option"]="".join(vCenter_df.loc["Deploy_Option"].values)
Format["target.vcsa"]["appliance"]["thin.disk.mode"]=True
Format["target.vcsa"]["appliance"]["name"]="".join(vCenter_df.loc["VM_Name"].values)
Format["target.vcsa"]["network"]["hostname"]="".join(vCenter_df.loc["System_Name"].values)
Format["target.vcsa"]["network"]["ip"]="".join(vCenter_df.loc["IP_Address"].values)
Format["target.vcsa"]["network"]["dns.servers"]="".join(vCenter_df.loc["DNS_Server"].values)
Format["target.vcsa"]["network"]["prefix"]=prefix
Format["target.vcsa"]["network"]["gateway"]="".join(vCenter_df.loc["Gateway"].values)

Format["target.vcsa"]["os"]["password"]="".join(vCenter_df.loc["OS_Password"].values)
Format["target.vcsa"]["os"]["ssh.enable"]=True
Format["target.vcsa"]["sso"]["password"]="".join(vCenter_df.loc["SSO_Password"].values)
Format["target.vcsa"]["sso"]["domain-name"]="".join(vCenter_df.loc["SSO_Domain-name"].values)
Format["target.vcsa"]["sso"]["site-name"]="".join(vCenter_df.loc["SSO_Site-name"].values)
print(Format)

with open(r"C:\vCenter_parameter.json","w") as f:
    js.dump(Format,f)
