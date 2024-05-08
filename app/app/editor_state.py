""" Module for editor state """

import reflex as rx

class EditorState(rx.State):
    """ handles editor state (text content)"""
    content: str = "<p>Editor content</p>"
    copied_data: str = ""

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content

    def process_clipboard_data(self):
        """ Passes on the clipboard data as context to chat """
        return str(self.content)

    def on_copy(self, clipboard_data):
        """Handles the copied content."""
        clipboard_data = self.content
        print(clipboard_data)

# EDITOR_STATE (\n)
# End-of-file (EOF)