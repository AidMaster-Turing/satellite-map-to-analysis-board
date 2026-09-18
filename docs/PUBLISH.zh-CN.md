# 发布到GitHub

本目录已按仓库组织，不需要GitHub Pages或服务器。

## 网页上传

1. 解压仓库ZIP，打开最外层satellite-map-to-analysis-board文件夹，看到README.md、VERSION、docs和skills。
2. 登录GitHub，打开 https://github.com/new 。
3. Repository name填satellite-map-to-analysis-board；Description可填“将单张卫星地图转为兼顾完整分析与当地建筑拼贴的灰棕色mapping展板”。
4. 公开分享选Public；个人使用选Private。已有README、.gitignore和MIT许可证，不必在创建仓库时生成重复文件。
5. 点击Create repository。
6. 空仓库Quick setup中点击uploading an existing file；已有文件的仓库使用Add file → Upload files。
7. 把解压目录里面的文件和子文件夹拖入，保持docs和skills层级。不要只上传ZIP，不要多套一层最外层目录。
8. 预览确认存在skills/satellite-map-to-analysis-board/SKILL.md。提交说明填Initial release: satellite map analysis skill，按页面提示提交。
9. 查看README和文件链接。若隐藏的.gitignore漏传，可用Add file → Create new file补充。
10. 本包已使用账号AidMaster-Turing；若仓库名或分支变化，同步修改README中的安装链接。

参见GitHub官方[创建仓库](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)和[上传文件](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)。

## Git推送方式

先创建GitHub空仓库，不添加README、许可证或.gitignore。在本仓库目录打开终端：

```bash
git init -b main
git add .
git commit -m "Initial release: satellite map analysis skill"
git remote add origin https://github.com/AidMaster-Turing/satellite-map-to-analysis-board.git
git push -u origin main
```

若提示身份未配置，在仓库内填写自己的user.name和user.email。登录遵循Git的正常认证流程，不将令牌写进文件。

之后更新：

```bash
git add .
git commit -m "Refine mapping workflow"
git push
```

已有仓库先检查状态与远端，不用强推覆盖历史。

## 分享安装

分享仓库首页供人阅读；安装使用技能目录链接：

```text
使用 $skill-installer 安装：
https://github.com/AidMaster-Turing/satellite-map-to-analysis-board/tree/main/skills/satellite-map-to-analysis-board
```

发布包只包含原创指令和辅助脚本。后续可添加有使用依据的案例图与署名。公开GitHub源码不等于在插件商店上架；本次提供独立Skill源码。
