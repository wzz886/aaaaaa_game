import sublime, sublime_plugin
# 打开选中文本对应的文件

class SelectionOpenPanelCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        wdw = self.view.window()
        sels = self.view.sel()
        astr = ""
        for sel in sels:
            astr = self.view.substr(sel)

        jidx = astr.find("#")
        if jidx < 0:
            wdw.run_command("show_overlay",{"overlay": "goto", "text": astr, "show_files":True})
        else:
            wdw.run_command("copy")
            wdw.run_command("show_overlay",{"overlay": "goto", "text": "", "show_files":True})
            wdw.run_command("paste")
