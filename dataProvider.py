import csv
import json

def get_build_queue():
    with open('build_queue.csv','rt')as f:
        data = csv.reader(f)
    
    return data


def get_free_VMs():
    with open('VMs.csv','rt')as f:
        data = csv.reader(f)
    
    return data


def get_compatible_VMS(div=None ,POR=None ,SuiteType=None ):
    data=json.load(open("VM_compatibility.json"))
    if(div == None):
        return data
    else:
        if(POR==None):
            return data[div]
        else:
            if(SuiteType==None):
                return data[div][POR]
            else:
                return data[div][POR][SuiteType]
    


def get_compatible_suites_by_VM(VM):
    data= json.load(open("VM_compatibility_Transpose.json"))
    return data[VM]