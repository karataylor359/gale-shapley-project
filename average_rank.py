import random
from gale_shapley import *
import numpy as np
import matplotlib.pyplot as plt

### HELPERS FOR COMPUTING AVERAGE RANK
def get_doc_rank(n, doc_pref):
    """
    Function to convert the doctor's preference list to a ranking,
    where doc_pref = [[], []],
    and index i in doc_pref contains the preference list K for doctor i,
    and index 0 in K represents the first choice doctor for i, index 1 in K represents second choice etc.

    convert to 
    index i in doc_rank contains the preference list K for doctor i,
    and index 0 in K represents the ranking of hospital 0 in i's preferences
    """
    rank = []

    for doc in range(n):
        curr_pref = doc_pref[doc]
        curr_rank = [-1] * n
        for i in range(len(curr_pref)):
            rank_index = curr_pref[i]
            curr_rank[rank_index] = i
        rank.append(curr_rank)

    # print("rank: ", rank)
    return rank

# doc_pref = [[0, 2, 1], [2, 0, 1], [1, 2, 0]] # random_pref(3)
# get_doc_rank(3, doc_pref)

def compute_ranks(n, doc_pref, hospital_pref, matchings):
    doc_rank = get_doc_rank(n, doc_pref)
    hospital_rank = hospital_pref

    total_doc_rank = 0
    total_hosp_rank = 0

    for hospital, doctor in matchings:
        total_doc_rank += doc_rank[doctor][hospital]
        total_hosp_rank += hospital_rank[hospital][doctor]

    return total_doc_rank / n, total_hosp_rank / n


### SIMULATION AVERAGE RANK VS N BELOW
def average_rank():
    n_values = [50, 100, 150, 200, 250]
    trials = 5

    avg_doc = []
    avg_hosp = []

    for n in n_values:
        doc_sum = 0
        hosp_sum = 0

        for _ in range(trials):
            doc_pref = random_pref(n)
            hospital_pref = random_pref(n)

            matchings, _ = gale_shapley(n, doc_pref, hospital_pref)

            d, h = compute_ranks(n, doc_pref, hospital_pref, matchings)
            doc_sum += d
            hosp_sum += h

        avg_doc.append(doc_sum / trials)
        avg_hosp.append(hosp_sum / trials)

    plt.plot(n_values, avg_doc, label="Doctors")
    plt.plot(n_values, avg_hosp, label="Hospitals")
    plt.xlabel("N, # of doctors/hospitals")
    plt.ylabel("Average Match Rank")
    plt.legend()
    plt.title("Average Match Rank vs N # of Doctors/Hospitals")
    plt.show()

    # Check THEOREM on doctors
    x = np.log(n_values)
    y = np.array(avg_doc)
    c = np.sum(x*y) / np.sum(x*x)
    print("Doctor fit: ~", c, "* log n")

    # Check THEOREM on hospitals
    x = n_values / np.log(n_values)
    y = np.array(avg_hosp)
    c = np.sum(x*y) / np.sum(x*x)
    print("Hospital fit: ~", c, "* n/log n")



### PLOT the rank distribution of the doctor's and hopital's partners
def rank_distribution(n=300, trials=300):
    doc_ranks = []
    hosp_ranks = []

    for _ in range(trials):
        doc_pref = random_pref(n)
        hospital_pref = random_pref(n)

        matchings, _ = gale_shapley(n, doc_pref, hospital_pref)

        d_avg, h_avg = compute_ranks(n, doc_pref, hospital_pref, matchings)

        doc_ranks.append(d_avg)
        hosp_ranks.append(h_avg)

    plt.hist(doc_ranks, alpha=0.5, label="Doctors")
    plt.hist(hosp_ranks, alpha=0.5, label="Hospitals")
    plt.legend()
    plt.title("Distribution of Average Paired Match for Doctors & Hospitals")
    plt.show()


# RUN average_rank() for part 2
# average_rank()

# RUN rank_distribution() for part 3
rank_distribution()
