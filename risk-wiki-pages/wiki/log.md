# 操作紀錄

> 只增不改,最新的在最下面。格式見 AGENTS.md 第 8 節。

## [初始化] schema | 建立 wiki 骨架與 AGENTS.md

## [2026-11-18] schema | 擴充論文頁 frontmatter 與批次 ingest 例外
- 更新 AGENTS.md:論文頁新增 `source_url`、`access`、`version_read` 欄位;ingest 流程新增「使用者明確授權批次處理」的例外。
- 原因:`raw/` 尚無 PDF,本批論文取自公開網頁版本,需記錄實際讀取的來源與版本。

## [2026-11-18] ingest | Artzner et al. 1999 — Coherent Measures of Risk(批次授權)
- 新增:sources/artzner-1999-coherent-measures.md
- 更新/新增:metrics/value-at-risk.md、metrics/expected-shortfall.md、concepts/coherent-risk-measure.md、concepts/tail-risk-measure-variants.md
- 備註:讀取 1998-07-22 工作稿全文;VaR 次可加性反例與表示定理已記錄。

## [2026-11-18] ingest | Rockafellar & Uryasev 2000 — Optimization of CVaR(批次授權)
- 新增:sources/rockafellar-2000-cvar-optimization.md
- 更新:metrics/expected-shortfall.md、metrics/value-at-risk.md、concepts/tail-risk-measure-variants.md
- 備註:讀取 1999-09-05 工作稿全文;論文假設連續分布,一般分布留待後續。

## [2026-11-18] ingest | Acerbi & Tasche 2002 — On the coherence of Expected Shortfall(批次授權)
- 新增:sources/acerbi-2002-coherence-expected-shortfall.md
- 更新:metrics/expected-shortfall.md、metrics/value-at-risk.md、concepts/tail-risk-measure-variants.md、concepts/coherent-risk-measure.md
- 備註:讀取 arXiv v4(非 v5);修正 TCE 與 CVaR 的等價關係。

## [2026-11-18] ingest | Sharpe 1994 — The Sharpe Ratio(批次授權)
- 新增:sources/sharpe-1994-sharpe-ratio.md
- 新增:metrics/sharpe-ratio.md
- 備註:公式在原頁面為圖片,依文字敘述重建,標〔待核對〕。

## [2026-11-18] ingest | Lo 2002 — The Statistics of Sharpe Ratios(批次授權)
- 新增:sources/lo-2002-statistics-sharpe-ratios.md、concepts/iid-and-serial-correlation.md
- 更新:metrics/sharpe-ratio.md
- 備註:PDF 文字抽取遺失部分符號,公式以論文表格數值交叉驗證。

## [2026-11-18] ingest | Magdon-Ismail & Atiya 2004 — Maximum Drawdown(批次授權,僅摘要)
- 新增:sources/magdon-ismail-2004-maximum-drawdown.md、metrics/maximum-drawdown.md
- 備註:**只取得摘要與二手片段**,全文抓取失敗;所有細節標〔待核對〕,MDD 結論信心為低。

## [2026-11-18] query | 整合比較:VaR、ES、Sharpe、MDD
- 新增:comparisons/risk-metrics-comparison.md、comparisons/var-vs-expected-shortfall.md、overview.md(更新)
