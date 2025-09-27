"""
Predictor 94
Generated on: 2025-09-09 06:32:45
Accuracy: 52.89%
"""


# PREDICTOR 94 - Accuracy: 52.89%
# Correct predictions: 5289/10000 (52.89%)

def predict_output(A, B, C, D, E):
    # Class 1 conditions: very high A, very low D, or specific high patterns
    if (A >= 85 and B >= 65 and C <= 20 and D >= 85 and E <= 10) or \
       (A >= 40 and A <= 50 and B >= 60 and C >= 50 and D <= 5) or \
       (A >= 85 and B <= 35 and C >= 60 and D <= 30) or \
       (A <= 50 and B >= 90 and C <= 15 and D <= 30 and E <= 20) or \
       (A <= 45 and B <= 25 and C >= 50 and D >= 75 and E >= 90):
        return 1
    
    # Class 3 conditions: low C with specific patterns
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 20 and C <= 15 and E <= 25) or \
       (E <= 20 and B >= 60 and C < 50) or \
       (B <= 10 and E <= 30) or \
       (E <= 15 and B >= 70 and C <= 30) or \
       (B <= 25 and C <= 35 and E < 30) or \
       (B <= 35 and E < 25 and D < 20) or \
       (A <= 15 and C <= 15 and E <= 15) or \
       (B >= 40 and B <= 50 and C >= 40 and C <= 50 and E >= 25):
        return 3
    
    # Class 4 conditions: specific ranges and patterns
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (E >= 90 and not (B >= 90 and C >= 70)) or \
       (C <= 10 and D >= 90 and B > 15) or \
       (B >= 80 and E >= 80 and C < 50) or \
       (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
       (B <= 10 and D >= 40 and E < 10) or \
       (A >= 90 and B <= 10 and E >= 60) or \
       (B >= 95 and C <= 20) or \
       (B <= 20 and D >= 50 and E <= 25) or \
       (B >= 75 and C <= 10) or \
       (C <= 10 and D >= 90) or \
       (B <= 30 and D >= 60 and E <= 5) or \
       (B >= 60 and C <= 20 and E >= 90) or \
       (C <= 5 and B >= 50 and E >= 70) or \
       (C <= 15 and D >= 80 and E <= 20) or \
       (C <= 15 and B >= 50 and E >= 70) or \
       (B >= 50 and B <= 60 and C <= 25 and D >= 45 and E >= 75):
        return 4
    
    # Class 2 conditions: high B with specific constraints
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
       (B >= 90 and C >= 80) or \
       (B >= 85 and C >= 70 and D >= 60) or \
       (A <= 20 and B >= 90 and C >= 70) or \
       (B >= 92 and C >= 40 and C <= 70) or \
       (B >= 65 and C < 50 and D >= 60 and A <= 40) or \
       (B >= 85 and C >= 30 and C <= 50) or \
       (B >= 80 and C >= 20 and D >= 70) or \
       (B >= 55 and B <= 60 and C >= 45 and C <= 60 and D >= 35 and D <= 55):
        return 2
    
    # Default to class 1
    return 1