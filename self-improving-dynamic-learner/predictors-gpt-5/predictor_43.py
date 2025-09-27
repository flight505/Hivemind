"""
Predictor 43
Generated on: 2025-09-09 13:49:56
Accuracy: 58.99%
"""


# PREDICTOR 43 - Accuracy: 58.99%
# Correct predictions: 5899/10000 (58.99%)

def predict_output(A, B, C, D, E):
    ed = E - D
    sumAB = A + B

    # Tiny C band (C <= 12)
    if C <= 12:
        # Fix: tiny C with low E and modest D and some A/B support -> 1
        if 10 <= D <= 20 and E <= 25 and (B >= 70 or sumAB >= 110):
            return 1
        # High D with high E -> 2
        if D >= 80 and E >= 55:
            return 2
        # High E -> 4
        if E >= 55:
            return 4
        # Strong 1 cues
        if sumAB >= 165 or (B >= 80 and E <= 30) or (A >= 75 and E <= 30):
            return 1
        # High D with low E -> 1
        if D >= 80 and E <= 30:
            return 1
        # Otherwise -> 3
        return 3

    # Very low C band (13..25)
    if C <= 25:
        # Fix: very low C, very low D, mid E -> 3
        if D <= 10 and 25 <= E <= 50:
            return 3
        # Fix: very low C with tiny D and high E -> 2
        if D <= 12 and E >= 60:
            return 2
        # Specific 1-case
        if C <= 22 and D >= 90 and E <= 20:
            return 1
        # Fix: very low C with very high D and high E -> 4
        if D >= 85 and E >= 60:
            return 4
        # High E with not-high D -> 4
        if E >= 70 and D <= 60:
            return 4
        # Low D with high E -> 4
        if D <= 20 and E >= 60:
            return 4
        # Very high E -> 4
        if E >= 85:
            return 4
        # Strong A+B -> 1
        if sumAB >= 165:
            return 1
        # Low E with moderate/high D -> 3
        if E <= 20 and D >= 20:
            return 3
        # Very high D with not-high E -> 1
        if D >= 85 and E <= 60:
            return 1
        return 1

    # Low C extension: very high E and moderate D -> 4
    if C <= 30 and E >= 70 and D <= 75:
        return 4
    # Pocket: low C, high D, very low E with decent B -> 4
    if C <= 30 and D >= 50 and E <= 20 and B >= 60:
        return 4

    # Very low E in low-mid C
    if 30 <= C <= 40 and E <= 5:
        if D >= 70:
            return 3
        if D >= 60:
            return 4

    # Class 2 in low-mid C
    if 30 <= C <= 45 and D <= 12 and E >= 70:
        return 2
    if 30 <= C <= 45 and B >= 80 and D >= 60 and E >= 60:
        return 2

    # Exceptions steering to 1 in low-mid C with very high E but not tiny D
    if 35 <= C <= 45 and E >= 95 and D >= 30:
        return 1
    if 30 <= C <= 40 and D >= 25 and E >= 70 and A <= 60 and B <= 60:
        return 1

    # Strong class 4 via E dominating D at low C
    if C <= 45 and ed >= 35:
        return 4

    # Mid-low C: low E with low D -> 3
    if 40 <= C <= 50 and D <= 25 and E <= 30:
        return 3

    # Exception: very low D, high E, very high A+B near C ~ 48 -> 1
    if 45 <= C <= 50 and D <= 5 and E >= 65 and sumAB >= 160:
        return 1

    # Specific class 4 at C ~ 48 with strong B, low D, high E
    if 45 <= C <= 50 and D <= 35 and E >= 70 and B >= 80:
        return 4

    # Mid C with very low E -> 1 or 4 depending on B/A+B
    if 50 <= C <= 60 and E <= 10:
        if B >= 80 or sumAB >= 150:
            return 1
        else:
            return 4

    # Fix: mid-high C with very high D and high E but very high A -> 1
    if 60 <= C <= 70 and D >= 85 and E >= 60 and A >= 90:
        return 1
    # Mid/High C with high D -> 3
    if 50 <= C <= 70 and D >= 75 and E >= 40:
        return 3

    # Mid C with very low D and high E -> 2
    if 45 <= C <= 60 and D <= 12 and E >= 60:
        return 2

    # 60-70 with small D and very low E -> 1 if A high, else 3
    if 60 <= C <= 70 and D <= 30 and E <= 15:
        if A >= 80:
            return 1
        return 3

    # High C corrections and specializations
    # Fix: very high C with strong B and low E -> 2
    if C >= 90 and B >= 70 and D >= 55 and E <= 30:
        return 2
    # Fix: high C with low E and small D -> 4
    if C >= 85 and E <= 30 and D <= 35:
        return 4
    # High C with tiny D and very low E -> 4
    if C >= 90 and E <= 10 and D <= 20:
        return 4
    # High C with tiny D and high E -> 2
    if 70 <= C < 90 and D <= 10 and E >= 60:
        return 2
    # High C with tiny D and low E -> 1
    if C >= 75 and D <= 10 and E <= 30:
        return 1
    # Very high C with very low E (and not tiny D) -> 1
    if C >= 88 and E <= 25 and D > 10:
        return 1

    # Class 2 via B synergy (mid/high C)
    if C >= 80 and B >= 90 and D >= 70 and E >= 60:
        return 2
    if 65 <= C <= 75 and D >= 50 and B >= 75 and E >= 60:
        return 2

    # Mid C with low D and moderate E -> 4
    if 50 <= C <= 60 and D <= 35 and E >= 35:
        return 4

    # Fix: mid-low C balanced with moderate D/E and strong A/B -> 2
    if 40 <= C <= 50 and 45 <= D <= 60 and 40 <= E <= 60 and (A >= 85 or B >= 65 or sumAB >= 150):
        return 2

    return 1