#! /bin/sh

rm  /boot/at.txt

cat /dev/ttyUSB2 >> /boot/at.txt &
sleep 1
chat -V -s '' "AT+CSQ" '' > /dev/ttyUSB2 < /dev/ttyUSB2
sleep 2
killall cat
more /boot/at.txt
exit 0

