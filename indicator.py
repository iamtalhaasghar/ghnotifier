#!/usr/bin/env python3

import gi

gi.require_version('AppIndicator3', '0.1')

from gi.repository import AppIndicator3, GObject


class Indicator:

    INDICATOR_ID = 'Github Notifier'

    def __init__(self):
        import github_notifier
        self.indicator = AppIndicator3.Indicator.new(
            self.INDICATOR_ID,
            github_notifier.APP_PATH + "/gh.png",
            AppIndicator3.IndicatorCategory.OTHER
        )

        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_label("0", self.INDICATOR_ID)

    def set_menu(self, menu):
        self.indicator.set_menu(menu)

    def update_label(self, label):
        GObject.idle_add(
            self.indicator.set_label,
            label, self.INDICATOR_ID,
            priority=GObject.PRIORITY_DEFAULT
        )
