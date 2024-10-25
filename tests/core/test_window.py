from neurostates.core.io import create_data_from_matrix
from neurostates.core.window import SlidingWindow

import numpy as np


def test_sliding_window_no_tapering_function():
    np.random.seed(42)
    n_subjects = 20
    n_regions = 90
    n_samples = 150
    matrix = np.random.rand(n_subjects, n_regions, n_samples)
    neurodata = create_data_from_matrix(matrix=matrix, modality="fmri", tr=2.0)

    size = 20
    step = 5
    sliding_window = SlidingWindow(size, step)
    sliding_window.apply_to(neurodata)

    n_windows_ref = int((n_samples - size) / step) + 1
    assert sliding_window.windows == n_windows_ref
    assert sliding_window.subjects == n_subjects
    assert sliding_window.regions == n_regions
    assert sliding_window.samples == size
