def read_sequences(file_path):
    #Reads sequences from a text file and stores as a list
    with open(file_path, 'r') as file:
        sequences = [line.strip() for line in file]
    return sequences

def find_overlap(s1, s2):
    #Finds the maximum overlap between the suffix of s1 and the prefix of s2.
    max_overlap = 0
    overlap_string = ""

    # Check suffix of s1 with prefix of s2
    for i in range(1, min(len(s1), len(s2)) + 1):
        if s1[-i:] == s2[:i]:
            if i > max_overlap:
                max_overlap = i
                overlap_string = s1 + s2[i:]

    # Check prefix of s1 with suffix of s2
    for i in range(1, min(len(s1), len(s2)) + 1):
        if s1[:i] == s2[-i:]:
            if i > max_overlap:
                max_overlap = i
                overlap_string = s2 + s1[i:]
    return overlap_string, max_overlap


def greedy_shortest_superstring(sequences):
    #Finds the shortest superstring using a greedy algorithm.
    while len(sequences) > 1:
        max_overlap = -1
        best_string = ""
        best_i, best_j = 0, 0

        # Iterate through all pairs to find the maximum overlap
        for i in range(len(sequences)):
            for j in range(len(sequences)):
                if i != j:
                    merged_string, overlap = find_overlap(sequences[i], sequences[j])
                    if overlap > max_overlap:
                        max_overlap = overlap
                        best_string = merged_string
                        best_i, best_j = i, j

        # If no overlap is found, concatenate the first two sequences
        if max_overlap == 0:
            best_string = sequences[0] + sequences[1]
            best_i, best_j = 0, 1

        # Merge the best pair and remove the second sequence
        sequences[best_i] = best_string
        sequences.pop(best_j)

    return sequences[0] if sequences else ""
def main():
    file_path = 'stringsequence.txt'
    sequences = read_sequences(file_path)
    superstring = greedy_shortest_superstring(sequences)
    print("Shortest superstring:", superstring)

main()
# Example usage:
    # sequences = []
    # for line in f1:
    #     sequences.append(line.strip())
    # print(sequences)
    # #
    # loop to find overlap
    #  while overlap>1:
    #         #combine the two  strings and delete the precursor overlap