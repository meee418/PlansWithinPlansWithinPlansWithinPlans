p_layers = [
[(0,62),(141,160)],	
[(62,91),(160,176)],
[(91,119),(176,190)],
[(119,141),(190,201)],
[(0,1)]
]

l_layers = [
[(202,274)],
[(275,307)],
[(308,338)],
[(339,353)],
[(0,1)] 
]

a_layers = [
[(354,431),(533,555)],
[(432,466),(556,575)],
[(467,500),(576,591)],
[(501,532),(592,601)],
[(0,1)]
]

n_layers = [
[(602,669)],
[(670,733)],
[(734,795)],
[(796,864)],
[(0,1)]
]

s_layers = [
[(865,910)],
[(911,954)],
[(955,995)],
[(996,1051)],
[(0,1)]
]
    
b_layers = [[(1119,1130)]]
for x in range (0,55):
  b_layers.append([(1118-x,1119-x), (1130+x,1131+x)])
b_layers.append([(1052,1063)])
