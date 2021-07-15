import sched
import time
from send_email import send_email

# Define o agendamento
s = sched.scheduler(time.time, time.sleep)

# Agendamento do tempo de loop das tarefas

def schedule(sc):
    send_email()

    # Define intervalo de 6000 segundos para o agentamento, e qual função será agendada
    s.enter(3600, 1, schedule, (sc,))

    return True

# Define intervalo de 6000 segundos para o agendamento, e qual função será agendada
s.enter(3600, 1, schedule, (s,))
# Executa o loop agendado
s.run()
