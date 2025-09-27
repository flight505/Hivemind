"""
Predictor 133
Generated on: 2025-09-09 13:29:55
Accuracy: 58.05%
"""


# PREDICTOR 133 - Accuracy: 58.05%
# Correct predictions: 5805/10000 (58.05%)

def predict_output(A, B, C, D, E):
    if A < 40 and B > 60 and C > 70:
        return 2
    if B > 60 and C > 40 and E > 80 and A < 90:
        return 2
    if B + C + E < 60:
        return 3
    if B < 20 and C < 15:
        return 3
    if 40 < B < 70 and 40 < C < 50 and 30 < E < 60:
        return 3
    if A > 90 and B > 70 and C < 40 and E < 60:
        return 3
    if B < 15 and 30 < C < 45 and E < 40:
        return 3
    if B < 30 and C < 10:
        return 3
    if C < 25 and E > 70 and D < 50 and B < 50:
        return 4
    if B < 40 and C > 60 and E < 40 and D < 50:
        return 4
    if B > 90 and C < 15 and E > 40:
        return 4
    if C < 30 and E > 70 and B > 10 and D < 50:
        return 4
    if B < 20 and C > 70 and E < 35 and D < 30:
        return 4
    if B > 40 and 20 < C < 30 and E < 30 and B < 90:
        return 3
    if B < 40 and C > 70 and E < 50 and D < 50:
        return 3
    if C > 0 and B / C > 3.5 and E > 50:
        return 1
    if B > 80 and C > 60 and E > 80:
        return 1
    if B > 90 and C > 60 and E < 50:
        return 1
    if B > 70 and C > 70 and E > 60:
        return 1
    if A + B > 160 and C < 40 and E > 50:
        return 2
    return 1