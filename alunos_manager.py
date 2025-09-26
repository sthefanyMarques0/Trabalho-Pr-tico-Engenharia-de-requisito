from typing import List, Dict


def adicionar_aluno(alunos: List[Dict], nome: str, idade: int, nota: float) -> None:
    """Adiciona um novo aluno (id simples baseado no tamanho da lista)."""
    novo_id = len(alunos) + 1
    aluno = {"id": novo_id, "nome": nome.strip(), "idade": int(idade), "nota": float(nota)}
    alunos.append(aluno)


def listar_alunos(alunos: List[Dict]) -> None:
    """Imprime a lista de alunos formatada."""
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print(f"{'ID':<4} {'Nome':<30} {'Idade':<6} {'Nota':<5}")
    print("-" * 50)
    for a in alunos:
        print(f"{a['id']:<4} {a['nome']:<30} {a['idade']:<6} {a['nota']:<5.2f}")

def calcular_media(alunos: List[Dict]) -> float:
    """Retorna a média das notas (0.0 se vazio)."""
    if not alunos:
        return 0.0
    return sum(a["nota"] for a in alunos)/len(alunos)