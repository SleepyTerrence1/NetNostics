#RUns probes, collects measurements
import subprocess as sp
Hostname = input("Enter Domain: ")
try:
    result = sp.run(["ping", "-c", "1", Hostname], capture_output = True, text=True, timeout = 5)
    
    if result.returncode == 0:
        print(f"\n{result.stdout}")
    else:
        print(result.stderr if result.stderr else "Invaild Domain")
    
except sp.TimeoutExpired:
    print("Server Timed Out")
except FileNotFoundError:
    print("Ping is not installed")
