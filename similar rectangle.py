def getnumof( rows, columns, B):
    default=0

    for i in range(rows):
        for j in range(i+1, rows,1):
            if(B[i][0] * B[j][1] == B[i][1] * B[j][0]):
                default += 1
    return  default

if __name__ == '__main__':
     
    # Input
    B =  [ [ 2, 4 ], [ 3, 6 ],
           [ 4, 8 ] ]
    columns = 2
    rows =  len(B)
 
    print(getnumof(rows, columns, B))
