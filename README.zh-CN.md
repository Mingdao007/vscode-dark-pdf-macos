# vscode-dark-pdf-macos

这是一个给 `Codex App` 用的技能（skill），用于在 macOS 和 Ubuntu 上配置 Visual Studio Code 的 LaTeX Workshop 深色 PDF 显示、右侧 PDF 标签页、`.tex` 自动换行、SyncTeX 的 tex↔PDF 联动，以及可选的 LaTeX 波浪线隐藏。

English version: [README.md](README.md)

## 仓库内容

- `vscode-dark-pdf-macos/`：可安装的 Codex App 技能包
- `vscode-dark-pdf-macos/scripts/apply_vscode_dark_pdf.py`：用于在 macOS 或 Ubuntu 上写入基础 VS Code 设置的辅助脚本
- `vscode-dark-pdf-macos/agents/openai.yaml`：Codex App 元数据

## 安装

1. 把 `vscode-dark-pdf-macos/` 复制到 `${CODEX_HOME:-$HOME/.codex}/skills/`。
2. 重启 Codex App，或刷新本地 skills。
3. 在对话里以 `$vscode-dark-pdf-macos` 调用这个 skill。

## 适用场景

你可以让 Codex App 帮你：

- 在 macOS 或 Ubuntu 的 VS Code 里配置 LaTeX Workshop 深色 PDF
- 让 PDF 固定在右侧标签页，并使用内置 viewer
- 给 `.tex` 编辑器开启自动换行，而不去改文档内容
- 让 PDF 里双击跳回源码，并用 `Ctrl+Alt+J` 从源码同步到 PDF
- 用 workspace 设置隐藏干扰性的 LaTeX 波浪线
- 排查白色 PDF 渲染、旧 PDF 路径缓存、缺失 `.synctex.gz`，以及 `vscode-pdf` 扩展冲突

## 已验证说明

- 在已验证的 Ubuntu 路线里，应用基础设置后，只要用 fresh path 重新打开 PDF，就不需要重启 VS Code。
- 在已验证的 Ubuntu 路线里，workspace `.vscode/settings.json` 中的 `[latex].editor.wordWrap = "on"` 也不需要重启 VS Code 就能生效。
- helper 脚本现在会把内置 PDF viewer 的反向 SyncTeX 设成 `double-click`。
- 反向 SyncTeX 还要求 PDF 旁边存在对应的 `.synctex.gz`，而且这条工作流以后每次编译都要带 `-synctex=1`，不能把它当成一次性补救。
- 如果 PDF 仍然偏白，下一步 fallback 是单次用 `--disable-gpu` 重新启动 VS Code。

## 触发示例

- `Configure dark PDF viewing in VS Code on Ubuntu with LaTeX Workshop.`
- `Make VS Code behave more like Overleaf for .tex editing plus PDF preview.`
- `Enable PDF double-click back to source in the LaTeX Workshop viewer.`
- `My PDF is still white in VS Code. Walk me through the dark-viewer path.`

## 隐私边界

这个仓库只包含可移植的 skill 逻辑和辅助脚本，不包含私有 memory 文件、本机绝对路径、私有 context 文件，或依赖某个用户环境才能工作的工作流。

## 仓库结构

- `vscode-dark-pdf-macos/`：Codex App 技能包
- `README.md`：英文说明
- `README.zh-CN.md`：中文说明
- `LICENSE`：MIT 许可证
- `CHANGELOG.md`：发布历史
