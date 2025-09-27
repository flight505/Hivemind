"""
Predictor 3
Generated on: 2025-09-09 03:50:43
Accuracy: 45.19%
"""


# PREDICTOR 3 - Accuracy: 45.19%
# Correct predictions: 4519/10000 (45.19%)

def predict_output(A, B, C, D, E):
    # Output=4 conditions
    if (E >= 90 and (C >= 99 or (B >= 20 and B <= 40) or (A > 90 and D > 80) or (B >= 88 and E >= 99))) or \
       (B <= 10 and C <= 12 and (A > 90 or D > 80)) or \
       (B >= 20 and B <= 30 and (C <= 12 or (A > 90 and D <= 80))) or \
       (C >= 99):
        return 4
    
    # Output=2 conditions
    elif (B >= 65 and C >= 70 and A <= 30) or \
         (B >= 65 and C >= 47 and E <= 10) or \
         (B >= 80 and C >= 30 and D > 60 and E < 40):
        return 2
    
    # Output=3 conditions
    elif (B <= 15 and C <= 12) or \
         (B >= 98 and C >= 92) or \
         (B == 32 and D <= 20) or \
         (E <= 36 and B <= 31 and C >= 38 and D < 40) or \
         (B >= 42 and C >= 40 and E <= 70 and A > 50):
        return 3
    
    # Default to Output=1
    else:
        return 1