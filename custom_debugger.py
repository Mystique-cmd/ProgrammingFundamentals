#Before setting breakpoints, or inspecting memory, we need to attach the debugger to a running process.
import psutil #used to interact with system processes
import ptrace.debugger #used to attach to processes and manipulate them

#list all running processes
for proc in psutil.process_iter(['pid', 'name']):# iterate over all processes on the system and returns the PID and name only 
    try:
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue
# Attach to a process by PID
pid = int(input("Enter the PID of the process to attach to: "))
debugger = ptrace.debugger.PtraceDebugger() 