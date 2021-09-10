import numpy as np
import scipy.ndimage
from matplotlib import pyplot as plt

filename = "sample_dataset.npy"
signatures = scipy.load(filename, allow_pickle=True)

for signature in signatures:
    if (len(signature['snr_db']) > 10 and signature['class_name']=="uav"):
        from skimage.transform import resize
        arr = signature['signature']
        arr = 20 * np.log10(np.abs(arr)).transpose()
        interp_times = 10
        res = resize(arr, (arr.shape[0] , arr.shape[1] * interp_times))
        arr = res
        print(arr.shape[1])
        # print(signature['ts'][0])
        # print(signature['ts'][-1])
        print(signature['ts'][-1]-signature['ts'][0])
        print("Length in seconds: " + str((signature['ts'][-1]-signature['ts'][0])/100))
        prf = signature['radar_parameters']['prf']
        plt.imshow(arr, cmap='jet', aspect='auto', vmax=np.max(arr) - 20, vmin=np.max(arr) - 70,
                      extent=[0, arr.shape[1]/200, -int(prf/2), int(prf / 2)])
        plt.title(signature['class_name'])
        plt.autoscale()
        # plt.colorbar(axdata)
        plt.xlabel('Time (seconds)')
        plt.ylabel('Doppler frequency shift (Hz)')
        plt.show()
