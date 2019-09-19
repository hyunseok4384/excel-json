#pip install simplejson
#pip install openpyxl
#pip install xlrd
#pip install xlwt
#pip install pandas

import simplejson as js
import pandas as pd
import openpyxl

Format = {"lab":{
                "vsphere":{
                            "host":[],
                            "vcenter":{
                                        "mgmt":{
                                                "ip":"xxx.xxx.xxx.xxx",
                                                "subnet":"xxx.xxx.xxx.xxx"
                                        },
                                        "user":"xxxxx",
                                        "pw":"xxxxx",
                                        "vmname":"xxxxx"
                            },
                            "topology":{
                                "dc":{
                                        "name":"xxxx",
                                        "clusters":[],
                                        "vDS":{
                                            "name":"xxxx",
                                            "PortGroup":[]
                                        }
                                }
                            }
                }
        }
}
ESXi_Format = {"mgmt":{},
                "hostname":"xxxxx",
                "user":"root",
                "pw":"xxxx",
                "addvk":[]
                }
ESXi_Mgmt_Fromat = {"ip":"xxx.xxx.xxx.xxx",
                    "subnet":"xxx.xxx.xxx.xxx"
                    }
Add_VMKernel_Foramt = {"use":"xxxx",
                        "ip":"xxx.xxx.xxx.xxx",
                        "subnet":"xxx.xxx.xxx.xxx",
                        "pgname":"xxxxx",
                        "vlan":"xxxx"
                        }
Cluster_Format = {"name":"xxxxx",
                    "members":[]
                }
PortGroup_Format = {"use":"xxx",
                    "name":"xxxx",
                    "vlan":"xxx"
                }

#df = pd.read_excel(r"C:\parameter\vCenter_Infra_parameter.xlsx",headers=0,index_col=0,sheet_name=None)
sheet_info = openpyxl.load_workbook(r"C:\parameter\vCenter_Infra_parameter.xlsx")
sheet_name = sheet_info.sheetnames
#print(sheet_name)
#['vCenter_Info', 'vDS', 'ESXi_01', 'ESXi_02', 'ESXi_03']

esxi_sheet = [x for x in sheet_name if "ESXi" in x]
#print(esxi_sheet)
#['ESXi_01', 'ESXi_02', 'ESXi_03']
Infra_Format = Format

"""VCSA Setting"""
topology_df = pd.read_excel(r"C:\parameter\vCenter_Infra_parameter.xlsx",headers=0,index_col=0,sheet_name="vCenter_Info")
#print("topology_Info : ", topology_df)
Infra_Format["lab"]["vsphere"]["vcenter"]["mgmt"]["ip"] = "".join(topology_df.loc["IP_Address"].values)
Infra_Format["lab"]["vsphere"]["vcenter"]["mgmt"]["subnet"] = "".join(topology_df.loc["Subnet"].values)
Infra_Format["lab"]["vsphere"]["vcenter"]["user"] = "".join(topology_df.loc["User"].values)
Infra_Format["lab"]["vsphere"]["vcenter"]["pw"] = "".join(topology_df.loc["Password"].values)
Infra_Format["lab"]["vsphere"]["vcenter"]["vmname"] = "".join(topology_df.loc["VM_Name"].values)
Infra_Format["lab"]["vsphere"]["topology"]["dc"]["name"] = "".join(topology_df.loc["DataCenter"].values)
Infra_Format["lab"]["vsphere"]["topology"]["dc"]["vDS"]["name"] = "".join(topology_df.loc["vDS"].values)
cluster_info = [x for x in topology_df.index if "Cluster" in x]
#print("cluster_value : ", cluster_info)
#cluster_value :  ['Cluster-01', 'Cluster-02', 'Cluster-03']

"""vDS PortGroup Setting"""
vDS_df = pd.read_excel(r"C:\parameter\vCenter_Infra_parameter.xlsx",headers=0,index_col=0,sheet_name="vDS")
#print("vDS_Info : ", vDS_df)
print("****************************************************************************")
Port_Number_Info = [p for p in vDS_df.index if "PortGroup" in p]
print("Port_Number_Info : ", Port_Number_Info)
print("****************************************************************************")
for v,Port_Number in enumerate(Port_Number_Info):
    print(v," : ",Port_Number)
    Port_list = []
    Port_list.append(PortGroup_Format.copy())
    Use_Port = "use-"+Port_Number.split("-")[-1]
    Name_Port = "name-"+Port_Number.split("-")[-1]
    Vlan_Port = "vlan-"+Port_Number.split("-")[-1]
    Port_list[-1]["use"] = "".join(vDS_df.loc[Use_Port].values)
    Port_list[-1]["name"] = "".join(vDS_df.loc[Name_Port].values)
    Port_list[-1]["vlan"] = "".join(str(vDS_df.loc[Vlan_Port].values[-1]))
    Infra_Format["lab"]["vsphere"]["topology"]["dc"]["vDS"]["PortGroup"].append(Port_list[-1].copy())

"""Cluster Member Setting"""
for c,cluster in enumerate(cluster_info):
    print("---------------------------------------------------------------------")
    print("cluster count : ", c)
    print("cluster_numbers : ", cluster)
    Cluster_list = []
    Cluster_list.append(Cluster_Format.copy())
    Cluster_list[-1]["name"] = "".join(topology_df.loc[cluster])
    Cluster_list[-1]["members"] = []
    #print("Before_Cluster_list[-1] : ", Cluster_list[-1])
    for i,esxi in enumerate(esxi_sheet):
        print("esxi count : ", i)
        df = pd.read_excel(r"C:\parameter\vCenter_Infra_parameter.xlsx",headers=0,index_col=0,sheet_name=esxi)
        #print("esxi_cluster : ", df.loc["Cluster"].values[-1])
        if Cluster_list[-1]["name"] == df.loc["Cluster"].values[-1]:
            #print("esxi_name : ", df.loc["FQDN"].values[-1])
            #print("cluster_name : ", Cluster_list[-1]["name"])
            member = {}
            member["mgmt"] = "".join(df.loc["Ip_Address"].values)
            #print("member : ", member)
            Cluster_list[-1]["members"].append(member.copy())
    #print("After_Cluster_list[-1] : ", Cluster_list[-1])
    Infra_Format["lab"]["vsphere"]["topology"]["dc"]["clusters"].append(Cluster_list[-1].copy())
    #print("Infra_View : ", Infra_Format)

"""ESXi Setting"""
for i,esxi in enumerate(esxi_sheet):
    print("-------------------------------------------------------------------------------")
    print("i : ", i)
    df = pd.read_excel(r"C:\parameter\vCenter_Infra_parameter.xlsx",headers=0,index_col=0,sheet_name=esxi)
    #print(df.index)

    number_info = [x for x in df.index if "VMKernel" in x]
    #print("number_info : ", number_info)
    #['VMKernel-01', 'VMKernel-02']
    ESXi_list = []
    Mgmt_list = []
    #print("Before ESXi_list : ", ESXi_list)
    ESXi_list.append(ESXi_Format.copy())
    Mgmt_list.append(ESXi_Mgmt_Fromat.copy())
    #print("After ESXi_list : ", ESXi_list)
    ESXi_list[-1]["hostname"]="".join(df.loc["FQDN"].values)
    ESXi_list[-1]["user"]="".join(df.loc["ESXi_User"].values)
    ESXi_list[-1]["pw"]="".join(df.loc["ESXi_Passeord"].values)
    Mgmt_list[-1]["ip"]="".join(df.loc["Ip_Address"].values)
    Mgmt_list[-1]["subnet"]="".join(df.loc["Subnet"].values)
    #print(ESXi_list[-1])
    ESXi_list[-1]["mgmt"] = Mgmt_list[-1].copy()
    ESXi_list[-1]["addvk"] = []

    if "VCSA-PortGroup" in df.index:
        print("VCSA-PortGroup is aru!!!!!!!")
        ESXi_list[-1]["portgroup"] = {}
        ESXi_list[-1]["portgroup"]["name"] = "".join(df.loc["VCSA-PortName"].values)
        ESXi_list[-1]["portgroup"]["vlan"] = "".join(str(df.loc["VCSA-Vlan"].values[-1]))

    for k,number in enumerate(number_info):
        print("k : ", k)
        vk_list = []
        vk_list.append(Add_VMKernel_Foramt.copy())
        Use_num = "Use-"+number.split("-")[-1]
        Ip_num = "Ip-"+number.split("-")[-1]
        Subnet_num = "Subnet-"+number.split("-")[-1]
        PortName_num = "PortName-"+number.split("-")[-1]
        Vlan_num = "Vlan-"+number.split("-")[-1]
        vk_list[-1]["use"]="".join(df.loc[Use_num].values)
        vk_list[-1]["ip"]="".join(df.loc[Ip_num].values)
        vk_list[-1]["subnet"]="".join(df.loc[Subnet_num].values)
        vk_list[-1]["pgname"]="".join(df.loc[PortName_num].values)
        vk_list[-1]["vlan"]="".join(str(df.loc[Vlan_num].values[-1]))
        #print("After VMKernel_Param : ", Add_VMKernel_Param)
        ESXi_list[-1]["addvk"].append(vk_list[-1].copy())
    #print("After ESXi_Param : ", ESXi_list[-1])
    Infra_Format["lab"]["vsphere"]["host"].append(ESXi_list[-1].copy())
print(Infra_Format)#ここまではOK!!!!!!!!!!!

with open(r"C:\infra_parameter.json","w") as f:
    js.dump(Infra_Format,f)
