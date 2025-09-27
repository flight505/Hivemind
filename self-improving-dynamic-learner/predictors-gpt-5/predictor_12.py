"""
Predictor 12
Generated on: 2025-09-09 12:31:50
Accuracy: 55.56%
"""


# PREDICTOR 12 - Accuracy: 55.56%
# Correct predictions: 5556/10000 (55.56%)

def predict_output(A, B, C, D, E):
    # Simple derived contrasts and sums (used in a few checks)
    diff_ED = E - D
    sum_BC = B + C

    # Very low C consistently maps to 3 in the sample
    if C <= 12:
        return 3

    # Strong class 4: very high E with low D and not-too-high C
    if E >= 90 and D <= 30 and C <= 40:
        return 4

    # Class 2 signals:
    #  - High C with very strong B
    if C >= 82 and B >= 85:
        return 2
    #  - High C with high E and very low D and decent B
    if C >= 74 and E >= 70 and D <= 10 and B >= 60:
        return 2

    # Low C band (13-25): defaults to 1 unless caught by the 4-rule above
    if 13 <= C <= 25:
        return 1

    # High C generally prefers 1 in this sample when not already classified
    if C >= 65:
        return 1

    # Mid C in this sample leans to 1
    if 50 <= C <= 64:
        return 1

    # Fallback
    return 1