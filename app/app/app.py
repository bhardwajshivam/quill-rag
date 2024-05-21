"""The main application"""

import reflex as rx
from app.components import chat, navbar
from app.state import State


def index() -> rx.Component:
    """The main app."""
    return rx.container(
                rx.section(
                        rx.heading("QUILL RAG",weight='medium',size='9'),
                        rx.text("Exploring the Potential of Large Language Models in Computational Argumentation",
                                weight='light', size='2'),
                        padding_left="12px",
                        padding_right="12px",
                        background_color="#4e2ba6",
                ),
                rx.flex(
                    rx.editor(
                        set_contents=State.content,
                        set_options=rx.EditorOptions(
                            button_list=[
                                ["font", "fontSize", "formatBlock"],
                                ["fontColor", "hiliteColor"],
                                [
                                    "bold",
                                    "underline",
                                    "italic",
                                    "strike",
                                    "subscript",
                                    "superscript",
                                ],
                                ["removeFormat"],
                                "/",
                                ["outdent", "indent"],
                                ["align", "horizontalRule", "list", "table"],
                                ["link"],
                                ["fullScreen", "showBlocks", "codeView"],
                                ["preview", "print"],
                            ]
                        ),
                        on_change=State.handle_change,
                        width="50%",
                        height="100%"
                    ),
                    rx.chakra.vstack(
                        navbar(),
                        chat.chat(),
                        chat.action_bar(),
                        background_color=rx.color("mauve", 1),
                        color=rx.color("mauve", 12),
                        min_height="100vh",
                        align_items="stretch",
                        spacing="0",
                        width="50%"
                    ),
                ),
                rx.section(
                        rx.heading("QuillRAG"),
                        rx.text("Contact: shivamb.work@gmail.com"),
                        padding_left="12px",
                        padding_right="12px",
                        background_color="#4e2ba6",
                )
            )

# Add state and page to the app.
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="violet",
    ),
)
app.add_page(index)
