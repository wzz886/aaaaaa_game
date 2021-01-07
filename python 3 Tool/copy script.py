import time, os, shutil

save_path_root = r"D:\saveScript"
copy_root = r"D:\Teon2Client\Assets"
copy_dirs = ("Editor", "LuaScript", "Script")

def saveScript():
	save_path = os.path.join(save_path_root, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
	if not os.path.exists(save_path):
		os.makedirs(save_path)
		print(f"创建新文件夹:{save_path}")

	exclude_ext = {".meta" : True}
	for str in copy_dirs:
		for root, dirs, files in os.walk(os.path.join(copy_root, str)):
			new_path = root.replace(copy_root, save_path, 1)
			# 创建文件夹
			if not os.path.exists(new_path):
				os.makedirs(new_path)
			for file in files:
				file_ext = os.path.splitext(file)[1]
				if exclude_ext.get(file_ext):
					continue;
				shutil.copyfile(os.path.join(root, file), os.path.join(new_path, file))

		print(f"已复制：{str}")


def deleteScript():
	save_num = 20
	print(f"只保留前{save_num}条")
	delete_dirs = os.listdir(save_path_root)
	delete_dirs.reverse()
	for i in range(save_num, len(delete_dirs)):
		path = os.path.join(save_path_root, delete_dirs[i])
		os.popen(f'rd /s /q {path}')
		# os.popen(f'del /F /S /Q {path}')
		print("删除：", path)


print(" ==========复制 开始===========")
saveScript()
print(" ==========复制 结束===========")

# print(" ==========删除 开始===========")
# deleteScript()
# print(" ==========删除 结束===========")
