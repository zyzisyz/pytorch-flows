#!/usr/bin/env python
# coding=utf-8

# *************************************************************************
#	> File Name: png2gif.py
#	> Author: Yang Zhang 
#	> Mail: zyziszy@foxmail.com
#	> Created Time: Tue 07 Jan 2020 11:45:25 PM CST
# ************************************************************************/

import argparse
import imageio
import os
import sys


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='PyTorch Flows')
	parser.add_argument('--img_dir', type=str, default=".")
	parser.add_argument('--duration', type=float, default="0.1")
	parser.add_argument('--gif_name', type=str, default="all")
	parser.add_argument('--format', type=str, default="png")
	args = parser.parse_args()

	path = args.img_dir
	duration = args.duration
	name = "{}.gif".format(args.gif_name)

	imgs = os.listdir(path)
	frames = []     # buffer
	print(imgs)
	for img in imgs:
		if(img.endswith(".{}".format(args.format))):
			a = imageio.imread(img)
			frames.append(a)

	imageio.mimsave(name, frames, 'GIF', duration=duration)


