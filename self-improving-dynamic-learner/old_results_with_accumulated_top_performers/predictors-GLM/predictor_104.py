"""
Predictor 104
Generated on: 2025-09-09 07:02:16
Accuracy: 50.25%
"""


# PREDICTOR 104 - Accuracy: 50.25%
# Correct predictions: 5025/10000 (50.25%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions: expanded patterns for low values
    if (B <= 15 and C <= 12 and E < 40) or (B <= 20 and E <= 10) or (C <= 15 and E <= 15):
        return 3
    
    # Class 4 conditions: expanded patterns for moderate B/D and high E
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or (E >= 90) or \
         (B <= 20 and D >= 60 and E >= 60) or (B >= 80 and C <= 40) or \
         (A >= 90 and B <= 10) or (D <= 10 and E >= 80):
        return 4
    
    # Class 2 conditions: expanded patterns for high B
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or (B >= 90 and C >= 80) or \
         (A <= 10 and B >= 80) or (B >= 80 and D <= 10) or (B >= 85 and C <= 40):
        return 2
    
    # Default to class 1
    else:
        return 1