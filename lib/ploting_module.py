import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from zbox_config import data_path
from zbox_config import plot_path

def draw():

    pm_raw_data = pd.read_csv(data_path + "record.csv")[-864:]

    data = pm_raw_data[["s_d0", "date", "time"]]
    data.index = data["date"] + " " + data["time"]
    data = data[["s_d0"]]
    data.index = pd.to_datetime(data.index)
    data = data.resample("5min").mean()
    data = data.interpolate()

    ax = data.plot(figsize=(12, 5), fontsize=24)
    ax.get_legend().remove()

    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=0)
    plt.ylabel('PM2.5', fontsize=26)

    plt.savefig(plot_path + "pm25_line.png", bbox_inches = "tight")
