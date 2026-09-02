"""Static contract checks for the Pine source.

This is not a Pine compiler. It catches accidental architectural violations.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PINE = ROOT / "indicators" / "TG_XAU_Bias_D_v1.pine"
text = PINE.read_text(encoding="utf-8")

required = [
    "//@version=6",
    "timeframe.isdaily and timeframe.multiplier == 1",
    "barstate.isconfirmed",
    "ta.ema(",
    "ta.atr(",
    "ta.dmi(",
    "ta.pivothigh(",
    "ta.pivotlow(",
    "alertcondition(",
    "confirmedBias",
    "structureToleranceAtr",
]

for token in required:
    assert token in text, f"Missing required token: {token}"

for forbidden in [
    "strategy(",
    "request.security(",
    "ta.rsi(",
    "ta.macd(",
]:
    assert forbidden not in text, f"Forbidden feature present: {forbidden}"

# Exact five state constants.
for token in [
    "BIAS_STRONG_BULL",
    "BIAS_BULL",
    "BIAS_NEUTRAL",
    "BIAS_BEAR",
    "BIAS_STRONG_BEAR",
]:
    assert token in text

# Chinese UI contract.
for token in [
    "XAU 日線方向",
    "已確認",
    "方向",
    "總分",
    "市場結構",
    "均線結構",
    "EMA20 斜率",
    "DMI 方向",
    "ADX 強度",
    "EMA 快線",
    "EMA 慢線",
]:
    assert token in text, f"Missing Chinese UI token: {token}"

print("PASS: Pine static architecture + Chinese UI contract")
