""" Module for editor state """

import reflex as rx

class EditorState(rx.State):
    """ handles editor state (text content)"""
    content: str = "<p>Editor content</p>"
    test: str = "Test"
    form_data: dict = {0:''}

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content
        self.form_data[0] += content
        #print(self.content)

    @rx.cached_var
    def process_clipboard_data(self) -> str:
        """ Passes on the clipboard data as context to chat """
        _current = self.content.lower()
        return _current


# EDITOR_STATE (\n)
# End-of-file (EOF)