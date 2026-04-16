import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("data/resultado-final-vestibular-2026.1.xlsx")

# Limpar e padronizar nomes de colunas
df.columns = (
    df.columns.str.lower()
              .str.strip()
              .str.replace(r'[\n\-]+', '', regex=True)
              .str.replace(' ', '_')
)

# Filtrar curso de Computação
computacao = df[df['curso/polo/instituição'].str.contains("Computação", case=False, na=False)]

# Encontrar maior nota e aluno correspondente
maior_nota = computacao['nota_final'].max()
melhor_aluno = computacao[computacao['nota_final'] == maior_nota]

print("Maior nota no curso de Computação:", maior_nota)
print("\nMelhor aluno e polo:")
print(melhor_aluno[['primeiro_nome', 'curso/polo/instituição', 'nota_final']])
