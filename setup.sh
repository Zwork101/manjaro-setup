#!/bin/zsh

echo "Installing packages..."

pacman -Syu
pacman -S xonsh qtile alacritty lightdm picom ttf-jetbrains-mono-nerd sublime-text

echo "Installing AUR packages..."

pamac build web-greeter qtile-extras

echo "Starting lighdm"

systemctl enable lightdm.service --force

echo "Configuring greeter..."

pkg=$(ls -1 /usr/share/xgreeters/ | grep "web")
echo "\n[Seat:*]\ngreeter-session=$pkg\n" | tee -a /etc/lightdm/lightdm.conf 

echo "Moving config files..."

rsync -rcxP ./files/ ~/
rm -rf /files

echo "All done!"