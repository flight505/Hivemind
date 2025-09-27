"""
Predictor 871
Generated on: 2025-09-10 00:58:03
Accuracy: 50.55%
"""


# PREDICTOR 871 - Accuracy: 50.55%
# Correct predictions: 5055/10000 (50.55%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (C > 85 and D < 25) or (D < 5 and E > 70) or (E > 90 and D < 25):
        return 4
    elif (B < 10 and C > 70) or (A > 70 and E > 90) or (A > 85 and D > 90 and C < 30):
        return 3
    elif (B > 80 and C > 50) or (B > 90) or (A < 5 and C < 10 and E > 60):
        return 2
    else:
        return 1