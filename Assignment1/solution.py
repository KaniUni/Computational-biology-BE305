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
print(repo)


def start_translation(mrna_frame_pr):
    lt = []
    for i in mrna_frame_pr:
        lt.append(repo.get(i))
    print(lt)
#### FIND A WAY TO CONVERT TO STRING



#convert dna to mrna(just change the T to U)
with open('dna.txt', 'r') as file:
    dna = file.read().replace('\n', '')
    mrna = dna.replace('T', 'U')

with open('mrna.txt', 'w') as file:
    file.write(mrna)


with open('mrna.txt', 'r') as f1, open('protein.txt' , 'w') as f2:
    mrna = f1.read()
    mrna_frames = []
    for i in range(0, len(mrna), 3):
        mrna_frames.append(mrna[i:i+3])


    for i in mrna_frames:
        if (i != 'AUG'):
            mrna_frames.remove(i)
        else:
            break
    start_translation(mrna_frames)



with open('protein.txt', 'w') as file:
    file.write()


