# Trabalho Prático — Grafos em Python

Projeto desenvolvido para a disciplina de Grafos utilizando Python.

O trabalho realiza:

- mineração de dados do GitHub;
- construção de grafos simples;
- implementação de lista e matriz de adjacência;
- testes de conectividade;
- benchmark de desempenho;
- exportação para visualização no Gephi.

---

## Autores

- Amanda
- Karen Joilly 
- Pedro Duarte
- Tiago 

Disciplina: Grafos  
Professor: Leonardo V. Cardoso 
Instituição: PUC Minas

---

# Objetivo

O objetivo do projeto é representar interações entre usuários do GitHub através de grafos.

As interações são obtidas a partir de:

- issues;
- comentários;
- usuários participantes do repositório.

Cada usuário é representado como um vértice e cada interação é representada como uma aresta.

---

# Repositório utilizado

Os dados foram minerados do repositório:

https://github.com/fastapi/typer

---

# Tecnologias utilizadas

- Python 3
- PyGithub
- python-dotenv
- pandas
- matplotlib
- networkx
- pytest
- CSV
- Gephi

---

# Estrutura do projeto

```text
codigo/
├── etapa01/
│   ├── teste_api.py
│   └── interacoes.csv
│
├── etapa02/
│   ├── src/
│   │   ├── AbstractGraph.py
│   │   ├── AdjacencyListGraph.py
│   │   ├── AdjacencyMatrixGraph.py
│   │   └── exceptions.py
│   │
│   └── tests/
│       ├── test_list_graph.py
│       ├── test_matrix_graph.py
│       └── test_exceptions.py
│
├── etapa03/
│   ├── src/
│   │   ├── Benchmark.py
│   │   └── GraphLoader.py
│   │
│   ├── tests/
│   │   └── test_benchmark.py
│   │
│   └── output/
│       ├── benchmark_resultados.txt
│       ├── grafo_lista.csv
│       ├── grafo_matriz.csv
│       └── gephi_print.png
│
relatorio/
```

---

# Funcionalidades implementadas

## Mineração de dados GitHub

O sistema utiliza a API do GitHub para:

- acessar issues;
- acessar comentários;
- gerar interações entre usuários.

As interações são exportadas para CSV.

---

# Grafos simples

O projeto implementa grafos simples, ou seja:

- não permite loops;
- não permite arestas paralelas.

---

# Estruturas implementadas

## Lista de adjacência

Representação baseada em conjuntos de vizinhos.

### Vantagens

- menor consumo de memória;
- eficiente para grafos esparsos.

---

## Matriz de adjacência

Representação baseada em matriz booleana.

### Vantagens

- acesso rápido às arestas;
- implementação simples.

---

# Funcionalidades dos grafos

- adicionar arestas;
- remover arestas;
- verificar arestas;
- calcular grau dos vértices;
- verificar conectividade;
- exportar para Gephi.

---

# Testes realizados

Foram implementados testes para:

- lista de adjacência;
- matriz de adjacência;
- exceções;
- benchmark de desempenho.

---

# Benchmark

Foi realizado benchmark comparando:

- lista de adjacência;
- matriz de adjacência.

Os resultados são salvos em:

```text
codigo/etapa03/output/benchmark_resultados.txt
```

---

# Instalação do projeto

## 1. Clonar repositório

```bash
git clone https://github.com/karenjoilly11/trabalho-pratico-grafos-typer.git
```

---

## 2. Entrar na pasta do projeto

```bash
cd trabalho-pratico-grafos-typer
```

---

## 3. Criar ambiente virtual

```bash
python3 -m venv venv
```

---

## 4. Ativar ambiente virtual

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Windows (CMD)

```cmd
venv\Scripts\activate
```

---

## Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 5. Instalar dependências

```bash
pip install PyGithub pandas matplotlib networkx pytest
```

---

## 6. Instalar dotenv

```bash
pip install python-dotenv
```

---

# Configuração do token GitHub

Criar arquivo `.env` na raiz do projeto:

```env
GITHUB_TOKEN=SEU_TOKEN_AQUI
```

---

# Como executar

## Executar mineração GitHub

```bash
python3 codigo/etapa01/teste_api.py
```

Esse comando gera:

```text
codigo/etapa01/interacoes.csv
```

---

# Executar testes

## Lista de adjacência

```bash
PYTHONPATH=. python3 codigo/etapa02/tests/test_list_graph.py
```

---

## Matriz de adjacência

```bash
PYTHONPATH=. python3 codigo/etapa02/tests/test_matrix_graph.py
```

---

## Exceções

```bash
PYTHONPATH=. python3 codigo/etapa02/tests/test_exceptions.py
```

---

## Benchmark

```bash
PYTHONPATH=. python3 codigo/etapa03/tests/test_benchmark.py
```

---

# Visualização no Gephi

Os grafos exportados podem ser visualizados no Gephi através dos arquivos:

- `grafo_lista.csv`
- `grafo_matriz.csv`

---


# Conclusão

O projeto permitiu aplicar conceitos fundamentais de teoria dos grafos utilizando dados reais do GitHub.

Também foi possível comparar diferentes representações de grafos e analisar desempenho, conectividade e visualização de redes.
