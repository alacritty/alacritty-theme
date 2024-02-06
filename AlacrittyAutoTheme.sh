#!/bin/bash

interface="org.freedesktop.portal.Settings"
monitor_path="/org/freedesktop/portal/desktop"
monitor_member="SettingChanged"
count=0 #D-Bus fires the change event 4 times so we'll only act on it once

dbus-monitor --profile "interface='$interface',path=$monitor_path,member=$monitor_member" |
	while read line; do
		let count++

		if [ $count = 3 ]; then
			theme="$(gsettings get org.gnome.desktop.interface color-scheme)"
			if [[ "$theme" == "'prefer-dark'" ]]; then
				#Need to set with full paths, goofy things are happening otherwise
				echo "$(echo import = [ \'~/.config/alacritty/themes/dark_theme.toml\' ] > ~/.config/alacritty/themes/theme.toml)"
			else
				echo "$(echo import = [ \'~/.config/alacritty/themes/light_theme.toml\' ] > ~/.config/alacritty/themes/theme.toml)"
			fi
			count=0
		fi 
	done
