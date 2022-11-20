​@[TOC](win11 BurpSuit pro v2022.11.1安装使用教程)​

1.通过[吾爱破解](https://www.52pojie.cn/thread-1544866-1-1.html)的网盘下载burpsuit文件(BurpSuite V2022.11.1.zip)，文件是通过本地破解pro证书实现的，需要搭配burpsuit的JAR版本进行使用。通过java命令进行启动，而非exe启动。

- 压缩包内已burpSuit文件夹下的burpsuite_pro_org.jar就是官方的BurpSuit的[JAR格式官方文件](https://portswigger.net/burp/releases)，可以自行下载并修改文件名替换升级。
- EN-JRE Burp.bat是英文版启动脚本，是通过java启动执行的，故需要提前安装jdk17，java8目前该破解版不支持。*参考第二步java安装教程。*

![在这里插入图片描述](https://img-blog.csdnimg.cn/8dc30f5797c8432ca53b24b104b2d1cd.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/0665a4272694410b9601acb03f0ae841.png)


2.安装依赖环境jdk17
因为软件已经不支持java8，可以直接从官网下载jdk17，并执行安装。
https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe
![在这里插入图片描述](https://img-blog.csdnimg.cn/9fccb14843d1431286339738226cf724.png)
在windows cmd命令行中，执行如下命令能看到java版本，表示安装成功。

```bash
java -version
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/b948af58bf9e4373b4769ddbb27c6cac.png)

3.破解流程
双击执行EN-JRE Burp.bat，勾选忽略升级，点击run按钮，会弹出BurpSuit激活界面，将破解软件的license内容粘贴到激活界面。
![在这里插入图片描述](https://img-blog.csdnimg.cn/bc17beda01014017ae9171ba276ddf15.png)
激活步骤第3步:复制证书到激活页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/6abcc3b450cb448893f95aed51216855.png)
点击手动激活即可
![在这里插入图片描述](https://img-blog.csdnimg.cn/4212dc6273024dc194ca5299b10c979d.png)
复制request到破解软件页面，并把生成的激活响应码粘贴到激活页面，点击下一步
![在这里插入图片描述](https://img-blog.csdnimg.cn/fda7cdfeeb4b402287d39f96885464f6.png)
提示激活成功，可以临时工程和默认配置开始使用，至此，破解过程完成。
![在这里插入图片描述](https://img-blog.csdnimg.cn/f9da20d8471f465e8d1c286da98c898c.png)
