#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd
# -------------------------------------------------------------------------------------------------------
#	script to plot the properties of the IP shocks
#	detected by several spacecrafts
#
# --------------------------------------------------------------------------------------------------------
data = pd.read_table('~/MEGA/work-Miho/programsR/TotData1UA_WithSirs.dat',sep='\t')
#data1AU_FFWsh = data1AURep[data1AURep.ShTy.eq('FF') & data1AURep.SC.ne('Helios-A') & data1AURep.SC.ne('Helios-B')&data1AURep.Brt.ge(1.2)&data1AURep.Nprt.ge(1.2)&data1AURep.Trt.ge(0.83)&data1AURep.Mach.gt(1.0)&data1AURep.ShIc.eq(1)]

data = data[data.ShTy.eq('FF') & data.SC.ne('Helios-A') & data.SC.ne('Helios-B')&data.Brt.ge(1.2)&data.Nprt.ge(1.2)&data.Trt.ge(0.83)&data.Mach.gt(1.0)&data.ShIc.eq(1)]

iSTA = data[data.SC.eq('STEREO-A')] 
iSTB = data[data.SC.eq('STEREO-B')] 



#-----------------------------------------------------
t = np.linspace(0,2*np.pi,100)
radius_20 = 20/100.
radius_40 = 40/100.
radius_60 = 60/100.
radius_80 = 80/100.
radius_100 = 100/100.
radius_120 = 120/100.
radius_140 = 140/100.

xs = 0
ys = 0
x2 =  radius_20 * np.cos(t)
y2 =  radius_20 * np.sin(t)
x4 =  radius_40 * np.cos(t)
y4 = radius_40 * np.sin(t)
x6 =  radius_60 * np.cos(t)
y6 =  radius_60 * np.sin(t)
x8 =  radius_80 * np.cos(t)
y8 =  radius_80 * np.sin(t)
x10 =  radius_100 * np.cos(t)
y10 =  radius_100 * np.sin(t)
x12 = radius_120 * np.cos(t)
y12 = radius_120 * np.sin(t)
x14 = radius_140 * np.cos(t)
y14 = radius_140 * np.sin(t)
#-----------------------------------------------------
#fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
#ax.plot(theta, r)

#plt.scatter(STA['mo_sc_long_heeq'],STA['mo_sc_heliodistance'] ,c='red', s=5 )
#plt.scatter(STB['mo_sc_long_heeq'],STB['mo_sc_heliodistance'] ,c='blue', s=5 )
#plt.scatter(PSP['mo_sc_long_heeq'],PSP['mo_sc_heliodistance'] ,c='black', s=5, label='PSP' )



plt.plot(iSTA['rd1AU'],iSTA['SCPhi'], 'ro', markersize=3, label='STA', c='red')
plt.plot(iSTB['rd1AU'],iSTB['SCPhi'], 'ro', markersize=3, label='STB', c='blue')




plt.plot(x2,y2,linestyle=':', color='black')
plt.plot(x4,y4,linestyle=':', color='black')
plt.plot(x6,y6,linestyle=':', color='black')
plt.plot(x8,y8,linestyle=':', color='black')
plt.plot(x10,y10,linestyle=':', color='black')
plt.plot(x12,y12,linestyle=':', color='black')
plt.plot(x14,y14,linestyle=':', color='black')

#ax.set_rmax(2)
#ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
#ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
#ax.grid(True)

#ax.set_title("Event longitudes[GSE]", va='bottom')


#plt.scatter(icmecat['mo_sc_heliodistance'],icmecat['mo_sc_long_heeq'],label=r'$F_{r}$', s=10)

plt.show()

























