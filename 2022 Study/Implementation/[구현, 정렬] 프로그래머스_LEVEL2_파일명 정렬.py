def splitFileName(fileName, order):
    result = ["", "", order, fileName]
    isNumberBegin = False
    for element in fileName:
        if element.isdigit():
            isNumberBegin = True
            result[1] += element
        else:
            if not isNumberBegin:
                result[0] += element.lower()
            else:
                break
    result[1] = int(result[1])

    return result

def solution(files):
    fileList = []
    for order, fileName in enumerate(files):
        fileList.append(splitFileName(fileName, order))

    result = []
    for element in sorted(fileList, key = lambda x: (x[0], x[1], x[2])):
        result.append(element[-1])

    return result

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))