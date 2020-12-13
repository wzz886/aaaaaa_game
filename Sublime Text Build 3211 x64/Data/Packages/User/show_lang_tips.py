#功能：鼠标停在_L(127016)上时，显示lang.lua中127016对应的文本
#注意：lang.lua文件必须打开才能正确显示（有待修改）

import os, re
# import chardet
import sublime
import sublime_plugin

# 目标所在的目录
TAGET_DIR = "localization"

# 目标文件名
TAGET_FILE = "lang.lua"

# 获取目标文件路径
def getLangFilePath():
	path = ""
	active_win = sublime.active_window()
	for folder in active_win.folders():
		basename = os.path.basename(folder)
		if basename == TAGET_DIR:
			path = os.path.join(folder, TAGET_FILE)
			break
		if basename == "src":
			path = os.path.join(folder, TAGET_DIR, TAGET_FILE)
			break
	return path

#判断是否是_L(+数字 类型
def isLangNumber(word_str, line_str):
    tab = re.findall(r"\D", word_str)
    if len(tab) == 0 and len(word_str) > 0 :
    	tab = re.findall(r"_L\s*\(\s*" + word_str, line_str)
    	if len(tab) > 0 :
    		return True

    	tab2 = re.findall(r"_F\s*\(\s*" + word_str, line_str)
    	if len(tab2) > 0 :
    		return True

    return False

'''
chardet导入使用不了
import chardet
def findWold(word_str):
	path = getLangFilePath()
	if not os.path.exists(path):
		return "0"
	word_str = "0"
	with open(path, "rb") as f:
		file_data = f.read()
		file_info = chardet.detect(file_data)
		file_encoding = file_info['encoding']
		file_data = file_data.decode(file_encoding)
		search_obj = re.search(r"\[\s*" + key + r"\s*\]\s*=s*.+,", file_data)
		if search_obj:
			word_str = search_obj.group(0)
	return word_str
'''

#只能打开lang.lua才能查到，很烦，有待修改
def findWold(word_str):
	str_file = word_str
	point = [0, 0]
	for win in sublime.windows():
		for view in win.views():
			if os.path.basename(view.file_name()) == TAGET_FILE:
				region = view.find(r"\[\s*" + word_str + r"\s*\]\s*=s*.+,", 0)
				if region:
					str_file = view.substr(region)
					point = view.rowcol(region.begin())
				else:
					str_file = "并没有此key:" + word_str
				break
		else:
			str_file = "没有打开【" + TAGET_FILE + "】点击打开"

	return [str_file, point]

class ShowLangTipsCommand(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
        def on_navigate(href):
            view.window().open_file(
                href,
                sublime.ENCODED_POSITION | sublime.FORCE_GROUP)

        word_str = view.substr(view.word(point))
        line_str = view.substr(view.line(point))
        if not isLangNumber(word_str, line_str) or word_str == "":
        	return

        tab = findWold(word_str)
        path = getLangFilePath()
        href = path + ":" + str(tab[1][0] + 1) + ":" + str(tab[1][1])
        body = "<body><a href=%s>%s</a></body>" % (href, tab[0])

        view.show_popup(
            body,
			flags       = sublime.HIDE_ON_MOUSE_MOVE_AWAY,
			location    = point,
			on_navigate = on_navigate,
			max_width   = 1024)

class ShowLangTipsSelectCommand(sublime_plugin.TextCommand):
    def on_hover(self, edit):
    	# self.view.sel()
        view.show_popup(
            "astr",
			flags       = sublime.HIDE_ON_MOUSE_MOVE_AWAY,
			location    = point,
			on_navigate = on_navigate,
			max_width   = 1024)

  #   	self.view.sel()
		# astr = ""
		# for sel in sels:
		# 	astr = view.substr(sel)




#_F(140048) 鼠标停在这里测试

