def create_repo(filename):
    file1 = 'codons.txt'
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
    f4.write(mrna)


with open('mrna.txt', 'r') as f1, open('protein.txt' , 'w') as f2:
    mrna = f1.read()
    mrna_frames = []
    start_index = mrna.find('AUG')
    if (start_index==-1):
        print("dna file cannot be translated as it misses the start codon")
        exit()
    mrna = mrna[start_index:]

    for i in range(0, len(mrna), 3):
        mrna_frames.append(mrna[i:i+3])

    f2.write(start_translation(mrna_frames))