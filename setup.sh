#!/bin/zsh

echo "Installing packages..."

pacman -Syu
pacman -S xonsh qtile alacritty lightdm picom ttf-jetbrains-mono-nerd python-pip python-psutil

pipx install -U 'xonsh[full]' --break-system-packages

curl -O https://download.sublimetext.com/sublimehq-pub.gpg && sudo pacman-key --add sublimehq-pub.gpg && sudo pacman-key --lsign-key 8A8F901A && rm sublimehq-pub.gpg
echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/x86_64" | sudo tee -a /etc/pacman.conf
pacman -Syu sublime-text

echo "Installing AUR packages..."

pamac build web-greeter qtile-extras sublime-text-4

echo "Starting lighdm"

systemctl enable lightdm.service --force

echo "Configuring greeter..."

# TODO: Edit entire greeter file
# echo "\n[Seat:*]\ngreeter-session=web-greeter\nuser-session=qtile\n" | tee -a /etc/lightdm/lightdm.conf 

echo "Moving config files..."

rsync -rcxP ./files/ ~/
rm -rf /files

echo "Moving data..."

mv ./ones/owl_house_dg.png /usr/share/pixmaps/owl_house_bg.png

echo "Configuring..."

echo "/bin/xonsh" | tee -a /etc/shells
chsh -s /bin/xonsh

echo "All done!"