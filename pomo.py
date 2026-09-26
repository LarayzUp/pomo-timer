import time

def contagem_regressiva(minutos, mensagem):
    print(f"\n{mensagem}")
    segundos_totais = minutos * 60

    while segundos_totais > 0:
        mins, segs = divmod(segundos_totais, 60)
        print(f"{mins:02d}:{segs:02d}", end="\r")
        time.sleep(1)
        segundos_totais -= 1

    print("00:00 - Tempo esgotado!    ")


def tocar_alerta():
    print("\a")


def pomodoro(ciclos, foco_min, pausa_curta_min, pausa_longa_min):
    for ciclo in range(1, ciclos + 1):
        print(f"\n===== Ciclo {ciclo} de {ciclos} =====")

        contagem_regressiva(foco_min, "Hora de focar! ")
        tocar_alerta()

        if ciclo % 4 == 0:
            contagem_regressiva(pausa_longa_min, "Pausa longa, relaxa! ")
        else:
            contagem_regressiva(pausa_curta_min, "Pausa curta! ")

        tocar_alerta()

    print("\nParabéns! Você concluiu todos os ciclos de hoje. ")


def main():
    print("=== Pomodoro Timer ===")
    try:
        ciclos = int(input("Quantos ciclos de foco você quer fazer? "))
        foco_min = int(input("Quantos minutos de foco por ciclo? "))
        pausa_curta_min = int(input("Quantos minutos de pausa curta? "))
        pausa_longa_min = int(input("Quantos minutos de pausa longa (a cada 4 ciclos)? "))
    except ValueError:
        print("Por favor, digite apenas números.")
        return

    pomodoro(ciclos, foco_min, pausa_curta_min, pausa_longa_min)


main()