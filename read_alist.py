#this program will read an alist format file and return a LDPC matrix!
import numpy as np

def read_alist(filename):
    liste = []
    with open(filename, "r") as fp:
        Lines = fp.readlines()
        for line in Lines: 
            liste.append(line.strip())
    int_liste=[]
    test=[]
    for line in liste:
        int_liste.append(line.split())
    for element in int_liste:
        test.append(list(map(int,element)))
    
    num_col = test[0][0]
    num_row = test[0][1]

    ones_col = test[1][0]
    ones_row = test[1][1]

    H = np.zeros((num_row,num_col))

    row_indices = []

    for element in test:
        if len(element) == ones_row:
            row_indices.append(element)
    for i,row in enumerate(H):
        for index in row_indices[i]:
            H[i][index-1] = 1
    return H

