---
type: comparison
updated: 2026-11-18
source_count: 6
---

# 四種風險指標總比較:VaR、ES、Sharpe ratio、MDD

> 這四者不屬於同一種東西:**VaR 與 ES 是「損失分布尾部」的風險度量**;**Sharpe ratio 是「報酬對波動」的績效比率**;**MDD 是「路徑」統計量**。比較時要先分清楚用途。

## 總表

| 面向 | [VaR](../metrics/value-at-risk.md) | [ES / CVaR](../metrics/expected-shortfall.md) | [Sharpe ratio](../metrics/sharpe-ratio.md) | [MDD](../metrics/maximum-drawdown.md) |
|---|---|---|---|---|
| 類型 | 尾部風險度量 | 尾部風險度量 | 風險調整績效比率 | 路徑型下跌統計 |
| 衡量什麼 | 最差 α 情境的損失門檻 | 最差 α 情境的平均損失 | 每單位波動的超額報酬 | 高點到低點最大跌幅 |
| 需要的輸入 | 損益分布與分位數 | 損益分布的尾部 | 均值與標準差(差額報酬) | 價值或報酬的時間序列路徑 |
| 核心假設 | 需機率模型;常態下才次可加 | 只需損失期望存在;不需常態 | 均值—變異數足夠;IID 簡化公式 | 理論基準為布朗運動帶漂移(摘要層級) |
| 一致性 | 否 | 是 | 不適用(非資本要求用度量) | 尚無已 ingest 論文討論 |
| 主要優點 | 簡單、普及、監管對接 | 一致、看尾部、可最佳化 | 尺度獨立、可做統計檢定 | 直觀、反映持續性損失 |
| 主要缺點 | 破壞次可加、忽略尾部嚴重度 | 尾部資料少時估計不穩〔推論,尚無論文驗證〕 | 忽略偏態/峰態/相關性、年化易誤用 | 依賴期間長度與取樣頻率、只看單一最糟事件 |
| 論文證據強度 | 高(三篇) | 高(三篇) | 高(兩篇) | **低**(僅摘要層級) |

## 適用情境對照

| 情境 | 建議 | 依據 |
|---|---|---|
| 訂資本要求、限額、分權管理 | ES(次可加 → 可分解) | Artzner et al. |
| 報告單一門檻、對接既有監管 | VaR(附局限說明) | Artzner et al.; Rockafellar & Uryasev |
| 用大量情境最佳化投資組合或避險 | ES / CVaR(線性規劃) | Rockafellar & Uryasev |
| 比較同類基金(序列相關小) | Sharpe ratio | Sharpe; Lo |
| 比較有序列相關的基金(如對沖基金) | 以 Lo 的穩健估計年化後再比 | Lo |
| 評估投資人對持續性虧損的承受度 | MDD(搭配報酬做 Calmar) | Magdon-Ismail & Atiya(摘要層級) |
| 報酬分布明顯偏態或厚尾 | 不要只靠 Sharpe;補 ES | Sharpe(明言不涵蓋高階動差) |

## 關鍵交叉結論
1. **VaR → ES 的演進**:VaR 破壞次可加性(Artzner)→ CVaR 提供可最佳化的替代(Rockafellar & Uryasev)→ ES 釐清並統一一般分布下的定義(Acerbi & Tasche)。詳見 [VaR 與 ES 比較](var-vs-expected-shortfall.md) 與 [尾部風險度量的變體](../concepts/tail-risk-measure-variants.md)。
2. **Sharpe ratio 的統計不確定性常被低估**:五年月資料的 Sharpe ratio 信賴區間可能涵蓋 0([Sharpe ratio 頁](../metrics/sharpe-ratio.md) 的算例);年化時更要檢查序列相關([IID 假設與序列相關](../concepts/iid-and-serial-correlation.md))。
3. **Sharpe 與 MDD 都隨時間縮放,但方式不同**:Sharpe ratio 在 IID 下隨 √T 增長;期望 MDD 在正漂移下約隨 ln T 增長(摘要層級〔待核對〕)。因此兩者都不能在不同長度的紀錄間直接比較。
4. **一致性公理只對「資本要求型風險度量」有意義**,不應拿來評價 Sharpe ratio 或 MDD 的優劣。

## 爭議與不確定性
- 本表中「尾部資料少時 ES 估計不穩」是 Agent 的推論,已 ingest 論文只顯示蒙地卡羅收斂速度(Rockafellar & Uryasev),沒有直接比較 ES 與 VaR 的估計誤差。
- MDD 一欄只有摘要層級來源,建議補讀全文後再更新本表。
- **建議立場**:同時看一個尾部度量(ES)與一個績效比率(Sharpe,附標準誤),MDD 作為輔助的直觀指標。
- **信心程度**:中。VaR/ES/Sharpe 部分有紮實理論來源;缺少實證回測與跨市場資料。
