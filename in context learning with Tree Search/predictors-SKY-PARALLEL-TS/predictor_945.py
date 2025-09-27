"""
Predictor 945
Generated on: 2025-09-10 01:07:55
Accuracy: 55.88%
"""


# PREDICTOR 945 - Accuracy: 55.88%
# Correct predictions: 5588/10000 (55.88%)

def predict_output(A, B, C, D, E):
    if (C > 90 and D > 90 and E < 5 and B < 20) or (A < 20 and B < 20 and C > 95 and D > 90 and E < 5):
        return 1
    if (A < 10 and B > 70 and C < 40) or \
       (C < 15 and D > 80 and B > 30 and A > 5) or \
       (C < 20 and D > 60 and E < 15 and B > 50) or \
       (C > 70 and D > 70 and E < 10) or \
       (A < 30 and C < 20 and D > 60 and E < 15 and B > 50) or \
       (A < 20 and B > 50 and C > 70 and D > 70 and E < 10):
        return 4
    if (B > 90 and C > 40 and D > 70) or \
       (A < 5 and B > 50 and E > 80) or \
       (A < 5 and B > 50 and C < 15 and E > 80) or \
       (B > 85 and C > 40 and D > 70 and A > 40):
        return 2
    if (A > 60 and B < 25 and C > 30 and D < 25) or \
       (B > 70 and C < 25 and D > 90) or \
       (A < 10 and B > 85 and C > 70 and D < 10) or \
       (C < 10 and D > 80 and B < 20) or \
       (A > 50 and B > 70 and C < 25 and D > 90) or \
       (A < 10 and B > 85 and C > 70 and D < 10) or \
       (A > 60 and B < 25 and C > 35 and D < 25 and E < 25):
        return 3
    else:
        return 1