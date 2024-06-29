import os

# 获取指定路径下所有指定后缀的文件
# dir 指定路径
# ext 指定后缀，链表&不需要带点 或者不指定。例子：['xml', 'java']
def GetFileFromThisRootDir(dir, ext=None):
    allfiles = []
    needExtFilter = (ext != None)
    for root, dirs, files in os.walk(dir):
        for filespath in files:
            filepath = os.path.join(root, filespath)
            extension = os.path.splitext(filepath)[1][1:]
            if needExtFilter and extension in ext:
                allfiles.append(filepath)
    return allfiles

if __name__ == '__main__':
    srcDir = "/Users/deltaqin/PycharmProjects/pythonProject/img"
    imgFiles = GetFileFromThisRootDir(srcDir, ['png'])
    suffix = "_temp.png"
    for f in imgFiles:
        print(os.path.getsize(f))
        if os.path.getsize(f) > 102400:
            cmd = "\"pngquant\"" + " --ext " + suffix + " --quality 50-50 " + f
            print(cmd)
            os.system(cmd)
            os.remove(f)
            newfile = f.replace(".png", suffix)
            os.rename(newfile, f)


