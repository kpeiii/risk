---
type: concept
updated: 2026-11-18
source_count: 2
---

# IID 假設與序列相關(對 Sharpe ratio 的影響)

## 概念
許多風險與績效指標的簡單公式(例如 Sharpe ratio 的標準誤與 √T 年化)隱含報酬**獨立同分布(IID)**。實際報酬常有序列相關、波動度時變等,使這些簡單公式失準。[Lo (2002)](../sources/lo-2002-statistics-sharpe-ratios.md) 系統性地量化這個問題。

## 三種設定(Lo, 2002)
1. **IID**:估計量漸近常態,$\text{SE}(\widehat{SR})\approx\sqrt{(1+\tfrac12SR^2)/T}$。均值估計誤差與變異數估計誤差漸近獨立。
2. **平穩(stationary)**:允許序列相關、條件異質變異等;用 GMM 估計並以 Newey–West 處理自相關,得穩健標準誤。
3. **時間聚合**:月度轉年度等頻率轉換,需加入前 q−1 階自相關。

## 時間聚合公式
IID:$SR(q)=\sqrt q\,SR$。一般平穩:$SR(q)=\eta(q)\,SR$,其中

$$\eta(q)=\frac{q}{\sqrt{q+2\sum_{k=1}^{q-1}(q-k)\rho_k}}$$

AR(1)(自相關係數 ρ):

$$\eta(q)=q\left[q+\frac{2\rho}{1-\rho}\left(q-\frac{1-\rho^q}{1-\rho}\right)\right]^{-1/2}$$

驗算:ρ = 0 時退化為 $\sqrt q$;ρ = 0.2、q = 12 時得 2.88,與論文 Table 2 一致。

## 數字
q = 12(月 → 年)的係數:

| 月度一階自相關 ρ | 年化係數 η(12) |
|---|---|
| −20% | 4.17 |
| 0%(IID) | 3.46 |
| +20% | 2.88 |

- 正序列相關使多期變異數增長快於 q,分母變大,年化 Sharpe ratio 變小;負序列相關則相反。
- 對沖基金的月度序列相關高(一階自相關 −20.2% 到 49.0%),IID 年化可高估逾 65%;例:Mortgage-backed securities 從 4.03 降為 2.44,Risk arbitrage A 反而從 3.25 升為 3.83;12 檔基金的排名也大幅改變。
- 10 檔共同基金序列相關小,兩種年化差異不大。

## 穩健估計的代價與診斷
- 穩健估計量需額外估計自相關,漸近變異數更大。例:月度 Sharpe ratio = 1.00 時,年化(q = 12)的穩健估計變異數為 IID 估計的 334%。
- 建議先用 **Ljung–Box Q 統計量**檢驗序列相關;不顯著就不必用穩健版。

## 與 Sharpe (1994) 的關係
[Sharpe (1994)](../sources/sharpe-1994-sharpe-ratio.md) 在簡化情況(各期無序列相關)導出 √T 縮放,並提醒複利與序列相關會使情況更複雜;Lo 補上其定量處理。

## 限制
漸近結果依賴大樣本;小樣本表現、偏態與厚尾的影響未被處理。

## 相關頁面
[Sharpe ratio](../metrics/sharpe-ratio.md)
