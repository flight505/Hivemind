"""
Predictor 835
Generated on: 2025-09-10 00:53:24
Accuracy: 55.55%
"""


# PREDICTOR 835 - Accuracy: 55.55%
# Correct predictions: 5555/10000 (55.55%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C < 10 and D > 90 and B > 70) or (A < 25 and B < 20 and C > 60 and D < 25) or (A > 85 and B > 85 and C < 30):
        return 4
    elif B > 75 and C > 60 and E > 80 or (A > 70 and B < 25 and C > 90):
        return 2
    elif D < 25 and C > 40 and A < 40 and E < 45 or (A > 90 and D > 90 and E < 25):
        return 3
    else:
        return 1