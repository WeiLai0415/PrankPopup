# 整蛊程序
> 作者：WeiLai0415  


## 安装模块
本程序仅需一个第三方模块：*PyQt5*

## 效果预览
本程序的效果是不断在电脑屏幕随机位置生成随机的写有某些话的窗口，其中每个窗口中有存在5秒的状态栏，提示用户可以通过重启电脑或杀死进程结束程序。  
运行效果如下图所示
![](https://s3.bmp.ovh/imgs/2021/09/cc1c6bd13aaa7e45.jpg)

***
## 更改程序运行效果
可以通过更改设置文件(`settings.wl`)更改运行效果：  

用文本编辑器(如*Notepad*，*VS code*等)打开`settings.wl`。  

- 第一行为窗口的标题(默认为`整蛊程序`)；
- 第二行为显示的文本(默认为`['Hello!', '你好！']`)，程序将使用Python的`random.randomchoice`方法选择每个窗口的文本。语法格式如下。
  + 内容被一对英文半角中括号`[]`包裹
  + 要显示的内容用英文半角双引号`""`，或单引号`''`(当然也可以两者兼而有之)包裹
  + 不同的内容之间用英文半角逗号`,`连接，最好后面加一个空格` `。
    - 注：最后一项不用以`,`结尾
- 第三行为文本的颜色，默认为`['#E58606', '#5D69B1', '#52BCA3', '#99C945', '#CC61B0', '#24796C', '#DAA51B', '#2F8AC4', '#764E9F', '#ED645A']`，程序将使用*Python*的`random.randomchoice`方法选择每个窗口标签的颜色。
  + 语法格式同上
  + 可以为颜色名称或16进制色号(如`['red', 'BlueViolet']`和`['#764E9F', '#ED645A']`都是合法的)

若编辑错误也不会报错，程序会自动修改(如果语法错误，则修改为默认值；若发生值错误(如输入颜色错误)，则由*Qt*自动修改。)
***
## 关闭程序
现在介绍如何关闭程序：
- 最简单的方法毫无疑问是重启计算机，这里不再赘述了。
- 还可以打开*Windows*任务管理器(快捷键：`Ctrl+Shift+Esc`)后找到本程序，选择结束任务。(如图所示)
- ![](https://s3.bmp.ovh/imgs/2021/09/14a9593e6eec8de8.jpg)

***
【注】此程序纯属娱乐，请勿用于非法或给其他人造成困扰的用途！
