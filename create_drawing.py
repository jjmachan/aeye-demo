from aeye_lib import Aeye
from PIL import Image, ImageDraw, ImageFont

aeye = Aeye('http://35.225.149.37:5000')
def caption(img_path):
    img = open(img_path, 'rb')
    caption = aeye.caption(img)

    img = Image.open(img_path)
    img_draw = ImageDraw.Draw(img)
    h, w = img.size
    img_draw.text((h//3.4, w-20), caption, fill='white')

    # save
    newname = img_path.split('.')
    newname[0] += '_captioned'
    newname = '.'.join(newname)
    img.save(newname)
    print(f'{newname} saved!')


def object_dection(img_path):
    colors = {
            'chair': 'red',
            'pottedplant': 'green',
            'sofa': 'pink'
            }
    img = open(img_path, 'rb')
    boxes = aeye.objects(img)

    img = Image.open(img_path)
    img_draw = ImageDraw.Draw(img)
    for obj in boxes:
        color = colors[obj]
        print(obj)
        for box in boxes[obj]:
            print(box)
            img_draw.rectangle(box, outline=color)

    # save
    newname = img_path.split('.')
    newname[0] += '_objects_marked'
    newname = '.'.join(newname)
    img.save(newname)
    print(f'{newname} saved!')

def mark_faces(img_path):
    img = open(img_path, 'rb')
    boxes = aeye.faces(img)

    img = Image.open(img_path)
    img_draw = ImageDraw.Draw(img)
    for box in boxes:
        print(box)
        img_draw.rectangle(box, outline='white')

    # save
    newname = img_path.split('.')
    newname[0] += '_faces_marked'
    newname = '.'.join(newname)
    img.save(newname)
    print(f'{newname} saved!')

def who_is_this(img_path):
    img = open(img_path, 'rb')
    name = aeye.whos_this(img)
    img = open(img_path, 'rb')
    boxes = aeye.faces(img)

    img = Image.open(img_path)
    img_draw = ImageDraw.Draw(img)
    for box in boxes:
        img_draw.rectangle(box, outline='white')
        xy = box[2:]
        img_draw.text(xy, name)

    # save
    newname = img_path.split('.')
    newname[0] += '_face_identified'
    newname = '.'.join(newname)
    img.save(newname)
    print(f'{newname} saved!')

if __name__ == '__main__':

    # Captioning the football image
    print('Generating captions...')
    football_img = 'demo/football.jpeg'
    caption(football_img)

    # Drawing bounding boxes in an indoor setting.
    print('detecting objects ...')
    indoor_img = 'demo/livingroom.jpg'
    object_dection(indoor_img)

    # face detection
    print('detecting faces ...')
    people_img = 'demo/people.jpg'
    mark_faces(people_img)

    # Face recognition
    print('recognising faces ...')
    disha_img = 'demo/disha.jpg'
    who_is_this(disha_img)
