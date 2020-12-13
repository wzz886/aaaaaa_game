#功能：自动去掉行尾空格

import os
import sublime
import sublime_plugin

#用法两种只能选一种
#-----------------------------------------
#用法一，根据配置文件，在保存时，自动去尾空格
#-----------------------------------------
'''
#需要尾格去空格的文件类型
NEED_TRIM_SPACE_FILE = {".lua":True}

#去掉文件空格
def trimSpace(self, edit):
	trailing_white_space = self.view.find_all("[\t ]+$")
	trailing_white_space.reverse()
	file_name = self.view.file_name()
	if NEED_TRIM_SPACE_FILE[os.path.splitext(file_name)[1]]:
		for r in trailing_white_space:
			self.view.erase(edit, r)

class TrimSpaceOnSaveCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		trimSpace(self, edit)

class OnSaveListener(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		view.run_command("trim_space_on_save")

'''
#-----------------------------------------
#用法二，设相应快键启动
#如：{ "keys": ["ctrl+shift+s"], "command": "trim_space_on_save" },
#-----------------------------------------

def saveAll():
	sublime.active_window().run_command("save")

#去掉文件空格
def trimSpace(self, edit):
	trailing_white_space = self.view.find_all("[\t ]+$")
	trailing_white_space.reverse()
	for r in trailing_white_space:
		self.view.erase(edit, r)

	sublime.set_timeout(saveAll, 100)

class TrimSpaceOnSaveCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		trimSpace(self, edit)

