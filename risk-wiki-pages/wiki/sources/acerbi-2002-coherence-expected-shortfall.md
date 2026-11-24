---
type: source
title: On the coherence of Expected Shortfall
authors: [Acerbi, Tasche]
year: 2002
raw_file: none
source_url: https://arxiv.org/pdf/cond-mat/0104295v4
access: full-text
version_read: arXiv v4(2001-10-09);正式版為 Journal of Banking & Finance 26, 1487–1503, 2002(arXiv 最新為 v5)
ingested: 2026-11-18
metrics: [expected-shortfall, value-at-risk]
---

# Acerbi & Tasche (2002) — On the coherence of Expected Shortfall

## 基本資料
- 作者:Carlo Acerbi、Dirk Tasche
- 發表:*Journal of Banking & Finance* 26, 2002;本頁讀取 arXiv v4,與 v5 或正式版的差異〔待核對〕。

## 研究問題
文獻中有多個「超過 VaR 的條件期望」版本(TCE、WCE、CVaR、ES)。它們之間是什麼關係?哪一個在任意分布(含離散、有跳躍的分布)下都是一致且易於估計的?

## 方法與資料
純數學推導,配一個三狀態的反例(Example 5.4)。比較五個概念:WCE、TCE(上下兩種)、CVaR、ES 及其負值 α-tail mean。

## 核心結論
1. **ES 在任何分布下都是一致的風險度量**,且對信賴水準 α 連續、隨 α 單調(α 越小風險越大)。
2. **ES 與 CVaR 是同一個物件**(Corollary 4.3);Pflug 所說的 CVaR = TCE 並非無條件成立,僅在分布連續等條件下為真。
3. **TCE 一般不具次可加性**:Example 5.4 以兩個互不重疊違約的債券說明 VaR 與 TCE 都可能違反次可加性。
4. 不等式:$TCE_{lower}\le TCE_{upper}\le ES$,且 $TCE\le WCE\le ES$;分布連續時 ES = WCE = TCE。
5. ES 可寫成所有分位數的平均:$ES_\alpha=-\frac1\alpha\int_0^\alpha q_u\,du$。
6. 估計上,樣本最差 $\lfloor n\alpha\rfloor$ 筆觀測值的平均會收斂到 tail mean(強大數律),即使在分位數不唯一、VaR 的順序統計量估計量失效的情況下仍成立。
7. ES 是 WCE 的穩健版本:ES 等於在所有能表示同一分布的機率空間上取 WCE 的最大值。

## 涉及的風險指標
- [預期短缺 ES / CVaR](../metrics/expected-shortfall.md)
- [風險值 VaR](../metrics/value-at-risk.md)

## 限制與注意事項
- 全文是理論性質,沒有實證資料。
- WCE 本身依賴底層機率空間的結構,僅在理論上有用。
- 作者指出 TCE 的天然估計量在分位數不唯一時有收斂問題。

## 與其他論文的關係
- **修正並補完** [Artzner et al. (1999)](artzner-1999-coherent-measures.md):原文的 TCE 被暗示接近一致,本文證明一般不然;一致且好算的是 ES。
- **統一** [Rockafellar & Uryasev (2000)](rockafellar-2000-cvar-optimization.md) 的 CVaR:一般分布下 CVaR 的最小化定義等於 ES。
- 詳細關係整理於 [尾部風險度量的變體與關係](../concepts/tail-risk-measure-variants.md)。
