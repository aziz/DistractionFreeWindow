#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin


ST3 = int(sublime.version()) >= 3000
ST3098 = int(sublime.version()) >= 3098
ST3116 = int(sublime.version()) >= 3116


class DistractionFreeWindowCommand(sublime_plugin.WindowCommand):

    def run(self):
        v = self.window if ST3 else self.window.active_view()

        is_in_dfm = v.settings().get('dfw_is_in_dfm', False)
        is_in_fs = v.settings().get('dfw_is_in_fs', False)
        is_in_dfw = v.settings().get('dfw_mode', False)
        is_in_nm = not (is_in_dfw or is_in_dfm or is_in_fs)

        prestine = {}
        prestine['minimap_vis'] = minimap_vis = self.is_minimap_visible()
        prestine['status_bar_vis'] = status_bar_vis = self.is_status_bar_visible()
        prestine['tabs_vis'] = tabs_vis = self.is_tabs_visible()
        prestine['side_bar_vis'] = side_bar_vis = self.is_side_bar_visible()
        if sublime.platform() is not 'osx':
            prestine['menu_vis'] = menu_vis = self.is_menu_visible()

        prestine['gutter_vis'] = gutter_vis = v.settings().get('gutter', True)
        prestine['line_numbers_vis'] = line_numbers_vis = v.settings().get('line_numbers', True)
        prestine['fold_buttons_vis'] = fold_buttons_vis = v.settings().get('fold_buttons', True)
        prestine['draw_centered'] = v.settings().get('draw_centered', False)
        prestine['wrap_width'] = v.settings().get('wrap_width', 0)
        prestine['rulers'] = v.settings().get('rulers', [])
        prestine['draw_indent_guides'] = indent_guides_vis = v.settings().get('draw_indent_guides', True)
        prestine['draw_white_space'] = v.settings().get('draw_white_space', 'selection')

        dfw_settings = sublime.load_settings('distraction_free_window.sublime-settings')

        if is_in_nm:
            self.window_setting_set('dfw_mode_prestine', prestine)

            if dfw_settings.get('dfw_hide_minimap') and minimap_vis:
                self.window.run_command('toggle_minimap')
            if dfw_settings.get('dfw_hide_status_bar') and status_bar_vis:
                self.window.run_command('toggle_status_bar')
            if dfw_settings.get('dfw_hide_tabs') and tabs_vis:
                self.window.run_command('toggle_tabs')
            if dfw_settings.get('dfw_hide_side_bar') and side_bar_vis:
                if ST3098:
                    self.window.set_sidebar_visible(False)
                else:
                    self.window.run_command('toggle_side_bar')
            if sublime.platform() is not 'osx':
                if dfw_settings.get('dfw_hide_menu') and menu_vis:
                    if ST3098:
                        self.window.set_menu_visible(False)
                    else:
                        self.window.run_command('toggle_menu')

            if dfw_settings.get('dfw_hide_gutter') and gutter_vis:
                self.all_views_in_window_setting_set('gutter', False)
            if dfw_settings.get('dfw_hide_line_numbers') and line_numbers_vis:
                self.all_views_in_window_setting_set('line_numbers', False)
            if dfw_settings.get('dfw_hide_fold_buttons') and fold_buttons_vis:
                self.all_views_in_window_setting_set('fold_buttons', False)
            if dfw_settings.get('dfw_hide_rulers'):
                self.all_views_in_window_setting_set('rulers', [])
            if dfw_settings.get('dfw_hide_indent_guides') and indent_guides_vis:
                self.all_views_in_window_setting_set('draw_indent_guides', False)
            if dfw_settings.get('dfw_hide_white_space'):
                self.all_views_in_window_setting_set('draw_white_space', 'none')
            if dfw_settings.get('dfw_draw_centered'):
                self.all_views_in_window_setting_set('draw_centered', True)
                self.all_views_in_window_setting_set('wrap_width', dfw_settings.get('dfw_wrap_width'))

            if dfw_settings.get('dfw_switch_to_single_layout'):
                self.window.run_command('max_pane')

            self.window_setting_set('dfw_mode', True)

        elif is_in_dfw:
            prestine_state = v.settings().get('dfw_mode_prestine')

            if minimap_vis != prestine_state['minimap_vis']:
                self.window.run_command('toggle_minimap')
            if status_bar_vis != prestine_state['status_bar_vis']:
                self.window.run_command('toggle_status_bar')
            if tabs_vis != prestine_state['tabs_vis']:
                self.window.run_command('toggle_tabs')
            if side_bar_vis != prestine_state['side_bar_vis']:
                if ST3098:
                    self.window.set_sidebar_visible(prestine_state['side_bar_vis'])
                else:
                    self.window.run_command('toggle_side_bar')
            if sublime.platform() is not 'osx':
                if menu_vis != prestine_state['menu_vis']:
                    if ST3098:
                        self.window.set_menu_visible(prestine_state['menu_vis'])
                    else:
                        self.window.run_command('toggle_menu')

            if gutter_vis != dfw_settings.get('dfw_hide_gutter'):
                self.all_views_in_window_setting_erase('gutter')
            if line_numbers_vis != dfw_settings.get('dfw_hide_line_numbers'):
                self.all_views_in_window_setting_erase('line_numbers')
            if dfw_settings.get('dfw_hide_fold_buttons'):
                self.all_views_in_window_setting_erase('fold_buttons')
            if dfw_settings.get('dfw_hide_rulers'):
                self.all_views_in_window_setting_erase('rulers')
            if indent_guides_vis != dfw_settings.get('dfw_hide_indent_guides'):
                self.all_views_in_window_setting_erase('draw_indent_guides')
            if dfw_settings.get('dfw_hide_white_space'):
                self.all_views_in_window_setting_erase('draw_white_space')
            if dfw_settings.get('dfw_draw_centered'):
                self.all_views_in_window_setting_erase('draw_centered')
                self.all_views_in_window_setting_erase('wrap_width')

            if dfw_settings.get('dfw_switch_to_single_layout'):
                self.window.run_command('max_pane')

            self.window_setting_erase('dfw_mode_prestine')
            self.window_setting_set('dfw_mode', False)

    def window_setting_set(self, setting_variable, setting_value):
        if ST3:
            self.window.settings().set(setting_variable, setting_value)
        else:
            for v in self.window.views():
                v.settings().set(setting_variable, setting_value)

    def window_setting_erase(self, setting_variable):
        if ST3:
            self.window.settings().erase(setting_variable)
        else:
            for v in self.window.views():
                v.settings().erase(setting_variable)

    def all_views_in_window_setting_set(self, setting_variable, setting_value):
        for v in self.window.views():
            v.settings().set(setting_variable, setting_value)

    def all_views_in_window_setting_erase(self, setting_variable):
        for v in self.window.views():
            v.settings().erase(setting_variable)

    def is_tabs_visible(self):
        if ST3116:
            return self.window.get_tabs_visible()
        else:
            v = self.window.active_view()
            state1_h = v.viewport_extent()[1]
            self.window.run_command('toggle_tabs')
            state2_h = v.viewport_extent()[1]
            self.window.run_command('toggle_tabs')
            if state1_h and state2_h:
                return (state1_h < state2_h)

    def is_minimap_visible(self):
        if ST3116:
            return self.window.is_minimap_visible()
        else:
            v = self.window.active_view()
            state1_w = v.viewport_extent()[0]
            self.window.run_command('toggle_minimap')
            state2_w = v.viewport_extent()[0]
            self.window.run_command('toggle_minimap')
            if state1_w and state2_w:
                return (state1_w < state2_w)

    def is_status_bar_visible(self):
        if ST3116:
            return self.window.is_status_bar_visible()
        else:
            v = self.window.active_view()
            state1_h = v.viewport_extent()[1]
            self.window.run_command('toggle_status_bar')
            state2_h = v.viewport_extent()[1]
            self.window.run_command('toggle_status_bar')
            if state1_h and state2_h:
                return (state1_h < state2_h)

    def is_side_bar_visible(self):
        if ST3098:
            return self.window.is_sidebar_visible()
        elif ST3:
            return self.window.settings().get('dfw_side_bar_vis', True)
        else:
            v = self.window.active_view()
            state1_w = v.viewport_extent()[0]
            self.window.run_command('toggle_side_bar')
            state2_w = v.viewport_extent()[0]
            self.window.run_command('toggle_side_bar')
            if state1_w and state2_w:
                return (state1_w < state2_w)

    def is_menu_visible(self):
        if ST3116:
            return self.window.is_menu_visible()
        elif ST3:
            return self.window.settings().get('dfw_menu_vis', True)
        else:
            v = self.window.active_view()
            state1_w = v.viewport_extent()[1]
            self.window.run_command('toggle_menu')
            state2_w = v.viewport_extent()[1]
            self.window.run_command('toggle_menu')
            if state1_w and state2_w:
                return (state1_w < state2_w)
