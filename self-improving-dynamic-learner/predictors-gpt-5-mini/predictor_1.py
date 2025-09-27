"""
Predictor 1
Generated on: 2025-09-09 12:01:11
Accuracy: 40.58%
"""


# PREDICTOR 1 - Accuracy: 40.58%
# Correct predictions: 4058/10000 (40.58%)

def predict_output(A, B, C, D, E):
    A = float(A); B = float(B); C = float(C); D = float(D); E = float(E)
    # Small C values correspond to category 3
    if C <= 12:
        return 3
    # Very large E corresponds to category 4
    if E > 90:
        return 4
    # Very large C corresponds to category 2
    if C >= 78:
        return 2
    # Moderate-to-large B corresponds to category 1
    if B >= 29:
        return 1
    # Fallback rule (covers any remaining cases)
    if (A + B + C + D + E) > 200:
        return 1
    return 3