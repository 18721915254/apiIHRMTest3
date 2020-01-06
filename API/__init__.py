import  app
import  logging

#初试化日志
#为撒怎么要做init中初始化日志
#这是因为 我们后面进行接口测试 都会调用封装的API接口 调用时 会自动运行 init函数 初始化日志器 从而实现自动初始化日志的功能

app.init_logging()

logging.info("阔以正常工作")