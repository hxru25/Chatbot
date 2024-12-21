import openai
import gradio

openai.api_key = "uropenapikey"

messages = [{"role": "system", "content": "You are a expert. Feel free to ask me anything!"}]


def CustomChatGPT(Input):
    messages.append({"role": "user", "content": Input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = CustomChatGPT(inp)
    history.append((input, output))
    return history, history


block = gradio.Blocks()
with block:
    gradio.Markdown("""<h1><center>My AI</center></h1>""")
    chatbot = gradio.Chatbot()
    message = gradio.Textbox(placeholder="How can I help you?")
    state = gradio.State()
    submit = gradio.Button("Send")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])
    

block.launch(share=True)
