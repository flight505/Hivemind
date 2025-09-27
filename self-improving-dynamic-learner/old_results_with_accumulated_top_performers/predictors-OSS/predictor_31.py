"""
Predictor 31
Generated on: 2025-09-09 03:58:25
Accuracy: 53.60%
"""


# PREDICTOR 31 - Accuracy: 53.60%
# Correct predictions: 5360/10000 (53.60%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic & logical checks.
    The rules are ordered from most specific to most general.
    """

    # 1. Very low C with high E  → class 4
    if C <= 12 and E >= 60:
        return 4

    # 2. Very low C with low B  → class 3
    if C <= 12 and B <= 15:
        return 3

    # 3. Very low C with very large D  → class 3
    if C <= 12 and D > 80:
        return 3

    # 4. Low‑mid C (20‑30) with very high E  → class 4
    if 20 <= C <= 30 and E >= 80:
        return 4

    # 5. Low‑mid C (20‑30) with high B  → class 4
    if 20 <= C <= 30 and B >= 80:
        return 4

    # 6. Mid C (30‑45) with very high E  → class 4
    if 30 <= C <= 45 and E >= 80:
        return 4

    # 7. Mid C (30‑45) with high B & moderate E  → class 2
    if 30 <= C <= 45 and B > 60 and E >= 70:
        return 2

    # 8. C in 40‑50 with high B & moderate E  → class 2
    if 40 <= C <= 50 and B >= 80 and E >= 60:
        return 2

    # 9. High C (≥75) with high B & high E, but D not too small  → class 2
    if C >= 75 and B >= 60 and E >= 60 and 10 <= D < 70:
        return 2

    # 10. High C (≥75) with high B & high E, D very small  → class 1
    if C >= 75 and B >= 60 and E >= 60 and D < 10:
        return 1

    # 11. Very high C (≥80) with high B & moderate E  → class 2
    if C >= 80 and B >= 80 and E >= 30:
        return 2

    # 12. Very high C (≥90) with low D & high E  → class 4
    if C >= 90 and D < 20 and E >= 70:
        return 4

    # 13. High C (≥70) with very high E but low B  → class 4
    if C >= 70 and E >= 80 and B <= 40:
        return 4

    # 14. High C (≥70) with very high B  → class 2
    if C >= 70 and B >= 80:
        return 2

    # 15. C between 60‑70, low D → class 4
    if 60 <= C < 70 and D < 20:
        return 4

    # 16. C between 60‑70, low D & low E → class 3
    if 60 <= C < 70 and D < 20 and E < 20:
        return 3

    # 17. C between 60‑70, low D & moderate E → class 4
    if 60 <= C < 70 and D < 20 and E >= 60:
        return 4

    # 18. C between 60‑70, low D & very low E → class 3 (handled above)

    # 19. B very high (≥90) and D very high (≥70) → class 2
    if B >= 90 and D >= 70:
        return 2

    # 20. B very high (≥90) and moderate C (40‑55) → class 2
    if B >= 90 and 40 <= C <= 55:
        return 2

    # 21. B very high (≥80) and moderate C (45‑55) → class 2
    if B >= 80 and 45 <= C <= 55:
        return 2

    # 22. B very high (≥80) and low D (<20) → class 4
    if B >= 80 and D < 20:
        return 4

    # 23. B low (≤10) and C in 30‑35 → class 4
    if B <= 10 and 30 <= C <= 35:
        return 4

    # 24. B low (≤10) and C ≤12 → class 3
    if B <= 10 and C <= 12:
        return 3

    # 25. B low (≤15) and high D (>70) → class 1
    if B <= 15 and D > 70:
        return 1

    # 26. B low (≤15) and high D (>70) and high E (>70) → class 1 (already covered)

    # 27. C high (≥70) with B low (≤15) and E low (<30) → class 4
    if C >= 70 and B <= 15 and E < 30:
        return 4

    # 28. C high (≥70) with B low (≤15) and E moderate (30‑70) → class 1
    if C >= 70 and B <= 15 and 30 <= E <= 70:
        return 1

    # 29. C low‑mid (30‑45) with very low E (<30) and high D (>70) → class 3
    if 30 <= C <= 45 and E < 30 and D > 70:
        return 3

    # 30. C low (≤20) and very low D (<20) → class 3
    if C <= 20 and D < 20:
        return 3

    # 31. C low (≤12) and E moderate (≥50) → class 4
    if C <= 12 and E >= 50:
        return 4

    # 32. Default fallback
    return 1