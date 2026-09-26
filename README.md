# Pomodoro Timer

Um cronômetro de produtividade feito em Python puro, direto no terminal — sem enrolação, sem dependências externas.

## O que é

A Técnica Pomodoro divide o trabalho em ciclos de foco intenso seguidos de pausas curtas (e uma pausa mais longa a cada 4 ciclos). Esse projeto automatiza essa contagem: você define quanto tempo quer focar e descansar, e o programa cuida do resto — incluindo um beep quando o tempo acaba.

Foi meu primeiro projeto explorando Python além do básico (contas, estruturas simples), como forma de praticar funções, loops e lógica de controle de fluxo na prática.

## Como funciona

- Você escolhe: número de ciclos, minutos de foco, minutos de pausa curta e minutos de pausa longa
- O programa mostra uma contagem regressiva em tempo real no terminal
- A cada 4 ciclos completados, entra automaticamente uma pausa longa
- Um alerta sonoro avisa quando cada etapa termina

## Como rodar

Pré-requisito: ter Python instalado ([python.org](https://python.org)).

```bash
git clone https://github.com/LarayzUp/pomodoro-timer-python.git
cd pomodoro-timer-python
python pomo.py
```

Depois é só responder as perguntas no terminal e focar. 🎯

## O que aprendi construindo isso

- Manipulação de tempo com o módulo `time`
- Formatação de strings (f-strings) para exibir o relógio corretamente
- Uso do operador `%` para controlar quando entra a pausa longa
- Tratamento de erros com `try/except` para evitar que o programa quebre com entradas inválidas
- Organização de código em funções separadas por responsabilidade

---

Feito por Lara Emylli — estudante de Ciência da Computação.
