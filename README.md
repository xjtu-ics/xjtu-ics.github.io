# 概述  

这里是西安交通大学ICS课程的主页，只有西安交通大学ICS团队的成员可以编辑此页面。  

如果您对西安交通大学课程主页有更好的设计想法，欢迎联系XJTU ICS团队并提交您的pull request。

# 团队成员使用指南

网页构建使用`github action`作为自动化构建工具，因此只需要将修改后的内容push到远程仓库即可对网站进行修改。

建议在对网页修改前在本地预览效果，本网页使用[mkdocs-material](https://squidfunk.github.io/mkdocs-material/)框架构建。

本地环境配置命令如下：
```bash
pip install mkdocs-material mkdocs-open-in-new-tab mkdocs-macros-plugin pandas tabulate mike
```

本地预览命令如下：
```bash
mkdocs serve
```

## 添加助教个人资料  

按照以下格式创建一个JSON文件填写您的个人信息。  

```json  
{  
    "homepage_url": "https://example.com",  
    "name": "您的姓名",  
    "email": "您的邮箱",  
    "office": "您的办公室",
    "office_hour": "TBD",  
    "intro": "个人简介"
}  
```  

然后按照以下目录结构将JSON文件和个人头像文件压缩为ZIP文件。如果没有添加图片，将使用默认头像。  

ZIP文件的名称是您姓名的缩写（例如jndu）。  

```
your name
├── example.json  
└── avatar.png（支持JPG、PNG、JPEG等格式）  
```  

将您的ZIP文件提交至`data/profile-ta`，并运行`make profile-ta`。  

## 生成日程  

使用`make g-events`命令生成所有课程的日程安排，并存储在`docs/static/data/events.csv`中。具体内容可以在Makefile中修改。  

## 修改日程  

目前只能手动修改`docs/static/data/events.csv`文件。

在`events.csv`文件中，可以看到如下内容：

```
title,Week,start,theme,Instructors,pptLink,location,Reading,extra
Lecture,1,2025-02-18T19:10:00,Overview,Hao Li && Danfeng Shan,assets/slides/01-overview-class-rules.pdf,主B-204,1,
Lecture,1,2025-02-20T19:10:00,"Bits, Bytes, & Integers",Danfeng Shan,assets/slides/02-bits-ints.pdf,主B-204,2.1-2.3,[datalab](labs/lab1.md) out
Lecture,2,2025-02-25T19:10:00,Machine Prog: Basics,Danfeng Shan,assets/slides/03-machine-basics.pdf,主B-204,3.1-3.3,
```
对这个csv文件的指定行与列进行修改即可同时对`homepage`的内容进行修改。

> 目前，`title`列仅有值为`Lecture`和`Lab`的对应内容可以在`homepage`中加载。具体筛选逻辑在`scripts/macros.py`。

其中，slide文件在`assets/slides`文件夹中上传，文档中出现的图片文件在`assets/images`中上传，其他文件在`assets/files`文件夹中上传。

> 有关网页内超链接，由于渲染方式的不同，在主页中出现的链接要以`labs/lab1.md`的形式添加，在calendar中出现的链接要以`labs/lab1`的形式添加。具体原因是在mkdocs中，md文档相对路径不需要添加`.md`后缀；而网页的有些部分需要以html的格式进行写入（如主页的slide按钮），此时相对路径需要添加`.md`后缀。

## 更新指导书

直接在`docs/labs`中寻找对应的实验指导书md文件修改即可。如果需要发布，可以修改`mkdocs.yml`文件中：
```yaml
  - Labs:
    - "Lab 0: Tutorial and Environmental Preparation": labs/lab0.md
    - "Lab 1: Data Lab": labs/lab1.md
    - "Lab 2: Bomb Lab": labs/lab2.md
    - "Lab 3: Attack Lab": labs/lab3.md
    - "Lab 4: Cache Lab": labs/lab4.md
    - "Lab 5: Optimization Lab": labs/lab5.md
    # - "Lab 6: Linker Lab": labs/lab6.md
```
这里控制着网页的目录结构，如果想发布指导书，只需删除注释即可。

## 关于多版本控制

该网页使用[mike](https://github.com/jimporter/mike)进行版本控制。

目前的工作流为：.github/workflow/ci.yml中配置了命令`mike deploy $DOC_VERSION latest --push`。其中`$DOC_VERSION`自动读取在xjtu-ics.github.io的repo settings中配置的[Repository variables](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-variables)，保证只有对仓库具有write权限的同学可以修改版本。

