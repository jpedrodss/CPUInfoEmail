import psutil
from bytes_conversion import get_size

# Função para imprimir valores de memória RAM

def print_memory_values():
    # print(""*20, "Memory Info", ""*20)

    # Define valores da memória
    svmem = psutil.virtual_memory()

    # Imprime os valores: Total, Disponível, Em uso e Porcentagem de uso da memória
    # print(f"Total: {get_size(svmem.total)}")
    # print(f"Disponível: {get_size(svmem.available)}")
    # print(f"Em uso: {get_size(svmem.used)}")
    # print(f"Porcentagem de uso: {svmem.percent}%")

    msg_compact = f"""
{"="*20}Memory Info{"="*20}
Total: {get_size(svmem.total)}
Disponível: {get_size(svmem.available)}
Em uso: {get_size(svmem.used)}
Porcentagem de uso: {svmem.percent}%
    """

    return msg_compact

print_memory_values()
