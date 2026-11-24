---
type: concept
updated: 2026-11-18
source_count: 3
---

# 尾部風險度量的變體與關係(TCE / WCE / CVaR / ES)

文獻中對「超過 VaR 的條件期望」有多個名稱與定義,常被誤以為相同。此頁整理它們的定義與關係,主要依 [Acerbi & Tasche (2002)](../sources/acerbi-2002-coherence-expected-shortfall.md)。

## 定義對照(α 為尾部機率)

| 名稱 | 直覺定義 | 出處 | 一致嗎? |
|---|---|---|---|
| TCE(尾部條件期望,下/上兩版) | 損失超過下/上 VaR 分位數時的條件平均 | Artzner et al. 1999 | **否**(一般不具次可加性) |
| WCE(最壞條件期望) | 在所有機率 > α 的事件上,條件期望的最壞者 | Artzner et al. 1999 | 是,但依賴底層機率空間 |
| CVaR | $\min_t\{t+\frac1\alpha E[(L-t)^+]\}$ | Rockafellar & Uryasev 2000;Pflug 2000 | 是 |
| ES / tail mean | 最差 100α% 情境的平均損失 | Acerbi et al. 2001;Acerbi & Tasche 2002 | 是(任意分布) |
| 其他別名:mean excess loss、mean shortfall、tail VaR | | Rockafellar & Uryasev | — |

## 關係
- **ES = CVaR**(同一物件)。
- 不等式:TCE(下) ≤ TCE(上) ≤ ES;TCE ≤ WCE ≤ ES(Acerbi & Tasche, Cor. 5.2)。
- 分布連續(或滿足一些邊界條件)時:ES = WCE = TCE(Cor. 5.3)。
- 分布有質量點(離散、混合)時三者可能不同,且 TCE、WCE 對 α 可能不連續,ES 則連續。
- ES 等於「在所有能表示同一分布的機率空間上,取 WCE 的最大值」(Cor. 6.3),即 ES 是 WCE 的穩健版本。
- Artzner 等人另證:在基底機率為均勻、且風險值彼此不同的有限空間,TCE = WCE(Prop. 5.3);任何只依賴分布且大於等於 VaR 的一致度量,在該情況下都不小於 WCE(Prop. 5.4)。

## 為什麼名稱會造成混亂
- Acerbi & Tasche 指出,Artzner 等人 1997 年的短文〈Thinking Coherently〉(Risk)中有一處措辭容易讓讀者以為 TCE 與 WCE 相同(1999 年論文本身則已提醒兩者在一般情況下不同)。
- Pflug 把 CVaR 寫成等於 TCE 且不加條件;Acerbi & Tasche 指出僅在分布連續等條件下成立。
- Rockafellar & Uryasev 在連續分布假設下定義 CVaR,此時與 TCE 一致;一般分布下需用最小化形式作為定義。

## 實務含意
- 實作時**用最小化形式或分位數積分形式**,避免用「找出超過 VaR 的樣本再取平均」(離散資料下可能不一致、不連續)。
- 估計端:樣本最差 ⌊nα⌋ 筆的平均會收斂到 ES,即便 VaR 的順序統計量估計量不收斂(Acerbi & Tasche, Prop. 4.1)。

## 相關頁面
[預期短缺 ES / CVaR](../metrics/expected-shortfall.md)、[風險值 VaR](../metrics/value-at-risk.md)、[一致性風險度量](coherent-risk-measure.md)。
