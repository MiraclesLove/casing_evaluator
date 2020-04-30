import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

data=pd.read_table('WA1.txt', delim_whitespace=True, index_col='M__DEPTH')

data=data.replace('-999.00000',np.nan)

data=data.rename(columns=({'M__DEPTH':'DEPT'}))
data['DEPT']=data.index

tops = ('Torok','Pebble SH','Walakpa SS', 'J-Klingak','Barrow SS','Klingak SH','T-Sag River SS', 'Shublik','Basement')
tops_depths=(100,1701,2071,2087,2990, 3102,3224,3258,3633)

# Create the figure and subplots
def triple_combo_plot(top_depth, bottom_depth):
    logs = data[(data.DEPT >= top_depth) & (data.DEPT <= bottom_depth)]
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 10), sharey=True)
    fig.suptitle("Well Composite", fontsize=22)
    fig.subplots_adjust(top=0.75, wspace=0.1)

    # General setting for all axis
    for axes in ax:
        axes.set_ylim(top_depth, bottom_depth)
        axes.invert_yaxis()
        axes.yaxis.grid(True)
        axes.get_xaxis().set_visible(False)
        for (i, j) in zip(tops_depths, tops):
            if ((i >= top_depth) and (i <= bottom_depth)):
                axes.axhline(y=i, linewidth=0.5, color='black')
                axes.text(0.1, i, j, horizontalalignment='center', verticalalignment='center')

    # 1st track: GR, CALI, SP track

    ax01 = ax[0].twiny()
    ax01.set_xlim(-100, 10)
    ax01.spines['top'].set_position(('outward', 0))
    ax01.set_xlabel("SP [mV]")
    ax01.plot(logs.SP, logs.DEPT, label='SP[mV]', color='blue')
    ax01.set_xlabel('SP[mV]', color='blue')
    ax01.tick_params(axis='x', colors='blue')
    ax01.grid(True)

    ax02 = ax[0].twiny()
    ax02.set_xlim(6, 36)
    ax02.plot(logs.CALI, logs.DEPT, '--', label='CALN[in]', color='black')
    ax02.spines['top'].set_position(('outward', 40))
    ax02.set_xlabel('CALI[in]', color='black')
    ax02.tick_params(axis='x', colors='black')

    ax03 = ax[0].twiny()
    ax03.set_xlim(0, 150)
    ax03.plot(logs.GR, logs.DEPT, label='GR[api]', color='green')
    ax03.spines['top'].set_position(('outward', 80))
    ax03.set_xlabel('GR[api]', color='green')
    ax03.tick_params(axis='x', colors='green')

    # 2nd track: Resistivities

    ax11 = ax[1].twiny()
    ax11.set_xlim(0.1, 100)
    ax11.set_xscale('log')
    ax11.grid(True)
    ax11.spines['top'].set_position(('outward', 80))
    ax11.set_xlabel('ILD[m.ohm]', color='red')
    ax11.plot(logs.ILD, logs.DEPT, label='ILD[m.ohm]', color='red')
    ax11.tick_params(axis='x', colors='red')

    ax12 = ax[1].twiny()
    ax12.set_xlim(0.1, 100)
    ax12.set_xscale('log')
    ax12.plot(logs.ILM, logs.DEPT, label='ILM[m.ohm]', color='purple')
    ax12.spines['top'].set_position(('outward', 40))
    ax12.set_xlabel('ILM[m.ohm]', color='purple')
    ax12.tick_params(axis='x', colors='purple')

    ax13 = ax[1].twiny()
    ax13.set_xlim(0.1, 100)
    ax13.set_xscale('log')
    ax13.plot(logs.LL8, logs.DEPT, '--', label='LL8[m.ohm]', color='black')
    ax13.spines['top'].set_position(('outward', 0))
    ax13.set_xlabel('LL8[m.ohm]', color='black')
    ax13.tick_params(axis='x', colors='black')

    # 3rd track: DT, RHOB, NPHI track

    ax21 = ax[2].twiny()
    ax21.grid(True)
    ax21.set_xlim(140, 40)
    ax21.spines['top'].set_position(('outward', 0))
    ax21.set_xlabel('DT[us/ft]')
    ax21.plot(logs.DT, logs.DEPT, label='DT[us/ft]', color='blue')
    ax21.set_xlabel('DT[us/ft]', color='blue')
    ax21.tick_params(axis='x', colors='blue')

    ax22 = ax[2].twiny()
    ax22.set_xlim(-15, 45)
    ax22.invert_xaxis()
    ax22.plot(logs.NPHI, logs.DEPT, label='NPHI[%]', color='green')
    ax22.spines['top'].set_position(('outward', 40))
    ax22.set_xlabel('NPHI[%]', color='green')
    ax22.tick_params(axis='x', colors='green')

    ax23 = ax[2].twiny()
    ax23.set_xlim(1.95, 2.95)
    ax23.plot(logs.RHOB, logs.DEPT, label='RHOB[g/cc]', color='red')
    ax23.spines['top'].set_position(('outward', 80))
    ax23.set_xlabel('RHOB[g/cc]', color='red')
    ax23.tick_params(axis='x', colors='red')

    plt.savefig ('triple_combo_plot.png', dpi=200, format='png')

#%matplotlib nbagg

triple_combo_plot(data.DEPT.min(),data.DEPT.max())
plt.show()

top_depth= 2960
bottom_depth=3340

triple_combo_plot(top_depth,bottom_depth)
plt.show()