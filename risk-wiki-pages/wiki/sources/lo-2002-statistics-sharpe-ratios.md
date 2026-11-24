---
type: source
title: The Statistics of Sharpe Ratios
authors: [Lo]
year: 2002
raw_file: none
source_url: https://traders.studentorg.berkeley.edu/papers/The-Statistics-of-Sharpe-Ratios.pdf
access: full-text
version_read: Financial Analysts Journal 58(4), 36–52, 2002 的 PDF 副本(部分數學符號在文字抽取中遺失,公式依上下文重建〔待核對〕)
ingested: 2026-11-18
metrics: [sharpe-ratio]
---

# Lo (2002) — The Statistics of Sharpe Ratios

## 基本資料
- 作者:Andrew W. Lo
- 發表:*Financial Analysts Journal* 58(4), 2002。PDF 文字抽取時希臘字母與部分公式遺失,下文公式以可驗證的數值(論文表格與正文數字)交叉核對過。

## 研究問題
Sharpe ratio 的組成部分(期望報酬與波動度)都得由資料估計,因此 Sharpe ratio 本身有估計誤差。這個誤差有多大?常見的「月度 Sharpe ratio 乘以 √12 得年度值」是否正確?

## 方法與資料
- 以大樣本漸近理論,在三種設定下推導 Sharpe ratio 估計量的分布:獨立同分布(IID)、平穩(stationary)、與時間聚合(time aggregation)。非 IID 情形使用廣義動差法(GMM)與 Newey–West 估計。
- 實證:10 檔最大共同基金(最早自 1963 年起,至 2000 年 6 月)與 12 檔對沖基金(1989–1995 年起,至 2000 年 12 月,取自 Altvest 資料庫,各基金至少 5 年月報酬)。

## 核心結論
1. IID 下,Sharpe ratio 估計量的標準誤約為 $\sqrt{(1+\tfrac12 SR^2)/T}$,可據此建立信賴區間。Sharpe ratio 越高,絕對標準誤越大(60 期樣本:SR=1.5 時 0.188,SR=3.0 時 0.303)。
2. **√q 年化規則僅在 IID 下成立。** 一般情況需以前 q−1 階自相關調整。正序列相關使調整係數低於 √q,負序列相關使其高於 √q。
3. AR(1) 範例:月度一階自相關 −20% 時,年化係數為 4.17;IID 為 3.46;+20% 時為 2.88。
4. 共同基金序列相關很小,IID 與穩健估計差異不大;對沖基金序列相關高(月度一階自相關介於 −20.2% 到 49.0%),以 IID 方式年化可高估超過 65%,基金排名也會大幅改變。例:Mortgage-backed securities 基金從 4.03 降到 2.44。
5. 穩健估計量有代價(額外估計誤差);除非序列相關顯著,不應使用。建議以 Ljung–Box Q 統計量先檢驗序列相關。
6. 作者提醒:Sharpe ratio 會隨聚合期間拉長而增大,這容易讓長期投資看起來更有吸引力,是誤導性的;它不是多期策略風險的完整摘要,不應單獨作為決策標準。

## 涉及的風險指標
- [Sharpe ratio](../metrics/sharpe-ratio.md)

## 限制與注意事項
- 漸近結果依賴大樣本;小樣本表現未在本文處理。
- 年化的校正只處理序列相關;未涉及偏態、厚尾對估計的影響。
- 實證樣本為 2000 年前後的共同基金與少量匿名對沖基金。

## 與其他論文的關係
- 補完 [Sharpe (1994)](sharpe-1994-sharpe-ratio.md) 未處理的統計性質,並修正其所述「常見年化作法」只在 IID 時成立。
- 序列相關與 IID 假設的整理見 [IID 假設與序列相關](../concepts/iid-and-serial-correlation.md)。
