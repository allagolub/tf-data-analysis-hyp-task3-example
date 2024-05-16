import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


chat_id = 1304567965

def solution(sample: np.ndarray) -> bool:
    res = ttest_1samp(sample, 300, alternative='less')
    return res[1] < 0.06
