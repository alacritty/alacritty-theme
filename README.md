# Alacritty Theme

Collection of colorschemes for easy configuration of the [Alacritty terminal
emulator].

[Alacritty terminal emulator]: https://github.com/alacritty/alacritty

## Installation

### Imports

Clone the repository, or download the theme of your choice:

```sh
# We use Alacritty's default Linux config directory as our storage location here.
mkdir -p ~/.config/alacritty/themes
git clone https://github.com/alacritty/alacritty-theme ~/.config/alacritty/themes
```

Add an import to your `alacritty.yml` (Replace `{theme}` with your desired
colorscheme):

```yaml
import:
 - ~/.config/alacritty/themes/{variant}/{theme}.yaml
```

### Manual

To manually include a colorscheme in an existing `alacritty.yml`, you just need
to copy the entire content of the theme into the root level of your
configuration file.

## Color Schemes

|                                                                       NAME                                                                        |                           COLORS                           |
|:-------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------:|
|                                   **_afterglow_**<br>[source](https://github.com/YabataDesign/afterglow-theme)                                    |        ![base16_default_dark](images/dark/afterglow.png)        |
|                                   **_alabaster_**<br>[source](https://github.com/tonsky/vscode-theme-alabaster)                                   |             ![alabaster](images/dark/alabaster.png)             |
|                                   **_alabaster_dark_**<br>[source](https://github.com/gargakshit/vscode-theme-alabaster-dark)                     |        ![alabaster_dark](images/dark/alabaster_dark.png)        |
|                                      **_argonaut_**<br>[source](https://github.com/pwaleczek/Argonaut-theme)                                      |        ![base16_default_dark](images/dark/argonaut.png)         |
|                  **_atom_one_light_**<br>[source](https://github.com/dexpota/kitty-themes/blob/master/themes/AtomOneLight.conf)                   |        ![atom_one_light](images/light/atom_one_light.png)        |
|                                        **_ayu_dark_**<br>[source](https://github.com/ayu-theme/ayu-colors)                                        |              ![ayu_dark](images/dark/ayu_dark.png)              |
|                                       **_ayu_light_**<br>[source](https://github.com/ayu-theme/ayu-colors)                                        |             ![ayu_light](images/light/ayu_light.png)             |
|                                   **_baitong_**<br>[source](https://github.com/cypj/baitong-theme)                                                |         ![baitong](images/dark/baitong.png)                     |
|                                   **_base16_default_dark_**<br>[source](https://github.com/chriskempson/base16)                                   |   ![base16_default_dark](images/dark/base16_default_dark.png)   |
|                                         **_blood_moon_**<br>[source](https://github.com/dguo/blood-moon)                                          |            ![blood_moon](images/dark/blood_moon.png)            |
|                                                                   **_bluish_**                                                                    |                ![bluish](images/dark/bluish.png)                |
|                                              **_breeze_**<br>[source](https://github.com/KDE/breeze)                                              |                ![breeze](images/dark/breeze.png)                |
|              **_campbell_**<br>[source](https://blogs.msdn.microsoft.com/commandline/2017/08/02/updating-the-windows-console-colors)              |              ![campbell](images/dark/campbell.png)              |
|              **_carbonfox_**<br>[source](https://github.com/edeneast/nightfox.nvim/raw/main/extra/carbonfox/nightfox_alacritty.yml)               |             ![carbonfox](images/dark/carbonfox.png)             |
|              **_catppuccin_**<br>[source](https://github.com/catppuccin/catppuccin)                                                               |              ![catppuccin](images/dark/catppuccin.png)          |
|                               **_challenger_deep_**<br>[source](https://github.com/challenger-deep-theme/alacritty)                               |       ![challenger_deep](images/dark/challenger_deep.png)       |
|                                              **_city_lights_**<br>[source](https://citylights.xyz/)                                               |           ![city_lights](images/light/citylights.png)            |
|                                 **_Cobalt2_**<br>[source](https://github.com/wesbos/cobalt2/tree/master/Cobalt2)                                  |               ![Cobalt2](images/dark/Cobalt2.png)               |
|                                 **_cyber_punk_neon_**<br>[source](https://github.com/Roboron3042/Cyberpunk-Neon)                                  |       ![cyber_punk_neon](images/dark/cyber_punk_neon.png)       |
|                                                **_darcula_**<br>[source](https://draculatheme.com)                                                |               ![darcula](images/dark/darcula.png)               |
|         **_dark_pastels_**<br>[source](https://invent.kde.org/utilities/konsole/-/blob/master/data/color-schemes/DarkPastels.colorscheme)         |          ![dark_pastels](images/dark/dark_pastels.png)          |
|                                                                  **_deep_space_**                                                                 |             ![depp_space](images/dark/deep_space.png)           |                                         
|                                     **_doom_one_**<br>[source](https://github.com/hlissner/emacs-doom-themes)                                     |              ![doom_one](images/dark/doom_one.png)              |
|                                                **_dracula_**<br>[source](https://draculatheme.com)                                                |               ![dracula](images/dark/dracula.png)               |
|                                     **_everforest_dark_**<br>[source](https://github.com/sainnhe/everforest)                                      |       ![everforest_dark](images/dark/everforest_dark.png)       |
|                                     **_everforest_light_**<br>[source](https://github.com/sainnhe/everforest)                                     |      ![everforest_light](images/light/everforest_light.png)      |
|                                           **_falcon_**<br>[source](https://github.com/fenetikm/falcon)                                            |                ![falcon](images/dark/falcon.png)                |
|                          **_flat_remix_**<br>[source](https://github.com/Mayccoll/Gogh/blob/master/themes/flat-remix.sh)                          |            ![flat_remix](images/dark/flat_remix.png)            |
| **_github_dark_**<br>[source](https://github.com/projekt0n/github-theme-contrib/blob/main/alacritty/github_dark.yml)                              | ![github_dark](images/dark/github_dark.png)                         |
| **_github_dark_colorblind_**<br>[source](https://github.com/projekt0n/github-theme-contrib/blob/main/alacritty/github_dark_colorblind.yml)        | ![github_dark_colorblind](images/dark/github_dark_colorblind.png)   |
| **_github_dark_default_**<br>[source](https://github.com/projekt0n/github-theme-contrib/blob/main/alacritty/github_dark_default.yml)              | ![github_dark_default](images/dark/github_dark_default.png)         |
| **_github_dimmed_**<br>[source](https://github.com/projekt0n/github-theme-contrib/blob/main/alacritty/github_dimmed.yml)                          | ![github_dimmed](images/dark/github_dimmed.png)                     |
| **_github_light_**<br>[source](https://github.com/projekt0n/github-theme-contrib/blob/main/alacritty/github_light.yml)                            | ![github_light](images/light/github_light.png)                       |
| **_github_light_colorblind_**<br>[source](https://github.com/projekt0n/github-theme-contrib/blob/main/alacritty/github_light_colorblind.yml)      | ![github_light_colorblind](images/light/github_light_colorblind.png) |
| **_github_light_default_**<br>[source](https://github.com/projekt0n/github-theme-contrib/blob/main/alacritty/github_light_default.yml)            | ![github_light_default](images/light/github_light_default.png)       |
|                                                                   **_gotham_**                                                                    |                ![falcon](images/dark/gotham.png)                |
|                                  **_gnome_terminal_**<br>[source](https://gitlab.gnome.org/GNOME/gnome-terminal)                                  |        ![gnome_terminal](images/dark/gnome_terminal.png)        |
|                                        **_gruvbox_dark_**<br>[source](https://github.com/morhetz/gruvbox)                                         |          ![gruvbox_dark](images/dark/gruvbox_dark.png)          |
|                                        **_gruvbox_light_**<br>[source](https://github.com/morhetz/gruvbox)                                        |         ![gruvbox_light](images/light/gruvbox_light.png)         |
|                                  **_gruvbox_material_medium_dark_**<br>[source](https://github.com/sainnhe/gruvbox-material)                      | ![gruvbox_material_medium_dark](images/dark/gruvbox_material_medium_dark.png) |
|                                  **_gruvbox_material_medium_light_**<br>[source](https://github.com/sainnhe/gruvbox-material)                      | ![gruvbox_material_medium_light](images/light/gruvbox_material_medium_light.png) |
|                                  **_hardhacker_**<br>[source](https:/light//github.com/hardhackerlabs/theme-alacritty)                                  |      ![hardhacker](images/dark/hardhacker.png)                  |
|                                                                **_high_contrast_**                                                                |         ![gruvbox_light](images/dark/high_contrast.png)         |
|                                 **_horizon-dark_**<br>[source](https://github.com/jolaleye/horizon-theme-vscode)                                  |          ![horizon-dark](images/dark/horizon-dark.png)          |
|                                                     **_hyper_**<br>[source](https://hyper.is)                                                     |                 ![hyper](images/dark/hyper.png)                 |
|                                 **_inferno_**<br>[source](https://github.com/hafiz-muhammad/inferno-alacritty-theme)                              |                 ![inferno](images/dark/inferno.png)             |
|                                                                    **_iterm_**                                                                    |                 ![iterm](images/dark/iterm.png)                 |
|                                 **_kanagawa_dragon_**<br>[source](https://github.com/rebelot/kanagawa.nvim)                                       |          ![kanagawa_dragon](images/dark/kanagawa_dragon.png)    |
|                                  **_kanagawa_wave_**<br>[source](https://github.com/rebelot/kanagawa.nvim)                                        |          ![kanagawa_wave](images/dark/kanagawa_wave.png)        |
|                                                                **_konsole_linux_**                                                                |             ![iterm](images/dark/konsole_linux.png)             |
|                                                                **_low_contrast_**                                                                 |             ![iterm](images/dark/low_contrast.png)              |
|                  **_Mariana_**<br>[source](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/alacritty/Mariana.yml)                   |                ![iterm](images/dark/mariana.png)                |
|                  **_marine_dark_**<br>[source](https://github.com/ProDeSquare/alacritty-colorschemes/blob/master/themes/marine_dark.yaml)         |                ![marine_dark](images/dark/marine_dark.png)         |
|                                  **_material_theme_**<br>[source](https://github.com/equinusocio/material-theme)                                  |        ![material_theme](images/dark/material_theme.png)        |
|                                                             **_material_theme_mod_**                                                              |    ![material_theme_mod](images/dark/material_theme_mod.png)    |
|                  **_meliora_**<br>[source](https://github.com/ramojus/mellifluous.nvim)                                                           |                ![meliora](images/dark/meliora.png)              |
|                  **_midnight-haze_**<br>[source](https://github.com/hafiz-muhammad/midnight-haze-alacritty-theme)                                 |    ![midnight-haze](images/dark/midnight-haze.png)              |
|    **_monokai_charcoal_**<br>[source](https://github.com/dodeca12/Monokai-Charcoal-Theme-for-Alacritty/blob/main/monokai_charcoal_white.yaml)     |      ![monokai_charcoal](images/dark/monokai-charcoal.png)      |
|                      **_monokai_pro_**<br>[source](https://gist.github.com/AlphaTechnolog/d1d5f6557f77f71519cb5713268da7dd)                       |           ![monokai_pro](images/dark/monokai_pro.png)           |
|                             **_moonlight_ii_vscode_**<br>[source](https://github.com/atomiks/moonlight-vscode-theme)                              |   ![moonlight_ii_vscode](images/light/moonlight_ii_vscode.png)   |
|                                            **_msx_**<br>[source](https://paulwratt.github.io/programmers-palettes/HW-MSX/HW-MSX-palettes.html)    |              ![msx](images/dark/msx.png)              |
|                                       **_nightfox_**<br>[source](https://github.com/EdenEast/nightfox.nvim)                                       |              ![nightfox](images/dark/nightfox.png)              |
|                                                             **_night_owlish_light_**                                                              |    ![night_owlish_light](images/light/night_owlish_light.png)    |
|                                       **_noctis-lux_**<br>[source](https://github.com/liviuschera/noctis)                                         |              ![noctis-lux](images/dark/noctis-lux.png)              |
|                                          **_nord_**<br>[source](https://github.com/arcticicestudio/nord)                                          |                  ![nord](images/dark/nord.png)                  |
|                                          **_nordic_**<br>[source](https://github.com/AlexvZyl/nordic.nvim)                                          |                  ![nordic](images/dark/nordic.png)                  |
|                                          **_nord_light_**<br>[source](https://github.com/nordtheme/alacritty/issues/28#issuecomment-1422225211)                                          |                  ![nord](images/light/nord_light.png)                  |
|                             **_oceanic_next_**<br>[source](https://github.com/voronianski/oceanic-next-color-scheme)                              |          ![oceanic_next](images/dark/oceanic_next.png)          |
|                                  **_omni_**<br>[source](https://github.com/getomni/alacritty/blob/main/omni.yml)                                  |                  ![omni](images/dark/omni.png)                  |
|                                                                  **_one_dark_**                                                                   |              ![one_dark](images/dark/one_dark.png)              |
|                                  **_palenight_**<br>[source](https://github.com/JonathanSpeek/palenight-iterm2)                                   |             ![palenight](images/dark/palenight.png)             |
|              **_papercolor_dark_**<br>[source](https://github.com/NLKNguyen/papercolor-theme/blob/master/colors/PaperColor.vim#L126)              |       ![papercolor_dark](images/dark/papercolor_dark.png)       |
|              **_papercolor_light_**<br>[source](https://github.com/NLKNguyen/papercolor-theme/blob/master/colors/PaperColor.vim#L36)              |      ![papercolor_light](images/light/papercolor_light.png)      |
|                  **_papertheme_**<br>[source](https://github.com/s6muel/paper-theme/blob/main/themes/alacritty/paper-theme.yml)                   |         ![papercolor_light](images/dark/papertheme.png)         |
|                                   **_pencil_dark_**<br>[source](https://github.com/mattly/iterm-colors-pencil)                                    |           ![pencil_dark](images/dark/pencil_dark.png)           |
|                                   **_pencil_light_**<br>[source](https://github.com/mattly/iterm-colors-pencil)                                   |          ![pencil_light](images/light/pencil_light.png)          |
|                                                                   **_rainbow_**                                                                   |               ![rainbow](images/dark/rainbow.png)               |
|                                  **_remedy_dark_**<br>[source](https://github.com/robertrossmann/vscode-remedy)                                   |           ![remedy_dark](images/dark/remedy_dark.png)           |
|                                        **_rose-pine_**<br>[source](https://github.com/rose-pine/alacritty)                                        |             ![rose-pine](images/dark/rose-pine.png)             |
|                                        **_rose-pine-dawn_**<br>[source](https://github.com/rose-pine/alacritty)                                        |             ![rose-pine-dawn](images/dark/rose-pine-dawn.png)             |
|                                        **_rose-pine-moon_**<br>[source](https://github.com/rose-pine/alacritty)                                        |             ![rose-pine-moon](images/dark/rose-pine-moon.png)             |
|                                      **_snazzy_**<br>[source](https://github.com/sindresorhus/hyper-snazzy)                                       |                ![snazzy](images/dark/snazzy.png)                |
|         **seashells**<br>[source](https://raw.githubusercontent.com/mbadolato/iTerm2-Color-Schemes/master/schemes/SeaShells.itermcolors)          |             ![seashells](images/dark/seashells.png)             |
| **smoooooth**<br>[source](https://github.com/gnachman/iTerm2/blob/33945e63ad48ed80d6cc1adf7cbeb663217652d2/plists/ColorPresets.plist#L4345-L4685) |             ![smoooooth](images/dark/smoooooth.png)             |
|                                      **_solarized_dark_**<br>[source](http://ethanschoonover.com/solarized)                                       |        ![solarized_dark](images/dark/solarized_dark.png)        |
|                                      **_solarized_light_**<br>[source](http://ethanschoonover.com/solarized)                                      |       ![solarized_light](images/light/solarized_light.png)       |
|                                    **_taerminal_**<br>[source](https://github.com/cozywigwam/iterm-taerminal)                                     |             ![taerminal](images/dark/taerminal.png)             |
|   **_tango_dark_**<br>[source](https://github.com/GNOME/gnome-terminal/blob/18939a24d21d6b7c6edd57a00a3a8a48f3aecec5/src/profile-editor.c#L213)   |            ![tango_dark](images/dark/tango_dark.png)            |
|                                      **_tender_**<br>[source](https://github.com/huyvohcmc/tender-alacritty)                                      |                ![tender](images/dark/tender.png)                |
|                                                                **_terminal_app_**                                                                 |          ![terminal_app](images/dark/terminal_app.png)          |
|                                                                 **_thelovelace_**                                                                 |          ![terminal_app](images/dark/thelovelace.png)           |
|                             **_tokyo-night_**<br>[source](https://github.com/zatchheems/tokyo-night-alacritty-theme)                              |           ![tokyo-night](images/dark/tokyo-night.png)           |
|                          **_tokyo-night-storm_**<br>[source](https://github.com/zatchheems/tokyo-night-alacritty-theme)                           |     ![tokyo-night-storm](images/dark/tokyo-night-storm.png)     |
|                                 **_tomorrow_night_**<br>[source](https://github.com/ChrisKempson/Tomorrow-Theme)                                  |        ![tomorrow_night](images/dark/tomorrow_night.png)        |
|                              **_tomorrow_night_bright_**<br>[source](https://github.com/ChrisKempson/Tomorrow-Theme)                              | ![tomorrow_night_bright](images/dark/tomorrow_night_bright.png) |
|                                     **_ubuntu_**<br>[source](https://design.ubuntu.com/brand/colour-palette/)                                     |                ![ubuntu](images/dark/ubuntu.png)                |
|                                        **_wombat_**<br>[source](https://github.com/djoyner/iTerm2-wombat)                                         |                ![wombat](images/dark/wombat.png)                |
|                                                                    **_xterm_**                                                                    |                 ![xterm](images/dark/xterm.png)                 |
|                                          **_zenburn_**<br>[source](https://github.com/jnurmine/Zenburn)                                           |               ![zenburn](images/dark/zenburn.png)               |

## Contributing

Bug reports and pull requests are welcome on GitHub at the [alacritty-theme]
repository.

[alacritty-theme]: https://github.com/alacritty/alacritty-theme

To add a new theme, just create a Pull Request with the following changes:

 - Add your theme to the `themes/{variant}` directory with the `{theme}.yaml` file format
 - Create a screenshot of your theme using the [`print_colors.sh`](./print_colors.sh) script
 - Add the screenshot to the `images/{variant}/` directory with the `{theme}.png` file format
 - Add your theme to the `schemes.yaml`
 - Add your theme to the `README.md`, following alphabetical ordering

## Maintainers

 * **indrajit** - *Author* - [eendroroy](https://github.com/eendroroy)
 * **Christian Dürr** - *Maintainer* - [chrisduerr](https://github.com/chrisduerr)

## License

The project is available as open source under the terms of the [Apache License, Version 2.0](LICENSE)
