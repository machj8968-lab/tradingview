# TG XAU 日線方向 v1｜驗收紀錄

## 已完成

- Pine Script v6 架構檢查
- EMA20 / EMA50 評分規則檢查
- EMA slope 評分規則檢查
- HH/HL、LH/LL 市場結構評分檢查
- DMI 方向評分檢查
- ADX 只作強度門檻，不直接加減方向分數
- 總分範圍 -6 ～ +6
- 五級 Bias 邊界測試
- Daily-only guard
- `barstate.isconfirmed` 收線確認路徑
- Confirmed Pivot 3/3，不使用 developing pivot
- Alert 僅在已確認 Daily bar 且 Bias 狀態改變時觸發
- 中文 Dashboard / 中文 Inputs / 中文 Alerts
- EMA 快線 / 慢線名稱明確化

## Non-repaint 設計

1. 正式 Bias 在即時 Daily K 未收線時，使用上一根已收線 bar 的 candidate 值。
2. Pivot 只有 `ta.pivothigh()` / `ta.pivotlow()` 在右側 K 數完整形成後才更新市場結構。
3. 正式 EMA 顯示同樣在未收線 Daily K 上維持上一根已確認值，使畫面與正式 Bias 定義一致。
4. 不使用 `request.security()`，因此本支 Daily-only 指標不存在高週期 request lookahead 問題。

## 自動測試

- `tests/test_bias_logic.py`：數學契約與分類邊界
- `tests/static_contract_check.py`：Pine 架構、禁用功能、中文 UI 契約

## 尚需 TradingView 端驗證

本環境沒有 TradingView 官方 Pine Compiler，因此「官方 Compile」不能在本地偽裝成已完成。
上傳 TradingView Pine Editor 後需確認：

- Pine v6 Compile 成功
- OANDA:XAUUSD 1D 正常顯示
- Dashboard 中文字型與欄寬正常
- 其他 timeframe 只顯示日線限定提示
- 即時未收線 Daily K 的正式 Bias 不跳動
- Alert 設成 Once Per Bar Close 後行為符合預期
