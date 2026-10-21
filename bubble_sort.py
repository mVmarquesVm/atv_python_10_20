def bubble_sort(lista):
    """
    Ordena uma lista usando o Bubble Sort.
    """

    # Guarda a quantidade de elementos da lista.
    n = len(lista)

    # i representa a PASSADA que estamos realizando.
    # Na primeira passada, i = 0.
    # Na segunda passada, i = 1.
    #
    # A cada passada, um elemento maior consegue "borbulhar" para o final da parte ainda não ordenada.
    for i in range(n - 1):

        print(f"\n--- PASSADA {i + 1} ---")

        # j representa a posição do elemento que estamos analisando naquele momento.
        #
        # lista[j]     -> elemento atual
        # lista[j + 1] -> elemento vizinho
        for j in range(n - 1 - i):

            print(
                f"j = {j}: comparando {lista[j]} e {lista[j + 1]}")

            # Se o elemento atual for maior que o próximo,
            # significa que eles estão na ordem errada.
            if lista[j] > lista[j + 1]:

                print("  -> Estão fora de ordem. Trocando!")

                # Troca os dois elementos.
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                print(f"  -> Lista agora: {lista}")

            else:
                print("  -> Já estão na ordem correta.")

        print(f"Resultado da passada {i + 1}: {lista}")

    return lista


numeros = [70,90,3,0,100,2]

print("LISTA ORIGINAL:")
print(numeros)

resultado = bubble_sort(numeros)

print("\nLISTA ORDENADA:")
print(resultado)