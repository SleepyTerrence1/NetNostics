#Calculate the results of measurements
from statistics import mean
list = [56.2, 30.9, 28.5, None, 28.2, None]

def AverageRTT(listThing):
    return mean(listThing)

def MinRTT(listThing):
    return min(listThing)

def MaxRTT(ListThing):
    return max(ListThing)

def PacketAnyalsis(listThing):
    sucessful_pings = [t for t in listThing if t is not None]

    total_sent = len(listThing)
    total_recieved = len(sucessful_pings)
    loss_percent = ((total_sent - total_recieved) / total_sent) * 100
    print(f"Packets Sent: {total_sent} | Recieved: {total_recieved} | Loss: {loss_percent}")

ListMOD = [t for t in list if t is not None]

try:
    AverageRTT(ListMOD)
    MaxRTT(ListMOD)
    MinRTT(ListMOD)
    PacketAnyalsis(list)
except:
    pass


"""
print(AverageRTT(ListMOD))
print(MaxRTT(ListMOD))
print(MinRTT(ListMOD))
PacketAnyalsis(list)
"""