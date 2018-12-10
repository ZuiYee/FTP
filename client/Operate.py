from ftplib import FTP
import setting


def ftpConnect(username, password):
    ftp = FTP()
    # 打开调试级别2，显示详细信息
    # ftp.set_debuglevel(2)
    ftp.connect(setting.ip, setting.port)
    ftp.login(username, password)  # 登录FTP服务器
    return ftp


def downloadFile(ftp, remotePath, localPath):  # 从FTP服务器下载文件
    filepath = open(localPath, 'wb')
    ftp.retrbinary("RETR" + remotePath, filepath.write, setting.buffsize)  # 1024字节一个块
    ftp.set_debuglevel(0)
    filepath.close()


def uploadFile(ftp, remotePath, localPath):
    filepath = open(localPath, 'rb')
    ftp.storbinary('STOR' + remotePath, filepath, setting.buffsize)
    ftp.set_debuglevel(0)
    filepath.close()


if __name__ == '__main__':
    # 登录服务器
    ftp = ftpConnect("user", "password")
    # 下载文件
    downloadFile(ftp, ' text.txt', r"G:\text.txt")
    # 上传文件
    uploadFile(ftp, ' text1.txt', r"G:\text1.txt")
    # 打印欢迎信息
    # print(ftp.getwelcome())
    # 获取当前路径
    # pwdPath = ftp.pwd()

    # 显示目录下所有目录信息
    # ftp.dir()

    # 设置FTP当前操作的路径
    # ftp.cwd(path)

    # 返回一个文件名列表
    # filenameList = ftp.nlst()

    # 新建远程目录
    # ftp.mkd('目录名')

    # 删除远程目录
    # ftp.rmd('目录名')

    # 删除远程文件
    # ftp.delete('文件名')

    # 将oldName修改名称为newName
    # ftp.rename('oldName', 'newName')

