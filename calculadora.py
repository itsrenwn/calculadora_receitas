import json

CATALOGO = {
    "1": {"nome": "Pão Italiano", "agua": 320, "sal": 10, "fermento": 5},
    "2": {"nome": "Ciabatta", "agua": 410, "sal": 11, "fermento": 6},
    "3": {"nome": "Pão de Forma", "agua": 300, "sal": 9, "fermento": 7}
}

def validar_receita(ingredientes):
    """Verifica se a hidratação está muito alta (alerta de pão difícil de modelar)."""
    hidratacao = (ingredientes['agua'] / ingredientes['farinha']) * 100
    if hidratacao > 80:
        return f"⚠️ Alerta: Hidratação em {hidratacao:.1f}%. Massa será muito mole!"
    return f"✅ Hidratação em {hidratacao:.1f}%. Proporção ideal."

def calcular_producao(id_receita, farinha_usuario):
    base = CATALOGO[id_receita]
    fator = farinha_usuario / 500
    
    resultado = {
        "farinha": farinha_usuario,
        "agua": base["agua"] * fator,
        "sal": base["sal"] * fator,
        "fermento": base["fermento"] * fator
    }
    return base["nome"], resultado

if __name__ == "__main__":
    print("--- SISTEMA DE GESTÃO DE PANIFICAÇÃO ---")
    print("Escolha a base:")
    for id, dados in CATALOGO.items():
        print(f"{id}. {dados['nome']}")
    
    opcao = input("\nDigite o número da receita: ")
    
    if opcao in CATALOGO:
        try:
            qtd_farinha = float(input("Quantas gramas de farinha você vai usar? "))
            nome, receita = calcular_producao(opcao, qtd_farinha)
            
            print(f"\n--- Receita para {nome} ---")
            for ing, peso in receita.items():
                print(f"{ing.capitalize()}: {peso:.2f}g")
            
            print(f"\nSTATUS: {validar_receita(receita)}")
            
        except ValueError:
            print("Erro: Digite um peso válido.")
    else:
        print("Opção inválida.")