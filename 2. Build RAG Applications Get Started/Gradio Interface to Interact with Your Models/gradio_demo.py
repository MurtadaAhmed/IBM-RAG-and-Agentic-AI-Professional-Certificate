import gradio as gr

def add_numbers(Num1, Num2):
    return Num1 + Num2

demo = gr.Interface(
    fn=add_numbers,
    inputs=[gr.Number(label="First Number"), gr.Number(label="Second Number")],
    outputs=gr.Number(label="Sum"),
    title="Local Gradio Sum Calculator"
)

if __name__ == "__main__":
    demo.launch()