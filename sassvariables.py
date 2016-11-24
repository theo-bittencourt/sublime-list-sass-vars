import sublime, sublime_plugin, os, re

class ListSassFontsVariables(sublime_plugin.TextCommand):
    def run(self, edit):
        self.edit = edit
        ListSassVariables().list_variables_for('fonts')

class ListSassColorsVariables(sublime_plugin.TextCommand):
    def run(self, edit):
        self.edit = edit
        ListSassVariables().list_variables_for('colors')

class ListSassVariables:
    REGEXP = "(\\$[a-zA-Z\\-_0-9]+)\\s*: *(.*)"

    def list_variables_for(self, fonts_or_colors):
        settings = sublime.load_settings('sassvariables.sublime-settings')

        filepath = os.path.join(
            sublime.active_window().folders()[0],
            settings.get("%sFilepath" % fonts_or_colors))

        if (os.path.isfile(filepath)):
            file = open(filepath, 'r')
            variables = re.findall(ListSassVariables.REGEXP, file.read())
            self.variables = [list(item) for item in variables]
            sublime.active_window().show_quick_panel(self.variables, self.insert_variable, sublime.MONOSPACE_FONT)
            file.close()
        else:
            sublime.error_message("File for %s not exists: %s" % (fonts_or_colors, filepath))

    def insert_variable(self, choice):
        if choice == -1:
            return
        sublime.active_window().active_view().run_command('insert_text', {'string': self.variables[choice][0]})

class InsertText(sublime_plugin.TextCommand):
    def run(self, edit, string=''):
        self.view.insert(edit, self.view.sel()[-1].end(), string)
