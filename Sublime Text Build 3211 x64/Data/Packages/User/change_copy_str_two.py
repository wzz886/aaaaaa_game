import sublime
import sublime_plugin

# 将大写字母转小写，差加上空格
def get_lower_case_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append(" ")
        lst.append(char)
    str = "".join(lst).lower()
    str = str.replace(" u i", " ui ")
    return str

class ChangeCopyStrTwoPanel(sublime_plugin.TextCommand):
    def run(self, edit):
        copy_str = sublime.get_clipboard()
        copy_str1 = get_lower_case_name(copy_str)
        self.view.run_command("insert_snippet",
            {
                "contents": "%s" % copy_str1
            }
        )
