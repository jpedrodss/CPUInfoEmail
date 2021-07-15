from bytes_conversion import get_size
import psutil

# Função para imprimir uso de disco

def print_disk_usage():
    # print(""*20, "Disk Usage", ""*20)
    # print("Partições e Uso:")

    # Define as particões da máquina
    partitions = psutil.disk_partitions()

    # Define nome e estrutura da partição
    partition_name = []
    partition_structure = []

    # Define valores de espaço da partição
    partition_occupied = []
    partition_size = []
    partition_available = []
    partition_percentage = []

    # Quantidade de arquivos lidos e arquivos escritos
    partition_read = []
    partition_write = []

    # Define o nome e estrutura da partição no sistema
    for partition in partitions:
        partition_name.append(f"=== HD: {partition.device}")
        partition_structure.append(f"Estrutura: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue

        # Define valores de espaço da partição
        partition_size.append(f"Tamanho: {get_size(partition_usage.total)}")
        partition_occupied.append(f"Em uso: {get_size(partition_usage.used)}")
        partition_available.append(
            f"Disponível: {get_size(partition_usage.free)}")
        partition_percentage.append(
            f"Porcentagem de Uso: {partition_usage.percent}%")

        # Define o total de arquivos lidos e escritos na máquina via partição
        disk_io = psutil.disk_io_counters()
        partition_read.append(f"Total lido: {get_size(disk_io.read_bytes)}")
        partition_write.append(
            f"Total escrito: {get_size(disk_io.write_bytes)}")

    msg_compact = f"""
{"="*20}Disk Usage{"="*20}
Partições e Uso:
{''.join(partition_name)}
{''.join(partition_structure)}
{''.join(partition_size)}
{''.join(partition_occupied)}
{''.join(partition_available)}
{''.join(partition_percentage)}
{''.join(partition_read)}
{''.join(partition_write)}
    """

    return msg_compact

print_disk_usage()
