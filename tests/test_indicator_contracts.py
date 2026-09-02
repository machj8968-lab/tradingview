from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IND = ROOT / "indicators"
FILES = {
    "D": IND / "TG_XAU_Bias_D_v1.pine",
    "W": IND / "TG_XAU_Bias_W_v1.pine",
    "M": IND / "TG_XAU_Bias_M_v1.pine",
    "SR": IND / "TG_XAU_Auto_SR_v1.pine",
    "KEY": IND / "TG_XAU_Key_Levels_v1.pine",
    "LIQ": IND / "TG_XAU_Liquidity_v1.pine",
    "FVG": IND / "TG_XAU_FVG_v1.pine",
    "FIB": IND / "TG_XAU_Auto_Fib_v1.pine",
}
for name, path in FILES.items():
    assert path.exists(), f"Missing indicator {name}: {path}"
    text = path.read_text(encoding="utf-8")
    assert text.startswith("//@version=6\n"), f"{name}: must use Pine v6"
    assert "indicator(" in text, f"{name}: indicator() declaration missing"
    assert "strategy(" not in text, f"{name}: strategy() is forbidden"

bias_contracts = {
    "D": "timeframe.isdaily and timeframe.multiplier == 1",
    "W": "timeframe.isweekly and timeframe.multiplier == 1",
    "M": "timeframe.ismonthly and timeframe.multiplier == 1",
}
for name, tf_token in bias_contracts.items():
    text = FILES[name].read_text(encoding="utf-8")
    for token in [tf_token, "barstate.isconfirmed", "ta.ema(", "ta.dmi(", "ta.pivothigh(", "ta.pivotlow(", "confirmedBias", "BIAS_STRONG_BULL", "BIAS_STRONG_BEAR", "市場結構", "均線結構", "ADX 強度"]:
        assert token in text, f"{name}: missing {token}"
    assert "request.security(" not in text, f"{name}: bias must stay native-timeframe only"

sr = FILES["SR"].read_text(encoding="utf-8")
for token in ["ta.pivothigh(", "ta.pivotlow(", "clusterAtrMult", "barstate.isconfirmed", '"R" + str.tostring(slot + 1)', '"S" + str.tostring(slot + 1)', "extend.both"]:
    assert token in sr, f"SR missing {token}"

key = FILES["KEY"].read_text(encoding="utf-8")
for token in ['request.security(syminfo.tickerid, "D", high[1]', 'request.security(syminfo.tickerid, "W", high[1]', 'request.security(syminfo.tickerid, "M", high[1]', "lookahead = barmerge.lookahead_on", "PDH｜昨日高點", "PWH｜上週高點", "PMH｜上月高點"]:
    assert token in key, f"KEY missing {token}"

liq = FILES["LIQ"].read_text(encoding="utf-8")
for token in ["EQH / EQL", "BSL｜買方流動性", "SSL｜賣方流動性", "barstate.isconfirmed", "line.style_dashed"]:
    assert token in liq, f"LIQ missing {token}"

fvg = FILES["FVG"].read_text(encoding="utf-8")
for token in ["low > high[2]", "high < low[2]", "barstate.isconfirmed", 'mitigationMode = input.string("50%"', "box.new", "50% CE"]:
    assert token in fvg, f"FVG missing {token}"

fib = FILES["FIB"].read_text(encoding="utf-8")
for token in ["ta.pivothigh(", "ta.pivotlow(", "barstate.isconfirmed", "0.382", "0.500", "0.618", "extend.right"]:
    assert token in fib, f"FIB missing {token}"

print("PASS: all TradingView indicator contracts")