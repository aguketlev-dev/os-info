import os
import platform
import socket
import json
from datetime import datetime
system = platform.system()
if system == "Windows":
    os_name = "Windows"
elif system == "Linux":
    os_name = "Linux"
else:
    os_name = "Unknown"
info = {
    "operating_system": os_name,
    "os_version": platform.version(),
    "computer_name": socket.gethostname(),
    "architecture": platform.machine(),
    "processor": platform.processor(),
    "logical_cpu_count": os.cpu_count(),
    "current_directory": os.getcwd(),
    "collection_time": datetime.now().astimezone().isoformat()
}
with open("system_info.json", "w", encoding="utf-8") as file:
    json.dump(info, file, ensure_ascii=False, indent=4)
print("Информация о системе собрана.")
