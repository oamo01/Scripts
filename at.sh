#! /bin/sh

rm  /boot/info.txt

cat /dev/ttyUSB2 >> /boot/info.txt &
sleep 1
chat -V -s '' "$1" '' > /dev/ttyUSB2 < /dev/ttyUSB2
sleep 2
killall cat
more /boot/info.txt
exit 0
