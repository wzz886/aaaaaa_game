
import shutil

# shutil 是高级的文件，文件夹，压缩包处理模块。


# 将文件内容拷贝到另一个文件中
#shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))
#shutil.copyfileobj(fsrc, fdst[, length])


# 拷贝文件
# shutil.copyfile(r"E:\桌面文件\python 3 Tool\learn_shutil.py", r"E:\桌面文件\python 3 Tool\learn_shutil_copy.py")

# 拷贝文件和权限
#shutil.copy(src, dst)


# 拷贝文件和状态信息
#shutil.copy2(src, dst)



# 递归的去删除文件夹 (不存在就报错)
#shutil.rmtree(r"E:\桌面文件\python 3 Tool\ddd")


# 拷贝目录，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
# shutil. copytree(src，dst，symlinks=False，ignore=None，copyfunction=copy2，ignore_dangling_symlinks=False)
# shutil.copytree(src="11", dst="22")
