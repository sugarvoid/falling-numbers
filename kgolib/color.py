def hex_to_rgba(hex_code: str, alpha: int = 255) -> tuple:
    hex_code = hex_code.lstrip("#")
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return r, g, b, alpha


if __name__ == "__main__":
    # Example usage:
    hex_color = "#ff3366"
    rgba_color = hex_to_rgba(hex_color, alpha=200)  # Adjust alpha as needed (0 to 255)
    print(rgba_color)
