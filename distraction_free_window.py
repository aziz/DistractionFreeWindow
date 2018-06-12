#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin


class DistractionFreeWindowCommand(sublime_plugin.WindowCommand):

    def run(self):
        w = self.window
        if w is None:
            w.status_msg('Distraction Free Window: Error: Window is None')
            return

        if w.active_view().settings().get('is_widget', False):
            w.status_msg('Distraction Free Window: Error: Active view is a widget.')
            return

        if w.is_sidebar_visible():
            # Preferences > Settings - Distraction Free
            distraction_free = sublime.load_settings('Distraction Free.sublime-settings')
            for v in w.views():
                v.settings().set('draw_centered', distraction_free.get('draw_centered', True))
                v.settings().set('draw_indent_guides', distraction_free.get('draw_indent_guides', True))
                v.settings().set('draw_white_space', distraction_free.get('draw_white_space', 'selection'))
                v.settings().set('fold_buttons', distraction_free.get('fold_buttons', True))
                v.settings().set('gutter', distraction_free.get('gutter', False))
                v.settings().set('line_numbers', distraction_free.get('line_numbers', False))
                v.settings().set('rulers', distraction_free.get('rulers', []))
                v.settings().set('scroll_past_end', distraction_free.get('scroll_past_end', True))
                v.settings().set('word_wrap', distraction_free.get('word_wrap', True))
                v.settings().set('wrap_width', distraction_free.get('wrap_width', 80))
            if sublime.platform() is not 'osx':
                w.set_menu_visible(False)
            w.set_sidebar_visible(False)
            w.set_tabs_visible(False)
            w.set_minimap_visible(False)
            # w.set_status_bar_visible(False)
        else:
            # Preferences > Settings
            preferences = sublime.load_settings('Preferences.sublime-settings')
            for v in w.views():
                v.settings().set('draw_centered', preferences.get('draw_centered', False))
                v.settings().set('draw_indent_guides', preferences.get('draw_indent_guides', True))
                v.settings().set('draw_white_space', preferences.get('draw_white_space', 'selection'))
                v.settings().set('fold_buttons', preferences.get('fold_buttons', True))
                v.settings().set('gutter', preferences.get('gutter', True))
                v.settings().set('line_numbers', preferences.get('line_numbers', True))
                v.settings().set('rulers', preferences.get('rulers', []))
                v.settings().set('scroll_past_end', preferences.get('scroll_past_end', True))
                v.settings().set('word_wrap', preferences.get('word_wrap', 'auto'))
                v.settings().set('wrap_width', preferences.get('wrap_width', 0))
            if sublime.platform() is not 'osx':
                w.set_menu_visible(True)
            w.set_sidebar_visible(True)
            w.set_tabs_visible(True)
            w.set_minimap_visible(True)
            # w.set_status_bar_visible(True)
