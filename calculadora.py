receita_base = {
    "farinha": 500,
    "agua": 375,
    "sal": 10,
    "fermento": 5
}

def calcular_proporcional(ingrediente_chave, nova_qtd):
    # Calcula o fator de escala baseado no ingrediente base (farinha)
    fator = nova_qtd / receita_base[ingrediente_chave]
    
    nova_receita = {item: qtd * fator for item, qtd in receita_base.items()}
    return nova_receita

if __name__ == "__main__":
    print("--- Escalonador de Receitas ---")
    farinha_usuario = float(input("Quantas gramas de farinha você tem? "))
    
    resultado = calcular_proporcional("farinha", farinha_usuario)
    
    print("\nPara essa quantidade, use:")
    for item, qtd in resultado.items():
        print(f"- {item.capitalize()}: {qtd:.2f}g")
        
    print("\n--- FIM ---")