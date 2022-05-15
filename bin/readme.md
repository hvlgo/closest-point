## 文件结构

* src
  * closest_point_gui.py
  * closest_point.py
  * MyWidget.py
  * Ui_untitled.py
* bin
  * requirement.txt
  * readme.md
* report.pdf
* hw3.pdf

## 各个文件的作用

closest_point_gui.py : 实现了图形界面，用命令 python closest_point_gui.py 即可运行GUI。MyWidget.py 和 Ui_untitled.py 是类文件，无需运行

GUI交互方式，点击窗口内的任何地方会在对应的地方画出一个点。当窗口中点的个数大于1个时，点击calculate会计算出当前屏幕中最近的点对，并将他们标红且连接起来。点击clear会清空屏幕中的所有点

closest_point.py : 实现了两种算法的命令行式程序。用命令python closest_point.py即可运行程序。默认n = 5000。可以使用命令python closest_point.py n 来指定运行时n的大小。默认两种算法都会执行，若要测试某种算法可在main函数中注释掉naive_closest_point()或者divide_closest_point()

hw3.pdf是第二题的证明，report.pdf是实验报告