"""
Predictor 72
Generated on: 2025-09-09 06:13:14
Accuracy: 51.56%
"""


# PREDICTOR 72 - Accuracy: 51.56%
# Correct predictions: 5156/10000 (51.56%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 20 and C <= 7 and E < 40) or \
       (B <= 35 and C <= 13 and E < 30) or \
       (B <= 35 and D > 90 and C <= 40 and E >= 90):
        return 3
    
    # Class 4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36 and C < 60) or \
         (E >= 90 and not (D > 90 and C < 40)) or \
         (B >= 90 and C <= 35 and A >= 10) or \
         (B >= 80 and E >= 80) or \
         (B <= 10 and C >= 60) or \
         (B <= 10 and C >= 30 and D >= 20) or \
         (B <= 25 and C >= 90) or \
         (B >= 60 and D >= 70 and C <= 30):
        return 4
    
    # Class 2 conditions
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
         (B >= 90 and C >= 80) or \
         (B >= 75 and A <= 20 and C >= 40) or \
         (B >= 80 and A <= 50 and C >= 50) or \
         (C >= 90 and B <= 15):
        return 2
    
    # Default to class 1
    else:
        return 1