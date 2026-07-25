# --- CONFIGURAÇÃO INICIAL ---
# Dicionário principal (Chave: Nome do Pokémon / Valor: Dicionário com atributos)
pokedex = {
    "Pikachu": {"tipo": "Elétrico", "nivel": 5},
    "Charmander": {"tipo": "Fogo", "nivel": 5}
}

executando = True # Flag booleana para o laço

print("🔴⚪ POKÉDEX DIGITAL COM DICIONÁRIOS ⚪🔴")

# --- LAÇO PRINCIPAL (WHILE) ---
while executando:
    print("\n" + "=" * 35)
    print("      MENU POKÉDEX    ")
    print("=" * 35)
    print("1 - Ver Pokédex Completa")
    print("2 - Registrar/Atualizar Pokémon")
    print("3 - Pesquisar detalhes do Pokémon")
    print("4 - Soltar Pokémon")
    print("5 - Desligar Pokédex")

    opcao = input("\nEscolha uma opção (1-5):")

    # 1. LISTAR CHAVES E VALORES (.items())
    if opcao == "1":
        print("\n 📖 --- SEUS POKÉMONS --- ")
        if not pokedex: #Verificar se o dicionário está vazio
            print("Sua Pokedéx está vazia")
        else: 
            # Recorta a chave (nome) e o valor (atributos) usando .items()
            for nome, dados in pokedex.items():
                print (f"• {nome:<12} | Tipo: {dados ['tipo']:<10} | Nível: {dados['nivel']}")
            print (f"\nTotal de Pokémons registrados: {len(pokedex)}")

    # 2. ADICIONAR / ATUALIZAR CHAVE NO DICIONÁRIO
    elif opcao == "2":
        nome = input("\nNome do Pokémon:").strip().capitalize()
        tipo = input("Tipo(ex: Fogo, Água, Planta)").strip().capitalize
        nivel = nivel = input("Nível Iniciado:").strip()

        # Adiciona ou substitui os dados da chave 'nome'
        pokedex[nome] = {
            "tipo": tipo,
            "nivel": nivel

        }
        print(f" ✨ {nome} foi registrado com sucesso no dicionário")

    # 3. BUSCAR PELA CHAVE ("in" e acesso direto)
    elif opcao == "3":
        busca = input("\nQual Pokémon deseja pesquisa?").strip().capitalize()

    #Verifica se a chave existe no dicionário
        if busca in pokedex:
            info = pokedex[busca] #acessa o diconario interno
            print(f"\n 🔍 FICHA TÉCNICA DE {busca.upper()}:")
            print(f" ⚡Tipo: {info['tipo']}")
            print(f" 📊 Nível: {info['nivel']}")
        else:
            print (f" ❌ {busca} não foi encontrado na Pokédex")

    #4. DELETAR CHAVE DO DICIONÁRIO ('del')
    elif opcao == "4":
        soltar = input("\nQual Pokémon deseja soltar?").strip().capitalize()

        if soltar in pokedex:
            del pokedex[soltar] #Remove a chave e todos os seus valores
            print(f"🕊️ {soltar} foi libertado da sua Pokédex!")
        else:
            print(f"⚠️ {soltar} não está registrado na Pokédex.")

    #5. ENCERRAR O LAÇO
    elif opcao == "5":
            print("\n Desligando Pokédex... Até a próxima jornada!👋")
            executando = False

    else: print("\n⚠️ Opção inválida! Escolha de 1 a 5")
    



