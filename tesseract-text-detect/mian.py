from TextDetectionTesseract import DetectImage

if __name__ == '__main__':
    detect_img = DetectImage('img/number-text.jpg')
    # print(detect_img.text_string())
    # print(detect_img.text_boxes())
    detect_img.text_characters()
    # detect_img.text_words()
    # detect_img.text_digits(r'--oem 3 --psm 6 outputbase digits')
