# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout
from qtile_extras import widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras.widget.decorations import RectDecoration
from libqtile.utils import guess_terminal

import os

mod = "mod4"
terminal = "alacritty"

os.system("picom -b")

default_group = {"font": "JetBrainsMono Nerd Font"}

COLOR = {
    "black": "#2D2727",
    "dark-purple": "#413543",
    "purple": "#8F43EE",
    "yellow": "F0EB8D",
}

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window he edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [
    Group("HOME", label="\uf4e2 "),
    Group(
        "FIREFOX",
        label="\uf269  ",
        matches=[Match(wm_class=["firefox"])],
        spawn="firefox",
        persist=True,
    ),
    Group(
	"DEV",
	label="\ue696 ",
	matches=[Match(wm_class=["Sublime_text"])]
    ),
    Group("MUSIC", label="\uf001  "),
    Group("VM", label="\ue62a "),
    Group(
	"STEAM",
	label="\uf1b6 ",
	matches=[Match(wm_class=["Steam"])]
    ),
]

commands = {"DEV": "subl"}

for num, i in enumerate(groups):
    index = num + 1
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                f"F{index}",
                lazy.group[i.name].toscreen(),
                (lambda: lazy.spawn(commands[i.name])) if i.name in commands else (lambda: None),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                f"F{index}",
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack=[], 
        border_width=3,
        margin_on_single=[20, 40, 20, 40],
        margin=[10, 20, 10, 20],
        border_focus=COLOR["yellow"],
        border_normal=COLOR["dark-purple"],
        border_normal_stack=COLOR["purple"],
        border_on_single=True
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

bubble = {
    "decorations": [
        RectDecoration(
            use_widget_background=True,
            radius=12,
            filled=True,
            # group=True
        )
    ],
    "background": COLOR["purple"],
    "foreground": COLOR["yellow"],
    "padding": 20
}

bubble_sep = widget.Sep(padding=10, linewidth=0)

screens = [
    Screen(
        bottom=bar.Bar(
            [
                # widget.CurrentLayout(fontsize=20),
                widget.GroupBox(
                    highlight_method="line",
                    active=COLOR["yellow"],
                    this_current_screen_border=COLOR["yellow"],
                    # this_screen_border=COLOR["purple"],
                    inactive=COLOR["purple"],
                    # highlight_color=[COLOR["yellow"], COLOR["purple"]]
                    padding_x=5,
                    fontsize=20
                ),
                widget.Spacer(),
                widget.Prompt(),
                # widget.WindowName(),
                widget.Spacer(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.CheckUpdates(
                    display_format="\ueb29 {updates}",
                    no_update_string="\uf00c",
                    **bubble,
                ),
                bubble_sep,
                widget.WidgetBox(
                    text_closed="  \uf878  ",
                    text_open="  \uf061  ",
                    widgets=[
                        bubble_sep,
                        widget.CPU(format="\uf4bc {load_percent}%", **bubble),
                        bubble_sep,
                        widget.Memory(
                            format="\ue28c {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
                            **bubble,
                        ),
                        bubble_sep,
                        widget.Net(
                            format="\uf0ac{down}\uf149{up}\uf148",
                            interface="enp0s3",
                            **bubble,
                        ),
                    ],
                    **bubble,
                ),
                bubble_sep,
                widget.Clock(format="%a %I:%M %p", **bubble),
                # widget.TextBox(
                #  text="\ue0b6",
                #  fontsize=25,
                #  padding=0,
                #  foreground=COLOR["purple"],
                #  background=COLOR["dark-purple"]
                # ),
                bubble_sep,
                widget.QuickExit(
                    default_text="Shutdown \u23fb",
                    countdown_format="[ {} ]",
                    # foreground=COLOR["yellow"],
                    # background=COLOR["purple"],
                    timer_interval=0.02,
                    # padding=15,
                    **bubble,
                ),
                # widget.Spacer(length=10, **bubble)
                # widget.TextBox(
                #  text="\ue0b4",
                #  padding=0,
                #  fontsize=25,
                #  foreground=COLOR["purple"],
                #  background=COLOR["dark-purple"]
                # )
            ],
            23,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background=COLOR["dark-purple"]
            #margin=[4, 0, 0, 0]
        ),
        wallpaper="/usr/share/pixmaps/owl_house_bg.png",
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Settings", wm_class="Steam") # Steam Settings
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
