#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-13 上午10:28

# Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，
# 默认的日志级别设置为WARNING
# 日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# 默认的日志格式为日志级别：Logger名称：用户输出消息。

import logging

# 配置非默认情况 level：等级，format：输出格式，datefmt：时间格式化，filename：文件名
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/tmp/test.log',
                    filemode='w')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

# filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），
#               这样日志会被存储在指定的文件中。没有filename参数时默认输出在输出框中
# filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
# format：指定handler使用的日志显示格式。
# datefmt：指定日期时间格式。
# level：设置rootlogger（后边会讲解具体概念）的日志级别
# stream：用指定的stream创建StreamHandler。
#       可以指定输出到sys.stderr,sys.stdout或者文件(f=open('test.log','w'))，默认为sys.stderr。
#           若同时列出了filename和stream两个参数，则stream参数会被忽略。

# format参数中可能用到的格式化串：
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息

