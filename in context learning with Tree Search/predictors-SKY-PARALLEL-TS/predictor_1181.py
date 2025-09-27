"""
Predictor 1181
Generated on: 2025-09-10 01:39:40
Accuracy: 53.55%
"""


# PREDICTOR 1181 - Accuracy: 53.55%
# Correct predictions: 5355/10000 (53.55%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 10 and D > 90) or (B > 60 and D < 30 and A < 40) or (A > 85 and B < 55 and C < 30 and D > 65 and E < 40):
        return 4
    elif (A > 90 and E < 10) or (C > 80 and D < 10 and E > 80):
        return 2
    elif (B < 10 and D > 80) or (A > 80 and D > 90) or (A < 10 and C < 15 and D > 30) or (B > 65 and C < 35 and D > 90 and A < 40 and E > 80):
        return 3
    else:
        return 1