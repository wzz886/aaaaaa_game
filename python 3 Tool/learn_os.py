import os,shutil

# 创建目录(上级目录不存在就报错)
#os.mkdir(r"os create01\os create 02")

# 创建目录(上级目录不存在就创建，目录已存在就报错)
path = r"os create01\os create 02"
if os.path.exists(path):
	father_path=os.path.abspath(os.path.dirname(path)+os.path.sep+".")
	shutil.rmtree(father_path)
else:
	os.makedirs(path)
