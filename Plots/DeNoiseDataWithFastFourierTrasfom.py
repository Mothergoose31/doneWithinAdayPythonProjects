import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16,12]
plt.rcParams.update({'font.size':18})

# create a signal with two frequencies

dt = 0.001
t = np.arange(0,1,dt)
f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
# sum of two frequencies
f_clean = f
f = f + 2.5*np.random.randn(len(t))
plt.plot(t,f,color='c',LineWidth=1.5,label = "noisy")
plt.plot(t,f_clean,color='k',LineWidth=2,label="clean")
plt.xlim(t[0],t[-1])
plt.legend()


n = len(t)
# compute the fast fourier transform
fhat = np.fft.fft(f,n)
# power spectrum (power per f)
PSD = fhat * np.conj(fhat)/n
# create x-axis or frequencies
freq= (1/(dt*n))* np.arange(n)
# only plot the first half
L = np.arange(1,np.floor(n/2),dtype='int')

fig,axs = plt.subplots(2,1)
plt.sca(axs[0])
plt.plot(t,f,color='c',LineWidth=1.5,label = "noisy")
plt.plot(t,f_clean,color='k',LineWidth=2,label="clean")
plt.xlim(t[0],t[-1])
plt.legend()
