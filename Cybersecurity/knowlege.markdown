# Inside a Computer System  计算机系统内部

1.Motherboard(主板) ———— 主板就像我们身体的骨骼和神经系统。它将所有不同的组件固定在一起，并将它们连接起来。在一块典型的台式机主板上，你会看到用于安装各类组件的不同接口——CPU 插槽、RAM 插槽、扩展插槽以及各种端口。其他所有组件都会插入主板，或通过主板进行连接。下图展示了一块典型的台式机主板。

![主板](/Cybersecurity/Computer_System_png/Motherboard.png)

2.CPU(中央处理器) ———— CPU（中央处理器，Central Processing Unit），通常称为处理器，可以类比为我们大脑的一部分。就像我们的大脑不断执行各种指令（如做加法、把牛奶倒进碗里等）一样，CPU 也会为计算机执行各种指令。现代 CPU 通常拥有多个核心，能够并行处理指令。CPU 通过 CPU 插槽连接到主板。下图展示的是一款典型的台式机 CPU。

![CPU](/Cybersecurity/Computer_System_png/CPU.png)

3.RAM(随机存取存储器) ———— RAM（随机存取存储器，Random Access Memory）可比作我们大脑中的短期记忆或工作记忆。当处理一项任务时，我们会暂时将相关信息保留在脑海中。RAM 的作用也是如此——它保存着 CPU 需要快速访问的数据。RAM 是易失性存储器：一旦断电，其中的所有内容都会

![RAM](/Cybersecurity/Computer_System_png/RAM.png)

4.Storage (SSD/HDD)(存储设备(SSD/HDD)) ———— 固态硬盘（SSD）和机械硬盘（HDD）都是存储设备，可类比于我们的长期记忆。就像美好的回忆会被永久记住一样，数据也会长期保存在存储设备中。HDD 使用较旧的技术，内部有移动部件，因此性能受到限制。SSD 没有移动部件，而是使用存储芯片，因此速度要快得多。HDD 仍然因其容量大、成本低而广受欢迎。存储设备可通过 SATA 数据线或 PCI Express 插槽连接。下图左侧显示的是一块 HDD，右侧显示的是一块 SSD。

![SSD/HDD](/Cybersecurity/Computer_System_png/Storage(SSD&HDD).png)

5.Network Adapter(网络适配器) ———— 就像我们使用声带与周围环境交流一样，网络适配器让计算机能够与其他系统通信。网络适配器分为无线和有线两种。它们通常集成在主板上，但也可以作为扩展卡添加。网络适配器通常通过 PCI Express 接口连接。下图展示的是一种插接式网络适配器，通常用于台式计算机。

![网络适配器](/Cybersecurity/Computer_System_png/Network_Adapter.png)

6.Power Supply (PSU)(电源供应器(PSU)) ———— 每个系统都需要电力。就像我们的心脏将血液泵送到身体各个器官一样，PSU（电源供应器）为所有系统组件提供能量。PSU 至关重要，需要仔细考虑——如果组件所需的功率超过 PSU 能够提供的功率，系统将会失效。PSU 从电源插座获取电力，并通过各种连接器进行分配，例如主板主电源连接器和 Molex 连接器。下图展示了台式电脑中使用的 PSU。
![电源供应器(PSU)](/Cybersecurity/Computer_System_png/Power_Supply(PSU).png)

7.Graphics Card(显卡) ———— 显卡可以类比为我们大脑中的视觉皮层。我们的眼睛获取信息，而视觉皮层将这些信息处理成图像。类似地，显卡接收来自操作系统和程序的信息，然后将处理后的视觉数据输出到显示器。显卡连接到主板上的 PCI Express 插槽。下图展示了一款现代台式电脑使用的显卡。
![显卡](/Cybersecurity/Computer_System_png/Graphics_Card.png)

8.Input/Output(输入/输出) ———— 就像我们拥有感官来获取信息，供大脑处理并据此采取行动一样，计算机也有输入和输出设备。输入设备包括键盘、麦克风、鼠标和扫描仪。输出设备包括显示器、打印机和扬声器。这些外围设备常用的连接器包括 USB、HDMI 和 DisplayPort。下图展示了一些基本的输入/输出（I/O）设备。
![Input/Output](/Cybersecurity/Computer_System_png/Input&Output.png)

# 组件图
![组件图](/Cybersecurity/Computer_System_png/Components.png)


第一步：按下电源按钮（Press the Power Button）

当我们按下计算机系统的电源按钮时，一个信号会发送到 PSU（Power Supply Unit，电源供应器），使电源开始向电脑供电。

可以把这想象成我们睡觉时身体处于关闭状态。当我们醒来并吸入氧气后，身体开始输送血液，整个身体便开始“启动”。

⸻

第二步：固件启动（Firmware Starts）

继续沿用第一步中的比喻。当身体开始运作后，我们的核心器官已经开始工作，但大脑还没有完全恢复意识。

和人体一样，计算机系统中也包含一种称为**固件（Firmware）**的软件，它负责让所有硬件组件启动。

负责管理这一过程的核心系统称为 UEFI（Unified Extensible Firmware Interface，统一可扩展固件接口）。

**注意：**你经常会看到 BIOS 这个术语，而不是 UEFI。BIOS 的作用与 UEFI 基本相同，只不过现在大多数情况下已经被 UEFI 所取代。

⸻

第三步：开机自检（Power-On Self Test）

现在身体已经开始运作，接下来要检查身体各部分是否都正常工作。如果有任何异常，就会发出警报信号。

计算机也是一样。

UEFI 加载的程序之一就是 Power-On Self Test（POST，开机自检），它会检查所有必需的硬件是否存在、是否配置正确，以及是否能够正常工作。

⸻

第四步：选择启动设备（Select Boot Device）

当我们的身体已经正常启动、配置正确并且功能完全正常后，身体就会寻找启动意识的位置，使我们真正恢复意识。

计算机系统也是如此。

UEFI 内部保存着一个**启动顺序（Boot Order）**列表，它会按照优先级依次查找哪个设备中包含操作系统的启动程序。

⸻

第五步：启动引导程序（Initiate Bootloader）

现在系统已经知道了我们大脑中负责意识的部分所在的位置，于是它开始执行“加载程序”，使意识真正启动。

计算机系统也遵循类似的过程。

在所选定的启动设备上，**Bootloader（启动引导程序）**会被启动。

Bootloader 会把操作系统从所选的启动设备加载到**随机存取内存（RAM，Random Access Memory）**中。

当操作系统成功加载完成后，UEFI 就会将计算机各个硬件组件的控制权交给操作系统。

![开机步骤](/Cybersecurity/Computer_System_png/step.png)