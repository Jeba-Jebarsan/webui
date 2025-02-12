import gradio as gr

def create_header():
    return gr.Markdown(
        """
        # 🌐 Custom Browser Agent
        ### Your AI-Powered Web Assistant
        """,
        elem_classes=["custom-header"]
    )

def create_agent_settings():
    with gr.Group(elem_classes=["settings-group"]) as group:
        agent_type = gr.Radio(
            choices=["custom", "org"],
            label="Agent Type",
            value="custom",
            info="Select the type of agent to use",
            elem_classes=["agent-type-radio"]
        )
        
        with gr.Row():
            max_steps = gr.Slider(
                minimum=1,
                maximum=200,
                value=100,
                step=1,
                label="Maximum Steps",
                info="Maximum number of steps the agent will take"
            )
            max_actions = gr.Slider(
                minimum=1,
                maximum=20,
                value=10,
                step=1,
                label="Actions per Step",
                info="Maximum actions per step"
            )
    
    return group, agent_type, max_steps, max_actions