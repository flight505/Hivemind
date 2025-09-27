"""
Predictor 4
Generated on: 2025-09-09 03:55:14
Accuracy: 45.86%
"""


# PREDICTOR 4 - Accuracy: 45.86%
# Correct predictions: 4586/10000 (45.86%)

def predict_output(A, B, C, D, E):
    # Output class 4 conditions
    if (B <= 15 and C <= 12 and E >= 60) or (B == 36 and 40 <= A <= 50 and 15 <= D <= 30):
        return 4
    
    # Output class 3 conditions
    elif B <= 15 and C <= 12 and E < 60:
        return 3
    
    # Output class 2 conditions
    elif (B >= 65 and C >= 70 and A <= 50) or \
         (B >= 84 and C >= 29 and D >= 50) or \
         (B >= 65 and 40 <= C < 70 and D <= 70 and A <= 90) or \
         (B >= 40 and C >= 40 and E >= 40):
        return 2
    
    # Default to output class 1
    else:
        return 1