from pick import pick


class CLI:
    def __init__(self, title, options):
        self.title = title
        self.options = options
        self.selected_option, self.selected_index = pick(options, title, indicator="->", default_index=0)