print("学习sublime 插件")

'''
教程
http://www.sublimetext.cn/docs/3/api_reference.html#sublime.View

Packages/Default/delete_word.py删除光标左侧或右侧的单词
Packages/Default/duplicate_line.py复制当前行
Packages/Default/exec.py使用幻像显示内联错误
Packages/Default/font.py显示如何使用设置
Packages/Default/goto_line.py提示用户输入，然后更新选择
Packages/Default/mark.py使用add_regions()将图标添加到装订线
Packages/Default/show_scope_name.py使用弹出窗口显示插入符号的范围名称
Packages/Default/trim_trailing_white_space.py在保存之前修改缓冲区
Packages/Default/arithmetic.py通过命令选项板运行时接受来自用户的输入

#光标处插入内容
point = self.view.sel()[0].a
self.view.insert(edit, point, "Hello, World!")

#复制选中内容
for region in self.view.sel():
	self.view.insert(edit, region.begin(), self.view.substr(region))

# 获取页面内容
self.view.substr(sublime.Region(0, self.view.size()))

# 获取配置信息
settings = sublime.load_settins("Preferences.sublime-settings")

#弹出式的窗口
sublime.error_message("hello world")

#在状态栏中显示消息
#win.status_message(string)	

#启动相应程序
import os
exeFile = "E:/Old/client/simulator/win32/jqKing.exe"
exePath = "E:/Old/client"
os.chdir(exePath)
os.startfile(exeFile)

#在文件尾列出，所有正在打开的文件路径
for win in sublime.windows():
	win.status_message("---------------")
	for view in win.views():
		file_name = view.file_name()
		str_file = str_file + repr(file_name) + '\n'
self.view.insert(edit, self.view.size(), str_file)


'''
