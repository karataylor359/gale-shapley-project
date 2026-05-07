import numpy as np
import matplotlib.pyplot as plt
from gale_shapley import *

# First part of S grade
def average_proposals():
    # n_values = [100, 200, 300, 400, 500, 600]
    n_values = [i for i in range(100, 801, 100)]
    num_trials = 5
    avg_props = []
    # index is average number of proposals made for value n,
    # corresponding to the n at this index in n_values
    
    for n in n_values:
        total_proposals = 0
        for _ in range(num_trials):
            doc_pref = random_pref(n)
            hospital_pref = random_pref(n)
            _, num_proposals = gale_shapley(n, doc_pref, hospital_pref)
            total_proposals += num_proposals
        
        avg_props.append(total_proposals / num_trials)
    
    # Plot the results of the simulation
    plt.figure()
    plt.plot(n_values, avg_props, marker='o')
    plt.xlabel("n (# of doctors = # of hospitals)")
    plt.ylabel("Average # proposals")
    plt.title("Average # of Doctor Proposals vs # of Doctors/Hospitals")
    plt.show()
    plt.close()

    # Find fit
    n_vals = np.array(n_values)
    x = n_vals * np.log(n_vals)
    y = np.array(avg_props)
    c = np.sum(x * y) / np.sum(x * x)
    print("Best fit: proposals ≈", c, "* n log n")
    plt.figure()
    plt.scatter(n_vals, y, label="Data")
    plt.plot(n_vals, c * x, color='red', label=f"{c:.2f} * n log n")
    plt.legend()
    plt.show()
    plt.close()

average_proposals()