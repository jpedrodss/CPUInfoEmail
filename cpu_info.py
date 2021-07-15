import psutil

# Função para imprimir valores de processador

def print_cpu_values():
    # print(""*20, "CPU Info", ""*20)

    # Imprime quantidade de nucleos físicos da máquina
    # print("Nucleos físicos:", psutil.cpu_count(logical=False))
    # Imprime quantidade de nucleos totais da máquina
    # print("Nucleos totais:", psutil.cpu_count(logical=True))

    # Define o valor da frequência do processador da máquina
    cpufreq = psutil.cpu_freq()

    # Imprime a frequencia máxima e atual da máquina
    # print(f"Frequência máxima: {cpufreq.max:.2f}Mhz")
    # print(f"Frequência atual: {cpufreq.current:.2f}Mhz")

    # Imprime o percentual de uso do processador
    use_process = []
    # print("Uso de processador por nucleo")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        use_process.append(f"• Nucleo {i}: {percentage}%")
        use_process.append("\n")
        # print(f"Nucleo {i}: {percentage}%")

    msg_compact = f"""
{"="*20}CPU Info{"="*20}
Núcleos físicos: {psutil.cpu_count(logical=False)}
Núcleos totais: {psutil.cpu_count(logical=True)}
Frequência máxima: {cpufreq.max:.2f}Mhz
Frequência atual: {cpufreq.current:.2f}Mhz
Uso do processador:\n{''.join(use_process)}
"""

    return msg_compact


print_cpu_values()
