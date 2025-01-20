import os

import psutil, platform
from psutil._common import bytes2human


def collect_metrics(node):

    # print(psutil.disk_partitions(all=False))
    print(f"{node} stats")
    print('MEMORY\n------')
    print(psutil.virtual_memory().percent)
    virtual_memory = psutil.virtual_memory().percent
    print('\nSWAP\n----')
    print(psutil.swap_memory().percent)
    swap_memory = psutil.swap_memory().percent
    print('\nCPU USAGE\n-----')
    print(psutil.cpu_percent(interval=1), "\n")
    cpu_usage = psutil.cpu_percent(interval=1)
    print('\nDisk Space USAGE\n-----')
    # print(psutil.disk_usage('/'))
    
    templ = "{:<17} {:>8} {:>8} {:>8} {:>5}% {:>5}  {}"
    print(
        templ.format(
            "Device", "Total", "Used", "Free", "Use ", "Type", "Mount"
        )
    )
    disk_usage_percent = {}
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cd-rom' in part.opts or not part.fstype:
                continue
        usage = psutil.disk_usage(part.mountpoint)    
        line = templ.format(
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint
        )
        print("\n", line)
        usage_percent = {part.device:usage.percent}
        disk_usage_percent.update(usage_percent)

    print(disk_usage_percent)
        

        
        

if __name__ == '__main__':
    collect_metrics(platform.node())
    