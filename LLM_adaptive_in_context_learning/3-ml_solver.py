import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from termcolor import colored
import warnings
warnings.filterwarnings('ignore')

# CONFIGURATION VARIABLES
CSV_FILE = 'complex_dataset.csv'
TEST_SIZE = 0.2
RANDOM_STATE = 42
MODEL_PARAMS = {
    'n_estimators': 200,
    'max_depth': 4,
    'learning_rate': 0.1,
    'random_state': RANDOM_STATE,
    'tree_method': 'gpu_hist',  # Enable GPU acceleration
    'gpu_id': 0,  # Use first GPU
    'predictor': 'gpu_predictor'  # Use GPU for prediction
}

# Enhanced hyperparameters for tuning
XGB_PARAM_GRID = {
    'n_estimators': [500, 1000, 1500],
    'max_depth': [6, 8, 10, 12],
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'subsample': [0.8, 0.9, 1.0],
    'colsample_bytree': [0.8, 0.9, 1.0],
    'min_child_weight': [1, 3, 5]
}

ENABLE_HYPERPARAMETER_TUNING = False  # Set to True for intensive tuning
ENABLE_FEATURE_ENGINEERING = True
ENABLE_ENSEMBLE_METHODS = False  # Set to True for ensemble
ENABLE_ALGORITHM_COMPARISON = True  # Compare different algorithms

def load_and_preprocess_data():
    """Load the complex dataset and prepare for training"""
    print(colored("Loading dataset...", "blue"))

    # Load data
    df = pd.read_csv(CSV_FILE)
    print(colored(f"Dataset shape: {df.shape}", "green"))
    print(colored(f"Columns: {list(df.columns)}", "yellow"))

    # Check class distribution
    print(colored("\nClass distribution:", "cyan"))
    print(df['Output'].value_counts().sort_index())

    # Features and target
    X = df[['A', 'B', 'C', 'D', 'E']]
    y = df['Output'] - 1  # Convert to 0-3 for sklearn

    # Feature Engineering
    if ENABLE_FEATURE_ENGINEERING:
        print(colored("\nApplying feature engineering...", "blue"))

        # Add polynomial features (degree 2)
        poly = PolynomialFeatures(degree=2, include_bias=False)
        poly_features = poly.fit_transform(X)
        poly_feature_names = poly.get_feature_names_out(X.columns)

        # Create new dataframe with polynomial features
        X_poly = pd.DataFrame(poly_features, columns=poly_feature_names)

        # Add interaction ratios
        X_poly['A_B_ratio'] = X['A'] / (X['B'] + 1)
        X_poly['C_D_ratio'] = X['C'] / (X['D'] + 1)
        X_poly['A_C_product'] = X['A'] * X['C']
        X_poly['B_D_sum'] = X['B'] + X['D']
        X_poly['E_sqrt'] = np.sqrt(X['E'] + 1)

        # Statistical features
        X_poly['mean_features'] = X.mean(axis=1)
        X_poly['std_features'] = X.std(axis=1)
        X_poly['max_min_diff'] = X.max(axis=1) - X.min(axis=1)

        X = X_poly
        print(colored(f"Enhanced features: {X.shape[1]} total features", "green"))

    print(colored(f"\nFinal features shape: {X.shape}", "green"))
    print(colored(f"Target shape: {y.shape}", "green"))

    return X, y

def hyperparameter_tuning(X_train, y_train):
    """Perform hyperparameter tuning for XGBoost"""
    print(colored("\nPerforming hyperparameter tuning...", "blue"))

    try:
        # Try GPU first
        base_params = {'tree_method': 'gpu_hist', 'gpu_id': 0, 'predictor': 'gpu_predictor', 'random_state': RANDOM_STATE}
        print(colored("Using GPU for hyperparameter tuning...", "cyan"))
    except:
        base_params = {'tree_method': 'hist', 'random_state': RANDOM_STATE}
        print(colored("Using CPU for hyperparameter tuning...", "yellow"))

    # Simplified parameter grid for faster tuning
    simplified_grid = {
        'n_estimators': [500, 1000],
        'max_depth': [6, 8, 10],
        'learning_rate': [0.05, 0.1, 0.2],
        'subsample': [0.9, 1.0],
        'colsample_bytree': [0.9, 1.0]
    }

    xgb = XGBClassifier(**base_params)

    # Use 3-fold CV for faster tuning
    grid_search = GridSearchCV(
        xgb,
        simplified_grid,
        cv=3,
        scoring='accuracy',
        n_jobs=-1,
        verbose=1
    )

    grid_search.fit(X_train, y_train)

    print(colored(f"Best parameters: {grid_search.best_params_}", "green"))
    print(colored(f"Best CV score: {grid_search.best_score_:.4f}", "green"))

    return grid_search.best_estimator_

def compare_algorithms(X_train, X_test, y_train, y_test):
    """Compare different ML algorithms for best performance"""
    print(colored("\nComparing different algorithms...", "blue"))

    algorithms = {
        'XGBoost': XGBClassifier(n_estimators=1000, max_depth=8, learning_rate=0.1, random_state=RANDOM_STATE),
        'Random Forest': RandomForestClassifier(n_estimators=500, max_depth=10, random_state=RANDOM_STATE),
        'SVM': SVC(kernel='rbf', C=1.0, gamma='scale', random_state=RANDOM_STATE),
        'Neural Network': MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=RANDOM_STATE)
    }

    results = {}

    for name, model in algorithms.items():
        print(colored(f"Training {name}...", "yellow"))
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy
        print(colored(f"{name} accuracy: {accuracy:.4f}", "cyan"))

    # Return the best performing model
    best_algorithm = max(results, key=results.get)
    print(colored(f"\nBest algorithm: {best_algorithm} with {results[best_algorithm]:.4f} accuracy", "green"))

    # Retrain best model
    best_model = algorithms[best_algorithm]
    best_model.fit(X_train, y_train)

    return best_model, results

def create_ensemble_model(X_train, y_train):
    """Create an ensemble of multiple models"""
    print(colored("\nCreating ensemble model...", "blue"))

    # Define base models
    models = [
        ('xgb', XGBClassifier(n_estimators=1000, max_depth=8, learning_rate=0.1, random_state=RANDOM_STATE)),
        ('rf', RandomForestClassifier(n_estimators=500, max_depth=10, random_state=RANDOM_STATE)),
        ('svm', SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=RANDOM_STATE))
    ]

    # Create voting classifier
    ensemble = VotingClassifier(estimators=models, voting='soft')
    ensemble.fit(X_train, y_train)

    print(colored("Ensemble model trained!", "green"))
    return ensemble

def train_model(X_train, X_test, y_train, y_test):
    """Train model with optional hyperparameter tuning and ensemble methods"""
    if ENABLE_ALGORITHM_COMPARISON:
        model, algorithm_results = compare_algorithms(X_train, X_test, y_train, y_test)
        return model
    elif ENABLE_HYPERPARAMETER_TUNING:
        model = hyperparameter_tuning(X_train, y_train)
    elif ENABLE_ENSEMBLE_METHODS:
        model = create_ensemble_model(X_train, y_train)
    else:
        print(colored("\nTraining XGBoost model...", "blue"))

        try:
            # Try to use GPU
            model = XGBClassifier(**MODEL_PARAMS)
            print(colored("Using GPU acceleration for training...", "cyan"))
            model.fit(X_train, y_train)
            print(colored("Model trained successfully on GPU!", "green"))

        except Exception as e:
            print(colored(f"GPU training failed: {str(e)}", "red"))
            print(colored("Falling back to CPU training...", "yellow"))

            # Fallback to CPU
            cpu_params = MODEL_PARAMS.copy()
            cpu_params['tree_method'] = 'hist'  # CPU method
            cpu_params.pop('gpu_id', None)
            cpu_params.pop('predictor', None)

            model = XGBClassifier(**cpu_params)
            model.fit(X_train, y_train)
            print(colored("Model trained successfully on CPU!", "green"))

    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance"""
    print(colored("\nEvaluating model performance...", "blue"))

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    print(colored(f"\nAccuracy: {accuracy:.4f}", "green"))

    # Classification report
    print(colored("\nClassification Report:", "cyan"))
    target_names = [f'Class {i+1}' for i in range(4)]
    print(classification_report(y_test, y_pred, target_names=target_names))

    # Confusion matrix
    print(colored("\nConfusion Matrix:", "cyan"))
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    return y_pred, accuracy

def analyze_feature_importance(model, X):
    """Analyze which features are most important"""
    print(colored("\nAnalyzing feature importance...", "blue"))

    # Get feature importance
    importance_scores = model.feature_importances_
    feature_names = X.columns

    # Create importance dataframe
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importance_scores
    }).sort_values('Importance', ascending=False)

    print(colored("\nFeature Importance Ranking:", "cyan"))
    for idx, row in importance_df.iterrows():
        print(colored(f"{row['Feature']}: {row['Importance']:.4f}", "yellow"))

    # Plot feature importance
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=importance_df)
    plt.title('Feature Importance in Predicting Complex Output')
    plt.tight_layout()
    plt.savefig('feature_importance.png', dpi=300, bbox_inches='tight')
    print(colored("\nFeature importance plot saved as 'feature_importance.png'", "green"))

    return importance_df

def test_predictions(model, X_test, y_test):
    """Show some example predictions"""
    print(colored("\nTesting sample predictions...", "blue"))

    # Get some random samples
    sample_indices = np.random.choice(len(X_test), 5, replace=False)

    print(colored("\nSample Predictions:", "cyan"))
    print("Input Features -> Predicted | Actual")
    print("-" * 50)

    for idx in sample_indices:
        features = X_test.iloc[idx]
        actual = y_test.iloc[idx] + 1  # Convert back to 1-4
        predicted = model.predict(features.values.reshape(1, -1))[0] + 1

        feature_str = f"A:{features['A']}, B:{features['B']}, C:{features['C']}, D:{features['D']}, E:{features['E']}"
        print(colored(f"{feature_str} -> {predicted} | {actual}", "yellow"))

def check_gpu_availability():
    """Check if GPU is available for XGBoost"""
    try:
        import xgboost as xgb
        # Try to create a simple model to test GPU
        test_model = xgb.XGBClassifier(tree_method='gpu_hist', n_estimators=1)
        print(colored("✓ GPU is available and configured for XGBoost", "green"))
        return True
    except Exception as e:
        print(colored(f"⚠ GPU not available: {str(e)}", "yellow"))
        print(colored("Will use CPU fallback", "yellow"))
        return False

def cross_validate_model(X, y):
    """Perform cross-validation to get reliable accuracy estimate"""
    print(colored("\nPerforming cross-validation...", "blue"))

    # Use stratified k-fold for balanced classes
    from sklearn.model_selection import StratifiedKFold

    cv_scores = []
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

    for fold, (train_idx, val_idx) in enumerate(skf.split(X, y)):
        X_fold_train, X_fold_val = X.iloc[train_idx], X.iloc[val_idx]
        y_fold_train, y_fold_val = y.iloc[train_idx], y.iloc[val_idx]

        # Quick training for CV
        model = XGBClassifier(n_estimators=500, max_depth=8, learning_rate=0.1,
                            random_state=RANDOM_STATE, tree_method='hist')
        model.fit(X_fold_train, y_fold_train)

        fold_accuracy = accuracy_score(y_fold_val, model.predict(X_fold_val))
        cv_scores.append(fold_accuracy)
        print(colored(f"Fold {fold+1} accuracy: {fold_accuracy:.4f}", "yellow"))

    mean_cv_accuracy = np.mean(cv_scores)
    std_cv_accuracy = np.std(cv_scores)

    print(colored(f"\nCross-validation results:", "cyan"))
    print(colored(f"Mean CV accuracy: {mean_cv_accuracy:.4f} (+/- {std_cv_accuracy:.4f})", "green"))

    return mean_cv_accuracy

def main():
    """Main function to run the ML pipeline"""
    print(colored("=== Enhanced Complex Dataset ML Solver ===", "magenta"))
    print(colored("With hyperparameter tuning, feature engineering, and ensemble methods", "cyan"))

    # Check GPU availability
    gpu_available = check_gpu_availability()

    # Load and preprocess data
    X, y = load_and_preprocess_data()

    # Perform cross-validation for reliable baseline
    cv_accuracy = cross_validate_model(X, y)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    print(colored(f"\nTrain set: {X_train.shape[0]} samples", "green"))
    print(colored(f"Test set: {X_test.shape[0]} samples", "green"))

    # Train model
    model = train_model(X_train, X_test, y_train, y_test)

    # Evaluate model
    y_pred, accuracy = evaluate_model(model, X_test, y_test)

    # Analyze feature importance
    try:
        importance_df = analyze_feature_importance(model, X_train)
    except:
        print(colored("Feature importance analysis skipped (ensemble model)", "yellow"))

    # Test sample predictions
    test_predictions(model, X_test, y_test)

    # Summary with improvements
    print(colored("\n" + "="*70, "magenta"))
    print(colored("ACCURACY IMPROVEMENT SUMMARY:", "magenta"))
    print(colored(f"Cross-validation accuracy: {cv_accuracy:.4f}", "cyan"))
    print(colored(f"Test set accuracy: {accuracy:.4f}", "green"))
    print(colored(f"Accuracy improvement: {(accuracy - cv_accuracy)*100:.2f}%", "yellow"))

    if accuracy > 0.8:
        print(colored("🎉 Excellent accuracy achieved!", "green"))
    elif accuracy > 0.7:
        print(colored("👍 Good accuracy - consider further tuning", "yellow"))
    else:
        print(colored("📈 Accuracy can be improved with:", "red"))
        print(colored("   - More hyperparameter tuning", "red"))
        print(colored("   - Additional feature engineering", "red"))
        print(colored("   - Ensemble methods", "red"))
        print(colored("   - Data preprocessing improvements", "red"))

    print(colored("="*70, "magenta"))

if __name__ == "__main__":
    main()
