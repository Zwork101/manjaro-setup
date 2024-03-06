#!/bin/zsh

echo "Installing packages..."

pacman -Syu
pacman -S xonsh qtile alacritty lightdm picom ttf-jetbrains-mono-nerd sublime-text

echo "Installing AUR packages..."

pamac build web-greeter qtile-extras

echo "Starting lighdm"

systemctl enable lightdm.service --force

echo "Configuring greeter..."

echo "\n[Seat:*]\ngreeter-session=web-greeter\nuser-session=qtile\n" | tee -a /etc/lightdm/lightdm.conf 

echo "Moving config files..."

rsync -rcxP ./files/ ~/
rm -rf /files

echo "Moving data..."

mv ./ones/owl_house_dg.png /usr/share/pixmaps/owl_house_bg.png

echo "All done!"