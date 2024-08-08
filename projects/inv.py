import os
import platform
import psutil

if 'Windows' in platform.platform():
    os.system('clear')
    cpu_count = os.cpu_count()
    men_info = psutil.virtual_memory().total
    os_version = platform.platform()
    python_verson = platform.python_version()
    print(f"""
        Number of cpu: {cpu_count}
        Total Memory: {men_info/1024**3:.2f} GB
        {os_version}
        Python Version: {python_verson}""")
else:
    pass