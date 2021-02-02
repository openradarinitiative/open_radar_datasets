import numpy as np
import scipy.ndimage
from matplotlib import pyplot as plt

filename = "sample_dataset.npy"
signatures = scipy.load(filename, allow_pickle=True)

for signature in signatures:
    if (len(signature['snr_db']) > 10):
        arr = signature['signature']
        arr = 20 * np.log10(np.abs(arr)).transpose()
        prf = signature['radar_parameters']['prf']
        plt.imshow(arr, cmap='jet', aspect='auto', vmax=np.max(arr) - 20, vmin=np.max(arr) - 70,
                      extent=[0, arr.shape[1], -int(prf/2), int(prf / 2)])
        plt.title(signature['class_name'])
        plt.autoscale()
        # plt.colorbar(axdata)
        plt.xlabel('Time (seconds) in samples')
        plt.ylabel('Doppler frequency shift (Hz)')
        plt.show()