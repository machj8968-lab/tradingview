# 驗收狀態

## 已完成的本地 / CI 檢查

- 所有 Pine 檔案要求 `//@version=6`。
- 所有模組使用 `indicator()`，禁止 `strategy()`。
- D/W/M Bias 各自限制到原生 1D/1W/1M，且不使用跨週期 `request.security()`。
- D/W/M Bias 維持五級計分契約與 closed-bar confirmed 狀態。
- S/R、Liquidity、Fib 使用 confirmed pivots。
- Liquidity sweep 與 FVG mitigation 只在 bar close 確認。
- Key Levels 的 Previous D/W/M High/Low 使用 `[1] + lookahead_on` 取得已確認高週期資料。
- FVG 使用標準 3-candle gap 並加入 ATR 最小尺寸過濾。
- Python contract tests 與 delimiter sanity checks 已加入 GitHub Actions。

## 仍需 TradingView 實機驗收

GitHub CI 不是 TradingView 官方 Pine compiler，因此每一支新 Pine 首次使用仍必須在 Pine Editor：

1. Compile。
2. 加到 XAUUSD 圖表。
3. 確認畫面沒有 runtime error。
4. 依建議週期目視檢查線、box、label 是否過密。
5. 若 TradingView 回報 compiler error，以 Pine Editor 的實際訊息為最高優先修正依據。