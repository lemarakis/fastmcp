from fastmcp import FastMCP
from system_stats import *

mcp = FastMCP("Research-Server")

@mcp.tool()
def get_cpu_usage():
    """
    Returns the current CPU usage of the server as a percentage.
    Use this tool when the user asks about processor load,
    system performance, or overall server health.
    """
    return cpu_usage()

@mcp.tool()
def get_memory_usage():
    """
    Returns the current memory (RAM) usage of the server.
    Includes total, used, and available memory in gigabytes.
    Use this tool for questions related to system resources
    or memory consumption.
    """
    return memory_usage()

@mcp.tool()
def get_disk_usage(path: str = "/"):
    """
    Returns disk usage statistics for a given filesystem path.
    Includes total, used, and free disk space in gigabytes.
    Use this tool when the user asks about available storage
    or disk capacity.
    """
    return disk_usage(path)

@mcp.tool()
def get_system_uptime():
    """
    Returns how long the server has been running since the last reboot.
    The uptime is provided in a human-readable format
    (days, hours, and minutes).
    """
    return system_uptime()

@mcp.tool()
def get_process_info(process_name: str):
    """
    Returns information about running processes that match
    the given process name (e.g. 'postgres', 'nginx').
    Includes process ID (PID), CPU usage, and memory usage.
    Use this tool to inspect specific services or applications
    running on the server.
    """
    return process_info(process_name)

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
