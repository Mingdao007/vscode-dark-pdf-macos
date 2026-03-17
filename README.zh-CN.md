# vscode-dark-pdf-macos

这是一个给 `Codex App` 用的技能（skill），用于在 macOS 上配置 Visual Studio Code 的 LaTeX Workshop 深色 PDF 显示、右侧 PDF 标签页、`.tex` 自动换行，以及可选的 LaTeX 波浪线隐藏。

English version: [README.md](README.md)

## 仓库内容

- `vscode-dark-pdf-macos/`：可安装的 Codex App 技能包
- `vscode-dark-pdf-macos/scripts/apply_vscode_dark_pdf.py`：用于写入基础 VS Code 设置的辅助脚本
- `vscode-dark-pdf-macos/agents/openai.yaml`：Codex App 元数据

## 安装

1. 把 `vscode-dark-pdf-macos/` 复制到 `${CODEX_HOME:-$HOME/.codex}/skills/`。
2. 重启 Codex App，或刷新本地 skills。
3. 在对话里以 `$vscode-dark-pdf-macos` 调用这个 skill。

## 适用场景

你可以让 Codex App 帮你：

- 在 macOS 的 VS Code 里配置 LaTeX Workshop 深色 PDF
- 让 PDF 固定在右侧标签页，并使用内置 viewer
- 给 `.tex` 编辑器开启自动换行，而不去改文档内容
- 用 workspace 设置隐藏干扰性的 LaTeX 波浪线
- 排查白色 PDF 渲染和 `vscode-pdf` 扩展冲突

## 触发示例

- `Configure dark PDF viewing in VS Code on macOS with LaTeX Workshop.`
- `Make VS Code behave more like Overleaf for .tex editing plus PDF preview.`
- `Hide LaTeX squiggles in this workspace without changing the document body.`
- `My PDF is still white in VS Code. Walk me through the dark-viewer path.`

## 隐私边界

这个仓库只包含可移植的 skill 逻辑和辅助脚本，不包含私有 memory 文件、本机绝对路径、私有 context 文件，或依赖某个用户环境才能工作的工作流。

## 仓库结构

- `vscode-dark-pdf-macos/`：Codex App 技能包
- `README.md`：英文说明
- `README.zh-CN.md`：中文说明
- `LICENSE`：MIT 许可证
- `CHANGELOG.md`：发布历史
