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

        # Preferences > Settings - Distraction Free
        DF_PREF = sublime.load_settings('Distraction Free.sublime-settings')
        # Preferences > Settings
        PREF = sublime.load_settings('Preferences.sublime-settings')

        # Not in distraction free mode
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
        # In distraction free mode
        else:
            for v in w.views():
                vs = v.settings()

                self.reset_setting(vs, PREF, 'draw_centered', False)
                self.reset_setting(vs, PREF, 'draw_indent_guides', True)
                self.reset_setting(vs, PREF, 'draw_white_space', 'selection')
                self.reset_setting(vs, PREF, 'fold_buttons', True)
                self.reset_setting(vs, PREF, 'gutter', True)
                self.reset_setting(vs, PREF, 'line_numbers', True)
                self.reset_setting(vs, PREF, 'rulers', [])
                self.reset_setting(vs, PREF, 'scroll_past_end', True)
                self.reset_setting(vs, PREF, 'word_wrap', 'auto')
                self.reset_setting(vs, PREF, 'wrap_width', 0)
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

    @staticmethod
    def reset_setting(view_prefs, global_prefs, setting, default):
        """Resets a viewport setting to it's state before distraction free mode."""
        # Syntax has the format 'Packages/[SYNTAX]/[SYNTAX].sublime-syntax'
        syntax = view_prefs.get('syntax').split('/')[1]

        # Preferences > Syntax Specific
        syntax_prefs = sublime.load_settings(syntax + '.sublime-settings')

        # First load the syntax settings, if they don't exist load the global setting
        view_prefs.set(setting, syntax_prefs.get(setting, global_prefs.get(setting, default)))
