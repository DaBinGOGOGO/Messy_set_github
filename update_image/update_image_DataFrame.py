import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
# df 实时更新图像

def df_figure(df,xlable='x',ylable='y',title='Title',save_figure=False,out='./plot_df.jpg'):
    plt.close() # 保证输出最新图像前，删掉之前的图像
    plt.ion()
    df.plot(x=xlable)
    # df.plot()
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.title(title)
    if save_figure:
        plt.savefig(out)
    plt.pause(1)
    # plt.ioff()


a=np.arange(1,6,1)
b=a**2
c=2*a+b
df=pd.DataFrame({'epoch': 0.0, 'f1_test': 0.0,'f1':0.0},index=[0])

for i in range(len(a)):
    dic = {'epoch': a[i], 'f1_test': b[i], 'f1':c[i]}
    df = df.append(dic, ignore_index=True)
    time.sleep(2)
    if i < len(a) - 1:
        save = False
    else:
        save = True
    df_figure(df,xlable='epoch',save_figure=save)

# print(df)





