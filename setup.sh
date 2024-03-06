#!/bin/bash

echo "Installing packages..."

pacman -Syu
pacman -S xonsh qtile alacritty lightdm picom ttf-jetbrains-mono-nerd sublime-text

echo "Installing AUR packages..."

yay -S web-greeter qtile-extras

echo "Starting lighdm"

systemctl enable lightdm.service --force

echo "Configuring greeter..."

echo "[Seat:*]\ngreeter-session=${ls -1 /usr/share/xgreeters/ | grep \"web\"}\n" >> /etc/lightdm/lightdm.conf 

echo "Moving config files..."

rsync -rcx /files ~/
rm -r /files

echo "All done!"