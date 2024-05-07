"""The main application"""

import reflex as rx
from app.components import chat, navbar

class EditorState(rx.State):
    """ handles editor state (text content)"""
    content: str = "<p>Editor content</p>"
    copied_data: str = ""

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content

    def on_copy(self, clipboard_data):
        """Handles the copied content."""
        self.copied_data = clipboard_data
        print(self.copied_data)


def index() -> rx.Component:
    """The main app."""
    return rx.container(
                rx.flex(
                    rx.editor(
                        set_contents=EditorState.content,
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
                        on_change=EditorState.handle_change,
                        on_copy=EditorState.on_copy,
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
        appearance="light",
        accent_color="violet",
    ),
)
app.add_page(index)
