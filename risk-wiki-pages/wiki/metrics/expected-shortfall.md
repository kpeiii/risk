---
type: metric
name_zh: 預期短缺
name_en: Expected Shortfall
abbr: ES(亦稱 CVaR)
updated: 2026-11-18
source_count: 3
---

# 預期短缺(Expected Shortfall, ES)/ 條件風險值(CVaR)

## 定義
「最差 100α% 情境的平均損失」。Acerbi & Tasche 證明,在其定義下 **ES 與 CVaR 是同一個物件**。名稱混亂的整理見 [尾部風險度量的變體與關係](../concepts/tail-risk-measure-variants.md)。

> 符號約定與 [VaR](value-at-risk.md) 相同:Acerbi & Tasche 的 α 是尾部機率;Rockafellar & Uryasev 的 β 是信賴水準(α = 1 − β)。

## 公式
以損失 $L=-X$、尾部機率 α 表示。分位數積分形式(Acerbi & Tasche):

$$ES_\alpha(X) = -\frac{1}{\alpha}\int_0^\alpha q_u(X)\,du$$

最小化形式(Rockafellar & Uryasev 與 Acerbi & Tasche 的 CVaR 定義,改寫成以 α 為尾部機率):

$$ES_\alpha = \min_{t\in\mathbb{R}}\left\{\, t + \frac{1}{\alpha}\,E\big[(L-t)^+\big]\right\}$$

最小值的達成點所組成的區間,其左端點就是 VaR(Rockafellar & Uryasev, Theorem 1)。因此**不必先算 VaR 就能算 CVaR**,VaR 反而是副產品。

情境抽樣近似(q 個情境):$\;t + \frac{1}{q\alpha}\sum_k (L_k - t)^+$,對 t 為凸的分段線性函數,可化為線性規劃。

## 白話解釋
VaR 只告訴你「進入最差 α 區域的門檻」;ES 告訴你「進去之後平均有多慘」。

## 數值範例(說明用範例)
沿用 [VaR 頁](value-at-risk.md) 的 20 個等機率情境(萬元):−30, −12, −8, −5, −3, −2, −1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 8, 10。

- α = 5%:最差 1 個情境 → **ES = 30 萬**(同一資料 VaR = 12 萬)。
- α = 10%:最差 2 個情境 → ES = (30 + 12)/2 = **21 萬**(VaR = 8 萬)。

論文中的常態分布數字(Rockafellar & Uryasev Table 4,最小變異數組合的月損失,以小數表示):

| 信賴水準 β | VaR | CVaR |
|---|---|---|
| 0.90 | 0.0678 | 0.0970 |
| 0.95 | 0.0902 | 0.1159 |
| 0.99 | 0.1321 | 0.1530 |

## 核心假設
- 只要求 $E[X^-]<\infty$(損失的期望存在);**不要求常態、也不要求分布連續**(Acerbi & Tasche 的定義)。
- 若使用 Rockafellar & Uryasev 原始論文的推導,則假設損失分布有密度且連續;他們明言一般分布留待後續。
- 估計端:ES 可用樣本最差 ⌊nα⌋ 筆的平均估計,且在分位數不唯一時仍收斂。
- 在損失為常態且 β ≥ 0.5 時,VaR 與 CVaR 都只是 μ + c·σ 的形式(c 為正),因此最小化兩者與最小化變異數可得同一組合(Rockafellar & Uryasev)。

## 優點
- **一致性風險度量**:滿足平移不變、次可加、正齊次、單調(Acerbi & Tasche, Proposition 3.1)。
- 對信賴水準連續,且隨 α 變小而單調上升:信賴水準小幅調整不會使結果劇烈跳動。
- VaR ≤ ES,所以最小化 ES 的組合其 VaR 也低。
- 損失對決策為凸時,ES 對決策為凸,可用**線性規劃**最佳化,即使報酬不是常態分布(Rockafellar & Uryasev)。
- 可同時處理線性與非線性工具(選擇權、期貨)、市場、信用與營運風險(依 Rockafellar & Uryasev 所述適用範圍)。
- 對 NIKKEI 例,ES 能辨識 VaR 看不到的風險,並使多工具同時避險比單一工具避險更有效。

## 缺點與限制
- 仍只是單一數字:不描述尾部內部的分散程度(ES 本身是平均)。
- 蒙地卡羅估計收斂較慢:偽隨機抽樣在數千到上萬樣本時,CVaR 與最小變異數解的差距仍可達約 2–5%,準隨機(Sobol)明顯較好(Rockafellar & Uryasev, Table 5–6)。
- 一致性公理並未唯一決定風險度量(Artzner 等人);選用 ES 仍是在一類度量中的選擇。
- Rockafellar & Uryasev 發表當時指出 CVaR 尚未成為金融業標準,在保險業較受歡迎(1999–2000 時點;現況〔待核對〕)。
- 尾部資料少:資料稀少時的估計誤差大小,尚無已 ingest 論文討論。

## 適用情境
- **適合**:需要關注尾部嚴重程度、離散或非常態報酬、信用與集中度風險、需用大量情境做投資組合最佳化或避險時。
- **不適合 / 需搭配其他指標**:只需報告單一門檻、或資料極少無法穩定估計尾部時。

## 相關論文
- [Artzner et al. (1999)](../sources/artzner-1999-coherent-measures.md) — 以 TCE / WCE 的形式提出此概念。
- [Rockafellar & Uryasev (2000)](../sources/rockafellar-2000-cvar-optimization.md) — 提出可最佳化的 CVaR 表示式與 LP 演算法。
- [Acerbi & Tasche (2002)](../sources/acerbi-2002-coherence-expected-shortfall.md) — 證明一般分布下 ES = CVaR 且一致。

## 爭議與不確定性
- **TCE 與 ES 是否相等**:Artzner 等人的行文讓人以為 TCE 近似一致;Rockafellar & Uryasev 與 Pflug 的敘述把 CVaR 當作 TCE;Acerbi & Tasche 指出僅在分布連續等條件下成立,一般情況 TCE 不具次可加性。
- **建議立場**:以 Acerbi & Tasche 的 ES 定義為準,並避免僅以「超過 VaR 的條件平均」來定義(離散分布會失效)。
- **信心程度**:高(數學結果有明確證明,且三篇論文方向一致);但實務表現(估計誤差、回測)尚無已 ingest 論文涵蓋。
