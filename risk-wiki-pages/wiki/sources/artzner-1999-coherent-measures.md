---
type: source
title: Coherent Measures of Risk
authors: [Artzner, Delbaen, Eber, Heath]
year: 1999
raw_file: none
source_url: https://risknet.de/elibrary/paper/coherent-measures-of-risk
access: full-text
version_read: 工作稿 1998-07-22(正式發表於 Mathematical Finance 9(3), 203–228, 1999)
ingested: 2026-11-18
metrics: [value-at-risk, expected-shortfall]
---

# Artzner et al. (1999) — Coherent Measures of Risk

## 基本資料
- 作者:Philippe Artzner、Freddy Delbaen、Jean-Marc Eber、David Heath
- 發表:*Mathematical Finance* 9(3), 1999;本頁讀取的是 1998 年 7 月的工作稿,與正式版可能有細節差異〔待核對〕。

## 研究問題
風險衡量應該滿足哪些最低限度的性質,才適合用來訂定資本要求、保證金與風險限額?現行方法(SPAN、SEC/NASD 規則、基於分位數的 VaR)是否符合這些性質?

## 方法與資料
純理論加上具體算例。以「未來淨值」為風險對象(而非價值變動),定義「可接受集合(acceptance set)」,再導出風險度量。樣本空間假設為有限集合。以 SPAN、SEC 保證金規則和 VaR 作為被檢驗的實務方法。

## 核心結論
1. 提出四條公理——平移不變性、次可加性、正齊次性、單調性——滿足者稱為**一致性(coherent)風險度量**。詳見 [一致性風險度量](../concepts/coherent-risk-measure.md)。
2. **表示定理**:一個風險度量是一致的,若且唯若它等於在一組「廣義情境(generalized scenarios)」機率測度上取預期損失的上確界。情境越多,度量越保守。
3. **VaR 不具次可加性**,論文用數位選擇權、信用債券集中度與風險配置三類算例說明,並主張應拒絕以 VaR 作為風險度量。詳見 [風險值 VaR](../metrics/value-at-risk.md)。
4. SPAN 的情境式計算本身是一致的;SEC/NASD 的保證金規則可視為其對偶,但在蝶式部位上過度保守(例中要求 30,而最壞損失僅 10)。
5. 提出**尾部條件期望(TCE)**與**最壞條件期望(WCE)**,其中 WCE 為一致的;在特定條件下 TCE 與 WCE 一致。後續研究發現 TCE 在一般情況下並不一致,見 [尾部風險度量的變體與關係](../concepts/tail-risk-measure-variants.md)。
6. 公理並未唯一決定某個度量,而是刻畫一整類;實際選擇仍需額外的經濟考量。

## 涉及的風險指標
- [風險值 VaR](../metrics/value-at-risk.md)
- [預期短缺 ES / CVaR](../metrics/expected-shortfall.md)(以 TCE / WCE 形式出現)

## 限制與注意事項
- 假設樣本空間有限,且只考慮單一期間。
- 作者自承:以單一數字描述風險會損失資訊,但認為實務上的決策本質是二元的(允許或不允許)。
- 此版本尚無 ES(Acerbi–Tasche)的一般化定義,TCE 的一致性主張後來被修正。
- 論文指出 VaR 使用的機率應是「估計的實際機率」還是「審慎選擇的主觀機率」並不明確。

## 與其他論文的關係
- 被 [Rockafellar & Uryasev (2000)](rockafellar-2000-cvar-optimization.md) 引為 VaR 缺陷的依據,並由後者提供可最佳化的 CVaR。
- 被 [Acerbi & Tasche (2002)](acerbi-2002-coherence-expected-shortfall.md) 修正:TCE 不一定一致,ES 才是在任何分布下都一致且易估計的版本。
- 與 [Sharpe (1994)](sharpe-1994-sharpe-ratio.md) 的取向不同:Sharpe 在均值—變異數架構下工作,Artzner 等人則指出以標準差構成的度量(−E[X]+ασ 形式)違反單調性。
