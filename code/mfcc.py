import librosa as lr

def audio2MFCC(filein, config):
	y, sr = lr.load(filein)
	return lr.feature.mfcc(y = y, sr = sr, n_mfcc = config.getint('mfcc', 'n_mfcc'), hop_length = config.getint('mfcc', 'hop_length'))

def MFCC2delta(mfcc):
	return lr.feature.delta(mfcc)
