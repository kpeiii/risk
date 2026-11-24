---
type: concept
updated: 2026-11-18
source_count: 3
---

# 一致性風險度量(Coherent Risk Measure)

## 概念
Artzner 等人提出的一組公理,用來規範「適合拿來訂資本要求、保證金或風險限額」的風險度量。風險對象是**未來淨值** $X$(不是價值變動),參考工具的總報酬為 $r$。風險度量 $\rho(X)$ 的意義:為使部位可接受,所需額外投入並投資於參考工具的最小現金。

## 四條公理(Artzner et al., 1999)
1. **平移不變性(T)**:$\rho(X+\alpha r)=\rho(X)-\alpha$。加現金就等量降低風險。
2. **次可加性(S)**:$\rho(X_1+X_2)\le\rho(X_1)+\rho(X_2)$。「合併不產生額外風險」。
3. **正齊次性(PH)**:$\rho(\lambda X)=\lambda\rho(X)$,$\lambda\ge0$。
4. **單調性(M)**:$X\le Y\Rightarrow\rho(Y)\le\rho(X)$。

同時滿足 T、S、PH、M 稱為一致。另有**相關性公理(R)**:對 $X\le0$ 且 $X\ne0$ 有 $\rho(X)>0$,用來避免風險集中未被偵測,但不屬於「一致」的定義。

## 為什麼要次可加性
Artzner 等人列出四個理由:(a) 否則交易人可以開兩個帳戶,分開計算保證金較低;(b) 否則公司有動機把自己拆成兩個獨立法人以降低資本要求;(c) 沒有防火牆的集團,所需資本應不高於防火牆隔離的情況;(d) 兩個交易台分別算風險後,主管可據以分配現金限額——**分權管理**的前提。

## 表示定理
有限樣本空間下,$\rho$ 為一致的若且唯若存在一組機率測度 $\mathcal P$(廣義情境),使得

$$\rho(X)=\sup_{P\in\mathcal P}E_P[-X/r]$$

- 情境越多,度量越保守。
- 模型風險可以藉由把來自不同模型的分布納入 $\mathcal P$ 處理。
- SPAN 的 16 個情境計算就是這個形式的實例(14 個完整損失情境加 2 個極端情境、極端情境只取 35% 損失)。
- 反向建構:給定一批「標準風險」及其保證金,可延伸出涵蓋它們的最大一致度量(SEC 規則的對偶)。

## 哪些度量被排除
- 單調性排除 $\rho(X)=-E[X]+\alpha\sigma(X)$(均值加標準差型)。
- 次可加性排除「半變異數型」$\rho(X)=-E[X]+\sigma((X-E[X])^-)$。
- 分位數型 [VaR](../metrics/value-at-risk.md) 滿足 T、PH、M,但**不滿足 S**。

## 數值範例:VaR 為何破壞次可加性(取自 Acerbi & Tasche, Example 5.4)
三個狀態 ω₁、ω₂、ω₃,機率分別為 p、p、1−2p。令 p = 3%、名目 N = 100。兩個債券 $X_i$:在 ω_i 損失 100,其餘為 0(可想成兩個違約事件不重疊的債券)。取 α = 5%(p < α < 2p):

| | $X_1$ 或 $X_2$ | $X_1+X_2$ | 是否次可加 |
|---|---|---|---|
| VaR₅% | 0 | 100 | 否(100 > 0+0) |
| ES₅% | 100 × 3%/5% = 60 | 100 | 是(100 ≤ 120) |

VaR 說兩個債券各自「沒風險」,合起來卻有 100;ES 則始終滿足不等式。

## 限制
- 公理沒有唯一決定某個度量,而是刻畫一整類;選擇仍須額外的經濟考量(Artzner 等人)。
- 原始論文限於有限樣本空間與單一期間;一般機率空間版本見 Delbaen (1998) 的工作論文〔本 wiki 尚未 ingest〕。
- 一致性是「資本要求用風險度量」的標準;[Sharpe ratio](../metrics/sharpe-ratio.md) 等績效比率並不是為此設計。

## 相關論文
[Artzner et al. (1999)](../sources/artzner-1999-coherent-measures.md)、[Acerbi & Tasche (2002)](../sources/acerbi-2002-coherence-expected-shortfall.md)、[Rockafellar & Uryasev (2000)](../sources/rockafellar-2000-cvar-optimization.md)(引用 Pflug 證明 CVaR 一致)。
