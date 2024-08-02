def create_repo(filename):
    file1 = filename
    with open(file1, 'r') as file:
        # read lines from the file
        lines = file.readlines()
    res = {}
    for line in lines:
       columns = line.strip().split()
       key = columns[0]
       value = columns[3]
       res[key] = value
    return res
repo = create_repo('codons.txt')


def start_translation(mrna_frame_pr):
    lt = []
    for i in mrna_frame_pr:
        lt.append(repo.get(i))
    lt = map(str, lt)
    var = ""
    st = var.join(lt)
    return st


#convert dna to mrna(just change the T to U)
with open('dna.txt', 'r') as f3, open('mrna.txt', 'w') as f4:
    dna = f3.read().replace('\n', '')
    mrna = dna.replace('T', 'U')
    print("mrna sequence is: "+ mrna)
    f4.write(mrna)


with open('mrna.txt', 'r') as f1, open('protein.txt' , 'w') as f2:
    mrna = f1.read()
    mrna_frames = []


    # Find the start codon
    start_index = mrna.find('AUG')
    if start_index == -1:
        print("mRNA sequence cannot be translated as it misses the start codon")
        exit()

    # Find the first occurrence of any stop codon after the start codon
    stop_codons = ['UAA', 'UAG', 'UGA']
    stop_index = len(mrna)  # Initialize with a large value (beyond the length of the mRNA)
    for codon in stop_codons:
        temp_index = mrna.find(codon, start_index)
        if temp_index != -1 and temp_index < stop_index:
            stop_index = temp_index

    # Check if a stop codon was found
    if stop_index == len(mrna):
        print("mRNA sequence cannot be translated as it misses a stop codon")
        exit()

    # Extract the mRNA sequence from the start codon to the stop codon
    mrna = mrna[start_index:stop_index ]  # gives the final string of mrna from start to stop codon that can be translated

    for i in range(0, len(mrna), 3):
        mrna_frames.append(mrna[i:i+3])

    print("amino acid sequence is: "+ start_translation(mrna_frames))
    f2.write(start_translation(mrna_frames))