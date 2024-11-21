from neurostates.core.window import window
from scipy.signal.windows import hamming

import numpy as np

def test_window_shape_tapering_none():
    np.random.seed(42) # ver como cambiar esto
    n_subjects = 20
    n_regions = 90
    n_samples = 150
    data_array = np.random.rand(n_subjects, n_regions, n_samples)

    size = 20
    step = 5
    sliding_window = window(data_array, size, step)
    windows, subjects, regions, samples = sliding_window.shape

    n_windows_ref = int((n_samples - size) / step) + 1
    assert windows == n_windows_ref
    assert subjects == n_subjects
    assert regions == n_regions
    assert samples == size

def test_window_shape_tapering():
    np.random.seed(42) # ver como cambiar esto
    n_subjects = 20
    n_regions = 90
    n_samples = 150
    data_array = np.random.rand(n_subjects, n_regions, n_samples)

    size = 20
    step = 5
    sliding_window = window(data_array, size, step, hamming)
    windows, subjects, regions, samples = sliding_window.shape

    n_windows_ref = int((n_samples - size) / step) + 1
    assert windows == n_windows_ref
    assert subjects == n_subjects
    assert regions == n_regions
    assert samples == size
