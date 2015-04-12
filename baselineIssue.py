from matlablike import *
close('all')

fileName = '150407Experiments.h5'

noVa = nddata_hdf5(fileName +'/NoVideoAmps')
filt = nddata_hdf5(fileName + '/200MHzBandpass')
noFilt = nddata_hdf5(fileName + '/NoBandpass')

HPLP = nddata_hdf5(fileName + '/highPassLongPulse') # data with a 2 us long pulse zoomed in on the waveform with a 200 MHz high pass filter.
NoHPLP = nddata_hdf5(fileName + '/NoFiltLongPulse') # data with a 2 us long pulse zoomed in on the waveform with no high pass filter.


figure()
plot(noVa.copy().ft('t',shift = True).runcopy(abs),label='No VideoAmp')
plot(filt.copy().ft('t',shift = True).runcopy(abs),label='200 MHz Bandpass')
plot(noFilt.copy().ft('t',shift = True).runcopy(abs),label='No Bandpass')
title('Frequency Spectrum Baseline Issue')
legend()
show()


figure()
plot(HPLP.copy().ft('t',shift = True).runcopy(abs),label='200 MHz HighPass Long Pulse')
plot(noVa.copy().ft('t',shift = True).runcopy(abs),label='No HighPass Long Pulse')
title('Frequency Spectrum Baseline Issue')
legend()

"""
Now pull that data that I took of a solid BDPA sample with the 200 MHz high pass filters in place.
See my notebook 'testing the reciever 15/04/09' in 'AWG Detection Train' 
"""


fileName = '150410Experiments.h5'
dataS = nddata_hdf5(fileName +'/phaseCycleWithBandPassWithSynthSwitch')
dataNS = nddata_hdf5(fileName +'/phaseCycleWithBandPassWithOutSynthSwitch')


figure()
colorlist = ['g','r','b','c']
for count in range(len(dataS.getaxis('phc'))):
    plot(dataS['phc',count].runcopy(real),linestyle = '-',alpha = 0.5,color = colorlist[count],label='real dim = %d'%count)
    plot(dataS['phc',count].runcopy(imag),linestyle = '--',alpha = 0.5,color = colorlist[count],label='imag dim = %d'%count)
title('200 MHz Bandpass with Synth Switch')
legend()
xlabel('frequency (GHz)')
ylabel('spectral count (arb)')

figure()
colorlist = ['g','r','b','c']
for count in range(len(dataNS.getaxis('phc'))):
    plot(dataNS['phc',count].runcopy(real),linestyle = '-',alpha = 0.5,color = colorlist[count],label='real dim = %d'%count)
    plot(dataNS['phc',count].runcopy(imag),linestyle = '--',alpha = 0.5,color = colorlist[count],label='imag dim = %d'%count)
title('200 MHz Bandpass without Synth Switch')
legend()
xlabel('frequency (GHz)')
ylabel('spectral count (arb)')


# grab the signal channels
signalS = dataS['phc',1].copy()
signalNS = dataNS['phc',1].copy()
figure()
plot(signalS.runcopy(real),linestyle = '-',alpha = 0.5,color = 'r',label='real S')
plot(signalS.runcopy(imag),linestyle = '--',alpha = 0.5,color = 'r',label='imag S')
plot(signalS.runcopy(abs),linestyle = '-',alpha = 0.8,color = 'r',label='abs S')
plot(signalNS.runcopy(real),linestyle = '-',alpha = 0.5,color = 'b',label='real NS')
plot(signalNS.runcopy(imag),linestyle = '--',alpha = 0.5,color = 'b',label='imag NS')
plot(signalNS.runcopy(abs),linestyle = '-',alpha = 0.8,color = 'b',label='abs NS')
legend()
title('Synth Switch Compare')

show()
