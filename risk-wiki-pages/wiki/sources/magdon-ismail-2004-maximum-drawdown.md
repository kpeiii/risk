---
type: source
title: Maximum Drawdown
authors: [Magdon-Ismail, Atiya]
year: 2004
raw_file: none
source_url: https://papers.ssrn.com/abstract=874069
access: abstract-only
version_read: 僅讀到 SSRN 摘要、Scribd 上的片段文字、以及引用該文的二手資料;全文未取得(Risk Magazine 17(10), 99–102, 2004)
ingested: 2026-11-18
metrics: [maximum-drawdown]
---

# Magdon-Ismail & Atiya (2004) — Maximum Drawdown

> ⚠️ **僅摘要層級**:本頁只依 SSRN 摘要與公開片段寫成,細節與公式皆標〔待核對〕。建議將 PDF 放入 `raw/` 後重新 ingest。

## 基本資料
- 作者:Malik Magdon-Ismail、Amir F. Atiya
- 發表:*Risk Magazine* 17(10), 99–102, 2004。完整的數學推導在同組作者的 *On the Maximum Drawdown of a Brownian Motion*(*Journal of Applied Probability* 41(1), 147–161, 2004);該文我只讀到摘要。

## 研究問題
最大回撤(MDD)衡量損失可以持續多深。能否給出 MDD 與平均報酬、Sharpe ratio 之間的解析關係,並由此提出可跨不同績效期間比較的 Calmar ratio 縮放規律?

## 方法與資料
- 假設投資組合價值服從帶漂移的布朗運動(Brownian motion with drift),利用反射布朗運動首次通過時間的結果。
- 摘要層級的資訊:給出 MDD 期望值與漂移、波動度之間的解析結果,並提出類似 Sharpe ratio「√T 縮放」的新縮放規律。〔具體公式待核對〕

## 核心結論(僅限摘要所能支持者)
1. MDD 與 Sharpe ratio、平均報酬有解析關係,且 MDD 是 Calmar ratio 與 Sterling ratio 等風險調整績效指標的組成。
2. 提出 Calmar ratio 的縮放規律,使不同長度績效紀錄的基金較容易比較。
3. 論文並討論這些結果對投資組合的含意。
4. 〔二手資料〕引用該系列結果的資料指出:正漂移時 MDD 期望值隨時間以對數速度成長;其漸近形式為 $\frac{\sigma^2}{2\mu}\left(\ln\frac{\mu^2T}{2\sigma^2}+C\right)$,其中常數 $C=2\ln2+\gamma$(來源:Bermin & Holm 2025 工作論文所引述;我未驗證)。
5. 〔背景知識〕零漂移時 MDD 約隨 √T 成長、負漂移時隨 T 線性成長(Wikipedia 文字中條件符號遺失,依標準結果補足〔待核對〕)。

## 涉及的風險指標
- [最大回撤 MDD](../metrics/maximum-drawdown.md)

## 限制與注意事項
- 布朗運動(含漂移)為理論基準,真實報酬有厚尾、序列相關與波動度聚集。
- MathWorks 的文件提醒:期望 MDD 是平均估計,不是損失上限;實際觀察到的回撤可以高於它。〔二手資料〕

## 與其他論文的關係
- 與 [Sharpe (1994)](sharpe-1994-sharpe-ratio.md) 在概念上並列:Sharpe ratio 的 √T 縮放與本文的 MDD 縮放互為對照。
- 與 [Lo (2002)](lo-2002-statistics-sharpe-ratios.md) 有潛在張力:若報酬有序列相關,布朗運動基準下的縮放規律可能失準〔推論,尚無論文直接驗證〕。
