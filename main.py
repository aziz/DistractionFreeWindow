#!/usr/bin/env python
# coding: utf-8

import os

import sublime
import sublime_plugin


class DistractionFreeWindowListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        view.window().run_command("distraction_free_window", {"toggle": False})


class DistractionFreeWindowCommand(sublime_plugin.WindowCommand):

    def _status_msg(self, msg):
        self.window.status_message('Distraction Free Window: {}'.format(msg))

    def run(self, toggle=True):
        packages_path = sublime.packages_path()
        session_file = os.path.join(os.path.dirname(packages_path), 'Local', 'Session.sublime_session')

        session_settings = {}
        try:
            with open(session_file, "r") as file:
                session_settings = sublime.decode_value(file.read())
        except FileNotFoundError:
            self._status_msg('Warning: Session file not found!')
        except IOError:
            self._status_msg('Warning: Could not read session file!')

        w = self.window
        if w is None:
            self._status_msg('Error: Window is None')
            return

        if w.active_view().settings().get('is_widget', False):
            self._status_msg('Error: Active view is a widget.')
            return

        # Preferences > Settings - Distraction Free
        DF_PREF = sublime.load_settings('Distraction Free.sublime-settings')
        # Preferences > Settings
        PREF = sublime.load_settings('Preferences.sublime-settings')

        if toggle:
            session_settings["distraction_free_window_active"] = not session_settings.get("distraction_free_window_active", True)

        if session_settings["distraction_free_window_active"]:
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

        if toggle:
            try:
                # toggle MaxPane if found
                PKGCTRL_PREF = sublime.load_settings('Package Control.sublime-settings')
                is_maxpane_installed = bool('MaxPane' in set(PKGCTRL_PREF.get('installed_packages', [])))
                if is_maxpane_installed:
                    self.window.run_command('max_pane')
            except Exception as e:
                pass

            try:
                with open(session_file, mode='w', newline='\n') as file:
                    file.write(sublime.encode_value(session_settings, pretty=True))
            except FileNotFoundError:
                self._status_msg('Error: Session file not found! Mode was not saved!')
            except IOError:
                self._status_msg('Error: Could not write to session file! Mode was not saved!')
