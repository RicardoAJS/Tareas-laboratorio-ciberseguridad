#!/bin/bash
echo "Registro de propina semanal"

read -p "Trabajaste el sabado? presiona 1 si se trabajo el sabado" dia
$T = 5

if [$dia = 1 ] ; then
	$T = 6
fi

for ((i = 0 ; i <= $T; i++ ))
do
	read -p "Ingresa la propina de dia $i" cantidad
	propina[$i] = $cantidad
done

for ((i = 0 ; i<= $T ; i++))
do
	echo ${propina[$i]}
do
