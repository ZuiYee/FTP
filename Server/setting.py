import sys
sys.path.append("..")
import GetIp


ip = GetIp.get_host_ip()

port = 21

path = 'G://steam'

# 上传速度
max_upload = 500 * 1024  # 500Kb/s

# 下载速度
max_download = 500 * 1024  # 500Kb/s

# 最大连接数
max_cons = 150

# 最多IP数
max_per_ip = 10

# 被动端口范围，注意被动端口数量要比最大IP数多，否则可能出现无法连接的情况
passive_ports = (2000, 2200)

# 是否开启匿名访问 on|off
enable_anonymous = 'on'

# 匿名用户目录
# anonymous_path = '/home/huangxm'

# 是否开启日志 on|off
enable_logging = 'on'

# 日志文件
logging_name = 'pyftp.log'

# 欢迎信息
welcome_msg = 'Welcome to my ftp'


