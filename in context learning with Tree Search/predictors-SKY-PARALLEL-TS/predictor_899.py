"""
Predictor 899
Generated on: 2025-09-10 01:00:50
Accuracy: 56.55%
"""


# PREDICTOR 899 - Accuracy: 56.55%
# Correct predictions: 5655/10000 (56.55%)

def predict_output(A, B, C, D, E):
    if (A < 20 and B > 70) or (C < 20 and D > 70 and B > 40) or (C < 10 and D > 90) or (B > 90 and C < 20 and D > 70) or (C < 10 and D > 50 and E > 60) or (C < 5 and D > 90):
        return 4
    elif B >= 85 and C > 80:
        return 2
    elif (A > 90 and E > 90) or (B > 80 and D > 90 and E < 10) or (A < 20 and C < 20 and B < 45 and D < 40):
        return 3
    else:
        return 1