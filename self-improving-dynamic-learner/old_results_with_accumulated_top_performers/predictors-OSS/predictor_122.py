"""
Predictor 122
Generated on: 2025-09-09 09:19:26
Accuracy: 58.40%
"""


# PREDICTOR 122 - Accuracy: 58.40%
# Correct predictions: 5840/10000 (58.40%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only simple arithmetic,
    comparisons and logical tests.
    The rules are ordered from most specific to most general
    and aim to correct the previously mis‑predicted cases.
    """

    # ------------------------------------------------------------------
    # Very high C (≥ 90) – dominant class 1
    if C >= 90:
        return 1

    # High C (80‑89) – class 2 only when B and E are both very high
    if C >= 80:
        if B >= 80 and E >= 80:
            return 2
        return 1

    # High C (75‑79) – same rule as above
    if C >= 75:
        if B >= 80 and E >= 80:
            return 2
        return 1

    # High C (70‑74) – class 2 only when B and E are both ≥ 80
    if C >= 70:
        if B >= 80 and E >= 80:
            return 2
        return 1

    # Mid‑high C (65‑69)
    if C >= 65:
        # very strong B + E give class 2
        if B >= 80 and E >= 80:
            return 2
        # high E alone forces class 4
        if E >= 80:
            return 4
        # otherwise, if B and E are both ≥ 60 → class 2
        if B >= 60 and E >= 60:
            return 2
        return 1

    # Upper‑mid C (55‑64) – default to class 1
    if C >= 55:
        return 1

    # Mid C (45‑54)
    if C >= 45:
        # very high E together with high D → class 3
        if E >= 90 and D >= 70:
            return 3
        # strong B + E give class 2
        if B >= 60 and E >= 60:
            return 2
        return 1

    # Mid‑low C (30‑44)
    if C >= 30:
        # very high E together with high D → class 3
        if E >= 90 and D >= 70:
            return 3
        # strong B + E give class 2
        if B >= 60 and E >= 60:
            return 2
        return 1

    # Very low C (≤ 12)
    if C <= 12:
        if B <= 15:
            return 3                     # low B with very low C
        if E >= 70:
            return 4                     # high E pushes to class 4
        return 1                         # other low‑C cases

    # Low C (13‑30)
    if C <= 30:
        if E >= 70:
            return 4                     # high E dominates
        # pattern for C≈20‑30 with moderate B and E → class 2
        if C >= 20 and B >= 20 and E >= 60:
            return 2
        if B <= 15:
            return 3                     # very low B → class 3
        return 1

    # Default fallback
    return 1