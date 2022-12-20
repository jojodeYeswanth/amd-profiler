import os
import json
import pandas as pd
import datetime
import subprocess
import time
import glob
#----------------------------------nativePlatformProfilier-----------------------------------


def nativePlatformDetails():

    core = os.popen(" lscpu | grep 'Core(s) per socket' | cut -f 2 -d ':' | awk '{$1=$1}1'").read()
    model_name = os.popen("lscpu | grep 'Model name' | cut -f 2 -d ':' | awk '{$1=$1}1'").read()
    Vcpu_count = os.popen("lscpu | grep 'On-line' | cut -f 2 -d ':' | awk '{$1=$1}1'").read()

    mem_max = os.popen(" vmstat -s |grep 'total memory'| awk '{$1=$1/(1024^2); print $1}'").read()
    mem_max1=float(mem_max)
    mem_max2=str(round(mem_max1,1))+"GB"
    mem_max2=mem_max2.replace(".","_")

    disk_capacity = getTotalDiskSize()

    nettype = os.popen('ls /sys/class/net').read()

    nettype = list(nettype.split())

    native_platform_name = model_name.replace(" ","").strip()+str(Vcpu_count).strip()+"c"+str(mem_max2).strip()+disk_capacity.strip()

    timestamp=str(datetime.datetime.now().strftime("%d%m%Y%H%M%S"))

    native_platform_id = native_platform_name + timestamp
    
    nativeplatformdetails = {
        "nativePlatformID" : native_platform_id,
        "nativePlatformName" : native_platform_name,
        "cores" : core.strip(),
        "model_name" : model_name.strip(),
        "vcpu_count" : str(Vcpu_count).strip(),
        "mem_max" : mem_max2.strip(),
        "disk_capacity" : disk_capacity.strip(),
        "net_type" : nettype
        }

    
    global output_path 
    output_path= os.path.join(path, "wrapper")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(output_path + " folder created.")
    else:
        print(output_path + " folder exists.")
    native_path= os.path.join(output_path,"nativeplatformdetails.json")
    with open(native_path,'w') as outfile:
        json.dump(nativeplatformdetails,outfile)


def getDiskSize():
    os.system('lsblk --json > lsblk.json')

    with open('lsblk.json', 'r') as f:
        demo= json.load(f)
        df = pd.DataFrame(demo)
        name, size = [], []


    if (df['blockdevices'].count() > 0):
        for i in range(df['blockdevices'].count()):
            if(df['blockdevices'][i]['type'] == 'disk'):
                name.append(df[ 'blockdevices' ][i]['name'])
                size.append(df[ 'blockdevices' ][i]['size'])
    

    for i in size:
        if 'G' in i:
            index= size. index(i)
            i = i.translate({ord('G'): None})
            i = float(i)
            i = str(round(i, 1)) + "G"
            size[index] = i

    df2 = pd.DataFrame()
    df2['name'] = [i for i in name]
    df2['size'] = [i for i in size]

    
    json_rec = json.dumps (json.loads(df2.to_json(orient="records")))

    os.remove('lsblk.json')
    return json_rec


def getTotalDiskSize():
    size = []
    demo2 = getDiskSize()
    df = pd.read_json(demo2)
   

    for i in list(df['size']):
        i=i.translate({ord('G'): None})
        size.append(float(i))

    totalSize = str(round(sum(size), 4))+'g'
    totalSize = totalSize.replace(".", "_")
    
    
    return totalSize

def rename_workloadfile():
    global output_path
    file_extension = ".err"
    files = os.listdir(output_path)
    newfilename = "WorkloadProfilier.json"
    newfile = os.path.join(output_path,newfilename)
    hostname=os.uname()[1]
    print(hostname)


    for file in files:
        if file.endswith(file_extension):
            os.remove(os.path.join(output_path,file))
            break

    pattern = output_path +"/" + hostname + "*.json"
    
    result = glob.glob(pattern)
    
    

    for file_name in result:
        old_name = file_name
        new_name = output_path+"/" + newfilename
        os.rename(old_name, new_name)
     
                

def run():
    pro = subprocess.call(["bash",'./njmondemo.sh'])

path = os.path.join(os.getcwd())
output_path = os.path.join(path, "wrapper")
if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(output_path + " folder created.")
    run()
    time.sleep(25)
    print("Data Collected")
    rename_workloadfile()
    nativePlatformDetails()

else:
    print(output_path + " folder exists.")
    run()
    time.sleep(25)
    print("Data Collected")
    rename_workloadfile()
    nativePlatformDetails()



