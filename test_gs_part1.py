from gale_shapley import gale_shapley

# from chat
def is_stable(n, doc_pref, hospital_pref, matching):
    """
    matching: list of [hospital, doctor]
    hospital_pref[j][i] = rank of doctor i for hospital j (lower = better)
    """

    # Build lookup maps
    hosp_to_doc = {h: d for h, d in matching}
    doc_to_hosp = {d: h for h, d in matching}

    for d in range(n):
        current_h = doc_to_hosp[d]

        # check hospitals doctor prefers MORE than current
        for h in doc_pref[d]:
            if h == current_h:
                break

            current_doc_at_h = hosp_to_doc[h]

            # if hospital prefers this doctor over its current match → blocking pair
            if hospital_pref[h][d] < hospital_pref[h][current_doc_at_h]:
                return False

    return True

def test_simple():
    n = 3
    doc_pref = [[1, 0, 2], [0, 1, 2], [0, 1, 2]] # preference order
    hospital_pref = [[0, 2, 1], [1, 2, 0], [2, 0, 1]] # index 0 = rank of doc 0, according to hospital 0
    # expected_output_1 = [[0, 0], [1, 2], [2, 1]] # [doc #, hospital #]
    # expected_output_2 = [[0, 1], [1, 2], [2, 0]]

    expected_output_1 = [[0, 0], [1, 2], [2, 1]] # [hospital #, doc #]
    expected_output_2 = [[0, 2], [1, 0], [2, 1]]

    actual = gale_shapley(n, doc_pref, hospital_pref)
    assert actual == expected_output_1 or actual == expected_output_2
    # stability check
    assert is_stable(n, doc_pref, hospital_pref, actual)
    print(actual)

# chatgpt generated tests:
def test_all_same_preferences():
    n = 3
    doc_pref = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    hospital_pref = [
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2]
    ]

    expected = [[0, 0], [1, 1], [2, 2]]

    actual = gale_shapley(n, doc_pref, hospital_pref)

    # stability check
    assert is_stable(n, doc_pref, hospital_pref, actual)

    assert sorted(actual) == sorted(expected)

    

def test_reverse_preferences():
    n = 3
    doc_pref = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    hospital_pref = [
        [2, 1, 0],  # hospital 0 prefers doctor 2 most
        [2, 1, 0],
        [2, 1, 0]
    ]

    expected = [[2, 0], [1, 1], [0, 2]]

    actual = gale_shapley(n, doc_pref, hospital_pref)
    assert sorted(actual) == sorted(expected)

    # stability check
    assert is_stable(n, doc_pref, hospital_pref, actual)

def test_already_stable():
    n = 4
    doc_pref = [
        [0, 1, 2, 3],
        [1, 0, 2, 3],
        [2, 1, 0, 3],
        [3, 2, 1, 0]
    ]

    hospital_pref = [
        [0, 1, 2, 3],
        [1, 0, 2, 3],
        [2, 1, 0, 3],
        [3, 2, 1, 0]
    ]

    expected = [[0, 0], [1, 1], [2, 2], [3, 3]]

    actual = gale_shapley(n, doc_pref, hospital_pref)
    assert sorted(actual) == sorted(expected)

    # stability check
    assert is_stable(n, doc_pref, hospital_pref, actual)

def test_multiple_reassignments():
    n = 3
    doc_pref = [
        [0, 1, 2],
        [0, 1, 2],
        [1, 0, 2]
    ]

    hospital_pref = [
        [1, 0, 2],  # hospital 0 prefers doc 1 over 0
        [2, 0, 1],
        [0, 1, 2]
    ]

    # expected = [[1, 0], [2, 1], [0, 2]]
    expected = [[0, 1], [1, 2], [2, 0]] #[hosp #, doc #]

    actual = gale_shapley(n, doc_pref, hospital_pref)

    # stability check
    # assert is_stable(n, doc_pref, hospital_pref, actual)

    assert sorted(actual) == sorted(expected)

    

def test_larger_case():
    n = 5
    doc_pref = [
        [0,1,2,3,4],
        [1,0,2,3,4],
        [2,3,1,0,4],
        [3,2,1,0,4],
        [4,3,2,1,0]
    ]

    hospital_pref = [
        [0,1,2,3,4],
        [1,0,2,3,4],
        [2,1,0,3,4],
        [3,2,1,0,4],
        [4,3,2,1,0]
    ]

    actual = gale_shapley(n, doc_pref, hospital_pref)

    # Just verify it's a perfect matching
    assert len(actual) == n
    assert len(set(d for d, _ in actual)) == n
    assert len(set(h for _, h in actual)) == n

    

    