import os
from typing import List

class RenomeadorArquivos:
    def __init__(self, caminho_pasta: str, prefixo: str, numero_inicial: int) -> None:
        self.caminho_pasta = caminho_pasta
        self.prefixo       = prefixo
        self.numero_atual  = numero_inicial

    def executar(self) -> None:
        if not self._pasta_valida():
            print("❌ Caminho da pasta inválido.")
            return

        for nome_antigo in self._listar_arquivos():
            self._renomear_arquivo(nome_antigo)

    def _pasta_valida(self) -> bool:
        return os.path.isdir(self.caminho_pasta)

    def _listar_arquivos(self) -> List[str]:
        return sorted(os.listdir(self.caminho_pasta))

    def _renomear_arquivo(self, nome_antigo: str) -> None:
        caminho_antigo = os.path.join(self.caminho_pasta, nome_antigo)

        if not os.path.isfile(caminho_antigo):
            return

        extensao     = os.path.splitext(nome_antigo)[1]
        novo_nome    = f"{self.prefixo}_{self.numero_atual}{extensao}"
        caminho_novo = os.path.join(self.caminho_pasta, novo_nome)
        try:
            os.rename(caminho_antigo, caminho_novo)
            print(f"✅ {nome_antigo} → {novo_nome}")
            self.numero_atual += 1
        except OSError as erro:
            print(f"⚠️ Erro ao renomear {nome_antigo}: {erro}")
