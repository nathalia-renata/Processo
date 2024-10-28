#soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
# informado um número
# ele calcule a sequência de Fibonacci 
# e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


def fibonacci(n):
    S = [0, 1]
    while True:
        Subtracao = S[-1] + S[-2]
        if Subtracao > n:
            break
        S.append(Subtracao)
    return S

def valor(num):
    if num < 0:
        return False
    S = fibonacci(num)
    return num in S

def main():
    try:
        number = int(input("Digite um número: "))
        if valor(number):
            print(f"O número {number} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {number} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Número inválido.")

if __name__ == "__main__":
    main()
