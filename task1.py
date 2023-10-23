# Задача 1
# Дан набор из p матриц зармерностью (n, n) и p векторов размерностью (n, 1). Найти сумму произведений мматриц на векторы
 
def sum_prod(matrixList, vectorList):
    newMatrixList = []

    for index in range(len(matrixList)):
        newMatrix = []

        for i in range(len(matrixList[index])):
            row = []
            for j in range(len(matrixList[index][i])):
                row.append(matrixList[index][i][j] * vectorList[index][j])
            
            newMatrix.append(row)

        newMatrixList.append(newMatrix)

    matrix = newMatrixList[0] 

    for index in range(1, len(newMatrixList)):
        for i in range(len(newMatrixList[index])):
            for j in range(len(newMatrixList[index][i])):
                matrix[i][j] += newMatrixList[index][i][j] 

    return matrix

inputFile = open("input.txt", "r")

testCount = int(inputFile.readline())

inputFile.readline()
 
for i in range(testCount):
    print ("Тест {}:".format(i + 1))

    n = int(inputFile.readline())
    p = int(inputFile.readline())

    matrixList = []
    vectorList = []

    for i in range(p):
        matrix = []

        for j in range(n):
            row = list(map(float, inputFile.readline().split(" ")))

            matrix.append(row)
        
        matrixList.append(matrix)
        
    for i in range(p):
        vectorList.append(list(map(float, inputFile.readline().split(" "))))

    print("Исходные данные:")
    print("n = {}".format(n))
    print("p = {}".format(p))

    for i in range(p):
        print("Матрица[{}]:".format(i))

        for row in matrixList[i]:
            for item in row:
                print("{}".format(item), end=" ")
            print()
        
        print()
    
    for i in range(p):
        print("Вектор[{}]: {}".format(i, vectorList[i]))

    print("\nСумма произведений матриц на векторы:")
    for row in sum_prod(matrixList, vectorList):
        for item in row:
            print("{}".format(item), end=" ")
        print()

    print("--------------------------------------------------")

    inputFile.readline()

inputFile.close()