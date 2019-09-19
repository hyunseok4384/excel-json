#pip install simplejson
#pip install openpyxl
#pip install xlrd
#pip install xlwt
#pip install pandas

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
                                        "cluster":[],
                                        "vDS":{
                                            "name":"xxxx",
                                            "PortGroup":[]
                                        }
                                }
                            }
                }
        }
}
ESXi_Format = {"mgmt":{"ip":"xxx.xxx.xxx.xxx","subnet":"xxx.xxx.xxx.xxx"},
                "hostname":"xxxxx",
                "user":"root",
                "pw":"xxxx",
                "addvk":[]
                }
Add_VMKernel_Foramt = {"use":"xxxx",
                        "ip":"xxx.xxx.xxx.xxx",
                        "subnet":"xxx.xxx.xxx.xxx",
                        "pgname":"xxxxx",
                        "vlan":"xxxx"
                        }
Cluster_Format = {"name":"xxxxx",
                    "member":[]
                }
PortGroup_Format = {"use":"xxx",
                    "name":"xxxx",
                    "vlan":"xxx"
                }

import simplejson as js
import pandas as pd
import openpyxl

#df = pd.read_excel(r"C:\parameter\vCenter_Infra_parameter.xlsx",headers=0,index_col=0,sheet_name=None)
sheet_info = openpyxl.load_workbook(r"C:\parameter\vCenter_Infra_parameter.xlsx")
sheet_name = sheet_info.sheetnames
print(sheet_name)
#['vCenter_Info', 'vDS', 'ESXi_01', 'ESXi_02', 'ESXi_03']

esxi_sheet = [x for x in sheet_name if "ESXi" in x]
print(esxi_sheet)
#['ESXi_01', 'ESXi_02', 'ESXi_03']
Infra_Format = Format
esxi_num = esxi_sheet.split("_")
for esxi in esxi_sheet:
    print("-------------------------------------------------------------------------------")
    print(esxi)
    df = pd.read_excel(r"C:\parameter\vCenter_Infra_parameter.xlsx",headers=0,index_col=0,sheet_name=esxi)
    #print(df.index)
    number_info = [x for x in df.index if "VMKernel" in x]
    print("number_info : ", number_info)
    #['VMKernel-01', 'VMKernel-02']
    ESXi_Param = ESXi_Format
    """
    print(df.loc["FQDN"].values)
    print(df.loc["ESXi_User"].values)
    print(df.loc["ESXi_Passeord"].values)
    print(df.loc["Ip_Address"].values)
    print(df.loc["Cluster"].values)
    """
    ESXi_Param["hostname"]="".join(df.loc["FQDN"].values)
    ESXi_Param["user"]="".join(df.loc["ESXi_User"].values)
    ESXi_Param["pw"]="".join(df.loc["ESXi_Passeord"].values)
    ESXi_Param["mgmt"]["ip"]="".join(df.loc["Ip_Address"].values)
    ESXi_Param["mgmt"]["subnet"]="".join(df.loc["Subnet"].values)
    print(ESXi_Param)
    for number in number_info:
        #print("number : ", number)
        #print("number : ",number.split("-")[-1])
        Add_VMKernel_Param = Add_VMKernel_Foramt
        Use_num = "Use-"+number.split("-")[-1]
        Ip_num = "Ip-"+number.split("-")[-1]
        Subnet_num = "Subnet-"+number.split("-")[-1]
        PortName_num = "PortName-"+number.split("-")[-1]
        Vlan_num = "Vlan-"+number.split("-")[-1]
        Add_VMKernel_Param["use"]="".join(df.loc[Use_num].values)
        Add_VMKernel_Param["ip"]="".join(df.loc[Ip_num].values)
        Add_VMKernel_Param["subnet"]="".join(df.loc[Subnet_num].values)
        Add_VMKernel_Param["pgname"]="".join(df.loc[PortName_num].values)
        Add_VMKernel_Param["vlan"]="".join(str(df.loc[Vlan_num].values))
        print(Add_VMKernel_Param)
        #ESXi_Param["addvk"].append(Add_VMKernel_Param)
    #Infra_Format["lab"]["vsphere"]["host"].append(ESXi_Param)
    #print(Infra_Format)
    """
    print(use_num, ":", df.loc[use_num].values)
    print(ip_num, ":", df.loc[ip_num].values)
    print(subnet_num, ":", df.loc[subnet_num].values)
    print(PortName_num, ":", df.loc[PortName_num].values)
    print(Vlan_num, ":", str(df.loc[Vlan_num].values))
    """
