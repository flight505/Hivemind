"""
Predictor 102
Generated on: 2025-09-09 07:00:03
Accuracy: 56.01%
"""


# PREDICTOR 102 - Accuracy: 56.01%
# Correct predictions: 5601/10000 (56.01%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions: low B, low C, low E
    if B <= 15 and C <= 12 and E < 40:
        return 3
    
    # Class 4 conditions: specific B and D ranges or very high E
    elif B >= 28 and B <= 36 and D >= 15 and D <= 36:
        return 4
    elif E >= 90 and D < 80:
        return 4
    
    # Class 2 conditions: high B with moderate A and high C, or very high B and C
    elif (B >= 65 and A <= 50 and A > 20 and C >= 70) or (B >= 90 and C >= 80):
        return 2
    
    # Default to class 1
    else:
        return 1