from rename import RenomeadorArquivos

def solicitar_entrada_usuario():
    caminho: str = input("Digite o caminho da pasta: ").strip()
    prefixo: str = input("Digite o prefixo: ").strip()
    try:
        numero_inicial: int = int(input("Digite o número inicial: ").strip())
        return caminho, prefixo, numero_inicial
    except ValueError:
        print("❌ Número inicial inválido. Use apenas números inteiros.")
        return None

def main() -> None:
    entrada = solicitar_entrada_usuario()

    if entrada:
        caminho, prefixo, numero_inicial = entrada
        renomeador = RenomeadorArquivos(caminho, prefixo, numero_inicial)
        renomeador.executar()

if __name__ == "__main__":
    main()
