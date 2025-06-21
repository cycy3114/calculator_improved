def start_repl_input(self, input_string):
    """Helper for testing REPL with simulated input"""
    import io
    from contextlib import redirect_stdin
    with redirect_stdin(io.StringIO(input_string)):
        self.start_repl()
