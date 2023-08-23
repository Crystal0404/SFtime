# SFtime



## 介绍



SFtime是一个基于[pycqbot](https://github.com/FengLiuFeseliud/pycqBot)开发的插件，可以从菠萝包获取作者更新时间，并转发到qq群。

在开始安装使用这个插件前，你需要了解一些关于pycqbot的基础知识，并成功启动一个pycqbot机器人。



## 插件的安装



1. 从本仓库下载SFtime.py，并且按照[pycqbot文档](https://fengliufeseliud.github.io/pycqBot/)将文件放于正确的插件文件夹

2. 查询插件依赖是否完整，你可以在cmd中用以下命令查询依赖列表(本插件依赖requests、beautifulsoup4、lxml)

```
pip list
```

3. 使用以下对应命令安装缺少的依赖(下载速度慢可以自行百度如何使用清华大学的pypi源)

```
pip install requests
pip install beautifulsoup4
pip install lxml
```

4. 正确编辑配置文件，配置文件内容如下(务必注意yaml语法中的空格不能用tab代替)

```yaml
SFtime:
  group1:
    group_id: ''
    name: ''
    url: ''
```

  如何添加多个群聊以及正确编写示例

```yaml
SFtime:
  group1:
    group_id: '11111111' #群号
    name: '这是作者的名字'
    url: 'https://book.sfacg.com/Novel/5555555' #这是作品的网页链接
  group2:
    group_id: '2222222'
    name: '张三'
    url: 'https://book.sfacg.com/Novel/6666666'
```

5. 按照pycqbot的文档将插件载入插件列表



## 插件的使用



在群聊中发送#time即可获取上次更新时间等信息



## 注意事项



暂时只能一个群聊绑定一本书
