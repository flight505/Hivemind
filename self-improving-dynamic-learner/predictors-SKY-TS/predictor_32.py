"""
Predictor 32
Generated on: 2025-09-09 19:14:13
Accuracy: 42.36%
"""


# PREDICTOR 32 - Accuracy: 42.36%
# Correct predictions: 4236/10000 (42.36%)

def predict_output(A, B, C, D, E):
    if B >= A and B >= C and B >= D and B >= E:
        if C > 50:
            return 2
        elif E > 50:
            return 4
        else:
            if A * E < 100:
                return 3
            else:
                return 1
    elif C >= A and C >= B and C >= D and C >= E:
        if D < 30:
            return 4
        else:
            return 1
    elif D >= A and D >= B and D >= C and D >= E:
        if B > 80:
            return 4
        elif D > 80 or B < 20 or C > 40:
            return 1
        else:
            return 3
    elif A >= B and A >= C and A >= D and A >= E:
        return 3
    elif E >= A and E >= B and E >= C and E >= D:
        if E > 50:
            return 4
        else:
            return 3
    else:
        return 1