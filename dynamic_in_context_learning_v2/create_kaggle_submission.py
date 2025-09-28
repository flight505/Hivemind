import os
import pandas as pd
from termcolor import colored

# IMPORTANT VARIABLES (ALL CAPS AS REQUESTED)
TRAIN_CSV_PATH = "test.csv"
SUBMISSION_CSV_PATH = "submission.csv"

def load_data():
    """Load the training data"""
    try:
        df = pd.read_csv(TRAIN_CSV_PATH)
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
    """Apply the deterministic rules in order to predict Transported"""
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

    # Rule 2: Destination = TRAPPIST-1e, CryoSleep = False, RoomService >= 800 and (Spa + VRDeck) <= 100 and ShoppingMall <= 300 -> False
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        get_safe_numeric(row, 'RoomService') >= 800 and
        (get_safe_numeric(row, 'Spa') + get_safe_numeric(row, 'VRDeck')) <= 100 and
        get_safe_numeric(row, 'ShoppingMall') <= 300):
        return False

    # Rule 3: Destination = TRAPPIST-1e, CryoSleep = False, ShoppingMall >= 500 and VRDeck <= 100 and Spa <= 100 -> True
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        get_safe_numeric(row, 'ShoppingMall') >= 500 and
        get_safe_numeric(row, 'VRDeck') <= 100 and
        get_safe_numeric(row, 'Spa') <= 100):
        return True

    # Rule 4: Destination = TRAPPIST-1e, CryoSleep = False, FoodCourt >= 700 and RoomService <= 200 and Spa <= 500 and VRDeck <= 600 -> True
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        get_safe_numeric(row, 'FoodCourt') >= 700 and
        get_safe_numeric(row, 'RoomService') <= 200 and
        get_safe_numeric(row, 'Spa') <= 500 and
        get_safe_numeric(row, 'VRDeck') <= 600):
        return True

    # Rule 5: Destination = TRAPPIST-1e, CryoSleep = False, TotalSpend = 0 and Age <= 12 -> True
    if (destination == 'TRAPPIST-1e' and cryo_sleep == False and
        total_spend == 0 and age is not None and age <= 12):
        return True

    # Rule 6: Destination = 55 Cancri e, CryoSleep = False, (ShoppingMall >= 600 and RoomService <= 50 and Spa <= 50 and VRDeck <= 50) OR (FoodCourt >= 3000 and RoomService = 0 and VRDeck <= 200 and Spa <= 300) -> True
    if (destination == '55 Cancri e' and cryo_sleep == False and
        ((get_safe_numeric(row, 'ShoppingMall') >= 600 and get_safe_numeric(row, 'RoomService') <= 50 and
          get_safe_numeric(row, 'Spa') <= 50 and get_safe_numeric(row, 'VRDeck') <= 50) or
         (get_safe_numeric(row, 'FoodCourt') >= 3000 and get_safe_numeric(row, 'RoomService') == 0 and
          get_safe_numeric(row, 'VRDeck') <= 200 and get_safe_numeric(row, 'Spa') <= 300))):
        return True

    # Rule 7: Destination = 55 Cancri e, CryoSleep = False -> False
    if destination == '55 Cancri e' and cryo_sleep == False:
        return False

    # Rule 8: Destination is missing, CryoSleep = False, (FoodCourt >= 1200 and RoomService <= 200) -> True
    if (pd.isna(destination) and cryo_sleep == False and
        get_safe_numeric(row, 'FoodCourt') >= 1200 and get_safe_numeric(row, 'RoomService') <= 200):
        return True

    # Rule 9: Destination is missing, HomePlanet = Europa, CryoSleep = False, (VRDeck >= 500 OR FoodCourt >= 3000) -> True
    if (pd.isna(destination) and home_planet == 'Europa' and cryo_sleep == False and
        (get_safe_numeric(row, 'VRDeck') >= 500 or get_safe_numeric(row, 'FoodCourt') >= 3000)):
        return True

    # Rule 10: Destination is missing, CryoSleep = False, TotalSpend > 0 -> False
    if pd.isna(destination) and cryo_sleep == False and total_spend > 0:
        return False

    # Rule 11: CryoSleep is missing and TotalSpend = 0 and HomePlanet = Europa and Destination = TRAPPIST-1e -> False
    if (pd.isna(cryo_sleep) and total_spend == 0 and
        home_planet == 'Europa' and destination == 'TRAPPIST-1e'):
        return False

    # Rule 12: Destination = PSO J318.5-22, CryoSleep = True, HomePlanet = Earth, Age >= 10 -> False
    if (destination == 'PSO J318.5-22' and cryo_sleep == True and
        home_planet == 'Earth' and age is not None and age >= 10):
        return False

    # Rule 13: Destination = PSO J318.5-22, CryoSleep = True, HomePlanet = Earth, Cabin side = P -> False
    if (destination == 'PSO J318.5-22' and cryo_sleep == True and
        home_planet == 'Earth' and cabin_side == 'P'):
        return False

    # Rule 14: CryoSleep = True and TotalSpend = 0 -> True
    if cryo_sleep == True and total_spend == 0:
        return True

    # Rule 15: CryoSleep = True and TotalSpend <= 10 -> True
    if cryo_sleep == True and total_spend <= 10:
        return True

    # Rule 16: Cabin deck in {A,B,C,D,E} and CryoSleep = True -> True
    if (cryo_sleep == True and cabin_deck in ['A', 'B', 'C', 'D', 'E']):
        return True

    # Rule 17: CryoSleep = False and (Spa + VRDeck) >= 1000 and NOT (HomePlanet = Europa and Destination = TRAPPIST-1e) -> False
    if (cryo_sleep == False and
        (get_safe_numeric(row, 'Spa') + get_safe_numeric(row, 'VRDeck')) >= 1000 and
        not (home_planet == 'Europa' and destination == 'TRAPPIST-1e')):
        return False

    # Rule 18: CryoSleep = False and TotalSpend >= 2000 and NOT (Destination = TRAPPIST-1e and ShoppingMall >= 500 and VRDeck <= 100 and Spa <= 100) -> False
    if (cryo_sleep == False and total_spend >= 2000 and
        not (destination == 'TRAPPIST-1e' and get_safe_numeric(row, 'ShoppingMall') >= 500 and
             get_safe_numeric(row, 'VRDeck') <= 100 and get_safe_numeric(row, 'Spa') <= 100)):
        return False

    # Rule 19: HomePlanet = Mars and CryoSleep = False and Destination != TRAPPIST-1e and TotalSpend > 0 -> False
    if (home_planet == 'Mars' and cryo_sleep == False and
        destination != 'TRAPPIST-1e' and total_spend > 0):
        return False

    # Rule 20: VIP = True and Destination = TRAPPIST-1e -> True
    if vip == True and destination == 'TRAPPIST-1e':
        return True

    # Rule 21: VIP = True and CryoSleep = False and TotalSpend > 0 and Destination != TRAPPIST-1e -> False
    if (vip == True and cryo_sleep == False and total_spend > 0 and
        destination != 'TRAPPIST-1e'):
        return False

    # Rule 22: HomePlanet = Europa and (CryoSleep = True OR TotalSpend <= 50) -> True
    if (home_planet == 'Europa' and
        (cryo_sleep == True or total_spend <= 50)):
        return True

    # Rule 23: Destination = TRAPPIST-1e and (CryoSleep = True OR TotalSpend <= 50) -> True
    if (destination == 'TRAPPIST-1e' and
        (cryo_sleep == True or total_spend <= 50)):
        return True

    # Rule 24: CryoSleep = False and TotalSpend = 0 and Age >= 16 -> False
    if (cryo_sleep == False and total_spend == 0 and
        age is not None and age >= 16):
        return False

    # Rule 25: HomePlanet = Earth and Cabin deck in {F,G} and CryoSleep = False and TotalSpend = 0 and Age >= 16 -> False
    if (home_planet == 'Earth' and cabin_deck in ['F', 'G'] and
        cryo_sleep == False and total_spend == 0 and
        age is not None and age >= 16):
        return False

    # Rule 26: HomePlanet = Mars and CryoSleep = True -> True
    if home_planet == 'Mars' and cryo_sleep == True:
        return True

    # Rule 27: Destination = PSO J318.5-22 and CryoSleep = False and TotalSpend > 0 -> False
    if (destination == 'PSO J318.5-22' and cryo_sleep == False and
        total_spend > 0):
        return False

    # Rule 28: Age >= 55 and CryoSleep = False and Destination = TRAPPIST-1e and TotalSpend = 0 -> True
    if (age is not None and age >= 55 and cryo_sleep == False and
        destination == 'TRAPPIST-1e' and total_spend == 0):
        return True

    # Rule 29: Age >= 55 and CryoSleep = False -> False
    if age is not None and age >= 55 and cryo_sleep == False:
        return False

    # Rule 30: CryoSleep is missing and TotalSpend = 0 -> True
    if pd.isna(cryo_sleep) and total_spend == 0:
        return True

    # Rule 31: Cabin is missing and CryoSleep = True -> True
    if pd.isna(cabin) and cryo_sleep == True:
        return True

    # Rule 32: Default rule
    if ((destination == 'TRAPPIST-1e' or home_planet == 'Europa') and total_spend < 200):
        return True
    else:
        return False

def create_submission_file(df):
    """Create Kaggle submission file with predictions"""
    submission_data = []

    print(colored(f"🔮 Making predictions for {len(df)} passengers for submission...", "blue"))

    for idx, row in df.iterrows():
        passenger_id = row['PassengerId']
        prediction = predict_with_rules(row)
        submission_data.append({'PassengerId': passenger_id, 'Transported': prediction})

        # Progress indicator
        if (idx + 1) % 500 == 0:
            print(colored(f"   Processed {idx + 1}/{len(df)} rows", "cyan"))

    # Create submission DataFrame
    submission_df = pd.DataFrame(submission_data)

    # Save to CSV
    try:
        submission_df.to_csv(SUBMISSION_CSV_PATH, index=False)
        print(colored(f"✅ Submission file created: {SUBMISSION_CSV_PATH}", "green"))
        print(colored(f"   📊 Total predictions: {len(submission_df)}", "yellow"))
        print(colored(f"   📈 Transported=True: {submission_df['Transported'].sum()}", "yellow"))
        print(colored(f"   📉 Transported=False: {len(submission_df) - submission_df['Transported'].sum()}", "yellow"))
    except Exception as e:
        print(colored(f"❌ Failed to save submission file: {e}", "red"))
        return False

    return True

def main():
    """Create Kaggle submission using deterministic rules"""
    print(colored("🚀 Kaggle Submission Creator (Deterministic Rules)", "cyan"))

    # Load data
    df = load_data()
    if df is None:
        return

    # Ensure we have required columns
    required_cols = ['PassengerId', 'HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'Age', 'VIP',
                     'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        print(colored(f"❌ Missing required columns: {missing_cols}", "red"))
        return

    print(colored("📋 Creating submission file...", "blue"))

    # Create submission
    success = create_submission_file(df)

    if success:
        print(colored("\n🏁 SUBMISSION CREATED SUCCESSFULLY!", "green"))
        print(colored("🎯 Ready to submit to Kaggle Spaceship Titanic challenge", "yellow"))
        print(colored(f"📁 File location: {os.path.abspath(SUBMISSION_CSV_PATH)}", "cyan"))
    else:
        print(colored("❌ Failed to create submission", "red"))

if __name__ == "__main__":
    main()
