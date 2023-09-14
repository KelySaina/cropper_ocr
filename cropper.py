import cv2
import pytesseract
import os

# Set the path to Tesseract OCR executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Cropper:
    def start(self, img_path):
        # Load the image
        image = cv2.imread(img_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply Canny edge detection
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours in the edge-detected image
        contours, _ = cv2.findContours(
            edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Create a directory to store the cropped images
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)

        # Iterate through the contours and find rectangles or squares
        for i, contour in enumerate(contours):
            # Approximate the contour to a polygon
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Check if the polygon has 4 vertices (a rectangle or square)
            if len(approx) == 4:
                # Get the bounding box coordinates
                x, y, w, h = cv2.boundingRect(approx)

                # Check if width is at least 100 pixels
                if w >= 100:
                    # Crop the region from the original image
                    cropped_region = image[y:y+h, x:x+w]

                    # Save the cropped image
                    cv2.imwrite(os.path.join(
                        output_dir, f'cropped_{i}.jpg'), cropped_region)

                    # Perform OCR on the cropped image
                    text = pytesseract.image_to_string(cropped_region)

                    # Save the OCR result to a file with the same name as the cropped image
                    with open(os.path.join(output_dir, f'cropped_{i}.txt'), 'w') as file:
                        file.write(text)
