import sublime, sublime_plugin, os
# cmd + alt + 7

class OpenActionViewCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    region   = self.view.sel()[0]
    all_defs = self.view.find_all(' def ')

    for d in all_defs:
      if d < region:
        line      = self.view.line(d)
        line_text = self.view.substr(line)
        view_name = line_text.split('def ')[1].strip()

    view_file_full_path = self.find_view_file_full_path(view_name)

    self.create_menu(view_file_full_path)

  def create_menu(self, view_file_full_path):
    array = ['.haml', '.html.erb', '.html.slim', '.js.erb', '.pdf.erb', '.html.haml']

    for c in array:
      if os.path.isfile(view_file_full_path + c):
        sublime.active_window().open_file(view_file_full_path + c)

  def find_view_file_full_path(self, view_name):
    file_name       = self.view.file_name()
    source_path     = os.path.dirname(file_name)
    view_folder     = file_name.split('/')[-1].split('_controller.rb')[0]
    rails_view_path = source_path.replace('controllers', 'views') + '/' + view_folder + '/'
    return rails_view_path + view_name
