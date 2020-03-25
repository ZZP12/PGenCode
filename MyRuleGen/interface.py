import os
from generate_retro_templates import process_an_example

def generate_rxn_rule(rxnstr, retro=False):
    os.system('java -jar rdt-2.1.0-SNAPSHOT-jar-with-dependencies.jar -Q SMI -q "{}" -j AAM -f TEXT'.format(rxnstr))
    os.system('rm ECBLAST_smiles_AAM.rxn')
    # os.system('java -jar rdt-2.1.0-SNAPSHOT-jar-with-dependencies.jar -Q SMI -q "{}" -j AAM -f XML'.format(rxnstr))
    # os.system('rm ECBLAST_smiles_AAM.rxn')
    with open('ECBLAST_smiles_AAM.txt', 'r') as f:
        x = f.readlines()
    os.system('rm ECBLAST_smiles_AAM.txt')
    rxnaam = ''
    for id, content in enumerate(x):
        if 'AAM' in content:
            rxnaam = x[id+1]
            break
    # verification
    if '>>' not in rxnaam:
        print('error')
        return
    rxnaam = rxnaam.split()[0]

    # non-retro
    if not retro:
        rxnaam = '>>'.join(rxnaam.split('>>')[-1::-1])
    rxnrule = process_an_example(rxnaam, super_general=True, v=True)

    return rxnrule



if __name__ == '__main__':
    rxnstr = 'C1(CCCC1C(=O)OCC)=O.C=CC(C)=O>>C1(CCCC1(C(=O)OCC)CCC(C)=O)=O'
    rxnrule = generate_rxn_rule(rxnstr)
    print(rxnrule)
    rxnrule = generate_rxn_rule(rxnstr, True)
    print(rxnrule)
