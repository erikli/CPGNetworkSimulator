import build.CPGNetworkSimulator as nsim
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

musclenames = ["IP", "GM", "VL", "TA", "SO", "BF", "GA", "HAM", "RF"]

left = ["MnIP_L_hind", "MnGM_L_hind", "MnVL_L_hind", "MnTA_L_hind", "MnSO_L_hind", "MnBF_L_hind","MnGA_L_hind","MnHAM_L_hind","MnRF_L_hind"]
right = ["MnIP_R_hind", "MnGM_R_hind", "MnVL_R_hind", "MnTA_R_hind", "MnSO_R_hind", "MnBF_R_hind","MnGA_R_hind","MnHAM_L_hind","MnRF_L_hind"]
mnnames = list()
mnnames.append(left)
mnnames.append(right)
simulator = nsim.CPGNetworkSimulator("./models/Human2CPG_3.txt",musclenames,mnnames)
lscondL = nsim.LimbSensorCondition(9)
lscondR = nsim.LimbSensorCondition(9)

simulator.setLscond([lscondL,lscondR])

dt=0.001
time = np.arange(0.0,10,dt)
acts00=np.zeros((len(time),9))
simulator.updateVariable("fbIa_IP",1.0)
alpha = 0.1
uvars=['FtoIP', 'FtoTA', 'FtoBF', 'FtoRF', 'FtoHAM', 'SwtoIP', 'SwtoTA', 'SwtoBF', 'SwtoHAM', 'SwtoRF']
initialvars=simulator.setupVariableVector(uvars)

for i,t in enumerate(time):
    #alpha+=0.0001
    simulator.setAlpha(alpha)
    for k in range(10):
        simulator.step(dt/10.0)
    
    #if t==5.0:
        #simulator.updateVariable("FtoIP",10.0)
        #print("updated variable")

    #if t==3.0:
        #lscondL.Ia=[1.0,0,0,0,0,0,0,0,0]
        #simulator.setLscond([lscondL,lscondR])
        #print("updated lscond")

    if t==2.0:
        simulator.updateVariableVector([1.0,2.0,1.0,0.5,14.0,11.0,12.0,0.0,9.0,10.0])
        #simulator.setBodyTilt(0.0,-1.0,0.0,0.0);
    if t==7.0:
        simulator.updateVariableVector(initialvars)
    act = simulator.getAct()
    acts00[i]=act[0][:]
    
fig, ax = plt.subplots()
plt.plot(time,acts00[:,7])
plt.show()