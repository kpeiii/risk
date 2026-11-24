---
type: metric
name_zh: 風險值
name_en: Value at Risk
abbr: VaR
updated: 2026-11-18
source_count: 3
---

# 風險值(Value at Risk, VaR)

## 定義
在指定的尾部機率 α(例如 1% 或 5%)下,損益分布的分位數取負號:損失超過這個門檻的機率不超過約 α。

> **符號約定提醒**:[Artzner et al.](../sources/artzner-1999-coherent-measures.md) 與 [Acerbi & Tasche](../sources/acerbi-2002-coherence-expected-shortfall.md) 用 α 表示**尾部機率**(小的數字,如 0.05);[Rockafellar & Uryasev](../sources/rockafellar-2000-cvar-optimization.md) 用 β 表示**信賴水準**(大的數字,如 0.95)。兩者換算為 α = 1 − β。閱讀論文時務必先確認這點。

## 公式
令 $X$ 為期末損益(正為獲利),參考工具報酬 $r=1$。依 Artzner 等人的定義(使用上分位數):

$$\text{VaR}_\alpha(X) = -\inf\{x : P[X \le x] > \alpha\}$$

Acerbi 與 Tasche 同樣採用上分位數 $x^{(\alpha)}$,即 $\text{VaR}_\alpha=-x^{(\alpha)}$。分位數不唯一時,使用下分位數 $\inf\{x:P[X\le x]\ge\alpha\}$ 會得到不同的 VaR——這是 VaR 沒有唯一「顯然定義」的原因。

## 白話解釋
「在最差的 α 比例情境之外,損失的門檻是多少」。它回答「損失至少要超過多少才算落入最差的 α」,但**不回答超過之後會虧多少**。

## 數值範例(說明用範例)
20 個等機率情境的損益(萬元):−30, −12, −8, −5, −3, −2, −1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 8, 10。

- α = 5%:$P[X\le -30]=0.05$ 不大於 α,$P[X\le -12]=0.10>\alpha$,故上分位數為 −12,**VaR = 12 萬**。若改用下分位數,VaR 變成 30 萬。
- α = 10%:VaR = 8 萬。
- 情境中那個 −30 的極端損失,在 α = 5% 的 VaR(12 萬)裡完全沒被反映。對照 [ES](expected-shortfall.md):同一資料 ES₅% = 30 萬。

## 核心假設
- 需要一個明確的機率模型(Artzner 等人稱為 model-dependent);論文指出該用估計的實際機率或審慎的主觀機率並不明確。
- 需事先固定持有期間(例如對沖再調整的間隔、清算所需時間)與信賴水準。
- 在**聯合常態分布**且 α < 0.5 時,分位數型 VaR 才滿足次可加性,因為此時 VaR 等於均值加上常數乘以標準差,而標準差滿足次可加。
- 關於一致性的完整討論見 [一致性風險度量](../concepts/coherent-risk-measure.md)。

## 優點
- 滿足平移不變性、正齊次性與單調性三條公理(Artzner 等人)。
- 實務與監管普遍使用;Artzner 等人引述一句話:監管者喜歡 VaR 是因為「可以被管制」,並解讀這指向建立與公告一套合理情境的困難。
- 在常態分布下 VaR 與標準差成比例,計算簡單(Rockafellar & Uryasev)。

## 缺點與限制
- **不具次可加性**,導致合併風險可以比分別風險之和更大,並使可接受集合非凸。Artzner 等人的三個例子:
  1. 兩個互補的數位選擇權(各自的觸發機率 0.8%):兩位交易員分別賣出同一種選擇權時,1% VaR 皆為負值;同一人同時賣出 A 與 B 時,1% VaR 卻為正值(1000 − l − u,l、u 為兩選擇權的初始價格)。
  2. 信用債券集中度:1,000,000 全買單一公司債,5% VaR 為負(顯示「沒有風險」);分散到 100 家公司後,至少兩家違約的機率大於 0.18,使 5% VaR 轉為正值——**分散反而讓 VaR 升高,而同一家公司債的集中風險未被偵測**。
  3. 風險配置:兩個代理人交換風險後,雙方都改善的 Pareto 配置無法被 VaR 辨識。
- **忽略尾部嚴重程度**:只看機率,不看超過門檻後的損失大小(「how bad is bad」)。
- 難以最佳化:用情境計算時,VaR 作為持倉的函數行為不佳,可能有多個局部極值(Rockafellar & Uryasev 引述 Mausser & Rosen 與 McKay & Keefer)。
- 可能為負而 CVaR 仍為大正值:Rockafellar & Uryasev 的 NIKKEI 部位在 0.95 水準下 VaR = −205,927(即 95% 機率獲利至少此數)、CVaR = 1,183,040(其餘情況平均虧損)。數字單位依原文〔待核對〕。
- 離散分布下對信賴水準不連續,且分位數可能不唯一(Acerbi & Tasche)。
- Artzner 等人在論文中表示,就他們所知,當時沒有有組織的交易所以 VaR 作為保證金要求的基礎(1998 年時點;現況〔待核對〕)。

## 適用情境
- **適合**:報酬近似聯合常態、以線性部位為主、僅作為「門檻值」的報告或監管指標;需要與既有監管框架對接時。
- **不適合**:跨部門加總與分權限額管理、信用或集中度風險、離散或厚尾的尾部風險、需要最佳化大量情境的投資組合。這些情境建議看 [ES / CVaR](expected-shortfall.md)。

## 相關論文
- [Artzner et al. (1999)](../sources/artzner-1999-coherent-measures.md) — 以公理與反例批評 VaR。
- [Rockafellar & Uryasev (2000)](../sources/rockafellar-2000-cvar-optimization.md) — 說明 VaR 難最佳化,並提供同時算 VaR 與最小化 CVaR 的方法。
- [Acerbi & Tasche (2002)](../sources/acerbi-2002-coherence-expected-shortfall.md) — 釐清分位數不唯一與 VaR 在離散分布下的不連續。

## 爭議與不確定性
目前已 ingest 的論文在「VaR 次可加性在實務上有多嚴重」上沒有互相矛盾的結論;三篇都同意其缺陷,差別在於提出的補救方式(WCE / CVaR / ES)。
- **建議立場**:把 VaR 當作報告用的門檻值,不用於加總、限額分配與最佳化。
- **信心程度**:中。三篇論文皆為理論與小型範例,缺乏實證資料(如真實投資組合中違反次可加性的頻率);此點尚無已 ingest 論文涵蓋。
