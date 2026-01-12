from fastapi import FastAPI, Query
from system_stats import *

app = FastAPI(title="Research Server Classic API")

@app.get("/api/cpu")
def api_cpu():
    return cpu_usage()

@app.get("/api/memory")
def api_memory():
    return memory_usage()

@app.get("/api/disk")
def api_disk(path: str = Query("/")):
    return disk_usage(path)

@app.get("/api/uptime")
def api_uptime():
    return system_uptime()

@app.get("/api/process")
def api_process(name: str):
    return process_info(name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
