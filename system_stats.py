import psutil
import shutil
import time

# --------------------
# CORE FUNCTIONS
# --------------------

def cpu_usage():
    return {"cpu_percent": psutil.cpu_percent(interval=1)}

def memory_usage():
    mem = psutil.virtual_memory()
    return {
        "total_gb": round(mem.total / 1024**3, 2),
        "used_gb": round(mem.used / 1024**3, 2),
        "available_gb": round(mem.available / 1024**3, 2),
        "percent": mem.percent,
    }

def disk_usage(path: str):
    du = shutil.disk_usage(path)
    return {
        "path": path,
        "total_gb": round(du.total / 1024**3, 2),
        "used_gb": round(du.used / 1024**3, 2),
        "free_gb": round(du.free / 1024**3, 2),
    }

def system_uptime():
    uptime_sec = time.time() - psutil.boot_time()
    days, rem = divmod(int(uptime_sec), 86400)
    hours, rem = divmod(rem, 3600)
    minutes, _ = divmod(rem, 60)
    return {
        "uptime": f"{days} ημέρες, {hours} ώρες, {minutes} λεπτά"
    }

def process_info(name: str):
    matches = []
    for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        if name.lower() in p.info["name"].lower():
            matches.append(p.info)
    return matches

