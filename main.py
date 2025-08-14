import flet as ft

# Função principal para rodar o aplicativo
def main(pagina: ft.Page):
    pagina.title = "TalkToMe"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Título principal
    titulo = ft.Text('TalkToMe', size=30, weight=ft.FontWeight.BOLD)
    pagina.add(titulo)

    # Função para enviar mensagens pelo túnel
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    # Assinatura do túnel de comunicação
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    # Função para enviar mensagem
    def enviar_mensagem(evento):
        nome_do_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value.strip()
        mensagem = f"{nome_do_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ""
        pagina.update()

    # Função para abrir o popup de entrada
    def abrir_popup(evento):
        pagina.add(popup)
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # Função para entrar no chat
    def entrar_no_chat(evento):
        popup.open = False
        pagina.remove(titulo, botao_inicial)
        pagina.add(chat)
        pagina.add(linha_enviar)
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat."
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    # COMPONENTES DA INTERFACE

    # Chat (mensagens enviadas)
    chat = ft.Column(scroll=True, expand=True)

    # Campo de texto para enviar mensagem
    campo_enviar_mensagem = ft.TextField(
        label='Digite aqui a sua mensagem',
        on_submit=enviar_mensagem
    )

    # Botão para enviar mensagem
    botao_enviar = ft.ElevatedButton(
        'Enviar',
        on_click=enviar_mensagem
    )

    # Linha com campo de mensagem e botão
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    # Popup de entrada no chat
    titulo_popup = ft.Text(f'Bem-vindo ao {titulo.value}', size=20)
    caixa_nome = ft.TextField(
        label='Digite seu nome',
        on_submit=entrar_no_chat
    )
    botao_popup = ft.ElevatedButton(
        'Entrar no Chat',
        on_click=entrar_no_chat
    )
    popup = ft.AlertDialog(
        title=titulo_popup,
        content=caixa_nome,
        actions=[botao_popup]
    )

    # Botão inicial para abrir o chat
    botao_inicial = ft.ElevatedButton(
        'Iniciar chat', 
        on_click=abrir_popup
    )
    pagina.add(botao_inicial)

# Executa o aplicativo no navegador
ft.app(target=main, view=ft.WEB_BROWSER)