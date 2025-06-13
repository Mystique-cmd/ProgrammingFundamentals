import psutil 
import ptrace.debugger 
import ctypes
import struct
import os
import sys

#Making the debugger cross-platform
class Debugger:
    def __init__(self, pid):
        self.pid = pid
    
    def attach(self):
        if sys.platform.startswith('win'):
            kernel32 = ctypes.windll.kernel32
            kernel32.DebugActiveProcess(self.pid)
        else:
            os.system(f"gdb -p {self.pid}")
        pass

#list all running processes
for proc in psutil.process_iter(['pid', 'name']):# iterate over all processes on the system and returns the PID and name only 
    try:
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue
# Attach to a process by PID
pid = int(input("Enter the PID of the process to attach to: "))
debugger = ptrace.debugger.PtraceDebugger() 

#step 2 : Reading Proceses and Registers
libc = ctypes.CDLL("libc.so.6")

class UserRegStruct(ctypes.Structure):
    _fields_ = [
        ("r15", ctypes.c_ulonglong),
        ("r14", ctypes.c_ulonglong),
        ("r13", ctypes.c_ulonglong),
        ("r12", ctypes.c_ulonglong),
        ("rbp", ctypes.c_ulonglong),
        ("rbx", ctypes.c_ulonglong),
        ("r11", ctypes.c_ulonglong),
        ("r10", ctypes.c_ulonglong),
        ("r9", ctypes.c_ulonglong),
        ("r8", ctypes.c_ulonglong),
        ("rax", ctypes.c_ulonglong),
        ("rcx", ctypes.c_ulonglong),
        ("rdx", ctypes.c_ulonglong),
        ("rsi", ctypes.c_ulonglong),
        ("rdi", ctypes.c_ulonglong),
        ("orig_rax", ctypes.c_ulonglong),
        ("rip", ctypes.c_ulonglong),
        ("cs", ctypes.c_uint16),
        ("eflags", ctypes.c_uint16),
        ("rsp", ctypes.c_ulonglong),
        ("ss", ctypes.c_uint16)
    ]
def get_registers(pid):
    regs = UserRegStruct()
    libc.ptrace(12, pid, None, ctypes.byref(regs))
    return regs
if __name__ == "__main__":
    regs = get_registers(pid)
    print(f"Registers for PID {pid}:")
for field in regs._fields_:
    print(f"{field[0]}: {getattr(regs, field[0])}")

#Step 3: Setting Breakpoints
def set_Breakpoints(self, address):
    if sys.platform.startswith('win'):
        kernel32 = ctypes.windll.kernel32
        kernel32.WriteProcessMemory(self.pid, address, b'\xCC', 1, None)
    else:
        libc.ptrace(7, self.pid, address, 0)  # PTRACE_POKETEXT
    print(f"Breakpoint set at {hex(address)}")
def remove_Breakpoints(self, address):
    if sys.platform.startswith('win'):
        kernel32 = ctypes.windll.kernel32
        kernel32.WriteProcessMemory(self.pid, address, b'\x00', 1, None)
    else:
        libc.ptrace(7, self.pid, address, 0)  # PTRACE_POKETEXT
    print(f"Breakpoint removed at {hex(address)}")  