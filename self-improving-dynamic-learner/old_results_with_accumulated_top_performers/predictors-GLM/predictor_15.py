"""
Predictor 15
Generated on: 2025-09-09 04:29:00
Accuracy: 55.77%
"""


# PREDICTOR 15 - Accuracy: 55.77%
# Correct predictions: 5577/10000 (55.77%)

def predict_output(A, B, C, D, E):
    # Class 1: very high values
    if A >= 85 and B >= 85 and C >= 85 and D >= 85 and E >= 50:
        return 1

    # Class 3 conditions
    if B <= 15 and C < 50 and E < 50 and D <= 80:
        return 3
    if C <= 10 and E < 50:
        return 3
    if E < 10 and C < 50 and B > 50:
        return 3
    if C < 50 and E < 30 and D > 70 and D < 85:
        return 3

    # Class 4 conditions
    if E >= 90 and D < 80:
        return 4
    if B >= 28 and B <= 36 and D >= 15 and D <= 36:
        return 4
    if B >= 80 and E >= 80:
        return 4
    if B <= 10 and C <= 5 and D >= 60 and E >= 60:
        return 4
    if B <= 10 and D >= 40 and E < 10:
        return 4
    if B >= 75 and C <= 10:
        return 4
    if C <= 10 and D >= 90:
        return 4
    if A >= 90 and B <= 10 and E >= 60:
        return 4
    if B <= 30 and D <= 30 and C > 70:
        return 4
    if B <= 30 and D >= 50 and E <= 25 and A > 60:
        return 4

    # Class 2 conditions
    if B >= 65 and A <= 50 and C >= 70 and A > 20:
        return 2
    if B >= 90 and C >= 80:
        return 2
    if B >= 90 and D >= 60:
        return 2
    if A <= 10 and B >= 70 and C >= 40:
        return 2

    # Default to class 1
    return 1