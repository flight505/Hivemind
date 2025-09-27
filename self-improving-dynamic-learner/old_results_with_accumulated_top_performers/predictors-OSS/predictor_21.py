"""
Predictor 21
Generated on: 2025-09-09 03:50:00
Accuracy: 47.94%
"""


# PREDICTOR 21 - Accuracy: 47.94%
# Correct predictions: 4794/10000 (47.94%)

def predict_output(A, B, C, D, E):
    # 1. Very low C
    if C <= 12:
        if E >= 60:
            return 4
        return 3

    # 2. Extremely high E with low‑moderate C
    if E >= 90 and C < 30:
        return 4

    # 3. Very high C (≥95) together with very low D → class 1
    if C >= 95 and D < 10:
        return 1

    # 4. High C (≥75) together with reasonably high B and E → class 2
    if C >= 75 and B >= 60 and E >= 70:
        return 2

    # 5. High B with moderate C (20‑30) → class 2
    if B > 80 and 20 <= C <= 30:
        return 2

    # 6. Moderate C (30‑45) with moderately high B → class 2
    if 30 <= C <= 45 and B >= 40:
        return 2

    # 7. High B with C 20‑50 → class 2
    if 20 <= C <= 50 and B > 80:
        return 2

    # 8. Very high E (≥90) with C 30‑45 → class 2
    if E >= 90 and 30 <= C <= 45:
        return 2

    # 9. C between 13‑30 with low E:
    #    use D to decide between 1 and 3
    if 13 <= C <= 30 and E < 60:
        if D > 80:
            return 1
        return 3

    # 10. Low B (≤20) with C 30‑40 and low E → class 3
    if B <= 20 and 30 <= C <= 40 and E < 60:
        return 3

    # 11. Very low E (<10) with relatively high C → class 4
    if E < 10 and C >= 50:
        return 4

    # 12. Low E (<20) with high C → class 3
    if E < 20 and C > 50:
        return 3

    # 13. Low B (≤15) with high E → class 4
    if B <= 15 and E >= 60:
        return 4

    # 14. Low‑moderate C (≤20) with high E → class 4
    if C <= 20 and E >= 60:
        return 4

    # 15. Low B (≤15) with C 20‑40 and very low E → class 4
    if B <= 15 and 20 <= C <= 40 and E < 10:
        return 4

    # 16. Default fallback
    return 1