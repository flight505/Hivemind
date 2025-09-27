"""
Predictor 683
Generated on: 2025-09-09 19:33:19
Accuracy: 56.32%
"""


# PREDICTOR 683 - Accuracy: 56.32%
# Correct predictions: 5632/10000 (56.32%)

def predict_output(A, B, C, D, E):
    # Rules for 4
    if C < 25 and E > 75:
        return 4
    if B > 65 and C < 30 and A > 50:
        return 4
    if C >= 85 and E < 20 and B < 50:
        return 4
    if C > 80 and D < 20 and B < 40:
        return 4
    # Rules for 3
    if B < 20 and C < 20:
        return 3
    if B > 55 and B < 65 and D > 70:
        return 3
    if A < 10 and D < 10 and B > 40:
        return 3
    # Rule for 2
    if A < 50 and B + C > 120:
        return 2
    # Default for 1
    return 1