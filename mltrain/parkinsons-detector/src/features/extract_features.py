def extract_features(data):
    features = {}
    
    # Example feature extraction: mean and standard deviation of a signal
    features['mean'] = data.mean()
    features['std_dev'] = data.std()
    
    # Add more feature extraction methods as needed
    # features['feature_name'] = some_feature_extraction_method(data)
    
    return features

def extract_time_domain_features(data):
    time_domain_features = {}
    
    # Example: calculate time domain features
    time_domain_features['max'] = data.max()
    time_domain_features['min'] = data.min()
    
    return time_domain_features

def extract_frequency_domain_features(data):
    frequency_domain_features = {}
    
    # Example: calculate frequency domain features using FFT
    fft_values = np.fft.fft(data)
    frequency_domain_features['fft_real'] = np.real(fft_values)
    frequency_domain_features['fft_imag'] = np.imag(fft_values)
    
    return frequency_domain_features