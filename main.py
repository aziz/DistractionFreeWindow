#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin


class DistractionFreeWindowCommand(sublime_plugin.WindowCommand):

    def _status_msg(self, msg):
        self.window.status_message('Distraction Free Window: {}'.format(msg))

    @staticmethod
    def _reset_setting(view_prefs, syntax_prefs, global_prefs, setting, default):
        view_prefs.set(setting, syntax_prefs.get(setting, global_prefs.get(setting, default)))

    def run(self):
        w = self.window
        if w is None:
            _status_msg('Error: Window is None')
            return

        if w.active_view().settings().get('is_widget', False):
            _status_msg('Error: Active view is a widget.')
            return

        # Preferences > Settings - Distraction Free
        DF_PREF = sublime.load_settings('Distraction Free.sublime-settings')
        # Preferences > Settings
        PREF = sublime.load_settings('Preferences.sublime-settings')

        if w.is_sidebar_visible():
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
            if PREF.get('distraction_free_window.toggle_menu', True):
                if sublime.platform() in ['linux', 'windows']:
                    w.set_menu_visible(False)
            w.set_sidebar_visible(False)
            if PREF.get('distraction_free_window.toggle_tabs', True):
                w.set_tabs_visible(False)
            if PREF.get('distraction_free_window.toggle_minimap', True):
                w.set_minimap_visible(False)
            if PREF.get('distraction_free_window.toggle_status_bar', False):
                w.set_status_bar_visible(False)
        else:
            for v in w.views():
                vs = v.settings()

                current_syntax = vs.get('syntax').split('/')[-1].split('.')[0]

                # Preferences > Syntax Specific
                SYNTAX_PREF = sublime.load_settings(current_syntax + '.sublime-settings')

                self._reset_setting(vs, SYNTAX_PREF, PREF, 'draw_centered', False)
                self._reset_setting(vs, SYNTAX_PREF, PREF, 'draw_indent_guides', True)
                self._reset_setting(vs, SYNTAX_PREF, PREF, 'draw_white_space', 'selection')
                self._reset_setting(vs, SYNTAX_PREF, PREF, 'fold_buttons', True)
                self._reset_setting(vs, SYNTAX_PREF, PREF, 'gutter', True)
                self._reset_setting(vs, SYNTAX_PREF, PREF, 'line_numbers', True)
                self._reset_setting(vs, SYNTAX_PREF, PREF, 'rulers', [])
                self._reset_setting(vs, SYNTAX_PREF, PREF, 'scroll_past_end', True)
                self._reset_setting(vs, SYNTAX_PREF, PREF, 'word_wrap', 'auto')
                self._reset_setting(vs, SYNTAX_PREF, PREF, 'wrap_width', 0)
            if PREF.get('distraction_free_window.toggle_menu', True):
                if sublime.platform() in ['linux', 'windows']:
                    w.set_menu_visible(True)
            w.set_sidebar_visible(True)
            if PREF.get('distraction_free_window.toggle_tabs', True):
                w.set_tabs_visible(True)
            if PREF.get('distraction_free_window.toggle_minimap', True):
                w.set_minimap_visible(True)
            if PREF.get('distraction_free_window.toggle_status_bar', False):
                w.set_status_bar_visible(True)

        try:
            # toggle MaxPane if found
            PKGCTRL_PREF = sublime.load_settings('Package Control.sublime-settings')
            is_maxpane_installed = bool('MaxPane' in set(PKGCTRL_PREF.get('installed_packages', [])))
            if is_maxpane_installed:
                self.window.run_command('max_pane')
        except Exception as e:
            pass
