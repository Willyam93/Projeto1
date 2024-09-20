import sqlite3
from plyer import notification

def obter_dados_vacinacao():
    conn = sqlite3.connect('Vacinas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT vacina, data FROM vacinas WHERE status='pendente'")
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def enviar_notificacao():
    vacinas = obter_dados_vacinacao()
    
    if vacinas:
        mensagem = "Você tem as seguintes vacinas pendentes:\n"
        for vacina, data in vacinas:
            mensagem += f"- {vacina} (Data: {data})\n"
    else:
        mensagem = "Todas as vacinas estão em dia!"

    notification.notify(
        title="Vacinação",
        message=mensagem,
        timeout=10,
        app_icon="",
    )

enviar_notificacao()
