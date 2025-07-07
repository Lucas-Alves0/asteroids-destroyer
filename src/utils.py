from pygame import *
from config import *
import pygame
import os


def load_image(path, scale=None):
    try:
        img = image.load(path).convert_alpha()
        if scale:
            img = transform.scale(img, scale)
        return img
    except Exception as e:
        print(f"Error loading image: {path}\n{e}")
        return Surface((10, 10))

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def check_collision(player, group):
    return sprite.spritecollide(player, group, False, sprite.collide_mask)

def check_shot_collision(shot_group, enemy_group):
    return sprite.groupcollide(shot_group, enemy_group, True, True, sprite.collide_mask)

def get_frame(sheet, col, row, frame_width=64, frame_height=44):
    sheet_width, sheet_height = sheet.get_size()

    if (col + 1) * frame_width > sheet_width or (row + 1) * frame_height > sheet_height:
        raise ValueError(f"Frame ({col}, {row}) fora dos limites da spritesheet ({sheet_width}x{sheet_height})")

    return sheet.subsurface(
        (col * frame_width, row * frame_height, frame_width, frame_height)
    )
