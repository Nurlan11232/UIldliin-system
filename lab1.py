#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def calculate_text_memory(lines, columns, colors):
    """Текстэн дэлгэцийн санах ой тооцоолох"""
    total_chars = lines * columns
    bits_per_color = math.log2(colors)
    bytes_per_char = 1 + (bits_per_color / 8)  # ASCII + өнгө
    total_bytes = total_chars * bytes_per_char
    return total_bytes

def calculate_graphics_memory(width, height, colors=None, bits_per_pixel=None):
    """График дэлгэцийн санах ой тооцоолох"""
    total_pixels = width * height
    
    if colors:
        bits_per_pixel = math.log2(colors)
    
    total_bits = total_pixels * bits_per_pixel
    total_bytes = total_bits / 8
    return total_bytes

def calculate_access_times(total_chars):
    """Кэш, үндсэн санах ой, дискний хандалтын хугацаа"""
    
    # Кэш: 1 тэмдэгт = 2 наносекунд
    cache_ns = total_chars * 2
    cache_ms = cache_ns / 1_000_000   # наносекунд → миллисекунд
    
    # Үндсэн санах ой: 1 тэмдэгт = 10 наносекунд
    memory_ns = total_chars * 10
    memory_ms = memory_ns / 1_000_000
    
    # Диск: 1024 тэмдэгт = 10 миллисекунд
    disk_ms = (total_chars / 1024) * 10
    
    return cache_ms, memory_ms, disk_ms

def main(): 
    # Бодлого 1: 80x25, 4 өнгө
    result1 = calculate_text_memory(80, 25, 4)
    print(f"1. Текстэн дэлгэц 80×25, 4 өнгө:")
    print(f"   Шаардлагатай RAM: {result1:.0f} байт = {result1/1024:.2f} КБ")
    print()
    
    # Бодлого 2: 60x40, 16 өнгө  
    result2 = calculate_text_memory(60, 40, 16)
    print(f"2. Текстэн дэлгэц 60×40, 16 өнгө:")
    print(f"   Шаардлагатай RAM: {result2:.0f} байт = {result2/1024:.2f} КБ")
    print()
    
    # Бодлого 3: 800x640, 16 өнгө
    result3 = calculate_graphics_memory(800, 640, colors=16)
    print(f"3. График горим 800×640, 16 өнгө:")
    print(f"   Шаардлагатай хадгалах хэмжээ: {result3:.0f} байт = {result3/1024:.2f} КБ")
    print()
    
    # Бодлого 4: 600x400, 8 бит
    result4 = calculate_graphics_memory(600, 400, bits_per_pixel=8)
    print(f"4. График горим 600×400, 8 бит өнгө:")
    print(f"   Шаардлагатай хадгалах хэмжээ: {result4:.0f} байт = {result4/1024:.2f} КБ")
    print()
    
    # Бодлого 5: "Си хэлний" ном
    total_chars5 = 500 * 30 * 60
    cache5, memory5, disk5 = calculate_access_times(total_chars5)
    print(f"5. 'Си хэлний' ном шалгах хугацаа:")
    print(f"   Нийт тэмдэгт: {total_chars5:,}")
    print(f"   Кэш: {cache5:.2f} мс")
    print(f"   Санах ой: {memory5:.2f} мс")
    print(f"   Диск: {disk5/1000:.2f} сек")
    print()
    
    # Бодлого 6: "Бодлогууд" ном
    total_chars6 = 100 * 20 * 50
    cache6, memory6, disk6 = calculate_access_times(total_chars6)
    print(f"6. 'Бодлогууд' номын хугацаа:")
    print(f"   Нийт тэмдэгт: {total_chars6:,}")
    print(f"   Кэш: {cache6:.2f} мс")
    print(f"   Санах ой: {memory6:.2f} мс")
    print(f"   Диск: {disk6/1000:.2f} сек")
    print()
if __name__ == "__main__":
    main()
