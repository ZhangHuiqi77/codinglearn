LearnHexo

<!--在myblog中gitbash后执行以下-->
hexo init <!--hexo初始化-->
hexo n "name" <!--新建.md文档的blog-->
hexo g <!-- generate 在本地生成文档-->
hexo s <!-- server 在本地显示，之后可在localhost:4000上看到-->
<!--在_config.yml文件中修改网页配置（git端的来源，网页的外观等）-->
hexo g 
hexo d <!--在myblog文件夹下执行这两步就可以把本地同步到github的主页啦-->
hexo g-d<!--在myblog文件夹下执行(等于上两步的合并)就可以把本地同步到github的主页啦-->
scaffolds/post.md 文件可以设置编辑的框架
添加categories的时候换行并用-短线，例如

---
title: jQuery对表单的操作及更多应用
date: 2017-05-26 12:12:57
categories: 
- web前端
tags:
- jQuery
- 表格
- 表单验证
---

换页面名字和作者的话在myblog/_config.yml文件中
基本搭建完成，下面需要把正文字体变小，并且正确增加tag，换个头像
如果想给一篇文章设置密码的话只需要加上一行  password: 123456