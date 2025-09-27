"""
Predictor 819
Generated on: 2025-09-10 00:50:43
Accuracy: 45.81%
"""


# PREDICTOR 819 - Accuracy: 45.81%
# Correct predictions: 4581/10000 (45.81%)

def predict_output(A, B, C, D, E):
    sum_abc = A + B + C
    diff_de = D - E
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (D > 60 and B < 20) or (C > 70 and D > 60 and E < 10) or (A > 40 and C < 45 and E > 80 and D > 15) or (sum_abc < 100 and diff_de > 50):
        return 4
    elif C > 95 or (B < 10 and D > 80) or (A > 70 and E < 20 and C < 30):
        return 3
    elif (B > 80 and E > 80 and C > 45) or (B > 65 and C > 60 and D > 55 and E > 15) or (A > 90 and E < 10) or (B > 70 and A < 55 and E > 85):
        return 2
    else:
        return 1