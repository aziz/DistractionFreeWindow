#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin


class DistractionFreeWindowCommand(sublime_plugin.WindowCommand):

    def _status_msg(self, msg):
        self.window.status_message('Distraction Free Window: {}'.format(msg))

    def run(self):
        w = self.window
        if w is None:
            _status_msg('Error: Window is None')
            return

        if w.active_view().settings().get('is_widget', False):
            _status_msg('Error: Active view is a widget.')
            return

        if w.is_sidebar_visible():
            # Preferences > Settings - Distraction Free
            DF_PREF = sublime.load_settings('Distraction Free.sublime-settings')
            for v in w.views():
                vs = v.settings()
                vs.set('draw_centered', DF_PREF.get('draw_centered', True))
                vs.set('draw_indent_guides', DF_PREF.get('draw_indent_guides', True))
                vs.set('draw_white_space', DF_PREF.get('draw_white_space', 'selection'))
                vs.set('fold_buttons', DF_PREF.get('fold_buttons', True))
                vs.set('gutter', DF_PREF.get('gutter', False))
                vs.set('line_numbers', DF_PREF.get('line_numbers', False))
                vs.set('rulers', DF_PREF.get('rulers', []))
                vs.set('scroll_past_end', DF_PREF.get('scroll_past_end', True))
                vs.set('word_wrap', DF_PREF.get('word_wrap', True))
                vs.set('wrap_width', DF_PREF.get('wrap_width', 80))
            if sublime.platform() is not 'osx':
                w.set_menu_visible(False)
            w.set_sidebar_visible(False)
            w.set_tabs_visible(False)
            w.set_minimap_visible(False)
            # w.set_status_bar_visible(False)
        else:
            # Preferences > Settings
            PREF = sublime.load_settings('Preferences.sublime-settings')
            for v in w.views():
                vs = v.settings()
                vs.set('draw_centered', PREF.get('draw_centered', False))
                vs.set('draw_indent_guides', PREF.get('draw_indent_guides', True))
                vs.set('draw_white_space', PREF.get('draw_white_space', 'selection'))
                vs.set('fold_buttons', PREF.get('fold_buttons', True))
                vs.set('gutter', PREF.get('gutter', True))
                vs.set('line_numbers', PREF.get('line_numbers', True))
                vs.set('rulers', PREF.get('rulers', []))
                vs.set('scroll_past_end', PREF.get('scroll_past_end', True))
                vs.set('word_wrap', PREF.get('word_wrap', 'auto'))
                vs.set('wrap_width', PREF.get('wrap_width', 0))
            if sublime.platform() is not 'osx':
                w.set_menu_visible(True)
            w.set_sidebar_visible(True)
            w.set_tabs_visible(True)
            w.set_minimap_visible(True)
            # w.set_status_bar_visible(True)

        try:
            # toggle MaxPane if found
            PKGCTRL_PREF = sublime.load_settings('Package Control.sublime-settings')
            is_maxpane_installed = bool('MaxPane' in set(PKGCTRL_PREF.get('installed_packages', [])))
            if is_maxpane_installed:
                self.window.run_command('max_pane')
        except Exception as e:
            pass
