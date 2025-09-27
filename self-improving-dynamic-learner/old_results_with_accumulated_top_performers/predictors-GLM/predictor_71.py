"""
Predictor 71
Generated on: 2025-09-09 06:09:31
Accuracy: 52.98%
"""


# PREDICTOR 71 - Accuracy: 52.98%
# Correct predictions: 5298/10000 (52.98%)

def predict_output(A, B, C, D, E):
    # Class 3: low B, low C, low E
    if (B <= 15 and C <= 12 and E < 40):
        return 3
    
    # Class 4: specific combinations of B, C, D, E ranges
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (E >= 90) or \
         (B >= 90 and C <= 35 and A >= 10) or \
         (B >= 80 and E >= 80) or \
         (B <= 10 and C >= 60):
        return 4
    
    # Class 2: high B with moderate A and high C, or very high B and C
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or (B >= 90 and C >= 80):
        return 2
    
    # Default to class 1
    else:
        return 1