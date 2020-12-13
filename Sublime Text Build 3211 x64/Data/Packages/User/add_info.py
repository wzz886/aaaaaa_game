import datetime
import sublime_plugin
class AddInfoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents": "%s"%datetime.datetime.now().strftime("%Y-%m-%d")
            }
        )
        sublime.error_message("Add Time")

