# -*- encoding: utf-8 -*-

import sublime
import sublime_plugin


class ReadOnlyBuffer():
    def get_plugin_settings(self):
        return sublime.load_settings("SublimeReadOnlyBuffer.sublime-settings")

    def set_plugin_settings(self):
        sublime.save_settings("SublimeReadOnlyBuffer.sublime-settings")

    def get_plugin_file_cache(self):
        settings = self.get_plugin_settings()
        return settings.get("cache", {})


class SetReadOnlyBufferCommand(ReadOnlyBuffer, sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view
        self.settings = self.get_plugin_settings()
        self.debug = self.settings.get("debug", False)

    def is_enabled(self):
        return not self.view.is_read_only()

    def description():
        return "Sets the buffer to read-only state (saving the unsaved contents is still possible"

    def run(self, edit):
        cache = self.get_plugin_file_cache()
        if(self.view.is_read_only()):
            sublime.status_message("Current buffer is already read-only")
            return

        self.view.set_read_only(True)
        if(self.view.file_name() is not None):
            cache[self.view.file_name()] = True
        self.settings.set("cache", cache)
        self.set_plugin_settings()
        sublime.status_message("Current buffer set to read-only")


class SetReadWriteBufferCommand(ReadOnlyBuffer, sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view
        self.settings = self.get_plugin_settings()
        self.debug = self.settings.get("debug", False)

    def is_enabled(self):
        return self.view.is_read_only()

    def description():
        return "Sets the buffer to read-write"

    def run(self, edit):
        cache = self.get_plugin_file_cache()
        if(not self.view.is_read_only()):
            sublime.status_message("Current buffer is already read-write")
            return

        self.view.set_read_only(False)
        if(self.view.file_name() is not None):
            cache[self.view.file_name()] = False
        self.settings.set("cache", cache)
        self.set_plugin_settings()
        sublime.status_message("Current buffer set to read-write")


class ReadOnlyEventListener(ReadOnlyBuffer, sublime_plugin.EventListener):
    def on_clone(self, view):
        cache = self.get_plugin_file_cache()
        if(view.file_name() is not None):
            file_name = view.file_name()
            if(file_name in cache):
                state = cache.get(file_name)
                view.set_read_only(state)
                if(state):
                    sublime.status_message("Current buffer set to read-only")
                else:
                    sublime.status_message("Current buffer set to read-write")

    def on_load(self, view):
        cache = self.get_plugin_file_cache()
        if(view.file_name() is not None):
            file_name = view.file_name()
            if(file_name in cache):
                state = cache.get(file_name)
                view.set_read_only(state)
                if(state):
                    sublime.status_message("Current buffer set to read-only")
                else:
                    sublime.status_message("Current buffer set to read-write")
