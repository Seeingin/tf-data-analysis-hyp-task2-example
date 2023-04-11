import pandas as pd
import numpy as np


chat_id = 752592494

def solution(x: np.array, y: np.array) -> bool:
    import scipy.stats as stats

    res = scipy.stats.ks_2samp(x, y, alternative='two-sided', method='auto')
    pvalue = res.pvalue
    if pvalue > 0.07:
      return False
    else:
      return True
