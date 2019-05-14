def det2x2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

matrix = [
    [ 6, 3, 2 ],
    [ 1, -2, 9 ],
    [ 3, 4, 5 ]
]

print("Mátrix:")
for array in matrix:
    print(array)

a,b,c = matrix[0]

efhi = [x[1:] for x in matrix[1:]]

dfgi = [x[::2] for x in matrix[1:]]

degh = [x[0:2] for x in matrix[1:]]

det = (
    a * det2x2(efhi)
    - b * det2x2(dfgi)
    + c * det2x2(degh)
)

print(f"A mátrix determinánsa: {det}")
