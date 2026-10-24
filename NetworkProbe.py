#RUns probes, collects measurements
import subprocess as sp
Hostname = input("Enter Domain: ")
Extracted_Time = [

]
try:
    print("Please wait for results...")
     
    for i in range(10):
        result = sp.run(["ping", "-c", "1", Hostname], capture_output = True, text=True, timeout = 15)
        if result.returncode == 0 and "time=" in result.stdout:
            SplitThing = result.stdout.split("time=")[1]
            time_num = float(SplitThing.split(" ")[0])

            Extracted_Time.append(time_num)

            print(f"Ping {i+1}: Recieved reply in {time_num} ms")
        else:
            Extracted_Time.append(None)
            print(f"Ping {i+1}: Failed")
            print(f"Error: {result.stderr}")

    sucessful_pings = [t for t in Extracted_Time if t is not None]
    total_sent = len(Extracted_Time)
    total_recieved = len(sucessful_pings)
except sp.TimeoutExpired:
    print("Server Timed Out")
except FileNotFoundError:
    print("Ping is not installed")
