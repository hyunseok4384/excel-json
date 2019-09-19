#pip install simplejson
#pip install openpyxl
#pip install xlrd
#pip install xlwt
#pip install pandas

Format = {
    "__version": "2.3.1",
    "__comments": "Sample template to deploy a vCenter Server Appliance with an embedded Platform Services Controller on an ESXi host.",
    "new.vcsa": {
        "esxi": {
            "hostname": "<FQDN or IP address of the ESXi host on which to deploy the new appliance>",
            "username": "root",
            "password": "<Password of the ESXi host root user. If left blank, or omitted, you will be prompted to enter it at the command console during template verification.>",
            "deployment.network": "VM Network",
            "datastore": "<A specific ESXi host datastore, or a specific datastore in a datastore cluster.>"
        },
        "appliance": {
            "thin.disk.mode": True,
            "deployment.option": "small",
            "name": "Embedded-vCenter-Server-Appliance"
        },
        "network": {
            "ip.family": "ipv4",
            "mode": "static",
            "ip": "<Static IP address. Remove this if using dhcp.>",
            "dns.servers": [
                "<DNS Server IP Address. Remove this if using dhcp.>"
            ],
            "prefix": "<Network prefix length. Use only when the mode is 'static'. Remove if the mode is 'dhcp'. This is the number of bits set in the subnet mask; for instance, if the subnet mask is 255.255.255.0, there are 24 bits in the binary version of the subnet mask, so the prefix length is 24. If used, the values must be in the inclusive range of 0 to 32 for IPv4 and 0 to 128 for IPv6.>",
            "gateway": "<Gateway IP address. Remove this if using dhcp.>",
            "system.name": "<FQDN or IP address for the appliance. Remove this if using dhcp.>"
        },
        "os": {
            "password": "<Appliance root password; refer to --template-help for password policy. If left blank, or omitted, you will be prompted to enter it at the command console during template verification.>",
            "ssh.enable": True
        },
        "sso": {
            "password": "<vCenter Single Sign-On administrator password; refer to --template-help for password policy. If left blank, or omitted, you will be prompted to enter it at the command console during template verification.>",
            "domain-name": "vsphere.local",
            "site-name": "<vCenter Single Sign-On site name>"
        }
    },
    "ceip": {
        "description": {
            "__comments": [
                "++++VMware Customer Experience Improvement Program (CEIP)++++",
                "VMware's Customer Experience Improvement Program (CEIP) ",
                "provides VMware with information that enables VMware to ",
                "improve its products and services, to fix problems, ",
                "and to advise you on how best to deploy and use our ",
                "products. As part of CEIP, VMware collects technical ",
                "information about your organization's use of VMware ",
                "products and services on a regular basis in association ",
                "with your organization's VMware license key(s). This ",
                "information does not personally identify any individual. ",
                "",
                "Additional information regarding the data collected ",
                "through CEIP and the purposes for which it is used by ",
                "VMware is set forth in the Trust & Assurance Center at ",
                "http://www.vmware.com/trustvmware/ceip.html . If you ",
                "prefer not to participate in VMware's CEIP for this ",
                "product, you should disable CEIP by setting ",
                "'ceip.enabled': false. You may join or leave VMware's ",
                "CEIP for this product at any time. Please confirm your ",
                "acknowledgement by passing in the parameter ",
                "--acknowledge-ceip in the command line.",
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            ]
        },
        "settings": {
            "ceip.enabled": False
        }
    }
}

import simplejson as js
import pandas as pd

df = pd.read_excel(r"C:\parameter\vCenter_Auto_parameter.xlsx",headers=0,index_col=0,sheet_name=["ESXi_Info","vCenter_Info"])
ESXi_df = df["ESXi_Info"]
vCenter_df = df["vCenter_Info"]

#deployment.network
Format["new.vcsa"]["esxi"]["hostname"]="".join(ESXi_df.loc["Target_ESXi"].values)
Format["new.vcsa"]["esxi"]["username"]="".join(ESXi_df.loc["ESXi_User"].values)
Format["new.vcsa"]["esxi"]["password"]="".join(ESXi_df.loc["ESXi_Passeord"].values)
Format["new.vcsa"]["esxi"]["datastore"]="".join(ESXi_df.loc["DataStore"].values)
Format["new.vcsa"]["esxi"]["deployment.network"]="".join(ESXi_df.loc["Deploy_Netowork"].values)
#print(Format)#OK

Format["new.vcsa"]["appliance"]["deployment.option"]="".join(vCenter_df.loc["Deploy_Option"].values)
Format["new.vcsa"]["appliance"]["thin.disk.mode"]=True
Format["new.vcsa"]["appliance"]["name"]="".join(vCenter_df.loc["VM_Name"].values)
#print(Format)#OK

Format["new.vcsa"]["network"]["system.name"]="".join(vCenter_df.loc["System_Name"].values)
Format["new.vcsa"]["network"]["ip"]="".join(vCenter_df.loc["IP_Address"].values)
Format["new.vcsa"]["network"]["dns.servers"]="".join(vCenter_df.loc["DNS_Server"].values)
Format["new.vcsa"]["network"]["prefix"]="".join(str(vCenter_df.loc["Prefix"].values[-1]))
Format["new.vcsa"]["network"]["gateway"]="".join(vCenter_df.loc["Gateway"].values)
#print(Format)#OK

Format["new.vcsa"]["os"]["password"]="".join(vCenter_df.loc["OS_Password"].values)
Format["new.vcsa"]["os"]["ssh.enable"]=True
Format["new.vcsa"]["sso"]["password"]="".join(vCenter_df.loc["SSO_Password"].values)
Format["new.vcsa"]["sso"]["domain-name"]="".join(vCenter_df.loc["SSO_Domain-name"].values)
Format["new.vcsa"]["sso"]["site-name"]="".join(vCenter_df.loc["SSO_Site-name"].values)
print(Format)

with open(r"C:\vcenter6.5_parameter.json","w") as f:
    js.dump(Format,f)
