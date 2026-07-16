import tkinter as tk

# 1.创建窗口
    # Tk()：Tk 类的构造函数（创建对象），调用它会创建一个主窗口。
a1 = tk.Tk()

# 2.获取用户的分辨率,不同的电脑的分辨率不一样，所以需要注意.
a2 = a1.maxsize() #(1470, 895) 返回的变量值是一个元组
print(a2)
k,g = a2 #k = 1470, g = 895,int value.




# 3.设置窗口大小
    # al.geometry('宽x高+距离屏幕左侧多少+距离屏幕上方多少')
    #⚠️注意，这里的x是字母x，不是乘号*。500x100不能有空格
    # 前面的+200是距离左侧，后面的200是距离屏幕上方的位置
    #⚠️注意，后面的两个+不能只单独写一个,要么都不,写要么写两个,否则会报错.
a1.geometry('500x500+200+200')

    # 接标题2的代码内容
    # 这里的数据不能是float只能是int.
    # a1.geometry(f'{int(k * 0.5)}x{int(g * 0.5)}')

# 设置窗口锁定缩放,这里默认是True可以被拉伸，False就是不可以拉伸
a1.resizable(width=False , height=False)

#设置窗口图标,只支持ico格式的图标,png jgp图片格式要去转换.
a1.iconbitmap('Tkinter/plum.ico') # 可以传相对路径和绝对路径




# 4.设置窗口背景颜色
a1.configure(bg='white') #可以颜色英文或编码

# 5.设置窗口标题
a1.title("这是一个窗口")

# 6.设置窗口透明度
# 第一个位置传参 字符串'-alpha'：TK库里面对这个字符串做了一个定义，透明值0～1
a1.attributes('-alpha', 1)

# 7.设置窗口置顶（永远在第一页面）
a1.attributes('-topmost', True)

# 8.设置窗口关闭时执行的函数
def guan():
    print("关闭了")
    # 9.销毁窗口
    a1.destroy()

a1.protocol('WM_DELETE_WINDOW', guan)

### 组件 ### 不能是a1开头了

# 标签组件 Label
# 创建在哪个窗口下：a1。标签显示什么文本：text。font('字体‘，尺寸)。fg是字体颜色。bg背景颜色.
a3 = tk.Label(a1,text ='这是一个东西', font=('微软雅黑', 20), fg='red', bg='black')
# 填充布局 pack()
a3.pack() #布局 显示在窗口哪里

# 10.开启窗口/主循环
a1.mainloop()




