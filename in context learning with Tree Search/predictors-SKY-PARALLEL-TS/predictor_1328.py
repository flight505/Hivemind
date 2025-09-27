"""
Predictor 1328
Generated on: 2025-09-10 02:07:02
Accuracy: 55.08%
"""


# PREDICTOR 1328 - Accuracy: 55.08%
# Correct predictions: 5508/10000 (55.08%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90) or (E < 20 and (C > 70 or (B > 55 and A < 40))):
        return 4
    elif C > 60 and D < 10 and E > 50:
        return 2
    elif A > 90 and C < 40 and D > 80:
        return 3
    else:
        return 1