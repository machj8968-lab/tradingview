"""Pure-Python mirror tests for TG XAU Bias D v1 scoring/classification.

These tests validate the agreed mathematical contract. They do not compile Pine.
"""


def ema_score(close, fast, slow):
    if close > fast > slow:
        return 2
    if close < fast < slow:
        return -2
    return 0


def slope_score(fast, past):
    if fast > past:
        return 1
    if fast < past:
        return -1
    return 0


def structure_score(high_state, low_state):
    if high_state == 1 and low_state == 1:
        return 2
    if high_state == -1 and low_state == -1:
        return -2
    return 0


def dmi_score(plus_di, minus_di):
    if plus_di > minus_di:
        return 1
    if minus_di > plus_di:
        return -1
    return 0


def classify(total, adx, threshold=25.0):
    if total >= 5 and adx >= threshold:
        return "STRONG_BULL"
    if total >= 2:
        return "BULL"
    if total <= -5 and adx >= threshold:
        return "STRONG_BEAR"
    if total <= -2:
        return "BEAR"
    return "NEUTRAL"


def run():
    # EMA contract
    assert ema_score(2400, 2350, 2300) == 2
    assert ema_score(2200, 2250, 2300) == -2
    assert ema_score(2400, 2250, 2300) == 0
    assert ema_score(2200, 2350, 2300) == 0

    # Slope contract
    assert slope_score(2350, 2300) == 1
    assert slope_score(2250, 2300) == -1
    assert slope_score(2300, 2300) == 0

    # Structure contract
    assert structure_score(1, 1) == 2      # HH + HL
    assert structure_score(-1, -1) == -2   # LH + LL
    assert structure_score(1, -1) == 0
    assert structure_score(-1, 1) == 0
    assert structure_score(0, 1) == 0
    assert structure_score(1, 0) == 0
    assert structure_score(0, 0) == 0

    # DMI contract
    assert dmi_score(30, 20) == 1
    assert dmi_score(20, 30) == -1
    assert dmi_score(25, 25) == 0

    # Bias threshold boundaries
    assert classify(6, 30) == "STRONG_BULL"
    assert classify(5, 25) == "STRONG_BULL"
    assert classify(6, 24.9) == "BULL"
    assert classify(2, 40) == "BULL"
    assert classify(1, 40) == "NEUTRAL"
    assert classify(0, 10) == "NEUTRAL"
    assert classify(-1, 40) == "NEUTRAL"
    assert classify(-2, 40) == "BEAR"
    assert classify(-6, 24.9) == "BEAR"
    assert classify(-5, 25) == "STRONG_BEAR"
    assert classify(-6, 30) == "STRONG_BEAR"

    # Score mathematical range
    all_scores = []
    for e in (-2, 0, 2):
        for s in (-1, 0, 1):
            for m in (-2, 0, 2):
                for d in (-1, 0, 1):
                    all_scores.append(e + s + m + d)
    assert min(all_scores) == -6
    assert max(all_scores) == 6

    print("PASS: TG XAU Bias D v1 logic contract")


if __name__ == "__main__":
    run()
