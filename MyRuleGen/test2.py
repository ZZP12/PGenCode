# read txt

with open('ECBLAST_smiles_AAM.txt', 'r') as f:
    x = f.readlines()

rxnaam = ''
for id, content in enumerate(x):
    if 'AAM' in content:
        rxnaam = x[id+1]
        break
# verification
if '>>' not in rxnaam:
    print('error')
else:
    print(rxnaam.split()[0])
