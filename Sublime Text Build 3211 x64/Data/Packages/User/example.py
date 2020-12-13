import sublime
import sublime_plugin
import os
import python

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# sublime.error_message("str_file_path")
		# self.view.insert(edit, 0, self.view.file_name())
		for region in self.view.sel():
			self.view.insert(edit, region.begin(), self.view.substr(region))

		# for w in sublime.windows():
		# 	self.view.insert(edit, 0, w.project_file_name() + "  |")

		# self.view.insert(edit, 0, sublime.window.project_file_name())

			# str_file_path =
			# if os.path.splitext(str_file_path)[1] == ".py":
			# 	# sublime.error_message(str_file_path)
			# 	self.view.run_command("trim_trailing_white_space")
			# 	# self.view.window():run_command("save")

			# 	for w in sublime.windows():
			# 		self.view.insert(edit, 0, w.project_file_name() + "  |")



			# sublime.error_message(str_file_path)
        # trailing_white_space = self.view.find("[\t ]+$", 0)
        # trailing_white_space.reverse()
        # for r in trailing_white_space:
        #     # self.view.erase(edit, r)
        #     self.view.replace(edit, r, "abc")

class ShowDefinitions(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
    	# sublime.error_message("hello world")
    	'''
        if not view.settings().get('show_definitions'):
            return

        if hover_zone != sublime.HOVER_TEXT:
            return

        def score(scopes):
            return view.score_selector(point, scopes)

        # Limit where we show the hover popup
        if score('text.html') and not score('text.html source'):
            is_class = score('meta.attribute-with-value.class')
            is_id = score('meta.attribute-with-value.id')
            if not is_class and not is_id:
                return
        else:
            if not score('source'):
                return
            if score('comment'):
                return
            # Only show definitions in a string if there is interpolated source
            if score('string') and not score('string source'):
                return

        symbol, locations = symbol_at_point(view, point)
        locations = filter_current_symbol(view, point, symbol, locations)
        ref_locations = lookup_references(view.window(), symbol)
        ref_locations = filter_current_symbol(view, point, symbol, ref_locations)
        if not locations and not ref_locations:
            return

        links = []
        for l in locations:
            links.append('<a href="%s">%s</a>' % (
                location_href(l), format_location(l)))
        links = '<br>'.join(links)
        plural = 's' if len(locations) > 1 else ''

        ref_links = []
        for l in ref_locations:
            ref_links.append('<a href="%s">%s</a>' % (
                location_href(l), format_location(l)))
        ref_plural = 's' if len(ref_links) != 1 else ''
        ref_links = '<br>'.join(ref_links)

        def on_navigate(href):
            view.window().open_file(
                href,
                sublime.ENCODED_POSITION | sublime.FORCE_GROUP)

        if len(locations) > 0:
            def_section = """
                <h1>Definition%s:</h1>
                <p>%s</p>
            """ % (plural, links)
        else:
            def_section = ""

        if len(ref_locations) > 0:
            ref_section = """
                <h1>Reference%s:</h1>
                <p>%s</p>
            """ % (ref_plural, ref_links)
            if len(def_section) != 0:
                ref_section = "<br>" + ref_section
        else:
            ref_section = ""

        body = """
            <body id=show-definitions>
                <style>
                    body {
                        font-family: system;
                    }
                    h1 {
                        font-size: 1.1rem;
                        font-weight: bold;
                        margin: 0 0 0.25em 0;
                    }
                    p {
                        font-size: 1.05rem;
                        margin: 0;
                    }
                </style>
                %s
                %s
            </body>
        """ % (def_section, ref_section)

        view.show_popup(
            body,
            flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY,
            location=point,
            on_navigate=on_navigate,
            max_width=1024)
'''
