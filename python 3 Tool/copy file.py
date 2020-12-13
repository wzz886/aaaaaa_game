


####################################################
## 作用：复制文件夹中所有的内容到新的文件夹
####################################################

# print(" 复制 开始 ")
# import os, shutil
# path1 = r"F:\Unity  Learn\GameFrame\Assets\Editor"
# path2 = r"F:\Unity  Learn\GameFrameNew\Assets\Editor"

# # 要排除的文件类型
# exclude_ext = {".meta" : True}
# for root, dirs, files in os.walk(path1):
# 	if files:
# 		# 创建文件夹
# 		new_path = root.replace(path1, path2, 1)
# 		if not os.path.exists(new_path):
# 			os.makedirs(new_path)
# 	for file in files:
# 		file_ext = os.path.splitext(file)[1]
# 		if exclude_ext.get(file_ext):
# 			continue;
# 		new_path = root.replace(path1, path2, 1);
# 		new_path = os.path.join(new_path, file)
# 		print('{}  ->   {}'.format(os.path.join(root, file), new_path))
# 		shutil.copyfile(os.path.join(root, file), new_path)
# print(" 复制 结束 ")

####################################################


####################################################
## 作用：复制单个文件
####################################################

# print(" 复制 开始 ")
# import os, shutil
# path1 = r"F:\Unity  Learn\GameFrame\Assets\Scripts\Framework\AssetBundle\AsyncOperation\ResourceWebRequester.cs"
# path2 = r"F:\Unity  Learn\GameFrameNew\Assets\Scripts\Framework\AssetBundle\AsyncOperation\ResourceWebRequester.cs"

# # 创建文件夹
# new_path = path1.replace(os.path.dirname(path1), os.path.dirname(path2), 1)
# if not os.path.exists(os.path.dirname(new_path)):
# 	os.makedirs(os.path.dirname(new_path))

# shutil.copy2(path1, path2)
# # shutil.copyfile(path1, path2)
# print('{}  ->   {}'.format(path1, path2))
# print(" 复制 结束 ")

#################################################### 


####################################################
## 作用：删除文件夹中，相应类型的文件
####################################################

# print(" 删除 开始 ")
# import os, shutil
# path = r"F:\有用的软件\工作环境需要\脚本"

# # 要删除的文件类型
# exclude_ext = {".meta" : True}
# for root, dirs, files in os.walk(path):
# 	for file in files:
# 		file_ext = os.path.splitext(file)[1]
# 		if exclude_ext.get(file_ext):
# 			os.remove(os.path.join(root, file))
# 			print('删除文件->{}'.format(os.path.join(root, file)))
print(" 删除 结束 ")

####################################################

