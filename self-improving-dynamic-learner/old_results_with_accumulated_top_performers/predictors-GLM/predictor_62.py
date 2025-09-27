"""
Predictor 62
Generated on: 2025-09-09 05:58:30
Accuracy: 50.17%
"""


# PREDICTOR 62 - Accuracy: 50.17%
# Correct predictions: 5017/10000 (50.17%)

def predict_output(A, B, C, D, E):
    # Output=3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 15 and C < 50 and E < 50 and D <= 80) or \
       (B >= 75 and C > 60 and D > 80 and E > 60):
        return 3
    
    # Output=2 conditions
    elif (B >= 65 and A <= 50 and C >= 70) or \
         (B >= 90 and C >= 80 and D > 20) or \
         (C >= 90 and D <= 10) or \
         (A <= 10 and B > 50 and D < 30):
        return 2
    
    # Output=4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (E >= 80) or \
         (B <= 20 and C >= 60) or \
         (B >= 28 and B <= 36 and E <= 10):
        return 4
    
    # Default Output=1
    else:
        return 1