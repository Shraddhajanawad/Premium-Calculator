
rates_table = {
    "Bangalore": {"baseRate": 0.02},
    "Mumbai": {"baseRate": 0.025},
    "Delhi": {"baseRate": 0.018}
}

risk_table = {
    "18-25": {"riskMultiplier": 1.2},
    "26-40": {"riskMultiplier": 1.0},
    "41-60": {"riskMultiplier": 1.5}
}

# -----------------------------
# LLM-style helper functions
# -----------------------------

def extractData(userProfile, fields):
    """Extract required data from user profile"""
    return {field: userProfile[field] for field in fields}


def lookupValue(table, key, valueField):
    """Lookup value from a knowledge table"""
    return table[key][valueField]


def calculate(operation, values):
    """Perform basic calculations"""
    if operation == "multiply":
        result = 1
        for v in values:
            result *= v
        return result
    raise ValueError("Unsupported operation")


def applyFormula(base, risk, coverage):
    """Apply premium formula"""
    premium = base * risk * coverage * 0.01
    return premium


# -----------------------------
# Main LLM-driven workflow
# -----------------------------

def calculatePremium(userProfile):
    # Step 1: Extract data
    data = extractData(userProfile, ['age', 'location', 'coverage'])

    # Step 2: Determine age group
    age = data['age']
    if 18 <= age <= 25:
        age_group = "18-25"
    elif 26 <= age <= 40:
        age_group = "26-40"
    else:
        age_group = "41-60"

    # Step 3: Lookup values
    baseRate = lookupValue(rates_table, data['location'], 'baseRate')
    riskMultiplier = lookupValue(risk_table, age_group, 'riskMultiplier')

    # Step 4: Reasoning calculation
    base_risk_value = calculate('multiply', [baseRate, riskMultiplier])

    # Step 5: Apply formula
    premium = applyFormula(baseRate, riskMultiplier, data['coverage'])

    return round(premium, 2)


# -----------------------------
# Example Execution
# -----------------------------

userProfile = {
    "age": 28,
    "location": "Bangalore",
    "coverage": 500000
}

finalPremium = calculatePremium(userProfile)
print("Calculated Premium:", finalPremium)