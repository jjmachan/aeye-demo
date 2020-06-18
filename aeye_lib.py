import requests
import json

class Aeye():
    def __init__(self, base_url):
        self.base_url = base_url
        r = requests.get(base_url)
        if r.status_code==200:
            print('Connected to service')
        else:
            print(f'Connection down! Check the url provided ({base_url})')

    def caption(self, img):
        url = self.base_url+'/captioning'
        r = requests.post(url, data=img)

        # remove the <start> and <end> token.
        str = r.text.split(' ')[1:-1]

        # return the final str
        return ' '.join(str)

    def objects(self, img):
        url = self.base_url+'/detection'
        r = requests.post(url, data=img)

        objects_detected = json.loads(r.json())
        return objects_detected

    def whos_this(self, img, threshold=0.5):
        url = self.base_url+'/face_recognition'
        r  = requests.post(url, data=img)

        person = r.json()
        name, confidence = person

        if confidence > threshold:
            return name
        return None

    def faces(self, img):
        url = self.base_url+'/get_faces'
        r  = requests.post(url, data=img)

        boxes, probs = json.loads(r.json())
        return boxes

if __name__ == '__main__':
    aeye = Aeye('http://35.225.149.37:5000')
    img = open('./test-images/people1.jpg', 'rb')
    name = aeye.faces(img)
    print(name)
