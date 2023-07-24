import psutil
import time


def exibir_info_cpu_memoria():
    try:
        while True:
            uso_cpu = psutil.cpu_percent(interval=1)
            uso_memoria = psutil.virtual_memory().percent

            print(f"Uso da CPU: {uso_cpu:.1f}% | Uso da Memória: {uso_memoria:.1f}%")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Encerrando o monitoramento...")


if __name__ == "__main__":
    exibir_info_cpu_memoria()
