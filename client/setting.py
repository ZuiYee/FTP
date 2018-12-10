import sys
sys.path.append("..")
import GetIp

ip = GetIp.get_host_ip()

port = 21

# 设置缓冲区大小
buffsize = 1024