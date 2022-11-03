def solution(numbers):
    answer = []
    for number in numbers:
        binaryNumber = ['0'] + list(bin(number)[2:])
        index = "".join(binaryNumber).rfind('0')
        binaryNumber[index] = '1'

        if number % 2 == 1:
            binaryNumber[index + 1] = '0'

        answer.append(int(''.join(binaryNumber), 2))

    return answer