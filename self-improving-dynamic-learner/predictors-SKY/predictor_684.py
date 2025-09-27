"""
Predictor 684
Generated on: 2025-09-09 19:34:32
Accuracy: 55.08%
"""


# PREDICTOR 684 - Accuracy: 55.08%
# Correct predictions: 5508/10000 (55.08%)

def predict_output(A, B, C, D, E):
    if B > 60 and C > 70 and E < 20 and D > 50:
        return 1
    if B > 80 and C >= 70 and E >= 70 and D < 20:
        return 1
    if B > 65 and C > 65 and E > 90:
        return 1
    if B < 25 and C < 20 and E < 50:
        return 3
    if B < 25 and C > 80 and E < 20:
        return 3
    if B < 25 and C < 20 and E > 50:
        return 4
    if C < 25 and E > 75:
        return 4
    if B > 65 and C < 30 and A > 50:
        return 4
    if C >= 85 and E < 20 and 25 <= B < 50:
        return 4
    if C > 80 and D < 20 and B < 40:
        return 4
    if E > 90 and C < 40 and A > 80:
        return 4
    if B > 55 and C > 35 and E > 60 and D < 10:
        return 2
    if B < 40 and C > 20 and E > 60 and D < 20:
        return 2
    if B > 60 and C > 70:
        return 2
    if B > 60 and C > 50 and E >= 70:
        return 2
    return 1