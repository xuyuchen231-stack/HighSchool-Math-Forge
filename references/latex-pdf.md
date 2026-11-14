# LaTeX 排版与 PDF 编译
首选 XeLaTeX + `ctexart`, `amsmath`, `amssymb`, `mathtools`, `graphicx`, `booktabs`, `hyperref`, `geometry`, `enumitem`。数学公式统一使用 `\(...\)` 和 `\[...\]`；多步推导使用 `align`/`aligned`，不要在段落中塞入无法阅读的长公式。公式编号应与正文引用一致。证明题以“证明”开始、结论结束。

图形优先 Python 生成 PDF 后通过 `\includegraphics` 引入；简单几何也可 TikZ 绘制，但须由数学关系确定坐标。原卷在有授权的情况下通过 `pdfpages` 保留原样，禁止用识别后排版替代原卷。

编译流程：依赖检查→运行 Python 绘图→XeLaTeX 至少两遍→逐页渲染 PDF→检查字体、中文、数学符号、边距、页码、图表标签、孤行、空白页与题号映射。缺少 TeX 工具时不宣称已编译。

版权：第三方高考试卷不应未经许可在公开 GitHub 仓库再发布；用户提供的试卷可在用户指定的私有交付中处理，视使用权限而定。
