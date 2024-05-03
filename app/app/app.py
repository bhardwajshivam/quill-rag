"""The main Chat app."""

import reflex as rx
from app.components import chat, navbar

class EditorState(rx.State):
    content: str = "<p>Editor content</p>"

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content


def index() -> rx.Component:
    """The main app."""
    return rx.container(
                rx.center(
                    "QUILL RAG",
                    border_width="thick",
                    width="100%"
                ),
                rx.flex(
                    rx.editor(
                        set_contents=EditorState.content,
                        on_change=EditorState.handle_change,
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
