import datetime
import sublime_plugin
class AddInfoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents": "--[[""\n"
                "简介：${1:xxx}""\n"
                "Author：wzz""\n"
                "Date："  "%s"  %datetime.datetime.now().strftime("%Y-%m-%d") +"\n"
                "--]]"
            }
        )
        sublime.error_message("hello world")

