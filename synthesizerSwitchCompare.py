from matlablike import *
close('all')

fileName = '150409Experiments.h5'
beforeAmp = nddata_hdf5(fileName + '/SwitchAfterIQmixBeforeAmpComparison')
afterAmp = nddata_hdf5(fileName + '/SwitchAfterIQmixAfterAmp')
finalConfig = nddata_hdf5(fileName + '/finalSynthesizerConfiguration')

figure()
plot(beforeAmp,alpha = 0.5,label='Before the Amplifier')
plot(afterAmp,alpha = 0.5,label='After the Amplifier')
plot(finalConfig,alpha = 0.5,label='Final Configuration')
title('Synthesizer Switch Comparison')
ylabel('Sampling Scope Voltage')
xlabel('time (ns)')
legend()


show()

