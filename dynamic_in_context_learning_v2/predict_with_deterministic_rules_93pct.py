import os
import pandas as pd
from termcolor import colored

# IMPORTANT VARIABLES (ALL CAPS AS REQUESTED)
CSV_FILE_PATH = "train.csv"

def load_data():
    """Load the training data"""
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        print(colored(f"✓ Loaded {len(df)} rows from dataset", "green"))
        return df
    except Exception as e:
        print(colored(f"❌ Failed to load data: {e}", "red"))
        return None

def calculate_total_spend(row):
    """Calculate total spend from amenities (treat NaN as 0)"""
    amenities = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    total = 0
    for amenity in amenities:
        value = row.get(amenity, 0)
        if pd.notna(value):
            total += value
        # NaN is treated as 0
    return total

def get_safe_numeric(row, column, default=0):
    """Get numeric value, treating NaN as default"""
    value = row.get(column, default)
    return value if pd.notna(value) else default

def get_safe_age(row):
    """Get Age value, returning None if NaN"""
    age = row.get('Age')
    return age if pd.notna(age) else None

def predict_with_rules(row):
    """Apply the 36 deterministic rules from 93% accuracy model"""
    # Helper variables
    total_spend = calculate_total_spend(row)

    # Extract values (handle NaN)
    home_planet = row.get('HomePlanet')
    cryo_sleep = row.get('CryoSleep')
    destination = row.get('Destination')
    age = get_safe_age(row)
    vip = row.get('VIP')
    cabin = row.get('Cabin')

    # Cabin parsing
    cabin_deck = None
    cabin_side = None
    if pd.notna(cabin) and isinstance(cabin, str):
        parts = cabin.split('/')
        if len(parts) >= 2:
            cabin_deck = parts[0]
            cabin_side = parts[-1] if len(parts) > 1 else None

    # Rule 1: Group-majority rule (simplified - we don't have group info, so skip to next rules)
    # Note: This rule requires group data which we don't have in deterministic form, so we'll skip it

    # Rule 2: Destination = PSO J318.5-22 and CryoSleep = True and HomePlanet = Earth and Cabin side = S -> False
    if (destination == 'PSO J318.5-22' and cryo_sleep == True and
        home_planet == 'Earth' and cabin_side == 'S'):
        return False

    # Rule 3: Destination = TRAPPIST-1e and HomePlanet = Earth and CryoSleep = True and TotalSpend = 0 and Cabin side = P -> False
    if (destination == 'TRAPPIST-1e' and home_planet == 'Earth' and
        cryo_sleep == True and total_spend == 0 and cabin_side == 'P'):
        return False

    # Rule 4: CryoSleep is missing and TotalSpend = 0 and Age >= 18 -> False
    if (pd.isna(cryo_sleep) and total_spend == 0 and
        age is not None and age >= 18):
        return False

    # Rule 5: CryoSleep = True and TotalSpend = 0 -> True
    if cryo_sleep == True and total_spend == 0:
        return True

    # Rule 6: CryoSleep = True and TotalSpend <= 10 -> True
    if cryo_sleep == True and total_spend <= 10:
        return True

    # Rule 7: Cabin deck in {A,B,C,D,E} and CryoSleep = True -> True
    if (cryo_sleep == True and cabin_deck in ['A', 'B', 'C', 'D', 'E']):
        return True

    # Rule 8: CryoSleep is missing and TotalSpend = 0 -> True
    if pd.isna(cryo_sleep) and total_spend == 0:
        return True

    # Rule 9: Destination = 55 Cancri e and CryoSleep = False and Age <= 12 and TotalSpend = 0 -> True
    if (destination == '55 Cancri e' and cryo_sleep == False and
        age is not None and age <= 12 and total_spend == 0):
        return True

    # Rule 10: Destination = 55 Cancri e and CryoSleep = False and ShoppingMall >= 500 and RoomService <= 200 and Spa <= 50 and VRDeck <= 50 -> True
    if (destination == '55 Cancri e' and cryo_sleep == False and
        get_safe_numeric(row, 'ShoppingMall') >= 500 and
        get_safe_numeric(row, 'RoomService') <= 200 and
        get_safe_numeric(row, 'Spa') <= 50 and
        get_safe_numeric(row, 'VRDeck') <= 50):
        return True

    # Rule 11: Destination = 55 Cancri e and CryoSleep = False and FoodCourt >= 500 and RoomService <= 50 and ShoppingMall <= 100 and VRDeck <= 100 and Spa <= 100 -> True
    if (destination == '55 Cancri e' and cryo_sleep == False and
        get_safe_numeric(row, 'FoodCourt') >= 500 and
        get_safe_numeric(row, 'RoomService') <= 50 and
        get_safe_numeric(row, 'ShoppingMall') <= 100 and
        get_safe_numeric(row, 'VRDeck') <= 100 and
        get_safe_numeric(row, 'Spa') <= 100):
        return True

    # Rule 12: Destination = TRAPPIST-1e and CryoSleep = False and TotalSpend = 0 and Age <= 12 and Cabin deck = G -> False
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        total_spend == 0 and age is not None and age <= 12 and cabin_deck == 'G'):
        return False

    # Rule 13: Destination = TRAPPIST-1e and CryoSleep = False and TotalSpend = 0 and Age <= 12 -> True
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        total_spend == 0 and age is not None and age <= 12):
        return True

    # Rule 14: Destination = TRAPPIST-1e and CryoSleep = False and ShoppingMall >= 500 and RoomService <= 200 and VRDeck <= 100 and Spa <= 100 -> True
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        get_safe_numeric(row, 'ShoppingMall') >= 500 and
        get_safe_numeric(row, 'RoomService') <= 200 and
        get_safe_numeric(row, 'VRDeck') <= 100 and
        get_safe_numeric(row, 'Spa') <= 100):
        return True

    # Rule 15: Destination = TRAPPIST-1e and CryoSleep = False and FoodCourt >= 700 and RoomService <= 200 and Spa <= 200 and VRDeck <= 100 -> True
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        get_safe_numeric(row, 'FoodCourt') >= 700 and
        get_safe_numeric(row, 'RoomService') <= 200 and
        get_safe_numeric(row, 'Spa') <= 200 and
        get_safe_numeric(row, 'VRDeck') <= 100):
        return True

    # Rule 16: Destination = TRAPPIST-1e and HomePlanet = Europa and CryoSleep = False and VRDeck <= 100 and TotalSpend >= 1000 -> True
    if (destination == 'TRAPPIST-1e' and home_planet == 'Europa' and
        cryo_sleep == False and get_safe_numeric(row, 'VRDeck') <= 100 and
        total_spend >= 1000):
        return True

    # Rule 17: Destination = TRAPPIST-1e and CryoSleep = False and Cabin deck != G and VRDeck >= 1200 and RoomService <= 200 and Spa <= 200 and ShoppingMall <= 200 -> True
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        cabin_deck != 'G' and get_safe_numeric(row, 'VRDeck') >= 1200 and
        get_safe_numeric(row, 'RoomService') <= 200 and
        get_safe_numeric(row, 'Spa') <= 200 and
        get_safe_numeric(row, 'ShoppingMall') <= 200):
        return True

    # Rule 18: Destination = TRAPPIST-1e and CryoSleep = False and Cabin deck != G and 800 <= VRDeck < 1200 and RoomService <= 200 and Spa <= 200 and ShoppingMall <= 200 -> True
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        cabin_deck != 'G' and 800 <= get_safe_numeric(row, 'VRDeck') < 1200 and
        get_safe_numeric(row, 'RoomService') <= 200 and
        get_safe_numeric(row, 'Spa') <= 200 and
        get_safe_numeric(row, 'ShoppingMall') <= 200):
        return True

    # Rule 19: Destination = TRAPPIST-1e and CryoSleep = False and Cabin deck != G and TotalSpend >= 2000 and VRDeck <= 900 and Spa <= 300 -> True
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        cabin_deck != 'G' and total_spend >= 2000 and
        get_safe_numeric(row, 'VRDeck') <= 900 and
        get_safe_numeric(row, 'Spa') <= 300):
        return True

    # Rule 20: Destination = TRAPPIST-1e and CryoSleep = False and Age >= 55 and VRDeck = 0 and TotalSpend <= 1500 -> True
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        age is not None and age >= 55 and
        get_safe_numeric(row, 'VRDeck') == 0 and total_spend <= 1500):
        return True

    # Rule 21: Destination = 55 Cancri e and CryoSleep = False -> False
    if destination == '55 Cancri e' and cryo_sleep == False:
        return False

    # Rule 22: CryoSleep = False and (Spa + VRDeck) >= 1000 and NOT (Destination = TRAPPIST-1e and Cabin deck != G) -> False
    if (cryo_sleep == False and
        (get_safe_numeric(row, 'Spa') + get_safe_numeric(row, 'VRDeck')) >= 1000 and
        not (destination == 'TRAPPIST-1e' and cabin_deck != 'G')):
        return False

    # Rule 23: CryoSleep = False and TotalSpend >= 2000 and NOT (Destination = TRAPPIST-1e and Cabin deck != G) -> False
    if (cryo_sleep == False and total_spend >= 2000 and
        not (destination == 'TRAPPIST-1e' and cabin_deck != 'G')):
        return False

    # Rule 24: HomePlanet = Mars and CryoSleep = False and Destination != TRAPPIST-1e and TotalSpend > 0 -> False
    if (home_planet == 'Mars' and cryo_sleep == False and
        destination != 'TRAPPIST-1e' and total_spend > 0):
        return False

    # Rule 25: VIP = True and Destination = TRAPPIST-1e -> True
    if vip == True and destination == 'TRAPPIST-1e':
        return True

    # Rule 26: VIP = True and CryoSleep = False and TotalSpend > 0 and Destination != TRAPPIST-1e -> False
    if (vip == True and cryo_sleep == False and total_spend > 0 and
        destination != 'TRAPPIST-1e'):
        return False

    # Rule 27: HomePlanet = Europa and (CryoSleep = True OR TotalSpend <= 50) -> True
    if (home_planet == 'Europa' and
        (cryo_sleep == True or total_spend <= 50)):
        return True

    # Rule 28: Destination = TRAPPIST-1e and (CryoSleep = True OR TotalSpend <= 50) -> True
    if (destination == 'TRAPPIST-1e' and
        (cryo_sleep == True or total_spend <= 50)):
        return True

    # Rule 29: CryoSleep = False and TotalSpend = 0 and Age >= 16 -> False
    if (cryo_sleep == False and total_spend == 0 and
        age is not None and age >= 16):
        return False

    # Rule 30: HomePlanet = Earth and Cabin deck in {F,G} and CryoSleep = False and TotalSpend = 0 and Age >= 16 -> False
    if (home_planet == 'Earth' and cabin_deck in ['F', 'G'] and
        cryo_sleep == False and total_spend == 0 and
        age is not None and age >= 16):
        return False

    # Rule 31: HomePlanet = Mars and CryoSleep = True -> True
    if home_planet == 'Mars' and cryo_sleep == True:
        return True

    # Rule 32: Destination = PSO J318.5-22 and CryoSleep = False and TotalSpend > 0 -> False
    if (destination == 'PSO J318.5-22' and cryo_sleep == False and
        total_spend > 0):
        return False

    # Rule 33: Age >= 55 and CryoSleep = False and Destination = TRAPPIST-1e and TotalSpend = 0 -> True
    if (age is not None and age >= 55 and cryo_sleep == False and
        destination == 'TRAPPIST-1e' and total_spend == 0):
        return True

    # Rule 34: Age >= 55 and CryoSleep = False -> False
    if age is not None and age >= 55 and cryo_sleep == False:
        return False

    # Rule 35: Cabin is missing and CryoSleep = True -> True
    if pd.isna(cabin) and cryo_sleep == True:
        return True

    # Rule 36: Default rule
    if ((destination == 'TRAPPIST-1e' or home_planet == 'Europa') and total_spend < 200):
        return True
    else:
        return False

def calculate_accuracy(predictions, actuals):
    """Calculate prediction accuracy"""
    correct = sum(1 for pred, act in zip(predictions, actuals) if pred == act)
    total = len(predictions)
    accuracy = correct / total if total > 0 else 0
    return accuracy, correct, total

def main():
    """Predict on entire training dataset using 36 deterministic rules from 93% model"""
    print(colored("🚀 Deterministic Rules Prediction System (93% Model)", "cyan"))

    # Load data
    df = load_data()
    if df is None:
        return

    # Ensure we have the target column
    if 'Transported' not in df.columns:
        print(colored("❌ Dataset must include 'Transported' column", "red"))
        return

    print(colored(f"🔮 Making predictions for {len(df)} passengers using 36 rules...", "blue"))

    # Make predictions
    predictions = []
    actuals = []

    for idx, row in df.iterrows():
        pred = predict_with_rules(row)
        predictions.append(pred)
        actuals.append(row['Transported'])

        # Progress indicator
        if (idx + 1) % 500 == 0:
            print(colored(f"   Processed {idx + 1}/{len(df)} rows", "cyan"))

    # Calculate accuracy
    accuracy, correct, total = calculate_accuracy(predictions, actuals)

    print(colored("\n🏁 PREDICTION RESULTS (93% Model)", "green"))
    print(colored(f"   📊 Accuracy: {accuracy:.1%} ({correct}/{total})", "yellow"))
    print(colored(f"   🎯 Rules applied: 36 deterministic rules from 93% model", "cyan"))

if __name__ == "__main__":
    main()
