#Calculate the results of measurements
from statistics import mean
from NetworkProbe import NetworkProbeLauncher
list1 = [10.0, 20.0, 30.0]
list2 = [10.0, None, 30.0, None]
list3 = [None, None, None]

def AverageRTT(listThing):
    if not sucessful_pings:
        return "N/A"
    return mean(listThing)

def MinRTT(listThing):
    if not sucessful_pings:
        return "N/A"
    return min(listThing)

def MaxRTT(ListThing):
    if not sucessful_pings:
        return "N/A"
    return max(ListThing)

def PacketAnyalsis(listThing):
    sucessful_pings = [t for t in listThing if t is not None]

    total_sent = len(listThing)
    total_recieved = len(sucessful_pings)
    loss_percent = ((total_sent - total_recieved) / total_sent) * 100

    return total_sent, total_recieved, loss_percent

ListMOD = [t for t in list3 if t is not None]
Functions = [AverageRTT, MinRTT, MaxRTT, PacketAnyalsis]

try:
    for function in Functions:
        try:
            function(ListMOD, ListMOD, ListMOD, list3)
        except:
            pass
except:
    pass


#print(f"\nPackets Sent: {total_sent} | Recieved: {total_recieved} | Loss: {float(loss_percent)}")
