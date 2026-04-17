import json

# Receita padrão (Baseada em 100% de farinha)
receita_base = {
    "farinha": 500,
    "agua": 375,
    "sal": 10,
    "fermento": 5
}

def calcular_porcentagens(ingredientes):
    """Calcula a porcentagem de cada ingrediente em relação à farinha."""
    farinha = ingredientes["farinha"]
    return {item: (qtd / farinha) * 100 for item, qtd in ingredientes.items()}

def escalonar_receita(farinha_desejada):
    """Calcula as quantidades baseadas na nova quantidade de farinha."""
    porcentagens = calcular_porcentagens(receita_base)
    return {item: (porcentagem / 100) * farinha_desejada for item, porcentagem in porcentagens.items()}

def salvar_receita(resultado):
    """Salva o resultado em um arquivo de texto."""
    with open("receita_final.txt", "w", encoding="utf-8") as f:
        f.write("--- RECEITA ESCALONADA ---\n")
        for item, qtd in resultado.items():
            f.write(f"{item.capitalize()}: {qtd:.2f}g\n")
    print("\n[OK] Receita salva em 'receita_final.txt'!")

if __name__ == "__main__":
    print("=== CALCULADORA DE PANIFICAÇÃO PROFISSIONAL ===")
    try:
        peso_farinha = float(input("Digite a quantidade de farinha (g): "))
        nova_receita = escalonar_receita(peso_farinha)
        
        print("\nIngredientes Calculados:")
        for item, qtd in nova_receita.items():
            print(f"- {item.upper()}: {qtd:.2f}g")
            
        salvar_receita(nova_receita)
    except ValueError:
        print("Erro: Por favor, insira um número válido.")