"""
Predictor 124
Generated on: 2025-09-09 23:30:47
Accuracy: 56.64%
"""


# PREDICTOR 124 - Accuracy: 56.64%
# Correct predictions: 5664/10000 (56.64%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 70) or \
       (C < 15 and D > 90) or \
       (B < 10 and C > 70) or \
       (D < 10 and E > 70) or \
       (C < 10 and B < 25 and E > 50):
        return 4
    if (B > 70 and C > 70 and E < 20) or \
       (B > 85 and C > 80 and A < 80) or \
       (B > 70 and D < 20 and A < 50 and E > 40):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or \
       (A < 50 and D < 25 and E < 20 and B < 80) or \
       (D < 15 and C > 40 and B < 80 and A < 70 and E < 25) or \
       (C <= 10 and E < 60 and B < 50 and D > 20) or \
       (A > 75 and B < 25 and C < 45 and D > 60):
        return 3
    else:
        return 1