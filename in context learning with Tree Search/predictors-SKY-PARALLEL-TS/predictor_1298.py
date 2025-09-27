"""
Predictor 1298
Generated on: 2025-09-10 02:02:09
Accuracy: 56.49%
"""


# PREDICTOR 1298 - Accuracy: 56.49%
# Correct predictions: 5649/10000 (56.49%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90 and A > 50) or (A < 15 and C > 75 and E < 25) or (C < 15 and D > 60 and B > 70 and E > 50) or (C < 5 and E > 55 and D < 40) or (C < 5 and E > 55):
        return 4
    elif (B > 85 and C > 80 and E < 50) or (A < 40 and D < 25 and E > 50 and C > 40 and B > 20):
        return 2
    elif (B < 10 and D > 80 and C < 40) or (C <= 10 and E < 60 and B > 20 and A < 70 and D < 50) or (A > 45 and A < 60 and C < 50 and D > 60 and B > 40) or (C < 5 and D > 90 and B < 15) or (C < 15 and D > 70 and A < 40 and B < 50) or (A > 40 and B < 50 and C < 50 and D > 45):
        return 3
    else:
        return 1