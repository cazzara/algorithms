from collections import defaultdict


def resident_hospital_matcher(
    residents_preferences, hospitals_preferences, hospital_slots
):
    """
    Implementation of Resident-Hospital stable matching algorithm
    Given by Gale-Shapley https://core.ac.uk/download/pdf/42368869.pdf

    residents_preferences dict with resident name as key 
    and list of prefered hospitals (descending order) as the value

    hospitals_preferences dict with hospital name as key
    and list of prefered residents (descending order) as the value

    {r1: [h1, h2], r2: [h2, h1], r3: [h2, h1]}

    {h1: [r1, r3, r2], h2: [r3, r2, r1]}

    hospital_slots dict of hospitals to number of residents they can accept

    {h1: 2, h2: 1}

    """

    def is_oversubscribed(num_residents, resident_capcity):
        return num_residents > resident_capcity

    def is_full(num_residents, resident_capcity):
        return num_residents == resident_capcity

    def get_worst_resident(current_residents, hospital_want_residents):
        res = {
            resident: hospital_want_residents.index(resident)
            for resident in current_residents
        }
        worst_res, idx = max(res.items(), key=lambda x: x[1])
        return worst_res

    match = defaultdict(list)
    free_residents = list(residents_preferences.keys())
    while free_residents:
        print(f"free_residents: {free_residents}")
        resident = free_residents.pop()
        # pdb.set_trace()
        while residents_preferences[resident]:
            hospital = residents_preferences[resident].pop()
            print(match)
            print(f"resident: {resident} hospital: {hospital}")
            match[hospital].append(resident)
            if is_oversubscribed(len(match[hospital]), hospital_slots[hospital]):
                print(f"hospital {hospital} is oversubscribed {match[hospital]}")
                worst_resident = get_worst_resident(
                    match[hospital], hospitals_preferences[hospital]
                )
                match[hospital].remove(worst_resident)
                print(f"worst resident {worst_resident} removed {match[hospital]}")
                free_residents.append(worst_resident)
                if worst_resident != resident:
                    break
            else:
                break
    return dict(match)
