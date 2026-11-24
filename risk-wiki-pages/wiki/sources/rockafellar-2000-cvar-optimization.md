---
type: source
title: Optimization of Conditional Value-at-Risk
authors: [Rockafellar, Uryasev]
year: 2000
raw_file: none
source_url: https://risknet.de/elibrary/paper/optimization-of-conditional-value-at-risk
access: full-text
version_read: 工作稿 1999-09-05(正式發表於 Journal of Risk 2(3), 21–41, 2000)
ingested: 2026-11-18
metrics: [value-at-risk, expected-shortfall]
---

# Rockafellar & Uryasev (2000) — Optimization of Conditional Value-at-Risk

## 基本資料
- 作者:R. Tyrrell Rockafellar、Stanislav Uryasev
- 發表:*Journal of Risk* 2(3), 2000;本頁讀取的是 1999 年 9 月工作稿〔版本差異待核對〕。

## 研究問題
能否找到一種在實務上可計算、可最佳化的方式,同時算出 VaR 並最小化 CVaR,用於投資組合最佳化與避險?

## 方法與資料
- 定義輔助函數 $F_\beta(x,\alpha)=\alpha+\frac{1}{1-\beta}E[(f(x,y)-\alpha)^+]$,證明對 $\alpha$ 取最小值即得 CVaR,最小值的左端點即 VaR。
- 以情境抽樣近似期望,把最小化 CVaR 化為**線性規劃**。
- 兩個數值應用:(1) 三資產投資組合(S&P 500、長期公債、小型股;常態報酬;偽隨機與 Sobol 準隨機兩種抽樣);(2) NIKKEI 蝶式選擇權部位的避險(取自 Mausser & Rosen 1999)。
- 理論前提:損失分布連續(無跳躍),有密度函數;作者明言把一般分布留給後續論文。

## 核心結論
1. CVaR 等於 $F_\beta$ 對 $\alpha$ 的最小值,且 VaR 是最小化者區間的左端點;因此最小化 CVaR 時可同時得到 VaR。
2. 當損失對決策變數為凸函數時,CVaR 對決策變數也是凸函數,最佳化屬凸規劃,不需要假設常態分布。
3. 定義上 VaR 不會超過 CVaR,因此低 CVaR 的投資組合必然 VaR 也低。
4. 若損失為常態分布且 $\beta\ge0.5$,並且期望報酬約束有效,則最小化 VaR、CVaR、變異數三者得到同一投資組合。
5. 準隨機(Sobol)抽樣的收斂明顯優於偽隨機:樣本數超過 10,000 時,與最小變異數解的差距小於 1%。
6. NIKKEI 避險範例顯示 CVaR 能捕捉 VaR 看不到的風險:同一部位在 0.95 水準下 VaR 為負(代表有 95% 機率獲利),但 CVaR 為正的大額損失;多工具同時避險也比單一工具避險大幅降低 CVaR。

## 涉及的風險指標
- [預期短缺 ES / CVaR](../metrics/expected-shortfall.md)
- [風險值 VaR](../metrics/value-at-risk.md)

## 限制與注意事項
- 連續分布與密度存在的假設只為簡化,一般(離散)分布的 CVaR 定義較複雜,留待後續;這正是 [Acerbi & Tasche (2002)](acerbi-2002-coherence-expected-shortfall.md) 後來釐清的部分。
- 數值實驗維度低(3 資產、11 工具),作者說明僅供示範。
- 論文把 CVaR 的 TCE 等價關係當作連續分布下的事實;一般分布下並不成立,見 [尾部風險度量的變體與關係](../concepts/tail-risk-measure-variants.md)。
- 發表當時作者指出 CVaR 尚未成為金融業標準,在保險業則逐漸受到採用(截至該論文時點)。

## 與其他論文的關係
- 承接 [Artzner et al. (1999)](artzner-1999-coherent-measures.md) 對 VaR 的批評;文中引用 Pflug(2000)證明 CVaR 的一致性。
- 其 CVaR 的最小化表示式,被 [Acerbi & Tasche (2002)](acerbi-2002-coherence-expected-shortfall.md) 證明與 ES 為同一物件。
