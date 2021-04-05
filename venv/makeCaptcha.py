import string
import random

from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha

# captcha has only string
letters = string.ascii_letters
myStringCaptcha = ''.join(random.choice(letters) for i in range(10))

# captcha has only number
letters = string.digits
myNumCaptcha = ''.join(random.choice(letters) for i in range(10))

# captcha has string and num
def get_string(letters_count, digits_count):
    letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))
# convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits)
    random.shuffle(sample_list)
# convert list to string
    final_string = ''.join(sample_list)
    return final_string

myCaptcha = get_string(5, 5)

#gen Captcha
image = ImageCaptcha(width = 280, height = 90)
audio = AudioCaptcha()

data = image.generate(myCaptcha)
data = image.generate(myStringCaptcha)
data = image.generate(myNumCaptcha)
data = audio.generate(myNumCaptcha)

image.write(myCaptcha, 'demoCaptcha.png')
image.write(myStringCaptcha, 'demoStringCaptcha.png')
image.write(myNumCaptcha, 'demoNumCaptcha.png')
audio.write(myNumCaptcha, 'demoNumCaptcha.waw')
