## WLS安装Ubuntu环境

win11通过wsl2进行安装ubuntu并进行开发

- 查看系统名称和版本 确保是wls版本2  
wsl -l -v

- 导出配置，这样就能像虚拟机一样进行系统备份
wsl --export Ubuntu d:\wsl_save\wls2_ubuntu2204.tar

- 恢复配置

  wsl --import Ubuntu d:\wsl_save\wls2_ubuntu2204.tar



## BOOFUZZ

boofuzz安装，参考[官方安装指导](https://github.com/jtpereyda/boofuzz/blob/master/INSTALL.rst)

1.python3.7以上的运行环境，推荐使用ubuntu22.04

sudo apt-get install python3-pip python3-venv build-essential

2.建立boofuzz的虚拟python环境，单独配置一个python环境，因为这样boofuzz升级就比较好处理，重新生成一个虚拟环境即可

```
mkdir boofuzz && cd boofuzz
python3 -m venv env
source env/bin/activate #去激活deactivate命令
```

3.升级安装pip和setuptools工具，保证boofuzz源码安装成功

```
pip install -U pip setuptools
```

4.下载[boofuzz最新源码安装](https://github.com/jtpereyda/boofuzz)，如更新boofuzz源码，重新编译安装即可

```
cd boofuzz-master
pip install -e .[dev]
```

5.编写测试套，python代码可以import boofuzz



- boofuzz和peach pro的模糊测试工具区别：

1.无法对接收报文进行针对性处理。

2.没有数据建模封装，每条消息都要单独写。

3.fuzz只能限制发送多条报文的依赖关系，通过一颗依赖树进行设置