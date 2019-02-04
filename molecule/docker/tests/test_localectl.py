# Make sure localectl_locale was set correctly.
def test_localectl_locale(host):
    assert host.run('grep LANG /etc/locale.conf').stdout == \
        'LANG=en_UK.UTF-8'


# Make sure localectl_keymap was set correctly.
def test_localectl_keymap(host):
    assert host.run('grep KEYMAP /etc/vconsole.conf').stdout == \
        'KEYMAP=uk'


# Make sure localectl_x11_keymap was set correctly.
# Use sed to return everything after the string Option
# from the 00-keyboad.conf file.
def test_localectl_x11_keymap(host):
    assert host.run("sed -n 's/Option//p' \
        /etc/X11/xorg.conf.d/00-keyboard.conf").stdout == \
        '         "XkbLayout" "uk"'
