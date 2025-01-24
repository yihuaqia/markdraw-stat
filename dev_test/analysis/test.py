# print which python version is being used
import sys
print(sys.version)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
import time

# print the current working directory
print(os.getcwd())
# print dependencies versions
print('numpy: ', np.__version__)
print('pandas: ', pd.__version__)
print('seaborn: ', sns.__version__)
print('matplotlib: ', plt.matplotlib.__version__)

# print the current time
print(time.ctime())
