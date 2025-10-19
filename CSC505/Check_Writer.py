"""
Check Writer: Convert a numeric amount to check-style words.
Examples:
  0.00      -> "Zero and 00/100 dollars"
  42.07     -> "Forty-two and 07/100 dollars"
  1234.56   -> "One thousand two hundred thirty-four and 56/100 dollars"
  1000000.0 -> "One million and 00/100 dollars"
"""

from decimal import Decimal, ROUND_HALF_UP

ONES_TEENS = [
    "zero","one","two","three","four","five","six","seven","eight","nine",
    "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
    "seventeen","eighteen","nineteen"
]
TENS = ["", "", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
SCALES = [(1_000_000_000, "billion"), (1_000_000, "million"), (1_000, "thousand")]

def normalize_amount(raw: str) -> Decimal:
    amt = Decimal(raw)
    if amt < 0:
        raise ValueError("Amount must be non-negative.")
    return amt.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def split_amount(amt: Decimal) -> tuple[int, int]:
    cents = int((amt * 100) % 100)
    dollars = int(amt // 1)
    return dollars, cents

def under_thousand_to_words(n: int) -> str:
    assert 0 <= n < 1000
    parts = []
    if n >= 100:
        parts.append(ONES_TEENS[n // 100] + " hundred")
        n %= 100
    if n >= 20:
        tens_word = TENS[n // 10]
        unit = n % 10
        if unit:
            parts.append(f"{tens_word}-{ONES_TEENS[unit]}")
        else:
            parts.append(tens_word)
    elif n > 0:
        parts.append(ONES_TEENS[n])
    return " ".join(parts)

def number_to_words(n: int) -> str:
    if n == 0:
        return "zero"
    parts = []
    remainder = n
    for scale_val, scale_name in SCALES:
        if remainder >= scale_val:
            chunk = remainder // scale_val
            parts.append(under_thousand_to_words(chunk))
            parts.append(scale_name)
            remainder %= scale_val
    if remainder:
        parts.append(under_thousand_to_words(remainder))
    return " ".join(parts)

def compose_check_line(dollars: int, cents: int) -> str:
    dollars_words = number_to_words(dollars)
    cents_str = f"{cents:02d}/100"
    if dollars == 0:
        line = f"Zero and {cents_str} dollars"
    else:
        line = f"{dollars_words.capitalize()} and {cents_str} dollars"
    return line

def amount_to_check_words(raw_amount: str) -> str:
    amt = normalize_amount(raw_amount)
    dollars, cents = split_amount(amt)
    return compose_check_line(dollars, cents)

if __name__ == "__main__":
    samples = ["0", "0.00", "42.07", "1234.56", "1000000", "100200300.04"]
    for s in samples:
        print(f"{s:>12} -> {amount_to_check_words(s)}")
