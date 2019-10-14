import sublime, sublime_plugin, os
# cmd + alt + l

class OpenActionViewCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    file_name   = self.view.file_name()
    source_path = os.path.dirname(file_name)
    folder_path = os.path.dirname(source_path)

    view_folder = file_name.split('/')[-1].split('_controller.rb')[0]

    region   = self.view.sel()[0]
    all_defs = self.view.find_all(' def ')

    # FIXME a few of them could be smaller then chosen region
    for d in all_defs:
      if d < region:
        line      = self.view.line(d)
        line_text = self.view.substr(line)
        view_name = line_text.split('def ')[1].strip()

    # FIXME complicated controller names

    rails_view_path = source_path.replace('controllers', 'views') + '/' + view_folder + '/'
    view_file_full_path = rails_view_path + view_name

    array = ['.haml', '.html.erb', '.html.slim', '.js.erb']

    for c in array:
      if os.path.isfile(view_file_full_path + c):
        sublime.active_window().open_file(view_file_full_path + c)

    # self.view.show_popup_menu('items', self.done)

  # def done(self):
  #   print("finished")