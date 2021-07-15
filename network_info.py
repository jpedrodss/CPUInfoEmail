from bytes_conversion import get_size
import psutil

# print(""*20, "Network Info", ""*20)

# Função para imprimir valores de rede

def print_network_info():
    if_addrs = psutil.net_if_addrs()

    # Define valores da interface
    interface = []
    # Define os valores de endereço IP ou MAC
    address_address = []
    address_netmask = []
    address_broadcast = []

    for interface_name, interface_addresses in if_addrs.items():
        # print(f"Interface: {interface_name}")
        interface.append(f"Interface: {interface_name}")
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                address_address.append(address.address)
                address_netmask.append(address.netmask)
                address_broadcast.append(address.broadcast)
                # print(f"    Endereço de IP: {address.address}")
                # print(f"    Máscara de IP: {address.netmask}")
                # print(f"    IP de Transmissão: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                address_address.append(address.address)
                address_netmask.append(address.netmask)
                address_broadcast.append(address.broadcast)
                # print(f"    Endereço MAC: {address.address}")
                # print(f"    Máscara de MAC: {address.netmask}")
                # print(f"    MAC de Transmissão: {address.broadcast}")

    net_io = psutil.net_io_counters()
    # print(f"Total de Bytes enviados: {get_size(net_io.bytes_sent)}")
    # print(f"Total de Bytes recebidos: {get_size(net_io.bytes_recv)}")
    msg_compact = f"""
{"="*20}Network Info{"="*20}
{interface[0]}
Endereço de IP ou MAC: {address_address[0]}
Máscara de IP ou MAC: {address_netmask[0]}
IP ou MAC de Transmissão: {address_broadcast[0]}
Total de Bytes enviados: {get_size(net_io.bytes_sent)}
Total de Bytes recebidos: {get_size(net_io.bytes_recv)}
    """
    return msg_compact

print_network_info()
