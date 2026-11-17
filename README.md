# pixel-tile-shuffle

Shuffles pixels in 2x2 blocks to create a micro-checkerboard visual effect.

## Project Description
This project demonstrates a simple image transformation that applies a "micro-checkerboard" pixel shuffle. It iterates through an image in 2x2 pixel blocks. Within each block, it swaps the top-left pixel with the bottom-right pixel, and the top-right pixel with the bottom-left pixel. The script generates a synthetic gradient image, applies this shuffle, and saves both the original and the transformed image, along with a side-by-side comparison.

## How it Works
1.  **Image Generation**: A `256x256` pixel synthetic image is created with distinct color gradients across its channels (vertical blue, horizontal green, constant red). This makes the pixel shuffling easily observable.
2.  **Pixel Shuffle**: The `apply_micro_checkerboard_shuffle` function takes the image and iterates over it, processing every `2x2` block of pixels. For each block, it reassigns the pixel values according to the specified swap pattern.
3.  **Output**: The script saves three image files:
    *   `original_image.png`: The initial synthetic image.
    *   `transformed_image.png`: The image after the micro-checkerboard shuffle.
    *   `comparison_output.png`: A single image showing the original and transformed images side-by-side for easy comparison.

## Requirements
The project uses the following Python libraries:
*   `numpy`
*   `opencv-python` (for `cv2`)

## How to Run
1.  **Save the Script**: Save the provided `main.py` script.
2.  **Create `requirements.txt`**: Create a file named `requirements.txt` in the same directory with the following content:
    ```
    numpy
    opencv-python
    ```
3.  **Install Dependencies**: Open your terminal or command prompt, navigate to the project directory, and install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Script**: Execute the Python script:
    ```bash
    python main.py
    ```
5.  **Check Output**: After execution, three new image files (`original_image.png`, `transformed_image.png`, `comparison_output.png`) will be created in the same directory. The script runs non-interactively and does not display any GUI windows, making it suitable for headless server environments.