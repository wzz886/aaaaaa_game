# 复制调试，未完成版，不可提交
import os, shutil

path_lua_1 = r"D:\aaaaaa\debugScript\Debug"
path_lua_2 = r"D:\teon2-unity-client-poc\Assets\LuaScript\Debug"

path_c_1 = r"D:\aaaaaa\debugScript\UIEditorTool"
path_c_2 = r"D:\Teon2Client\Assets\Editor\UIEditorTool"


# 复制文件夹的内容到相应的文件夹
# from_path:从哪里复制
# to_path:复制到哪里
def copyDirs(from_path, to_path):
	for root, dirs, files in os.walk(from_path):
		if files:
			# 创建文件夹
			new_path = root.replace(from_path, to_path, 1)
			if not os.path.exists(new_path):
				os.makedirs(new_path)
		for file in files:
			new_path = root.replace(from_path, to_path, 1);
			new_path = os.path.join(new_path, file)
			print('{}  ->   {}'.format(os.path.join(root, file), new_path))
			shutil.copyfile(os.path.join(root, file), new_path)


def startCopy():
	print("-------------- 复制 开始 ")
	copyDirs(path_lua_1, path_lua_2)
	copyDirs(path_c_1, path_c_2)
	print("-------------- 复制 结束 ")

def startSave():
	print("-------------- 保存 开始 ")
	copyDirs(path_lua_2, path_lua_1)
	copyDirs(path_c_2, path_c_1)
	print("-------------- 保存 结束 ")


def deleteDirs(path):
	if os.path.exists(path):
		os.popen(f'rd /s /q {path}')
		print("删除：", path)
	
	

# 0为保存，从项目中保存到d盘debugScript
# 1为复制，从d盘debugScript复制到顶目
# 其它为删，从项目中删除，删除前会先保存到d盘
flag = -1
if (flag == 0):
	startSave()
elif (flag == 1):
	startCopy()
else:
	startSave()
	deleteDirs(path_lua_2)
	deleteDirs(path_c_2)
	print("-------------- 删除 结束 ")


