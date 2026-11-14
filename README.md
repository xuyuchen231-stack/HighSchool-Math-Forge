# HighSchool-Math-Forge

面向中国高中数学与高考数学的通用 Agent Skill。沿用 HighSchool-English-Forge / HighSchool-Chemistry-Forge 的“原卷 + 独立解题 + 零基础逐题精讲 + 知识拓展 + 专业教辅 PDF”路线，数学部分优先使用 **LaTeX** 排版、**Python** 科学绘图和 **SymPy** 辅助验算。

## 主要能力
- 无答案试卷逐题求解，证明与计算分开核验，避免把数值试验误当严格证明。
- 完整知识体系索引，基础讲解、长步骤推导、易错点、变式训练。
- 函数图像、解析几何、立体几何、统计图表可复现绘制；清楚区分示意图与精确图。
- 原卷保留、答案与过程、知识精讲、图形与 PDF 逐页质量检查。

## 快速开始
```bash
python scripts/validate.py
python scripts/plot_examples.py --out examples/figures
# 安装 TeX Live + XeLaTeX 与 ctex 后
xelatex -interaction=nonstopmode -halt-on-error -output-directory=examples templates/lesson.tex
```

推荐 Python 依赖：`pip install -r requirements.txt`。运行绘图前需安装支持中文的字体；缺少字体时可使用英文图注并在正文说明。`scripts/validate.py` 只做文件/索引结构校验，不能证明解题正确性。

## 状态
v0.1.1 为可执行的工作流骨架、完整课程专题索引、若干基础教学示范与绘图脚本；**不是**所有专题已完成知识精讲，更未完成全国历年真题穷尽式验证。真题应由用户提供或从合法授权来源获取，不在仓库批量转载第三方试卷。

## 目录
- `SKILL.md`：Agent 入口与硬性质量要求
- `knowledge/`：课程专题索引与基础知识示范
- `references/`：无答案求解、验证、绘图、LaTeX、教辅成品规范
- `scripts/`：结构验证、数学图像生成
- `templates/`：XeLaTeX 中文教辅样例
- `prompts/`：使用提示词

## GitHub 发布与绘图示例
完整源码现已上传。运行 `python scripts/plot_examples.py --out examples/figures` 生成四组 PNG + 矢量 PDF 科学绘图；GitHub Actions 会校验结构与绘图，并提供可下载的运行产物。切线示例已修正为 `y=-2x+6`，请勿使用旧版错误的 `y=-2x+8`。
