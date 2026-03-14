import psutil 
import ptrace.debugger 
import ctypes
import ctypes.util
import struct
import os
import sys
import signal

#The script loader: Need to add a place where user would be able to input the script file path
class ScriptLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.lines = []
    
    def load_script(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Script file {self.filepath} not found.")
        
        with open(self.filepath, 'r') as file:
            self.lines = file.readlines()
        print(f"Script loaded from {self.filepath}")

    def preview(self, num_lines=5):
        print(f"\nPreviewing first {num_lines} lines of the script:")
        for i, line in enumerate(self.lines[:num_lines] ,1):
            print(f"{i:03}: {line.strip()}")

#Setting and removing breakpoints
class BreakpointManager:
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

#Step Execution Control
class ExecutionControl:
    def __init__(self, pid):
        self.pid = pid
    
    def continue_execution(self):
        if sys.platform.startswith('win'):
            kernel32 = ctypes.windll.kernel32
            kernel32.ResumeThread(kernel32.OpenThread(0x0002, False, self.pid))
        else:
            libc.ptrace(PTRACE_CONT, self.pid, 0, 0)
    
    def step_instruction(self):
        if sys.platform.startswith('win'):
            kernel32 = ctypes.windll.kernel32
            kernel32.StepInto(self.pid)
        else:
            libc.ptrace(PTRACE_SINGLESTEP, self.pid, 0, 0)
    
    def step_over(self):
        if sys.platform.startswith('win'):
            kernel32 = ctypes.windll.kernel32
            kernel32.StepOver(self.pid)
        else:
            libc.ptrace(PTRACE_SINGLESTEP, self.pid, 0, 0)

#constants from sys/ptrace.h
PTRACE_SINGLESTEP = 9
PTRACE_CONT = 7
PTRACE_ATTACH = 16
PTRACE_DETACH = 17
PTRACE_PEEKUSER = 3
PTRACE_POKUSER = 4

libc = ctypes.CDLL(ctypes.util.find_library('c'))

def single_step(pid):
    libc.ptrace(PTRACE_SINGLESTEP, pid, 0, 0)
    os.waitpid(pid, 0)


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
    print(f"{field[0]}: {getattr(regs, field[0]):#x}") 