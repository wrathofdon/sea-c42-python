# Name: Don Pham
# CodeFellows Python F2: SEA-C42
# Homework 14: Election prediction

import csv
import os
import time

def read_csv(path):
    """
    Reads the CSV file at path, and returns a list of rows. Each row is a
    dictionary that maps a column name to a value in that column, as a string.
    """
    output = []
    for row in csv.DictReader(open(path)):
        output.append(row)
    return output


################################################################################
# Problem 1: State edges
################################################################################

def row_to_edge(row):
    """
    Given an *ElectionDataRow* or *PollDataRow*, returns the
    Democratic *Edge* in that *State*.
    """
    return float(row["Dem"]) - float(row["Rep"])


def state_edges(election_result_rows):
    """
    Given a list of *ElectionDataRow*s, returns *StateEdge*s.
    The input list has no duplicate *States*;
    that is, each *State* is represented at most once in the input list.
    """

    d = {}
    for row in election_result_rows:
        state = row["State"]
        d[state] = row_to_edge(row)
    return d
    # TODO: Implement this function
    # pass


################################################################################
# Problem 2: Find the most recent poll row
################################################################################

def earlier_date(date1, date2):
    """
    Given two dates as strings (formatted like "Oct 06 2012"), returns True if
    date1 is before date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))

def most_recent_poll_row(poll_rows, pollster, state):
    """
    Given a list of *PollDataRow*s, returns the most recent row with the
    specified *Pollster* and *State*. If no such row exists, returns None.
    """
    recent = "Jan 01 1950"
    recent_x = None
    for x in poll_rows:
        if (x["Pollster"] == pollster and x["State"] == state and earlier_date(recent, x["Date"])):
            recent = x["Date"]
            recent_x = x
        else:
            pass
    return recent_x
    # TODO: Implement this function
    # pass


################################################################################
# Problem 3: Pollster predictions
################################################################################

def unique_column_values(rows, column_name):
    """
    Given a list of rows and the name of a column (a string),
    returns a set containing all values in that column.
    """
    s = set()
    for x in rows:
        s.update([x[column_name]])
    return s



    # TODO: Implement this function
    # pass

def pollster_predictions(poll_rows):
    """
    Given a list of *PollDataRow*s, returns *PollsterPredictions*.
    For a given pollster, uses only the most recent poll for a state.
    """
    d = poll_rows.copy()
    i = 0
    edge_index = {}
    for row in poll_rows:
        i += 1
        row.update({"ID": i})
        # The first step is to give all polls a unique ID key
        edge_index.update({i: state_edges([row])})
        # We also need  to map ID key to state edge
    predict = {}
    poll_unq = unique_column_values(poll_rows, "Pollster")
    state_unq = unique_column_values(poll_rows, "State")
    for pollster in poll_unq:
        predict.update({pollster: {}})
        for state in state_unq:
            recent = most_recent_poll_row(d, pollster, state)
            if (recent):
                index = recent["ID"]
                edge = edge_index[index]
                predict[pollster].update(edge)
    return predict

    # TODO: Implement this function
    # pass


################################################################################
# Problem 4: Pollster errors
################################################################################

def average_error(state_edges_predicted, state_edges_actual):
    """
    Given predicted *StateEdges* and actual *StateEdges*, returns
    the average error of the prediction.
    """
    states = list(state_edges_actual.keys())
    total = 0
    number = 0
    for s in states:
        diff = 0
        if (s in state_edges_predicted):
            diff = abs(state_edges_predicted[s] - state_edges_actual[s])
            number += 1
        total += diff
    return total / number

    # TODO: Implement this function
    # pass


def pollster_errors(pollster_predictions, state_edges_actual):
    """
    Given *PollsterPredictions* and actual *StateEdges*,
    retuns *PollsterErrors*.
    """
    pollsters = list(pollster_predictions.keys())
    d = {}
    for poll in pollsters:
        result = average_error(pollster_predictions[poll], state_edges_actual)
        d.update({poll: result})
    return d
    # TODO: Implement this function
    # pass


################################################################################
# Problem 5: Pivot a nested dictionary
################################################################################

def pivot_nested_dict(nested_dict):
    """
    Pivots a nested dictionary, producing a different nested dictionary
    containing the same values.
    The input is a dictionary d1 that maps from keys k1 to dictionaries d2,
    where d2 maps from keys k2 to values v.
    The output is a dictionary d3 that maps from keys k2 to dictionaries d4,
    where d4 maps from keys k1 to values v.
    For example:
      input = { "a" : { "x": 1, "y": 2 },
                "b" : { "x": 3, "z": 4 } }
      output = {'y': {'a': 2},
                'x': {'a': 1, 'b': 3},
                'z': {'b': 4} }
    """
    abc = list(nested_dict.keys())
    d = {}
    for a in abc:
        xyz = list(nested_dict[a].keys())
        for x in xyz:
            d.setdefault(x, {})
            d[x].update({a: nested_dict[a][x]})
    return d

    # TODO: Implement this function
    # pass


################################################################################
# Problem 6: Average the edges in a single state
################################################################################

def average_error_to_weight(error):
    """
    Given the average error of a pollster, returns that pollster's weight.
    The error must be a positive number.
    """
    return error ** (-2)

# The default average error of a pollster who did no polling in the
# previous election.
DEFAULT_AVERAGE_ERROR = 5.0


def pollster_to_weight(pollster, pollster_errors):
    """"
    Given a *Pollster* and a *PollsterErrors*,
    return the given pollster's weight.
    """
    if pollster not in pollster_errors:
        weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
    else:
        weight = average_error_to_weight(pollster_errors[pollster])
    return weight


def weighted_average(items, weights):
    """
    Returns the weighted average of a list of items.

    Arguments:
    items is a list of numbers.
    weights is a list of numbers, whose sum is nonzero.

    Each weight in weights corresponds to the item in items at the same index.
    items and weights must be the same length.
    """
    assert len(items) > 0
    assert len(items) == len(weights)
    num = 0
    den = 0
    for i in range(len(items)):
        num += items[i] * weights[i]
        den += weights[i]
    return num / den

    # TODO: Implement this function
    # pass


def average_edge(pollster_edges, pollster_errors):
    """
    Given *PollsterEdges* and *PollsterErrors*, returns the average
    of these *Edge*s weighted by their respective *PollsterErrors*.
    """
    # TODO: Implement this function
    # pass

    pollster = list(pollster_edges.keys())
    edges = []
    weights = []
    for poll in pollster:
        weight = 0.04
        if (poll in pollster_errors):
            weight = average_error_to_weight(pollster_errors[poll])
        edges.append(pollster_edges[poll])
        weights.append(weight)
    return weighted_average(edges, weights)


def test_average_edge():
    assert(average_edge({"p1":3, "p2":4, "p3":5}, {"p1":1, "p2":1, "p3":1}) == 4)
    assert(average_edge({"p1":3, "p2":4, "p3":5}, {"p1":1, "p2":1, "p3":1, "p4":2, "p5": -8}) == 4)
    assert(average_edge({"p1":3, "p2":4}, {"p1":1, "p2":1}) == 3.5)
    assert(average_edge({"p1":2, "p2":4, "p3":4, "p4":6}, {"p1":1, "p2":1, "p3":1, "p4":5}) == 3.3684210526315788)
    assert(average_edge({"p1":1, "p2":2, "p3":3, "p4":4, "p5":5},
                        {"p1":1, "p2":2, "p3":3, "p4":4, "p5":5}) == 1.560068324160182)
    assert(average_edge({"p1":3, "p2":4, "p3":5}, {"p1":5, "p2":5}) == 4)
    assert(average_edge({"p1":3, "p2":4, "p3":5}, {}) == 4)

################################################################################
# Problem 7: Predict the 2012 election
################################################################################


def predict_state_edges(pollster_predictions, pollster_errors):
    """
    Given *PollsterPredictions* from a current election and
    *PollsterErrors* from a past election,
    returns the predicted *StateEdges* of the current election.
    """
    state_pivot = pivot_nested_dict(pollster_predictions)
    # pivots dictionary of states
    states = list(state_pivot.keys())
    d = {}
    for state in states:
        average = average_edge(state_pivot[state], pollster_errors)
        d.update({state: average})
    return d
    # each piv is l
    # TODO: Implement this function
    # pass




def test_predict_state_edges():
    pollster_predictions = {
      'PPP': { 'WA': -11.2, 'CA': -2.0, 'ID': -1.1 },
      'IPSOS': { 'WA': -8.7, 'CA': -3.1, 'ID': 4.0 },
      'SurveyUSA': { 'WA': -9.0, 'FL': 0.5 },
      }
    pollster_errors = {'PPP': 1.2, 'IPSOS': 4.0, 'SurveyUSA':3.5, 'NonExistant':100.0}
    assert(predict_state_edges(pollster_predictions, pollster_errors) == {'CA':
    -2.0908256880733944, 'FL': 0.5, 'ID': -0.6788990825688075, 'WA': -10.799509886766941})




################################################################################
# Electoral College, Main Function, etc.
################################################################################

def electoral_college_outcome(ec_rows, state_edges):
    """
    Given electoral college rows and state edges, returns the outcome of
    the Electoral College, as a map from "Dem" or "Rep" to a number of
    electoral votes won.  If a state has an edge of exactly 0.0, its votes
    are evenly divided between both parties.
    """
    ec_votes = {}               # maps from state to number of electoral votes
    for row in ec_rows:
        ec_votes[row["State"]] = float(row["Electors"])

    outcome = {"Dem": 0, "Rep": 0}
    for state in state_edges:
        votes = ec_votes[state]
        if state_edges[state] > 0:
            outcome["Dem"] += votes
        elif state_edges[state] < 0:
            outcome["Rep"] += votes
        else:
            outcome["Dem"] += votes/2.0
            outcome["Rep"] += votes/2.0
    return outcome


def test_electoral_college_outcome():
electoral_college = [
    {'State': 'AK', 'Name': 'Alaska', 'Electors': 2, 'Population': 710000},
    {'State': 'AL', 'Name': 'Alabama', 'Electors': 8, 'Population': 4780000},
    {'State': 'AR', 'Name': 'Arkansas', 'Electors': 4, 'Population': 2916000}
]
state_edges = {'AK': -4.0, 'AL': 2.0, 'AR': 1.0}
assert(electoral_college_outcome(electoral_college, state_edges) == {'Rep': 2.0, 'Dem': 12.0})

state_edges = {'AK': -4.0, 'AL': 0.0, 'AR': 1.0}
assert(electoral_college_outcome(electoral_college, state_edges) == {'Rep': 6.0, 'Dem': 8.0})



def print_dict(dictionary):
    """
    Given a dictionary, prints its contents in sorted order by key.
    Rounds float values to 8 decimal places.
    """
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if type(value) == float:
            value = round(value, 8)
        print(key, value)


def main():
    """
    Main function, which is executed when election.py is run as a Python script.
    """
    # Read state edges from the 2008 election
    edges_2008 = state_edges(read_csv("data/2008-results.csv"))

    # Read pollster predictions from the 2008 and 2012 election
    polls_2008 = pollster_predictions(read_csv("data/2008-polls.csv"))
    polls_2012 = pollster_predictions(read_csv("data/2012-polls.csv"))

    # Compute pollster errors for the 2008 election
    error_2008 = pollster_errors(polls_2008, edges_2008)

    # Predict the 2012 state edges
    prediction_2012 = predict_state_edges(polls_2012, error_2008)

    # Obtain the 2012 Electoral College outcome
    ec_2012 = electoral_college_outcome(read_csv("data/2012-electoral-college.csv"),
                                        prediction_2012)

    print("Predicted 2012 election results:")
    print_dict(prediction_2012)
    print()

    print("Predicted 2012 Electoral College outcome:")
    print_dict(ec_2012)
    print()


# If this file, election.py, is run as a Python script (such as by typing
# "python election.py" at the command shell), then run the main() function.
if __name__ == "__main__":
    main()


###
### Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").
