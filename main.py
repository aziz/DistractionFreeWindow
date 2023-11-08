#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin


PKG_NAME = __package__.split('.')[0]


class DistractionFreeWindowCommand(sublime_plugin.WindowCommand):

    def __status_msg(self, msg):
        print('{}: {}'.format(PKG_NAME, msg))
        self.window.status_message('{}: {}'.format(PKG_NAME, msg))

    @staticmethod
    def __reset_v_pref(V_PREF, PREF, SYNTAX_PREF, setting, default):
        if SYNTAX_PREF is not None:
            V_PREF.set(setting, SYNTAX_PREF.get(setting, PREF.get(setting, default)))
        else:
            V_PREF.set(setting, PREF.get(setting, default))

    @staticmethod
    def __set_v_pref(V_PREF, DF_PREF, setting, default):
        V_PREF.set(setting, DF_PREF.get(setting, default))

    def run(self):
        if self.window is None:
            self.__status_msg('Error: Window is None.')
            return

        active_v = self.window.active_view()
        if active_v is None:
            self.__status_msg('Error: Active view is None.')
            return

        if active_v.settings().get('is_widget', False):
            self.__status_msg('Error: Active view is a widget.')
            return

        # Preferences > Settings
        PREF = sublime.load_settings('Preferences.sublime-settings')

        # Preferences > Settings - Distraction Free
        DF_PREF = sublime.load_settings('Distraction Free.sublime-settings')

        if self.window.is_sidebar_visible():
            for v in self.window.views():
                V_PREF = v.settings()
                self.__set_v_pref(V_PREF, DF_PREF, 'draw_centered', True)
                self.__set_v_pref(V_PREF, DF_PREF, 'draw_centered', True)
                self.__set_v_pref(V_PREF, DF_PREF, 'draw_indent_guides', True)
                self.__set_v_pref(V_PREF, DF_PREF, 'draw_white_space', 'selection')
                self.__set_v_pref(V_PREF, DF_PREF, 'fold_buttons', True)
                self.__set_v_pref(V_PREF, DF_PREF, 'gutter', False)
                self.__set_v_pref(V_PREF, DF_PREF, 'line_numbers', False)
                self.__set_v_pref(V_PREF, DF_PREF, 'rulers', [])
                self.__set_v_pref(V_PREF, DF_PREF, 'scroll_past_end', True)
                self.__set_v_pref(V_PREF, DF_PREF, 'word_wrap', True)
                self.__set_v_pref(V_PREF, DF_PREF, 'wrap_width', 80)
            if PREF.get('distraction_free_window.toggle_menu', True):
                if sublime.platform() in ['linux', 'windows']:
                    self.window.set_menu_visible(False)
            self.window.set_sidebar_visible(False)
            if PREF.get('distraction_free_window.toggle_tabs', True):
                self.window.set_tabs_visible(False)
            if PREF.get('distraction_free_window.toggle_minimap', True):
                self.window.set_minimap_visible(False)
            if PREF.get('distraction_free_window.toggle_status_bar', False):
                self.window.set_status_bar_visible(False)
        else:
            for v in self.window.views():
                V_PREF = v.settings()
                current_syntax = V_PREF.get('syntax').split('/')[-1].split('.')[0]
                # Preferences > Syntax Specific
                SYNTAX_PREF = sublime.load_settings(current_syntax + '.sublime-settings') if current_syntax is not None else None
                self.__reset_v_pref(V_PREF, PREF, SYNTAX_PREF, 'draw_centered', False)
                self.__reset_v_pref(V_PREF, PREF, SYNTAX_PREF, 'draw_indent_guides', True)
                self.__reset_v_pref(V_PREF, PREF, SYNTAX_PREF, 'draw_white_space', 'selection')
                self.__reset_v_pref(V_PREF, PREF, SYNTAX_PREF, 'fold_buttons', True)
                self.__reset_v_pref(V_PREF, PREF, SYNTAX_PREF, 'gutter', True)
                self.__reset_v_pref(V_PREF, PREF, SYNTAX_PREF, 'line_numbers', True)
                self.__reset_v_pref(V_PREF, PREF, SYNTAX_PREF, 'rulers', [])
                self.__reset_v_pref(V_PREF, PREF, SYNTAX_PREF, 'scroll_past_end', True)
                self.__reset_v_pref(V_PREF, PREF, SYNTAX_PREF, 'word_wrap', 'auto')
                self.__reset_v_pref(V_PREF, PREF, SYNTAX_PREF, 'wrap_width', 0)
            if PREF.get('distraction_free_window.toggle_menu', True):
                if sublime.platform() in ['linux', 'windows']:
                    self.window.set_menu_visible(True)
            self.window.set_sidebar_visible(True)
            if PREF.get('distraction_free_window.toggle_tabs', True):
                self.window.set_tabs_visible(True)
            if PREF.get('distraction_free_window.toggle_minimap', True):
                self.window.set_minimap_visible(True)
            if PREF.get('distraction_free_window.toggle_status_bar', False):
                self.window.set_status_bar_visible(True)

        try:
            # toggle MaxPane if found
            PKGCTRL_PREF = sublime.load_settings('Package Control.sublime-settings')
            INSTALLED_PACKAGES = PKGCTRL_PREF.get('installed_packages', [])
            is_maxpane_installed = bool('MaxPane' in set(INSTALLED_PACKAGES))
            if is_maxpane_installed:
                self.window.run_command('max_pane')
        except Exception:
            pass
