import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
    
wav_filename = 'hz_220.wav'
sr=44100
x, sr = librosa.load(wav_filename, sr=sr)
print(x)
print(sr)
print(type(x), type(sr))

plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)
plt.show()
plt.pause(0.001)
