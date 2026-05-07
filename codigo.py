# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuário enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - Frontend e Backend

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="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")

st.write("### Chat com IA") # markdown

# session state = memoria do streamlit
if "lista_mensagens"  not in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva aqui sua mensagem")

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o-mini"
    )

    resposta_ia = resposta_modelo.choices[0].message.content

    # exibir resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)