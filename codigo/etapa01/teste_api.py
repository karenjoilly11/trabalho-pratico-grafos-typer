# Importa a biblioteca PyGithub para acessar a API do GitHub
from github import Github

# Importa biblioteca para gerar arquivos CSV
import csv


# Token de autenticação da API do GitHub
TOKEN = "TOKEN_DE_AUTENTICACAO_AQUI"


# Cria conexão com a API do GitHub
g = Github(TOKEN)


# Seleciona o repositório que será analisado
repo = g.get_repo("fastapi/typer")


# Obtém apenas as issues fechadas do repositório
issues = repo.get_issues(state="closed")


# Conjunto utilizado para evitar arestas paralelas
# Em grafos simples não podem existir arestas repetidas
arestas = set()


# Cria arquivo CSV para armazenar as interações
with open(
    "codigo/etapa01/interacoes.csv",
    mode="w",
    newline="",
    encoding="utf-8"
) as arquivo:

    # Objeto responsável por escrever no CSV
    writer = csv.writer(arquivo)

    # Cabeçalho do arquivo
    writer.writerow(["origem", "destino", "tipo"])

    # Limite de issues processadas
    contador = 0

    # Percorre todas as issues
    for issue in issues:

        # Ignora Pull Requests
        # Pull Requests aparecem como issues na API do GitHub
        if issue.pull_request is None:

            # Usuário que criou a issue
            autor_issue = issue.user.login

            # Obtém comentários da issue
            comentarios = issue.get_comments()

            # Percorre todos os comentários
            for comentario in comentarios:

                # Usuário que realizou o comentário
                autor_comentario = comentario.user.login

                # Evita loops
                # Um vértice não pode apontar para ele mesmo
                if autor_comentario != autor_issue:

                    # Cria representação da aresta
                    aresta = (
                        autor_comentario,
                        autor_issue,
                        "comentario"
                    )

                    # Evita arestas paralelas
                    if aresta not in arestas:

                        arestas.add(aresta)

                        # Escreve aresta no CSV
                        writer.writerow(aresta)

            contador += 1

        # Limita quantidade de issues analisadas
        # para evitar mineração excessiva
        if contador >= 20:
            break


# Mensagem final
print("CSV gerado com sucesso!")