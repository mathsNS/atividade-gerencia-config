# NexusBank

Projeto desenvolvido para a disciplina de Gerência de Configuração da Universidade Federal do Cariri (UFCA), com foco na prática de estratégias de branching e merging utilizando Git e GitHub.

O NexusBank é um sistema bancário simples feito em Python utilizando Programação Orientada a Objetos (POO). O principal objetivo do projeto foi colocar em prática a estratégia **Trunk-Based Development (TBD)** durante o desenvolvimento em grupo.

---

# Objetivo da atividade

A proposta da atividade foi entender melhor como funciona o trabalho colaborativo utilizando Git e GitHub, principalmente em relação a:

* integração de código;
* commits e merges;
* organização do fluxo de desenvolvimento;
* resolução de conflitos;
* trabalho simultâneo entre os integrantes.

O foco da atividade não era criar um sistema complexo, mas sim experimentar a estratégia de desenvolvimento na prática.

---

# Estratégia utilizada

## Trunk-Based Development (TBD)

No Trunk-Based Development, os desenvolvedores trabalham principalmente na branch principal (`main`), realizando integrações frequentes e commits pequenos.

Durante o desenvolvimento do projeto:

* todos os integrantes trabalharam simultaneamente;
* as alterações foram integradas constantemente;
* os commits foram feitos em pequenas etapas;
* conflitos de merge foram simulados e resolvidos.

Essa estratégia é muito utilizada em ambientes com integração contínua e deploy frequente.

---

# Funcionalidades do sistema

O sistema possui funcionalidades básicas de um banco digital:

* cadastro de clientes;
* criação de contas;
* depósito;
* saque;
* exibição de saldo;
* rendimento simples da conta poupança.

---

# Estrutura do projeto

```txt
NexusBank/
│
├── cliente.py
├── conta_corrente.py
├── conta_poupanca.py
├── banco.py
├── main.py
└── README.md
```

---

# Classes do sistema

## Cliente

Responsável por armazenar as informações básicas do cliente.

## ContaCorrente

Responsável pelas operações de:

* depósito;
* saque;
* exibição de saldo.

## ContaPoupanca

Responsável pelas operações de:

* depósito;
* saque;
* rendimento simples;
* exibição de saldo.

## Banco

Responsável por armazenar e organizar os clientes e contas do sistema.

---

# Divisão das tarefas

## Antonia

* Estrutura inicial do projeto
* Classe `Cliente`
* Integração frequente na branch principal

## Abner

* Classe `ContaCorrente`
* Operações bancárias
* Commits frequentes

## Matheus

* Classe `ContaPoupanca`
* Classe `Banco`
* Integração das classes no `main.py`
* Organização do README
* Simulação e resolução de conflitos

---

# Relato da atividade

Durante o desenvolvimento do NexusBank, o grupo utilizou a estratégia Trunk-Based Development trabalhando principalmente na branch `main`.

As alterações foram realizadas em pequenas etapas, com commits frequentes e integração contínua entre os integrantes. O grupo também simulou conflitos de merge para entender melhor como ocorre a resolução de conflitos em ambientes colaborativos.

A estratégia facilitou bastante a integração do projeto, principalmente por permitir que todos acompanhassem constantemente as alterações realizadas no sistema.

Ao mesmo tempo, o grupo percebeu que trabalhar diretamente na branch principal exige mais atenção e comunicação entre os integrantes para evitar conflitos e problemas de integração.

---

# Vantagens percebidas

* Integração rápida;
* Fluxo de desenvolvimento simples;
* Facilidade de acompanhar alterações;
* Menor acúmulo de branches;
* Melhor colaboração entre os integrantes.

---

# Dificuldades encontradas

* Necessidade de sincronização frequente;
* Possibilidade de conflitos na branch principal;
* Dependência de boa comunicação entre os integrantes.

---

# Tecnologias utilizadas

* Python
* Git
* GitHub

---

# Conclusão

A atividade ajudou o grupo a entender melhor como funciona o desenvolvimento colaborativo utilizando Git e GitHub.

O Trunk-Based Development se mostrou uma estratégia simples e eficiente para equipes pequenas, principalmente em projetos com integração contínua e alterações frequentes.