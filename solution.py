import pandas as pd
import numpy as np


chat_id = 752592494

def solution(x: np.array, y: np.array) -> bool:
    import scipy
    import scipy.stats as stats

    res = stats.cramervonmises_2samp(x, y)
    pvalue = res.pvalue
    if pvalue > 0.07:
      return False
    else:
      return True
