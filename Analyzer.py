#Calculate the results of measurements
import statistics as st
list = [56, 30, 28, None, 28, None]

def AverageRTT(List):
    return st.mean(List)

def MinRTT(List):
    return st.median_low(List)
