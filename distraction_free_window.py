#!/usr/bin/env python
# coding: utf-8

import sublime
import sublime_plugin

ST3 = int(sublime.version()) >= 3000
ST3098 = int(sublime.version()) >= 3098
ST3116 = int(sublime.version()) >= 3116


class DistractionFreeWindowCommand(sublime_plugin.WindowCommand):

    def run(self):
        debug = False
        w = self.window
        prestine = {}
        prestine['minimap_vis']        = minimap_vis         = self.is_minimap_visible(w)
        prestine['status_bar_vis']     = status_bar_vis      = self.is_status_bar_visible(w)
        prestine['tabs_vis']           = tabs_vis            = self.is_tabs_visible(w)
        prestine['side_bar_vis']       = side_bar_vis        = self.is_side_bar_visible(w)

        prestine['gutter_vis']         = gutter_vis          = w.settings().get('gutter')
        prestine['line_numbers_vis']   = line_numbers_vis    = w.settings().get('line_numbers')
        prestine['fold_buttons_vis']   = fold_buttons_vis    = w.settings().get('fold_buttons')
        prestine['draw_centered']      = draw_centered_vis   = w.settings().get('draw_centered')
        prestine['wrap_width']         = wrap_width_value    = w.settings().get('wrap_width')
        prestine['rulers']             = rulers_value        = w.settings().get('rulers')
        prestine['draw_indent_guides'] = indent_guides_value = w.settings().get('draw_indent_guides')
        prestine['draw_white_space']   = white_space_value   = w.settings().get('draw_white_space')

        is_in_dfm = self.is_in_dfm(w)
        is_in_fs  = self.is_in_fs(w)
        is_in_dfw = w.settings().get('dfw_mode', False)
        is_in_nm  = not (is_in_dfw or is_in_dfm or is_in_fs)

        if debug:
            print('-------------------------')
            print('-------------------------')
            print('gutter:       ', gutter_vis)
            print('line_numbers: ', line_numbers_vis)
            print('fold_buttons: ', fold_buttons_vis)
            print('-------------------------')
            print('minimap:      ', minimap_vis)
            print('status_bar:   ', status_bar_vis)
            print('tabs:         ', tabs_vis)
            print('side_bar:     ', side_bar_vis)
            print('draw_centered:', draw_centered_vis)
            print('wrap_size:    ', wrap_width_value)
            print('-------------------------')
            print('in dfm:       ', is_in_dfm)
            print('in fs:        ', is_in_fs)
            print('in nm:        ', is_in_nm)
            print('in dfw:       ', is_in_dfw)
            print('-------------------------')

        settings = sublime.load_settings('distraction_free_window.sublime-settings')

        if is_in_nm: # normal mode going to dfw mode
            # save original state
            # print('-- normal mode going to dfw mode --')
            w.settings().set('dfw_mode_prestine', prestine)

            if settings.get('dfw_hide_minimap') and minimap_vis:
                w.run_command('toggle_minimap')
            if settings.get('dfw_hide_status_bar') and status_bar_vis:
                w.run_command('toggle_status_bar')
            if settings.get('dfw_hide_tabs') and tabs_vis:
                w.run_command('toggle_tabs')
            if settings.get('dfw_hide_side_bar') and side_bar_vis:
                if ST3098:
                    w.set_sidebar_visible(False)
                else:
                    w.run_command('toggle_side_bar')

            if settings.get('dfw_hide_gutter'):
                w.settings().set('gutter', False)
            if settings.get('dfw_hide_line_numbers'):
                w.settings().set('line_numbers', False)
            if settings.get('dfw_hide_fold_buttons'):
                w.settings().set('fold_buttons', False)
            if settings.get('dfw_hide_rulers'):
                w.settings().set('rulers', [])
            if settings.get('dfw_hide_indent_guides'):
                w.settings().set('draw_indent_guides', False)
            if settings.get('dfw_hide_white_space'):
                w.settings().set('draw_white_space', 'none')
            if settings.get('dfw_draw_centered'):
                w.settings().set('draw_centered', True)
                w.settings().set('wrap_width', settings.get('dfw_wrap_width'))

            # changing layout
            if settings.get('dfw_switch_to_single_layout'):
                w.run_command('max_pane')

            # set view settings to dfw_mode: true
            w.settings().set('dfw_mode', True)

        elif is_in_dfw: # dfw mode going to normal mode
            # print('-- dfw mode going to normal mode --')
            prestine_state = w.settings().get('dfw_mode_prestine')
            # return to orginal
            if minimap_vis != prestine_state['minimap_vis']:
                w.run_command('toggle_minimap')
            if status_bar_vis != prestine_state['status_bar_vis']:
                w.run_command('toggle_status_bar')
            if tabs_vis != prestine_state['tabs_vis']:
                w.run_command('toggle_tabs')
            if side_bar_vis != prestine_state['side_bar_vis']:
                if ST3098:
                    w.set_sidebar_visible(prestine_state['side_bar_vis'])
                else:
                    w.run_command('toggle_side_bar')

            if settings.get('dfw_hide_gutter'):
                w.settings().erase('gutter')
            if settings.get('dfw_hide_line_numbers'):
                w.settings().erase('line_numbers')
            if settings.get('dfw_hide_fold_buttons'):
                w.settings().erase('fold_buttons')
            if settings.get('dfw_hide_rulers'):
                w.settings().erase('rulers')
            if settings.get('dfw_hide_indent_guides'):
                w.settings().erase('draw_indent_guides')
            if settings.get('dfw_hide_white_space'):
                w.settings().erase('draw_white_space')
            if settings.get('dfw_draw_centered'):
                w.settings().erase('draw_centered')
                w.settings().erase('wrap_width')

            # changing layout
            if settings.get('dfw_switch_to_single_layout'):
                w.run_command('max_pane')

            # remove orginal object
            w.settings().erase('dfw_mode_prestine')
            # set window settings to dfw_mode: false
            w.settings().set('dfw_mode', False)

    def is_tabs_visible(self, view):
        if ST3116:
            return self.window.get_tabs_visible()
        else:
            w = self.window
            state1_h = w.active_view().viewport_extent()[1]
            w.run_command('toggle_tabs')
            state2_h = w.active_view().viewport_extent()[1]
            w.run_command('toggle_tabs')
            if state1_h and state2_h:
                return (state1_h < state2_h)

    def is_minimap_visible(self, view):
        if ST3116:
            return self.window.is_minimap_visible()
        else:
            w = self.window
            state1_w = w.active_view().viewport_extent()[0]
            w.run_command('toggle_minimap')
            state2_w = w.active_view().viewport_extent()[0]
            w.run_command('toggle_minimap')
            if state1_w and state2_w:
                return (state1_w < state2_w)

    def is_status_bar_visible(self, view):
        if ST3116:
            return self.window.is_status_bar_visible()
        else:
            w = self.window
            state1_h = w.active_view().viewport_extent()[1]
            w.run_command('toggle_status_bar')
            state2_h = w.active_view().viewport_extent()[1]
            w.run_command('toggle_status_bar')
            if state1_h and state2_h:
                return (state1_h < state2_h)

    def is_in_dfm(self, view):
        return self.window.settings().get('dfw_is_in_dfm', False)

    def is_in_fs(self, view):
        return self.window.settings().get('dfw_is_in_fs', False)

    def is_side_bar_visible(self, view):
        if ST3098:
            return self.window.is_sidebar_visible()
        else:
            w = self.window
            if ST3:
                return w.settings().get('dfw_side_bar_vis', True)
            else: # ST2
                state1_w = w.active_view().viewport_extent()[0]
                w.run_command('toggle_side_bar')
                state2_w = w.active_view().viewport_extent()[0]
                w.run_command('toggle_side_bar')
                if state1_w and state2_w:
                    return (state1_w < state2_w)


class DfwTestFsEvents(sublime_plugin.EventListener):

    def on_window_command(self, window, command_name, args):
        if command_name != 'toggle_full_screen':
            return None

        # print('on toggle fullscreen called')
        pre_fs_height = window.active_view().viewport_extent()[1]

        def post_fs():
            post_fs_height = window.active_view().viewport_extent()[1]
            if pre_fs_height > post_fs_height:
                    is_in_fs = False
            else:
                    is_in_fs = True

            window.settings().set('dfw_is_in_fs', is_in_fs)

        sublime.set_timeout(post_fs, 1)
        return None


class DfwTestSideBarEvents(sublime_plugin.EventListener):

    def on_window_command(self, window, command_name, args):
        if command_name != 'toggle_side_bar':
            return None

        # print('on toggle side bar called')
        pre_width = window.active_view().viewport_extent()[0]

        def post_toggle():
            post_width = window.active_view().viewport_extent()[0]
            #print(pre_width,post_width)
            if pre_width <= post_width:
                    side_bar_vis = False
            else:
                    side_bar_vis = True

            window.settings().erase('dfw_side_bar_vis')
            window.settings().set('dfw_side_bar_vis', side_bar_vis)

        sublime.set_timeout(post_toggle, 10)
        return None
