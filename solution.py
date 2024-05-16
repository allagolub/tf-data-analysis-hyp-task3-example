import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest as ztest


chat_id = 1304567965

def solution(x):
    res = ztest(x1=x, value=300, alternative='smaller')
    return res[1] < 0.06
