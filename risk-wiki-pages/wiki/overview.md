---
type: overview
updated: 2026-11-18
source_count: 6
---

# 整體綜述:投資風險指標

> 目前已 ingest 6 篇論文(5 篇全文、1 篇僅摘要)。這是第一批,涵蓋面仍窄,下面的結論都限於這些論文的範圍。

## 目前的整體理解
1. **風險度量有「資本用」與「績效用」兩大類。** VaR 與 ES 是損失分布尾部的度量,用來設資本與限額;Sharpe ratio 是績效比率;MDD 是路徑型統計量。先分清用途,再選指標。([總比較](comparisons/risk-metrics-comparison.md))
2. **VaR 的核心缺陷是次可加性**,導致分散化反而讓 VaR 升高、風險集中無法偵測。([一致性風險度量](concepts/coherent-risk-measure.md)、[VaR](metrics/value-at-risk.md))
3. **ES(= CVaR)是目前材料中唯一在任意分布下一致、又可估計與可最佳化的尾部度量。** 這個結論來自三篇論文逐步累積:Artzner 提出公理,Rockafellar & Uryasev 給出可用的計算,Acerbi & Tasche 統一定義。([ES](metrics/expected-shortfall.md)、[變體關係](concepts/tail-risk-measure-variants.md))
4. **Sharpe ratio 的估計誤差與年化方式被廣泛低估。** 五年月資料的信賴區間可能涵蓋 0;對有序列相關的資產,√12 年化可高估逾 65%。([Sharpe ratio](metrics/sharpe-ratio.md)、[序列相關](concepts/iid-and-serial-correlation.md))
5. **MDD 的理論基礎目前只有摘要層級的證據**,結論暫列為低信心。([MDD](metrics/maximum-drawdown.md))

## 重大爭議與修正
- **TCE 是否一致**:Artzner 等人早期措辭容易讓人以為 TCE ≈ WCE,Acerbi & Tasche 證明一般不然。已在 ES 與變體頁處理。
- **年化規則**:Sharpe 的簡化作法與 Lo 的修正並非矛盾,而是精確度不同。已在 Sharpe ratio 頁處理。
- 目前沒有已 ingest 論文之間互相衝突的「實證」結論——因為已 ingest 的論文大多是理論或小型示範。

## 資料缺口與建議的下一批論文
- **MDD 全文**:Magdon-Ismail、Atiya、Pratap、Abu-Mostafa (2004) *On the Maximum Drawdown of a Brownian Motion*(J. Applied Probability);以及回撤型最佳化(Chekhlov、Uryasev、Zabarankin 的 CDaR)。
- **ES 的估計與回測**:Acerbi、Nordio、Sirtori (2001);Pflug (2000)。
- **Sharpe ratio 的替代與修正**:Sortino、Calmar、Sharpe ratio 的分布與多重檢定問題。
- **厚尾與極值理論**(Embrechts 等人)對 VaR/ES 估計的影響。
- **VaR 的實證與監管面**:Jorion、Duffie & Pan 的 VaR 綜述;ES 納入監管的背景。
- 目前**沒有**任何已 ingest 論文討論:回測方法、估計誤差比較、真實市場的跨期結果、監管實務。

## 品質提醒
- 6 篇論文的 PDF **尚未放入 `raw/`**;本批內容取自公開網頁版本(版本與正式發表版可能不同,見各論文頁的 `version_read`)。建議你下載正式版 PDF 放入 `raw/`,之後 Agent 可據以核對。
- 凡標〔待核對〕、〔二手資料〕、〔背景知識〕、〔Agent 推論〕之處,都不是直接來自已 ingest 論文全文。
