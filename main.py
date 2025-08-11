# PASSO A PASSO

# Tela Início:
# Título Principal: ...
# Botão Iniciar chat

# AO CLICAR NO BOTÃO:
# Abrir popup
# Título: Bem Vindo ao ...
# Caixa de Texto: Escreva Seu Nome no Chat
# Botão ao entrar no chat
                    
# AO CLICAR NO BOTÃO:
# Fechar popup
# Sumir com o título
# Sumir com o botão iniciar chat
# Carregar chat
# Carregar campo de enviar mensagem
# Botão enviar

# AO CLICAR NO BOTÃO:
# Enviar mensagem
# Limpar o input

# ----------------------------- #

# CTRL + C no terminal para poder escrever

# Biblioteca Flet
# pip install flet <- No terminal
import flet as ft

# Função principal para rodar seu aplicativo
def main(pagina):
    # Título Principal
    titulo = ft.Text('DijaTalk')
    pagina.add(titulo)  
    
    # Para existir uma sincronização entre as mensagem enviadas
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)

        pagina.update() 

    # Túnel de Comunicação
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_do_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        # Mensagem pra ser enviada no tunel
        mensagem = f"{nome_do_usuario}: {texto_campo_mensagem}"
        # Enviar mensagem pra todos
        pagina.pubsub.send_all(mensagem)
        # limpar o input 
        campo_enviar_mensagem.value = ""

        pagina.update()

    # Chat (mensagens enviadas)
    chat = ft.Column()
    # Input para a mensagem
    campo_enviar_mensagem = ft.TextField(label='Digite aqui a sua mensagem', on_submit=enviar_mensagem)
    # Botão enviar texto
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    # Colocando um do lado do outro
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    
    # Abrir popup  
    def abrir_popup(evento):
        pagina.add(popup)
        pagina.dialog = popup
        popup.open = True

        pagina.update()

    # Entrar no chat
    def entrar_no_chat(evento):
        # Sumir com o título
        popup.open = False
        # Sumir com o botão iniciar chat
        pagina.remove(titulo, botao_inicial)  
        # Carregar chat
        pagina.add(chat)
        # Campo de enviar mensagem e Botão enviar 
        pagina.add(linha_enviar)
        # Usuario entrou no chat 
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat."
        pagina.pubsub.send_all(mensagem)

        pagina.update()
    
    # Título: Bem Vindo ao Hashzap
    titulo_popup = ft.Text('Bem Vindo ao DijaTalk')
    # Caixa de Texto: Escreva Seu Nome no Chat
    caixa_nome = ft.TextField(label='Digite seu nome', on_submit=entrar_no_chat)
    # Botão ao entrar no chat
    botao_popup = ft.ElevatedButton('Entrar no Chat', on_click=entrar_no_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])  

    # Botão Iniciar Chat
    botao_inicial = ft.ElevatedButton('Iniciar chat', on_click=abrir_popup)
    pagina.add(botao_inicial)

# Executa a função com o flet
ft.app(target=main, view=ft.WEB_BROWSER)

