import random

# function to generate preference list independently and at random
def random_pref(n):
    all_prefs = []
    for i in range(n):
        perm = list(range(n))
        random.shuffle(perm)
        all_prefs.append(perm)

    return all_prefs


# function to run doctor proposing gale shapley
# input: n number of doctors/hospitals, list of doctor preferences, list of hospital rpeferences
# output: [final matchings] -> index i is hospital number, [hospital #, doc matching]
#         and the total number of proposals made by doctor
def gale_shapley(n, doc_pref, hospital_pref):
    num_proposals = 0
    free_docs = [i for i in range(n)]
    
    last_proposal_index = [-1] * n
    matchings = [[i, None] for i in range(n)] # index i is hospital number, [hospital #, doc matching]

    while free_docs:
        # print("\nFREE DOCS", free_docs)
        new_doc = free_docs[0]
        # print("NEW DOC: ", new_doc)
        last_proposal_index[new_doc] += 1
        hospital = doc_pref[new_doc][last_proposal_index[new_doc]]
        # print("PROPOSING TO hospital # ", hospital)
        prev_doc = matchings[hospital][1]
        num_proposals += 1
        

        # if hospital prefers new doc over prev_doc, switch to new_doc
        if (prev_doc is None) or hospital_pref[hospital][new_doc] < hospital_pref[hospital][prev_doc]:
            # print(f"SWITCH PREV DOC {prev_doc} with NEW DOC {new_doc} for hospital {hospital}")
            free_docs.remove(new_doc)
            matchings[hospital][1] = new_doc
            
            # if prev_doc is None, don't add to free_docs
            if isinstance(prev_doc, int):
                free_docs.append(prev_doc)
            
        # else:
        #     print("NO SWITCH!")
        
        
        # print("new matchings: ", matchings)

    return matchings, num_proposals
    

if __name__ == "__main__":
    # Part S
    # generate preference list for doctors and hospitals
    n = 10
    doc_pref = random_pref(n)
    hospital_pref = random_pref(n)
    matchings = gale_shapley(doc_pref, hospital_pref)
    print(matchings)
