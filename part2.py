
# function to generate preference list as described inthe popularity model
def popularity_pref(n):
    return

# thanks chat
def weighted_permutation(items, weights):
    """
    Generate a weighted random permutation (without replacement).
    
    items: list of items (e.g., hospital indices)
    weights: corresponding popularity weights
    """
    items = items[:]
    weights = weights[:]
    result = []
    
    while items:
        total_weight = sum(weights)
        r = random.uniform(0, total_weight)
        
        cumulative = 0
        for i, w in enumerate(weights):
            cumulative += w
            if r <= cumulative:
                result.append(items.pop(i))
                weights.pop(i)
                break
                
    return result


def generate_preferences(n, a):
    """
    Generate doctor and hospital preference lists under the popularity model.
    
    n: number of doctors/hospitals
    a: sorted list of popularity values (length n)
    
    Returns:
        doctor_prefs: list of lists
        hospital_prefs: list of lists
    """
    # Assign random permutation of popularity values
    doctor_pop = random.sample(a, n)
    hospital_pop = random.sample(a, n)
    
    doctors = list(range(n))
    hospitals = list(range(n))
    
    # Generate doctor preferences
    doctor_prefs = []
    for _ in doctors:
        pref_list = weighted_permutation(hospitals, hospital_pop)
        doctor_prefs.append(pref_list)
    
    # Generate hospital preferences
    hospital_prefs = []
    for _ in hospitals:
        pref_list = weighted_permutation(doctors, doctor_pop)
        hospital_prefs.append(pref_list)
    
    return doctor_prefs, hospital_prefs