# Wiki 目錄

> 每次 ingest 後由 Agent 更新。格式見 AGENTS.md 第 8 節。

## 綜述
- [整體綜述](overview.md) — 目前對風險指標的整體理解、爭議與資料缺口

## 論文(sources)
- [Artzner et al., 1999 — Coherent Measures of Risk](sources/artzner-1999-coherent-measures.md) — 提出一致性公理,批評 VaR|全文
- [Rockafellar & Uryasev, 2000 — Optimization of CVaR](sources/rockafellar-2000-cvar-optimization.md) — 可用線性規劃最佳化的 CVaR|全文
- [Acerbi & Tasche, 2002 — On the coherence of Expected Shortfall](sources/acerbi-2002-coherence-expected-shortfall.md) — 證明 ES 在任意分布下一致且等於 CVaR|全文
- [Sharpe, 1994 — The Sharpe Ratio](sources/sharpe-1994-sharpe-ratio.md) — 一般化定義與使用條件|全文
- [Lo, 2002 — The Statistics of Sharpe Ratios](sources/lo-2002-statistics-sharpe-ratios.md) — 估計誤差與序列相關下的年化|全文
- [Magdon-Ismail & Atiya, 2004 — Maximum Drawdown](sources/magdon-ismail-2004-maximum-drawdown.md) — MDD 與 Sharpe、Calmar 的關係|**僅摘要**

## 風險指標(metrics)
- [風險值 VaR](metrics/value-at-risk.md) — 最差 α 情境的損失門檻,缺次可加性|3 篇論文
- [預期短缺 ES / CVaR](metrics/expected-shortfall.md) — 最差 α 情境的平均損失,一致且可最佳化|3 篇論文
- [夏普比率 Sharpe ratio](metrics/sharpe-ratio.md) — 每單位波動的超額報酬|2 篇論文
- [最大回撤 MDD](metrics/maximum-drawdown.md) — 高點到低點最大跌幅|1 篇論文(僅摘要)

## 概念(concepts)
- [一致性風險度量](concepts/coherent-risk-measure.md) — 四條公理、表示定理、VaR 反例
- [尾部風險度量的變體與關係](concepts/tail-risk-measure-variants.md) — TCE / WCE / CVaR / ES 對照
- [IID 假設與序列相關](concepts/iid-and-serial-correlation.md) — Sharpe ratio 的標準誤與年化修正

## 比較與綜合分析(comparisons)
- [四種風險指標總比較](comparisons/risk-metrics-comparison.md) — VaR、ES、Sharpe、MDD 的假設、優缺點與適用情境
- [VaR 與 ES 比較](comparisons/var-vs-expected-shortfall.md) — 含同一資料的數字對照
