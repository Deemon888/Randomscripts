#!/bin/bash
clear;figlet "CACU"
sleep 1

# ctrl c (to stop of course)

while :
do

read -p "(input first number)> " no1
echo -e ""
read -p "(input sign for equation)> " eqs
echo -e ""
read -p "(inut second number)> " no2

if [[ $eqs == "x" ]]; then
  eqs=*
elif [[ $eqs == "*" ]]; then
  eqs=*
elif [[ $eqs == "**" ]]; then
  eqs=**
elif [[ $eqs == "/" ]]; then
  eqs=/
elif [[ $eqs == "+" ]]; then
  eqs=+
elif [[ $eqs == "-" ]]; then
  eqs=-
else
echo "error"
exit
fi

if [[ -z "$no1" ]]; then
echo "error: var 'no1' is empty"
exit
elif [[ -z "$no2" ]]; then
echo "error: var 'no2' is empty"
exit
elif [[ -z "$eqs" ]]; then
echo "error: var 'eqs' is empty"
exit
else
sleep 0
fi

A=$(( no1 "$eqs" no2))
echo -e "$no1 $eqs $no2 = $A\n"
done
