CATALOGO = {
    "1": {"nome": "Pão Italiano", "agua": 350, "sal": 10, "fermento": 5},
    "2": {"nome": "Ciabatta", "agua": 410, "sal": 11, "fermento": 6},
    "3": {"nome": "Pão de Forma", "agua": 300, "sal": 9, "fermento": 7}
}

def calcular_porcentagens(ingredientes):
    """Calcula a porcentagem de cada ingrediente em relação à farinha."""
    farinha = ingredientes.get("farinha", 1)
    return {item: (qtd / farinha) * 100 for item, qtd in ingredientes.items() if item != "farinha"}

def escalonar_receita(farinha_desejada, id_receita="1"):
    """Calcula as quantidades baseadas na nova quantidade de farinha."""
    base = CATALOGO.get(id_receita, CATALOGO["1"])
    fator = farinha_desejada / 500
    return {
        "farinha": farinha_desejada,
        "agua": base["agua"] * fator,
        "sal": base["sal"] * fator,
        "fermento": base["fermento"] * fator
    }

def validar_receita(ingredientes):
    """Verifica a hidratação da massa."""
    farinha = ingredientes.get("farinha", 1)
    agua = ingredientes.get("agua", 0)
    hidratacao = (agua / farinha) * 100
    if hidratacao > 80:
        return f"⚠️ Alerta: Hidratação em {hidratacao:.1f}%. Massa será muito mole!"
    return f"✅ Hidratação em {hidratacao:.1f}%. Proporção ideal."

if __name__ == "__main__":
    print("--- SISTEMA DE GESTÃO DE PANIFICAÇÃO ---")
    # ... (seu código do menu aqui se desejar rodar manualmente)