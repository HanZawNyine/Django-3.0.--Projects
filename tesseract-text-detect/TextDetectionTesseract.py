import cv2
import pytesseract


class DetectImage:
    def __init__(self, image_path):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        self.img = cv2.imread(image_path)
        self.hImg, self.wImg, _ = self.img.shape

    ### detecting characters
    def text_characters(self):
        boxes = pytesseract.image_to_boxes(self.img)
        for b in boxes.splitlines():
            b = b.split(' ')
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(self.img, (x, self.hImg - y), (w, self.hImg - h), (0, 0, 255), 5)
            cv2.putText(self.img, b[0], (x, self.hImg - y+200), cv2.FONT_HERSHEY_SIMPLEX, 5, (50, 50, 255), 5)
        self.run()

    ###detecting words
    def text_words(self):
        boxes = pytesseract.image_to_data(self.img)
        for x, b in enumerate(boxes.splitlines()):
            if x != 0:
                b = b.split('\t')
                if len(b) == 12:
                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 0, 255), 1)
                    cv2.putText(self.img, b[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 5, (50, 50, 255), 5)
        self.run()

    def text_digits(self, config):
        boxes = pytesseract.image_to_data(self.img, config=config)
        for x, b in enumerate(boxes.splitlines()):
            if x != 0:
                b = b.split('\t')
                if len(b) == 12:
                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(self.img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 5, (50, 50, 255), 2)
        self.run()

    def text_string(self):
        return pytesseract.image_to_string(self.img)

    def text_boxes(self):
        return pytesseract.image_to_boxes(self.img)

    def run(self):
        img = cv2.resize(self.img, (980, 600))
        cv2.imshow('Result', img)
        cv2.waitKey(0)


if __name__ == '__main__':
    detect_img = DetectImage('img/letter-to-santa-claus.png')
    # print(detect_img.text_string())
    # print(detect_img.text_boxes())

    detect_img.text_characters()
    # detect_img.text_words()
    # detect_img.text_digits(r'--oem 3 --psm 6 outputbase digits')
