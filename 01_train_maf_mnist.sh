#!/bin/bash

#*************************************************************************
#	> File Name: tran.sh
#	> Author: Yang Zhang 
#	> Mail: zyziszy@foxmail.com 
#	> Created Time: Tue Jan  7 20:44:04 2020
# ************************************************************************/

python -u main.py \
	--epochs 500 \
	--flow maf \
	--cond \
	--dataset MNIST


