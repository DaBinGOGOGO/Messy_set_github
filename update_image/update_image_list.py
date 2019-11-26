import matplotlib.pyplot as plt
import time

# list实时更新图像
def list_figure(ax,ay,xlable='x',ylable='y',title='Title',save_figure=False,out='./plot.jpg'):
    plt.clf()
    plt.plot(ax, ay)  # 画出当前 ax 列表和 ay 列表中的值的图形
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.title(title)
    if save_figure:
        plt.savefig(out)
    plt.pause(0.1)
    plt.ioff()

ax = []                    # 定义一个 x 轴的空列表用来接收动态的数据
ay = []                    # 定义一个 y 轴的空列表用来接收动态的数据
plt.ion()                  # 开启一个画图的窗口
for i in range(10):       # 遍历0-99的值
    ax.append(i)           # 添加 i 到 x 轴的数据中
    ay.append(i**2)        # 添加 i 的平方到 y 轴的数据中
    time.sleep(5)
    if i<10-1:
        save=False
    else:
        save=True
    list_figure(ax,ay,save_figure=save)




