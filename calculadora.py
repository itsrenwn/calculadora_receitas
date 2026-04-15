# Receita Base de Ciabatta (Proporções em gramas)
receita_base = {
    "farinha": 500,
    "agua": 375,
    "sal": 10,
    "fermento": 5
}

def exibir_receita(ingredientes):
    print("\n--- Lista de Ingredientes ---")
    for item, qtd in ingredientes.items():
        print(f"{item.capitalize()}: {qtd}g")

if __name__ == "__main__":
    exibir_receita(receita_base)