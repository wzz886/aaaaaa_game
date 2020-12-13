import sublime, sublime_plugin
# 打开选中文本对应的文件

class SelectionSymbolPanel(sublime_plugin.TextCommand):
	def run(self, edit):
		wdw = self.view.window()
		sels = self.view.sel()

		astr = ""
		sels = self.view.sel()

		for sel in sels:
			astr = self.view.substr(sel)

		if not astr:
			astr = ""
		astr = "#" + astr
		self.view.run_command("copy")
		wdw.run_command("goto_symbol_in_project")
		wdw.run_command("paste")
