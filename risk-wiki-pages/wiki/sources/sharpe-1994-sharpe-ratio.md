---
type: source
title: The Sharpe Ratio
authors: [Sharpe]
year: 1994
raw_file: none
source_url: https://web.stanford.edu/~wfsharpe/art/sr/sr.htm
access: full-text
version_read: 作者在 Stanford 網站上的重印版(原載 Journal of Portfolio Management, Fall 1994, 21(1), 49–58;部分公式以圖片呈現,本頁依文字敘述重建〔待核對〕)
ingested: 2026-11-18
metrics: [sharpe-ratio]
---

# Sharpe (1994) — The Sharpe Ratio

## 基本資料
- 作者:William F. Sharpe
- 發表:*Journal of Portfolio Management* 21(1), 1994;本頁讀取作者網站上的重印版。公式在原頁面為圖片,以下公式依文字敘述與常見形式重建,標〔待核對〕。

## 研究問題
1966 年作者提出「報酬對變異性比率(reward-to-variability ratio)」,如今通稱 Sharpe ratio。本文要把原始定義一般化(基準不限於無風險資產),並說明它在什麼條件下可以有效地總結一個投資策略。

## 方法與資料
- 理論推導,建立在 Markowitz 的均值—變異數架構上(假設單期報酬的均值與標準差足以評價投資組合)。
- 定義事前(ex ante)與事後(ex post)兩種版本,並分析尺度獨立性、時間相依性、與既有投資組合結合時的最佳決策。
- 以少量數字範例說明(如整體股市年超額報酬均值 6%、標準差 15%,Sharpe ratio 為 0.40)。無實證資料集。

## 核心結論
1. Sharpe ratio 應以**差額報酬(differential return)**計算,即基金報酬減基準報酬,是「零投資策略」的報酬。原始版本的基準是無風險利率。
2. 事後版本與 t 統計量密切相關:t 統計量等於 Sharpe ratio 乘以觀測期數的平方根。
3. **尺度獨立**:改變名目價值會同時等比例改變均值與標準差,比率不變。
4. **時間相依**:在各期差額報酬無序列相關的簡化情況下,T 期的 Sharpe ratio 為單期的 √T 倍;實務上常據此年化,但複利與序列相關會使關係更複雜。
5. 若既有部位是無風險資產,最佳做法是選 Sharpe ratio 最高的基金,再用借貸調整到想要的風險水準。若既有部位有風險,只有在候選基金與其他持有部位的相關性相近時,選最高 Sharpe ratio 才合理。
6. 對彼此不相關的多個策略,最佳風險配置應與其 Sharpe ratio 成比例。
7. 用「預期報酬/標準差」(不扣基準)比較基金可能得出錯誤選擇;例:X(5%/10%)與 Y(8%/20%)、無風險利率 3%,以超額報酬計 Y 較優(0.25 對 0.20)。
8. 作者警告:未經調整的事後 Sharpe ratio 當作事前預測值的替代品,值得嚴重質疑。

## 涉及的風險指標
- [Sharpe ratio](../metrics/sharpe-ratio.md)

## 限制與注意事項
- 只用到均值與標準差,不涵蓋偏態、峰態等其他動差(作者明言超出本文範圍)。
- 比率不包含與其他資產的相關性資訊;相關性不同時需另外補充。
- 作者強調事後比率與無偏預測之間的關係留待他文討論。

## 與其他論文的關係
- [Lo (2002)](lo-2002-statistics-sharpe-ratios.md) 補上本文留白的統計性質:估計誤差、序列相關下的年化,並指出 √T 年化僅在特定條件下正確。
- 與 [Artzner et al. (1999)](artzner-1999-coherent-measures.md) 取向不同:本文在均值—變異數架構下評價績效,不討論風險度量的公理。
