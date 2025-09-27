"""
Predictor 123
Generated on: 2025-09-09 09:20:35
Accuracy: 54.99%
"""


# PREDICTOR 123 - Accuracy: 54.99%
# Correct predictions: 5499/10000 (54.99%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor.
    Uses only basic arithmetic, comparisons and logical operators.
    The rules are ordered from the most specific to the most general
    and aim to correct the previously mis‑predicted cases while keeping
    good overall performance.
    """

    # ------------------------------------------------------------------
    # 1. Very high C (≥ 90) – dominant class 1
    if C >= 90:
        return 1

    # ------------------------------------------------------------------
    # 2. High C (70‑89)
    if C >= 70:
        # strong B + E together → class 2
        if B >= 80 and E >= 80:
            return 2
        # low B and low E → class 4
        if B <= 30 and E < 30:
            return 4
        # otherwise default to class 1
        return 1

    # ------------------------------------------------------------------
    # 3. Very low C (≤ 12) – always class 3 unless E is very high
    if C <= 12:
        if E >= 70:
            return 4          # high E overrides
        return 3

    # ------------------------------------------------------------------
    # 4. Low C (13‑15) – also class 3 (the training set shows this range
    #    behaves like the ≤12 region)
    if C <= 15:
        if E >= 70:
            return 4
        return 3

    # ------------------------------------------------------------------
    # 5. Low C (16‑30)
    if C <= 30:
        # very high D together with low C → class 3
        if D >= 80:
            return 3
        # high E pushes to class 4
        if E >= 70:
            return 4
        # otherwise class 1
        return 1

    # ------------------------------------------------------------------
    # 6. Mid‑low C (31‑40)
    if C <= 40:
        # very high E → class 4
        if E >= 80:
            return 4
        # moderate‑high E (60‑79) → class 2
        if E >= 60:
            return 2
        # low E together with high D → class 3
        if E < 30 and D >= 70:
            return 3
        # default
        return 1

    # ------------------------------------------------------------------
    # 7. Mid C (41‑45)
    if C <= 45:
        # very high E → class 4
        if E >= 80:
            return 4
        # low E (regardless of B) also tends to class 4
        if E < 30:
            return 4
        # moderate‑high E (60‑79) → class 2
        if E >= 60:
            return 2
        return 1

    # ------------------------------------------------------------------
    # 8. Upper‑mid C (46‑55) – follow the same pattern as 41‑45
    if C <= 55:
        if E >=80:
           4
        if E < 30:
            return 4
        if E >= 60:
            return 2
        return 1

    # ------------------------------------------------------------------
    # 9. Remaining C values (56‑69) – default to class 1
    return 1