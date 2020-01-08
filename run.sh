#!/bin/bash

#*************************************************************************
#	> File Name: run.sh
#	> Author: Yang Zhang 
#	> Mail: zyziszy@foxmail.com 
#	> Created Time: Wed Jan  8 23:55:44 2020
# ************************************************************************/


bash 01_train_maf_mnist.sh
wait

bash 02_train_realnvp_mnist.sh
wait
