# pip install psutil py-cpuinfo wmi

import platform
import psutil
import cpuinfo
import wmi

print(f"architecture: {platform.architecture()}")
print(f"network name: {platform.node()}")
print(f"operating system: {platform.platform()}")
print(f"processor: {platform.processor()}")

my_cpuinfo = cpuinfo.get_cpu_info()
print(f"full cpu name: {my_cpuinfo['brand_raw']}")
print(f"hz_actual_friendly: {my_cpuinfo['hz_actual_friendly']}")
print(f"hz_advertised_friendly: {my_cpuinfo['hz_advertised_friendly']}")
print(my_cpuinfo.keys())
print(f"total ram: {psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} GB")

pc = wmi.WMI()
os_info = pc.Win32_OperatingSystem()[0]
print(os_info)
print(pc.Win32_Processor()[0].name)
print(pc.Win32_VideoController()[0].name)