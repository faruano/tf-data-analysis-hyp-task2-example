import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp
chat_id = 761791964 # Ваш chat ID, не меняйте название переменной
def solution(x: np.array, y: np.array) -> bool:
    return anderson_ksamp([x, y]).pvalue < 0.04 # Ваш ответ, True или False
