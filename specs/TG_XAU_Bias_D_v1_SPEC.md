# TG XAU Bias D v1｜實作規格

## 範圍

本指標專為 XAUUSD 設計，只在 1D 顯示正式方向結果。

不包含：支撐壓力、流動性、FVG、Fibonacci、進出場、SL/TP、策略回測與券商整合。

## 五級方向

| 內部值 | 顯示 |
|---:|---|
| +2 | 強多 |
| +1 | 多 |
| 0 | 中性 |
| -1 | 空 |
| -2 | 強空 |

## 組成

### EMA 結構

- `close > EMA20 > EMA50` → +2
- `close < EMA20 < EMA50` → -2
- 其他 → 0

### EMA20 斜率

預設回看 3 根 Daily K。

- `EMA20 > EMA20[3]` → +1
- `EMA20 < EMA20[3]` → -1
- 相等 → 0

### 市場結構

使用已確認 `ta.pivothigh()` / `ta.pivotlow()`，預設 left/right = 3/3。

High：
- 新 confirmed high 高於上一個 → HH
- 低於上一個 → LH
- 差距落在 `ATR(14) × 0.05` 內 → EQH

Low：
- 新 confirmed low 高於上一個 → HL
- 低於上一個 → LL
- 差距落在 `ATR(14) × 0.05` 內 → EQL

計分：
- HH + HL → +2
- LH + LL → -2
- 其他混合／相等組合 → 0

### DMI / ADX

預設 DI=14、ADX smoothing=14。

- +DI > -DI → +1
- -DI > +DI → -1
- 相等 → 0

ADX 不直接加減方向分，只作為強多／強空門檻。

## 總分

`EMA + Slope + Structure + DMI`，範圍 -6～+6。

## 分類

1. score >= +5 且 ADX >= 25 → 強多
2. score >= +2 → 多
3. score <= -5 且 ADX >= 25 → 強空
4. score <= -2 → 空
5. 其他 → 中性

## 收線確認 / Non-repaint

- 正式 Bias 只在目前 1D K 棒收線後更新。
- 即時尚未收線的 Daily K 保留上一根已收線 Daily K 的正式結果。
- Pivot 只有在右側確認 K 完成後才寫入市場結構。
- v1 不使用 `request.security()`。
- Bias 變化警報必須通過 `barstate.isconfirmed`。
- 精確週期限制：`timeframe.isdaily and timeframe.multiplier == 1`。

## 顯示

- EMA20 / EMA50 預設顯示，可關閉。
- 青綠色 = EMA 快線（預設20）。
- 橘色 = EMA 慢線（預設50）。
- 中文 Dashboard 預設顯示。
- 詳細模式：方向、總分、市場結構、均線結構、EMA20 斜率、DMI、ADX。
- 市場結構 Debug 預設關閉。
- Score Debug 預設關閉。
- 非 1D：不顯示正式 Bias / EMA，只可選擇顯示「僅限日線使用」。

## 驗證目標

優先人工查看 XAUUSD Daily 2024-01-01 至今：

- 明顯多頭
- 明顯空頭
- 正常回調
- EMA 壓縮／震盪
- 趨勢反轉
- 低 ADX
- 高 ADX
- EMA 與市場結構衝突
