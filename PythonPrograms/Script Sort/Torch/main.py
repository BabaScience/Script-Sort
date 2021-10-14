from cy_model import Topsort
import pprint

r'''
Path from the begining:
/anaconda3/lib/python3.8/site-packages/torch
'''
path = r'../../../../anaconda3/lib/python3.8/site-packages/torch/'
p = r'Test/'
anaconda = r'../../../../anaconda3/'
fp = 'anaconda.txt'
d = Topsort(path=path, f_name='torch.txt')
t_list = d.sort()
# pprint.pprint(d.graph)
print('------------------------------TOPSORT-----------------------------')
for directory in t_list:
    pprint.pprint(directory)
print(len(t_list))

for element in d._more:
    pprint.pprint(element)
