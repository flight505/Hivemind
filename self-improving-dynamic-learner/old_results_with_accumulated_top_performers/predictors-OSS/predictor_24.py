"""
Predictor 24
Generated on: 2025-09-09 03:50:57
Accuracy: 51.83%
"""


# PREDICTOR 24 - Accuracy: 51.83%
# Correct predictions: 5183/10000 (51.83%)

def predict_output(A, B, C, D, E):
    # 1. Low C (very small values)
    if C < 20:
        if B >= 80:                     # low C together with very high B → class 4
            return 4
        if B <= 20:                     # low C and low / moderate B → class 3
            return 3
        # medium B, decide by E
        if E >= 60:
            return 4
        return 

    # 2. Very high C (>=80) – low B stays in class 1
    if C >= 80:
        if B <= 20:                     # high C but low B → class 1
            return 1
        return 1

    # 3. Extremely high E (>=90) with moderate‑low C → class 4
    if E >= 90:
        if C < 45:
            return 4
        if B >= 80:                     # when C is higher, high B may give class 2
            return 2
        return 4

    # 4. High B (>=80) with mid‑range C (30‑45) → class 2
    if B >= 80 and 30 <= C <= 45:
        return 2

    # 5. High B with C in 20‑30 and very low E → class 4
    if B >= 80 and 20 <= C <= 30 and E < 20:
        return 4

    # 6. Low B (<=15) with very low C (<30) → class 3
    if B <= 15 and C < 30:
        return 3

    # 7. Low B (<=15) with high E → class 4
    if B <= 15 and E >= 60:
        return 4

    # 8. Very low B (<=10) with medium C (60‑70) → class 4
    if B <= 10 and 60 <= C <= 70:
        return 4

    # 9. Low B (<=15) with medium‑high C (45‑70) → class 4
    if B <= 15 and 45 <= C <= 70:
        return 4

    # default fallback
    return 1