# Git 分支开发与 Pull Request 工作流 SOP

## 1. 概述

本文记录一次完整的 GitHub 团队开发流程。

以 CALC-001 任务为例：

- 仓库：`git-workflow-practice`
- 开发任务：为 Python 计算器新增乘法功能
- 主分支：`main`
- 功能分支：`feature/CALC-001-multiply`
- 开发工具：VSCode
- 代码托管平台：GitHub

整体流程：

```text
接收开发需求
    ↓
更新本地 main
    ↓
创建 feature 分支
    ↓
在 VSCode 中开发、测试
    ↓
Stage Changes
    ↓
Commit
    ↓
Push / Publish Branch
    ↓
Create Pull Request
    ↓
Code Review
    ↓
修改代码、再次 Commit 和 Push
    ↓
Merge Pull Request
    ↓
更新本地 main
    ↓
删除本地和远程 feature 分支
```

## 2. 创建功能分支

### 2.1 更新本地主分支

开始新任务之前，先确保工作区没有未处理的改动。

```powershell
git status
git switch main
git pull --ff-only origin main
```

通过 VSCode 也可以切换到 `main`，然后在 Source Control 菜单中选择 Pull。

### 2.2 创建功能分支

使用命令行：

```powershell
git switch -c feature/CALC-001-multiply
```

或者在 VSCode 中：

1. 点击左下角当前分支名称。
2. 选择 Create new branch。
3. 输入 `feature/CALC-001-multiply`。
4. 确认创建并切换。

检查当前分支：

```powershell
git branch
```

`*` 表示当前所在分支。

注意：创建分支不会复制一个新的项目文件夹。不同分支对应不同的 Git 提交版本。

## 3. 开发与测试

在当前功能分支中修改代码。

CALC-001 的实际工作包括：

- 在 `calculator.py` 中新增 `multiply(a, b)`。
- 修改 `main.py`，调用乘法函数。
- 增加 `test_calculator.py`，测试正数、负数、零和小数。

运行程序：

```powershell
python main.py
python test_calculator.py
```

开发完成后，通过 VSCode Source Control 查看每个文件的 Diff，确认没有意外修改。

## 4. 暂存、提交和推送代码

### 4.1 Stage Changes

在 VSCode 中：

1. 打开 Source Control（`Ctrl + Shift + G`）。
2. 在 Changes 区域找到修改的文件。
3. 点击文件旁边的 `+`，将改动加入 Staged Changes。

对应命令：

```powershell
git add calculator.py main.py
```

### 4.2 Commit

在 VSCode 的消息输入框中填写：

`feat: add calculator multiplication`

点击 Commit。

对应命令：

```powershell
git commit -m "feat: add calculator multiplication"
```

Commit 只将修改记录到本地仓库，不会自动上传 GitHub。

### 4.3 Push

第一次推送功能分支：

```powershell
git push -u origin feature/CALC-001-multiply
```

VSCode 中可以使用 Publish Branch。

已经建立追踪关系的分支，后续可以直接使用：

```powershell
git push
```

VSCode 的 Sync Changes 通常先执行 Pull，再执行 Push；如果只需要推送，也可以单独选择 Push。

## 5. 创建 Pull Request

Push 完成后，进入 GitHub 仓库页面。

操作步骤：

1. 点击 Pull requests。
2. 点击 New pull request，或者直接使用 Compare & pull request。
3. 设置 Base 为 `main`。
4. 设置 Compare 为 `feature/CALC-001-multiply`。
5. 检查 Files changed。
6. 填写 PR 标题、修改内容和测试结果。
7. 点击 Create pull request。

示例标题：

`feat: add calculator multiplication`

PR 描述建议包含：

- 需求背景
- 修改内容
- 测试结果
- 关联任务编号

**重要：Create Pull Request 只是提出合并申请，不会直接修改 main。**

## 6. Code Review 与修改

PR 创建之后，其他开发人员可以审查代码、提出修改意见。

CALC-001 的模拟审核意见是补充乘法边界测试。

我们在原功能分支中新增 `test_calculator.py`，然后执行：

```powershell
git add test_calculator.py
git commit -m "test: add multiplication edge case tests"
git push
```

新的提交会自动出现在已经存在的 Pull Request 中。

不需要重新创建 PR。

如果团队配置了 CI，还需要检查自动化测试和代码质量检查是否通过。

## 7. Merge Pull Request

当 Code Review 通过，且满足项目的合并条件后：

1. 打开对应的 GitHub PR。
2. 检查 Commits、Files changed 和 Checks。
3. 点击 Merge pull request。
4. 点击 Confirm merge。

合并完成之后，`main` 就会包含功能分支中的修改。

常见合并方式：

| 方式 | 含义 |
|---|---|
| Merge commit | 创建合并提交，保留分支历史 |
| Squash and merge | 将多个提交压缩成一个提交 |
| Rebase and merge | 重新应用功能分支上的提交 |

本次 CALC-001 使用的是 Merge commit 方式。

需要注意：Merge 完成并不代表功能分支自动消失。

## 8. 同步本地主分支

在 GitHub 上完成 Merge 后，本地 `main` 不会自动更新。

执行：

```powershell
git switch main
git pull --ff-only origin main
```

或者通过 VSCode：

1. 切换到 `main`。
2. 打开 Source Control。
3. 选择 Pull。

此时本地 `main` 应包含刚刚合并的乘法功能。

## 9. 删除完成任务的分支

确认 PR 已合并，且分支不再需要后，可以清理功能分支。

删除本地分支：

```powershell
git branch -d feature/CALC-001-multiply
```

删除远程分支：

```powershell
git push origin --delete feature/CALC-001-multiply
```

也可以在 GitHub 已合并的 PR 页面点击 Delete branch。

清理失效的远程跟踪引用：

```powershell
git fetch --prune
```

检查所有分支：

```powershell
git branch -a
```

CALC-001 完成清理后，仓库只保留 `main`。

## 10. 常见问题

### Q1：创建新分支会生成新的文件夹吗？

不会。Git 在同一个工作目录中切换不同分支对应的文件版本。

### Q2：Commit 与 Push 有什么区别？

Commit 创建本地提交；Push 将本地提交推送到远程仓库。

### Q3：为什么创建 PR 后仍然有两个分支？

因为 PR 只是合并请求。只有完成 Merge，目标分支才会包含请求中的代码修改。

### Q4：PR 创建后还能继续修改代码吗？

可以。在原功能分支继续 Commit 和 Push，PR 就会自动更新。

### Q5：Merge 后两个分支为什么代码一样？

因为功能分支的修改已经合入 main。但两个分支的提交历史不一定完全相同。

### Q6：删除分支会删除已合并的功能吗？

不会。已经合并进入 main 的修改仍会保留。

### Q7：为什么要在每个新任务中创建独立分支？

为了隔离不同任务，方便审核、测试、回滚和多人协作，减少未经审核的修改直接影响主分支。

## 11. 常用命令速查

| 目标 | 命令 |
|---|---|
| 查看状态 | `git status` |
| 查看本地分支 | `git branch` |
| 查看所有分支 | `git branch -a` |
| 切换主分支 | `git switch main` |
| 更新主分支 | `git pull --ff-only origin main` |
| 创建功能分支 | `git switch -c feature/xxx` |
| 查看差异 | `git diff` |
| 暂存文件 | `git add 文件名` |
| 提交代码 | `git commit -m "说明"` |
| 首次推送分支 | `git push -u origin feature/xxx` |
| 后续推送 | `git push` |
| 删除本地分支 | `git branch -d feature/xxx` |
| 删除远程分支 | `git push origin --delete feature/xxx` |
| 清理远程引用 | `git fetch --prune` |
| 查看提交历史 | `git log --oneline --graph --all` |

## 12. CALC-001 实践总结

本次实践完成了：

- GitHub 远程仓库创建与 Clone
- Git 用户身份配置
- 功能分支创建
- VSCode 图形化 Git 操作
- 开发与测试
- Commit 和 Push
- 创建 Pull Request #1
- 模拟 Code Review
- 追加测试代码并更新 PR
- Merge Pull Request
- 同步本地 main
- 删除本地和远程功能分支

核心经验：

**一个开发任务使用一个功能分支，完成开发与测试后提交 Pull Request，通过审核后合并，最后清理分支。**

这是一套常见的团队开发工作流，具体企业可能会使用不同的分支管理和审核规则。