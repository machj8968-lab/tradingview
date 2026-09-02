# TG XAU TradingView 指標系統 v1

## 核心原則

- 商品：XAUUSD only。
- Pine Script v6。
- 每支指標單一職責，不做超級大雜燴。
- Bias / Pivot / Liquidity / FVG 的正式狀態以已收線資料為準。
- 高週期 Key Levels 使用已確認前一週期 High/Low；目前週期 Open 因在週期開始即已知，可即時顯示。
- 視覺語言：S/R = 實線；Liquidity = 虛線；FVG = Box；Fib = 細水平線。

## 模組

### TG XAU 日線方向 v1
- 只在 1D 工作。
- EMA 20/50，EMA20 slope 3 bars，Pivot 3/3，DMI 14，ADX 14。
- Score -6..+6，輸出 強多 / 多 / 中性 / 空 / 強空。

### TG XAU 週線方向 v1
- 只在 1W 工作。
- EMA 20/50，EMA20 slope 3 bars。
- Pivot 預設 2/2，減少週線結構確認延遲。
- Score framework 與 Daily 一致。

### TG XAU 月線方向 v1
- 只在 1M 工作。
- EMA 20/50，EMA20 slope 2 bars。
- Pivot 預設 2/2；月線本身很慢，不使用 3/3 以免確認延遲過長。
- Score framework 與 Daily 一致。

### TG XAU 自動支撐壓力 v1
- 自動使用目前圖表週期。
- Confirmed Pivot 3/3。
- ATR 0.20 預設聚類附近 pivot；畫面只顯示聚類核心線。
- 價格上方最近 R1-R3、下方最近 S1-S3。

### TG XAU 關鍵價位 v1
- PDH / PDL / Daily Open。
- PWH / PWL / Weekly Open。
- PMH / PML / Monthly Open。
- Previous High/Low 使用已確認資料。

### TG XAU 流動性 v1
- v1 只做 confirmed swing EQH / EQL。
- EQH => BSL；EQL => SSL。
- ATR 0.10 預設相等容差。
- 收線確認 sweep；預設掃過後移除。

### TG XAU FVG v1
- 標準三根 K FVG。
- Bull FVG：`low > high[2]`。
- Bear FVG：`high < low[2]`。
- 最小 gap 預設 0.10 ATR。
- 預設 50% CE 作為 mitigation 條件。
- Box 表示區域，CE 使用點線。

### TG XAU 自動斐波 v1
- 使用最新 confirmed swing high / low。
- Pivot 預設 5/5，避免短週期雜訊。
- 預設顯示 0.382 / 0.500 / 0.618。
- 0 / 1 anchor 預設關閉。

## 建議使用方式

### 方向圖
- 1M：只開月線方向。
- 1W：只開週線方向。
- 1D：只開日線方向。

### H1：Location
- Auto S/R
- Key Levels
- Liquidity

### M15：Setup
- Liquidity
- FVG
- Auto Fib
- 必要時 Key Levels

### M5：Entry
- Liquidity
- FVG
- 不建議把全部高週期工具一起塞進來。