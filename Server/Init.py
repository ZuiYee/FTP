from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
import logging
import setting


def myFtpServer():

    # 实例化用户
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', 'password', setting.path, perm='elradfmwMT')  # 添加用户 参数:username,password,允许的路径,权限

    if setting.enable_anonymous == 'on':
        authorizer.add_anonymous('G://steam')  # 允许匿名用户
    # authorizer.add_anonymous('/home/nobody')

    # 下载上传速度设置
    dtpHandler = ThrottledDTPHandler
    dtpHandler.read_limit = setting.max_download
    dtpHandler.write_limit = setting.max_upload

    # 实例化FTP
    handler = FTPHandler
    handler.authorizer = authorizer

    # 日志记录
    if setting.enable_logging == 'on':
        logging.basicConfig(filename=setting.logging_name, level=logging.INFO)

    # 欢迎信息
    handler.banner = setting.welcome_msg

    # 添加被动端口范围
    if setting.passive_ports:
        handler.passive_ports = range(setting.passive_ports[0], setting.passive_ports[1])

    # handler.masquerade_address = '151.25.42.11'  # 伪装ip地址

    address = (setting.ip, setting.port)  # FTP使用端口
    server = FTPServer(address, handler)  # FTP服务器实例

    # 连接限制
    server.max_cons = setting.max_cons
    server.max_cons_per_ip = setting.max_per_ip

    # 开启服务器
    server.serve_forever()


if __name__ == '__main__':
    myFtpServer()



