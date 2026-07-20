import tkinter as tk
from tkinter import messagebox

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
    d1 = messagebox.askokcancel('是否关闭','确定继续关闭吗？')
    if d1:
        # 9.销毁窗口
        a1.destroy()
    else:
        pass

a1.protocol('WM_DELETE_WINDOW', guan)

### 组件 ### 不能是a1开头了

# 标签组件 Label
# 创建在哪个窗口下：a1。标签显示什么文本：text。font('字体‘，尺寸)。fg是字体颜色。bg背景颜色.
## a3 = tk.Label(a1,text ='账号', font=('微软雅黑', 20), fg='red', bg='black')

# 三种布局都只是设置这个组件的位置，布局是可以直接1以.pack()的格式写在label后面，
    # 例如tk.Label(a1,text ='这是一个东西', font=('微软雅黑', 20), fg='red', bg='black').pack()
# 填充布局 pack() 默认布局，
## a3.pack() #布局 显示在窗口哪里
    
# 自定义布局 place(x,y)设置组件的位置，不能超过窗口大小的范围
## a3.place(x=100, y=100)

# 网格布局 grid(row,column) 行，列 有一个自动填充例如一个在c=1，另一个c=3，第二个c也还是在c=2的位置
## a3.grid(row=1, column=1)








# 字符串变量 StringVar
s1 = tk.StringVar() #创建一个字符串变量
s1.set('请输入账号') # 当成一个提示文本

s2 = tk.StringVar()
s2.set('请输入密码')

# 输入框组件 Entry
tk.Label(a1, text='账号', width=3, font=('微软雅黑', 20)).place(x=50, y=100)
tk.Label(a1, text='密码', width=3, font=('微软雅黑', 20)).place(x=50, y=150)
# textvariable就是要用来绑定的变量
# state='normal'是默认状态，'disabled'是禁用状态，'readonly'是只读状态
tk.Entry(a1,state='normal', textvariable=s1, font=('微软雅黑', 20)).place(x=110, y=100)
tk.Entry(a1, textvariable=s2, font=('微软雅黑', 20)).place(x=110, y=150)

def dl():
    # 字符串变量获取 通过.get()方法
    print(f'输入的账号:{s1.get()}')
    print(f'输入的密码:{s2.get()}')
    if s1.get() in hao:
        if s2.get() == hao[s1.get()]:
            messagebox.showinfo('提示', '登录成功')
        else:
            messagebox.showerror('提示', '密码错误')
    else:
        d1 = messagebox.askokcancel('ERROR', '账号不存在')
        if d1:# 选择ok
            print('重新输入')
        else:# 选择cacel
            print('关闭窗口')
    
# 按钮 Button,command是点击按钮后执行的函数
tk.Button(a1,command=dl, width=5, text='登录', font=('微软雅黑', 20)).place(x=250, y=200)

# 四种弹窗组件 messagebox，需要从tkinter导入messagebox。
## messagebox.showerror('标题', '内容')     红色的三角感叹号
## messagebox.showinfo('标题', '内容')      蓝色的三角感叹号
## messagebox.showwarning('标题', '内容')   黄色的三角感叹号
## messagebox.askokcancel('标题', '内容')   多了一个cancel的按钮。应用场景很多，可以做二次阻拦。可以判断用户选择的是ok还是cancel。



s3 = tk.StringVar() #创建一个字符串变量
s3.set('请输入账号') # 当成一个提示文本

s4 = tk.StringVar()
s4.set('请输入密码')

    

# 顶层窗口/内层窗口 Toplevel()。 在主窗口内又打开了一个窗口
## a3 = tk.Toplevel()

hao = {}
a3 = None
def zc2():
    # global 全局变量
    global hao
    if s3.get() not in hao:
        hao[s3.get()] = s4.get()
        messagebox.showinfo('成功', '注册成功')
        print(hao)
        a3.destroy()
    else:
        messagebox.showerror('提示', '账号已存在')


def zc():
    global a3
    a3 = tk.Toplevel()
    a3.title('注册页面')
    a3.geometry('500x500')
    a3.resizable(width=False , height=False)
    a3.iconbitmap('Tkinter/plum.ico')
    tk.Label(a3, text='账号: ', font=('微软雅黑', 20)).grid(row=1, column=1)
    tk.Entry(a3,textvariable=s3, font=('微软雅黑', 20)).grid(row=1, column=2)
    tk.Label(a3, text='密码: ', font=('微软雅黑', 20)).grid(row=2, column=1)
    tk.Entry(a3,textvariable=s4, font=('微软雅黑', 20)).grid(row=2, column=2)
    tk.Button(a3,command=zc2, text='确定注册',font=('微软雅黑', 20)).place(x=100, y=100)

tk.Button(a1,command=zc, width=5, text='注册', font=('微软雅黑', 20)).place(x=120, y=200)



a4 = tk.Tk()
a4.title('bibi')
a4.geometry('500x500')

# 创建主菜单
menu = tk.Menu(a4)
# 设置菜单名
menu.add_cascade(label='员工')
menu.add_cascade(label='员工2')


# 开启菜单栏
a4.config(menu=menu)

a4.mainloop()




# 10.开启窗口/主循环
a1.mainloop()




