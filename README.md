# Sistema de Gerenciamento de Notas com TDD

VA2 - Testes unitário e TDD

## Funcionalidades

- Criar aluno com nome
- Adicionar notas
- Validar notas inválidas (fora do intervalo 0 a 10)
- Calcular média das notas
- Verificar situação do aluno (Aprovado, Recuperacao, Reprovado)

## Regras de negócio

- Média >= 7 → Aprovado
- Média entre 5 e 6.9 → Recuperacao
- Média < 5 → Reprovado

## Tecnologias

- Python 3
- pytest
- pytest-html

## Como executar

Instalar dependências:

```bash
pip install -r requirements.txt
```

Rodar os testes:

```bash
pytest -v
```

Gerar relatório HTML:

```bash
pytest --html=report.html
```

## Metodologia

Cada funcionalidade foi desenvolvida seguindo o ciclo TDD:

1. **RED** → escreve o teste antes de implementar (teste falha)
2. **GREEN** → implementa o mínimo necessário para o teste passar
3. **REFACTOR** → melhora o código sem quebrar os testes
