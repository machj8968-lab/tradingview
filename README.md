# tradingview

XAUUSD 專用 TradingView / Pine Script 指標專案。所有自製 TradingView 指標統一放這裡，不與 MT4/MT5 EA 混用。

## 指標清單

| 檔案 | 用途 | 建議週期 |
|---|---|---|
| `TG_XAU_Bias_M_v1.pine` | 月線宏觀方向 | 1M |
| `TG_XAU_Bias_W_v1.pine` | 週線主要方向 | 1W |
| `TG_XAU_Bias_D_v1.pine` | 日線戰術方向 | 1D |
| `TG_XAU_Auto_SR_v1.pine` | 當前週期自動支撐 / 壓力 | H1 優先 |
| `TG_XAU_Key_Levels_v1.pine` | PDH/PDL、PWH/PWL、PMH/PML 與 Open | H1/M15/M5 |
| `TG_XAU_Liquidity_v1.pine` | EQH/EQL 流動性池 | H1/M15/M5 |
| `TG_XAU_FVG_v1.pine` | 三 K FVG + 50% CE | M15/M5 |
| `TG_XAU_Auto_Fib_v1.pine` | confirmed swing 自動 Fib | H1/M15 |

## 建議工作流

`Monthly / Weekly / Daily = Direction` → `H1 = Location` → `M15 = Setup` → `M5 = Entry`

不要把所有模組同時塞在同一張圖。建議 TradingView 存三套 Layout：

- **方向**：M/W/D 各自只開對應 Bias。
- **位置**：H1 開 S/R + Key Levels + Liquidity。
- **進場**：M15/M5 開 Liquidity + FVG；需要時再開 Auto Fib。

## 視覺語言

- S/R：實線。
- Liquidity：虛線。
- FVG：區域 Box。
- Fib：水平細線。
- Bias：右上角中文 Dashboard。

## 測試

```bash
python tests/test_bias_logic.py
python tests/test_indicator_contracts.py
python tests/source_sanity.py
```

GitHub Actions 會在 push / PR 自動跑上述測試。這些檢查不是 TradingView 官方 Pine Compiler；新指標第一次仍需在 Pine Editor 實際 Compile。