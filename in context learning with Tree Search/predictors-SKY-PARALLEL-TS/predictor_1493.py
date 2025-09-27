"""
Predictor 1493
Generated on: 2025-09-10 02:35:36
Accuracy: 48.95%
"""


# PREDICTOR 1493 - Accuracy: 48.95%
# Correct predictions: 4895/10000 (48.95%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or \
       (C < 30 and E < 20 and A > 40) or \
       (C > 60 and E < 35 and A > 50) or \
       (A > 70 and B < 5 and C > 50) or \
       (E < 5 and A > 30 and D > 40 and C > 35) or \
       (A > 70 and C < 30 and D > 50 and E > 70):
        return 4
    elif B > 90 and E > 80:
        return 2
    elif (A > 85 and D > 85 and E > 85) or \
         (A > 85 and E < 15 and B > 50) or \
         (A > 80 and B < 40 and D > 50):
        return 3
    else:
        return 1