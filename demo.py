#
# 1．添加主程序入口，完成如下任务：
# （1）在当前目录打开名为“文件测试数据“文本文件。
# ①提示，文件后缀是txt。
# ②提示，如果文件中有中文，需要指定编码格式。
# （2）创建并打开以今天日期命名的文件。
# （3）将名为“文件测试数据“文本文件中的内容按照行的方式复制到以今天日期命名的文件中。
# ①提示，使用for循环。
# （4）关闭文件。
# ①提示，所有打开的文件都需要关闭。
# ②提示，先打开的文件，后关闭。
# （5）正确处理在程序中可能发生的错误或异常。
# ①提示，异常处理结构要完整。
# ②提示，异常的提示信息要和错误、异常相符。
#

from datetime import date

#添加主程序入口
if __name__ == '__main__':

    #异常处理
    try:

        f1 = None

        f2 = None

        #在当前目录打开名为“文件测试数据“文本文件
        f1 = open('文件测试数据.txt','rt',encoding='utf-8')

    except FileNotFoundError as e:

        print(e)

    else:

        filename = str(date.today()) + '.txt'

        lines = f1.readlines()

        #创建并打开以今天日期命名的文件
        f2 = open(filename,'wt',encoding='utf-8')

        for line in lines:

            f2.write(line)

    finally:

        if f2:

            f1.close()

        if f1:

            f2.close()


