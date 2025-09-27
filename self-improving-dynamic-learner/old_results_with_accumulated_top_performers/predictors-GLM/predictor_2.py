"""
Predictor 2
Generated on: 2025-09-09 03:40:08
Accuracy: 52.86%
"""


# PREDICTOR 2 - Accuracy: 52.86%
# Correct predictions: 5286/10000 (52.86%)

def predict_output(A, B, C, D, E):
    # Class 3: 
    #   Condition 1: B<=15 and C<50
    #   Condition 2: B between 30-42, C between 38-40, E<90
    if (B <= 15 and C < 50) or (B >= 30 and B <= 42 and C >= 38 and C <= 40 and E < 90):
        return 3
    # Class 2:
    #   Condition 1: B>=65, A<=50, A>1
    #   Condition 2: E>=90, C>=36, D<=27
    elif (B >= 65 and A <= 50 and A > 1) or (E >= 90 and C >= 36 and D <= 27):
        return 2
    # Class 4:
    #   Condition: B between 28-36, D between 15-36
    elif B >= 28 and B <= 36 and D >= 15 and D <= 36:
        return 4
    # Otherwise class 1
    else:
        return 1