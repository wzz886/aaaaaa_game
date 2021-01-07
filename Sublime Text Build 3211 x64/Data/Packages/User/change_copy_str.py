import sublime
import sublime_plugin

def get_lower_case_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)
    str = "".join(lst).lower()
    str = str.replace("_u_i", "_ui")
    return str

class ChangeCopyStrPanel(sublime_plugin.TextCommand):
    def run(self, edit):
        copy_str = sublime.get_clipboard()
        copy_str1 = get_lower_case_name(copy_str)
        self.view.run_command("insert_snippet",
            {
                "contents": "[\"%s\"] = self.%s,"%(copy_str1, copy_str)
            }
        )
