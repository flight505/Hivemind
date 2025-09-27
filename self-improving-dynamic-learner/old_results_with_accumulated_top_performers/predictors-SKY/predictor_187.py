"""
Predictor 187
Generated on: 2025-09-09 07:35:55
Accuracy: 42.11%
"""


# PREDICTOR 187 - Accuracy: 42.11%
# Correct predictions: 4211/10000 (42.11%)

def predict_output(A, B, C, D, E):
    if A >= B and A >= C and A >= D and A >= E:
        if E < 10:
            return 4
        elif A > 90 and C < 50:
            return 4
        elif C > 60:
            return 1
        else:
            return 3
    elif B >= A and B >= C and B >= D and B >= E:
        if C > 70:
            return 2
        else:
            return 1
    elif C >= A and C >= B and C >= D and C >= E:
        if A > 60:
            return 1
        else:
            return 2
    elif D >= A and D >= B and D >= C and D >= E:
        if D > 70:
            if A > 70:
                return 3
            else:
                return 1
        else:
            return 3
    else:
        return 4