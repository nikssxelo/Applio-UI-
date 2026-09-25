import gradio as gr


def convert_audio(audio_file, model_name):
    if audio_file is None:
        return None

    # RVC conversion engine will be connected here in the next step.
    # For now, return the uploaded audio so we can verify the interface.
    return audio_file


with gr.Blocks(title="Applio RVC") as app:
    gr.Markdown(
        """
        # 🎙️ Applio RVC
        ### Voice Conversion Interface
        """
    )

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                label="Input Audio",
                type="filepath"
            )

            model = gr.Dropdown(
                choices=["No model loaded"],
                value="No model loaded",
                label="RVC Model"
            )

            convert_button = gr.Button(
                "Convert",
                variant="primary"
            )

        with gr.Column():
            audio_output = gr.Audio(
                label="Converted Audio",
                type="filepath"
            )

    convert_button.click(
        fn=convert_audio,
        inputs=[audio_input, model],
        outputs=audio_output
    )


if __name__ == "__main__":
    app.launch(
        server_name="0.0.0.0",
        server_port=7860
      )
