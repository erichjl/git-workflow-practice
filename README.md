# git-workflow-practice
Practice Git workflow with Python(git 工作流练习)

# Git Workflow Practice
一个用于学习 Git 和 GitHub 企业开发工作流的 Python 练习项目。

## 1. 项目介绍

当前项目包含一个简单的计算器程序，用于模拟真实软件开发中的版本控制和团队协作。

项目结构：

```text
git-workflow-practice/
├── calculator.py
├── main.py
├── .gitignore
└── README.md
```

运行程序：

```powershell
python main.py
```

## 2. Git 首次配置

首次安装 Git 后，需要配置提交者的用户名和邮箱。

```powershell
git config --global user.name "YourName"
git config --global user.email "you@example.com"
```

查看当前配置：

```powershell
git config --global user.name
git config --global user.email
git config --list
```

说明：

- `--global`：对当前用户的 Git 仓库生效。
- `--local`：仅对当前仓库生效。
- `user.name`：Commit 作者名称。
- `user.email`：Commit 作者邮箱。

Git 提交身份不等于 GitHub 登录认证。

## 3. 创建及克隆仓库

### 方法一：从 GitHub 克隆已有仓库（推荐团队协作时使用）

先在 GitHub 创建远程仓库，然后执行：

```powershell
git clone https://github.com/<username>/<repository>.git
cd <repository>
```

`git clone` 会自动创建本地项目文件夹和 `.git` 目录。

### 方法二：初始化本地仓库

对于已经存在的本地项目，可以使用：

```powershell
git init
```

如果需要关联 GitHub 远程仓库：

```powershell
git remote add origin <repository-url>
```

注意：克隆已有仓库后，不需要再次执行 `git init`。

## 4. 查看 Git 仓库状态

```powershell
# 查看当前工作区状态
git status

# 查看本地分支
git branch

# 查看当前分支名
git branch --show-current

# 查看远程仓库地址
git remote -v

# 查看提交历史
git log --oneline
```

Git 文件状态：

| 状态 | 含义 |
|---|---|
| Untracked | 新文件尚未被 Git 跟踪 |
| Modified | 已跟踪文件发生修改 |
| Staged | 文件改动已加入暂存区 |
| Committed | 改动已记录到本地仓库 |

## 5. .gitignore 文件

`.gitignore` 用于指定不需要纳入版本控制的文件。

本项目使用 Python 模板，并额外忽略 VSCode 的本地配置。

常见规则：

```gitignore
__pycache__/
*.py[cod]
.vscode/
.env
```

说明：

- `__pycache__/`：Python 字节码缓存目录。
- `*.py[cod]`：Python 编译生成的缓存文件。
- `.vscode/`：本项目不共享的 VSCode 配置。
- `.env`：可能包含 API Key、密码等敏感信息的环境配置。

`.gitignore` 不会自动停止跟踪已经被提交过的文件。

## 6. 第一次提交代码

新增或修改代码后，先查看状态：

```powershell
git status
```

将需要提交的文件加入暂存区：

```powershell
git add calculator.py main.py
```

或者暂存当前目录下所有未忽略的修改：

```powershell
git add .
```

检查待提交的内容：

```powershell
git diff --cached
```

创建 Commit：

```powershell
git commit -m "feat: initialize calculator project"
```

提交成功后，Git 会生成一个唯一的 Commit ID。

常见提交信息：

| 类型 | 用途 |
|---|---|
| feat | 新功能 |
| fix | 修复 Bug |
| docs | 文档更新 |
| refactor | 代码重构 |
| test | 测试代码 |
| chore | 日常维护 |

## 7. 推送代码到 GitHub

```powershell
git push origin main
```

其中：

- `origin` 是远程仓库名称。
- `main` 是要推送的分支。

如果首次推送时出现身份认证失败，可以按 GitHub 提示通过浏览器完成认证。

`Everything up-to-date` 表示没有新的本地提交需要推送。

注意：`git commit` 仅创建本地提交，`git push` 才会将提交上传到远程仓库。

## 8. 基础开发流程

目前已经掌握：

```text
GitHub 创建仓库
       ↓
git clone
       ↓
VSCode 打开项目
       ↓
修改 Python 文件
       ↓
git status
       ↓
git add
       ↓
git commit
       ↓
git push
       ↓
GitHub 查看提交
```

后续继续学习：

- Git 分支管理
- Pull Request / Merge Request
- Code Review
- Git Merge
- 分支冲突解决
- 团队协作工作流

## 9. 常见问题

### Q1：Commit 时提示 Author identity unknown

原因：Git 没有配置用户名和邮箱。

解决：

```powershell
git config --global user.name "YourName"
git config --global user.email "you@example.com"
```

然后重新执行 `git commit`，通常不需要重新 `git add`。

### Q2：Push 时提示 Authentication failed

原因：远程仓库认证失败，例如凭据无效、过期或尚未完成登录。

解决：检查远程仓库地址及账号权限，并通过 Git Credential Manager、GitHub CLI 或 SSH 等支持的方式认证。

GitHub 不支持通过普通账号密码直接进行 HTTPS Git 操作。

### Q3：为什么出现 __pycache__？

Python 导入模块时可能自动生成字节码缓存。

一般不需要提交到 Git，通过 `.gitignore` 忽略即可。

### Q4：为什么出现 .vscode？

这是 VSCode 的工作区配置目录。

个人编辑器设置通常不需要提交；团队共用的调试和扩展配置则可以按项目规范提交。
