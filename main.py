import numpy as np
import cv2

def generate_synthetic_image(width=256, height=256):
    """
    Generates a synthetic gradient image for testing the pixel shuffle.
    The image has a vertical gradient for the Blue channel,
    a horizontal gradient for the Green channel, and a constant Red channel.
    This distinct channel separation makes the 2x2 pixel shuffling easily visible.

    Args:
        width (int): The width of the generated image.
        height (int): The height of the generated image.

    Returns:
        numpy.ndarray: A 3-channel (BGR) NumPy array representing the image.
    """
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            # Blue channel varies vertically (0 at top, 255 at bottom)
            img[y, x, 0] = int(255 * (y / height))
            # Green channel varies horizontally (0 at left, 255 at right)
            img[y, x, 1] = int(255 * (x / width))
            # Red channel is a constant medium intensity for visibility
            img[y, x, 2] = 100
    return img

def apply_micro_checkerboard_shuffle(image_np):
    """
    Applies a 'micro-checkerboard' pixel shuffle effect to the input image.
    It iterates through 2x2 pixel blocks and performs the following swaps:
    - The top-left pixel is swapped with the bottom-right pixel.
    - The top-right pixel is swapped with the bottom-left pixel.

    Pixels in the last row or column (if image dimensions are odd) that
    cannot form a complete 2x2 block will remain unchanged.

    Args:
        image_np (numpy.ndarray): The input image (height, width, channels)
                                  as a NumPy array.

    Returns:
        numpy.ndarray: A new image array with the micro-checkerboard shuffle applied.
    """
    # Create a copy of the original image to store the shuffled result.
    # This prevents modifying the image in-place while still needing original pixel data.
    shuffled_img = np.copy(image_np)
    height, width, _ = image_np.shape

    # Iterate through the image in 2x2 pixel blocks.
    # The loop limits (height - 1, width - 1) ensure that 'r + 1' and 'c + 1'
    # always remain within the image bounds, effectively skipping any
    # last row/column that cannot form a complete 2x2 block.
    for r in range(0, height - 1, 2):
        for c in range(0, width - 1, 2):
            # Extract the four pixels from the current 2x2 block in the ORIGINAL image.
            p_tl = image_np[r, c]         # Top-left pixel
            p_tr = image_np[r, c+1]       # Top-right pixel
            p_bl = image_np[r+1, c]       # Bottom-left pixel
            p_br = image_np[r+1, c+1]     # Bottom-right pixel

            # Apply the specified pixel swaps to the corresponding positions
            # in the `shuffled_img` array.
            shuffled_img[r, c] = p_br         # Top-left gets Bottom-right
            shuffled_img[r, c+1] = p_bl       # Top-right gets Bottom-left
            shuffled_img[r+1, c] = p_tr       # Bottom-left gets Top-right
            shuffled_img[r+1, c+1] = p_tl     # Bottom-right gets Top-left

    return shuffled_img

def main():
    """
    Main function to generate an image, apply the shuffle, and save outputs.
    """
    print("Starting pixel-tile-shuffle project...")

    # 1. Generate a synthetic test image
    print("Generating a 256x256 synthetic gradient image...")
    original_image = generate_synthetic_image(width=256, height=256)
    original_filepath = "original_image.png"
    cv2.imwrite(original_filepath, original_image)
    print(f"Original image saved as '{original_filepath}'")

    # 2. Apply the micro-checkerboard shuffle
    print("Applying micro-checkerboard shuffle effect...")
    transformed_image = apply_micro_checkerboard_shuffle(original_image)
    transformed_filepath = "transformed_image.png"
    cv2.imwrite(transformed_filepath, transformed_image)
    print(f"Transformed image saved as '{transformed_filepath}'")

    # 3. Create a comparison image (original vs. transformed side-by-side)
    print("Creating a comparison image (original and transformed side-by-side)...")
    # Ensure images have the same height and width, then stack horizontally
    comparison_image = np.hstack((original_image, transformed_image))
    comparison_filepath = "comparison_output.png"
    cv2.imwrite(comparison_filepath, comparison_image)
    print(f"Comparison image saved as '{comparison_filepath}'")

    print("\nPixel-tile-shuffle project completed successfully.")
    print("Please check 'original_image.png', 'transformed_image.png', and 'comparison_output.png' for results.")

if __name__ == "__main__":
    main()