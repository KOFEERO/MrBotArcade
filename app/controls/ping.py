import ping3
def veryfi_ping_machine(machines):
    list_machines = []

    for machine in machines:
        maquina = ping3.ping(machine.ip, timeout=0.29)
        if maquina is not None:
            list_machines.append(machine.ip)
    return list_machines
