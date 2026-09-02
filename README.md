# tradingview

TradingView / Pine Script 專用專案。之後所有自製指標統一放在這裡，不與 MT4/MT5 EA 專案混用。

## 目前指標

### TG XAU 日線方向 v1

檔案：`indicators/TG_XAU_Bias_D_v1.pine`

用途：只針對 XAUUSD 的 1D 圖表，以已收線資料判斷五級大方向：

- 強多
- 多
- 中性
- 空
- 強空

核心組件：

- EMA20 / EMA50 結構
- EMA20 三日斜率
- Confirmed Pivot 3/3 市場結構（HH/HL/LH/LL）
- DMI 方向
- ADX 趨勢強度

畫面上的兩條均線：

- 青綠色：EMA 快線（預設 EMA20）
- 橘色：EMA 慢線（預設 EMA50）

兩條線只作為方向評分的一部分，不是單獨的買賣訊號；可在設定中關閉顯示，計算仍會繼續。

## 原則

- Pine Script v6
- Daily only
- Closed-bar confirmed bias
- Non-repaint 優先
- 每支指標單一職責
- S/R、Liquidity、FVG、Fib 等後續各自拆成獨立指標

## 測試

```bash
python tests/test_bias_logic.py
python tests/static_contract_check.py
```

注意：以上測試驗證數學契約與靜態架構，不等同 TradingView 官方 Pine Compiler。最終仍需在 TradingView Pine Editor 實際編譯與圖表驗證。
