import cv2
from PIL import Image


import random
active = True

#img= cv2.imread("./outfits/skirt.png")
#img=img.convert('RGB')
#img = Image.fromarray(img, 'RGB')
#img.show()

# import urllib.request
# u = urllib.request.urlopen("https://us.shein.com/ROMWE-Goth-Solid-Lace-Up-Shirred-Cami-Dress-p-9765265-cat-1727.html?src_identifier=st%3D2%60sc%3Dgoth%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_goods_detail1659469818111&mallCode=1&scici=Search~~EditSearch~~1~~goth~~~~0
# ")

class Outfit:
    def __init__(self, name, description, link, photo, photo2):
        self.name = name
        self.description = description
        self.link = link
        self.photo = photo
        self.photo2 = photo2
        self.option = []
        self.score = 0
    

    def scores(self, question):
       
        if question[0] == self.option[0]:
            self.score += 1
        if question[1] == self.option[1]:
            self.score += 1
        if question[2] == self.option[2]:
            self.score += 1
        if question[3] == self.option[3]:
            self.score += 1
        if question[4] == self.option[4]:
            self.score += 1
        if question[5] == self.option[5]:
            self.score += 1
        if question[6] == self.option[6]:
            self.score += 1
        if question[7] == self.option[7]:
            self.score += 1
        if question[8] == self.option[8]:
            self.score += 1
        if question[9] == self.option[9]:
            self.score += 1

        return self.score
        




outfit_1 = Outfit("Casual Outfit + 'Normal' Aesthetic", " Normal fashion is described as unpretentious and average-looking clothing.\n I think this graphic tee with these jeans would be a great fit for you and your style!\n If the tee selected is not your style, there are other options for the graphic listed on the site.", "https://www2.hm.com/en_us/productpage.1002471021.html AND https://www.forever21.com/us/2000456655.html?dwvar_2000456655_color=01&dwvar_2000456655_size=2&quantity=1", "./outfits/jeans.png", "./outfits/shortshirt.png")
outfit_1.option = ["peaceful", "pop", "stay inside", "neutral", "blend in", "forever 21", "3", "1", "3", "1"]

outfit_2 = Outfit("Black Dress + 'Goth' Aesthetic", "Goth fashion is a style that is marked by dark, mysterious, and homogenous features.\n I think this black dress would look amazing on you!", "https://us.shein.com/ROMWE-Goth-Solid-Lace-Up-Shirred-Cami-Dress-p-9765265-cat-1727.html?src_identifier=st%3D2%60sc%3Dgoth%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_goods_detail1659469818111&mallCode=1&scici=Search~~EditSearch~~1~~goth~~~~0", "./outfits/dress2.png", "")
outfit_2.option= ["expressive", "rock", "go out", "neutral", "stand out", "hot topic", "1", "3", "2", "3"]

outfit_3 = Outfit("Argyle Set + 'Soft' Aesthetic", "A style that includes many pastel colors, maximalist accessories, and an overall 'cutesy' look.\n This tennis skirt and argyle vest with a button up to go below it would look great on you!", "https://us.shein.com/SHEIN-Teen-Girls-Argyle-Print-Tank-Top-And-Pleated-Skirt-Set-p-9708356-cat-2016.html?src_identifier=st%3D2%60sc%3Dsoft%20girl%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_search1659635902333&mallCode=1&scici=Search~~EditSearch~~1~~soft_20girl~~~~0 AND https://www.forever21.com/us/2000454077.html?dwvar_2000454077_color=01&quantity=1", "./outfits/skirt.png", "./outfits/shirt.png")
outfit_3.option = ["vibrant", "lofi", "neutral", "cool", "neutral", "forever 21", "3", "3", "1", "2"]



#def prompt_user():
print("                             WELCOME!\n I am the Fashion Bot and I will help you make an outfit your choices to this quiz. Answer the following 10 questions honestly and I will generate an outfit I think you will look great in + let you know which style would suit you most!\n")

question_1 = input(" Which of these words best describe you? (adventorous, peaceful, vibrant, creative, intelligant, or expressive): ")

question_2 = input(" What is your typical music taste? (pop, rock, indie, lofi, country): ")

question_3 = input(" What do you like to do on a Saturday? (stay inside, go out, neutral): ")

question_4 = input(" What color do you typically lean towards in your outfits? NOTE: Warm- reds, yellows, and oranges. Cool- blues, purples, and greens. Neutrals- whites, blacks, and greys.\n (warm, cool, neutral): ")

question_5 = input(" Do you prefer to blend in, stand out, or are you neutral? (blend in, stand out, neutral): ")

question_6 = input(" What store do you typically shop at? (forever 21, hot topic, zara): ")

question_7 = input(" Rate dresses from 1-3. 1-Hate, 2- Neutral, 3-Love. (1, 2, 3): ")

question_8 = input(" Rate jeans from 1-3. 1-Hate, 2- Neutral, 3-Love. (1, 2, 3): ")

question_9 = input(" Rate cropped shirts from 1-3. 1-Hate, 2- Neutral, 3-Love. (1, 2, 3): ")

question_10 = input("Rate graphic tees/ t-shirts from 1-3. 1-Hate, 2- Neutral, 3-Love. (1, 2, 3): ")

responses = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]

outfit_1.scores(responses)
outfit_2.scores(responses)
outfit_3.scores(responses)

score_list = [outfit_1.score, outfit_2.score, outfit_3.score]

score_list.sort()
if score_list[0] == outfit_1.score:
    print(f"The FASHION BOT suggests this outfit:\n{outfit_1.name}.\n.{outfit_1.description}.\nHere is the link(s):\n{outfit_1.link}.")
    img= cv2.imread(outfit_1.photo)
    img = Image.fromarray(img, 'RGB')
    print(img.show())
    img= cv2.imread(outfit_1.photo2)
    img = Image.fromarray(img, 'RGB')
    print(img.show())

elif score_list[0] == outfit_2.score:
    print(f"The FASHION BOT suggests this outfit:\{outfit_2.name}.\n {outfit_2.description}.\nHere is the link(s):\n{outfit_2.link}.")
    img= cv2.imread(outfit_2.photo)
    img = Image.fromarray(img, 'RGB')
    print(img.show())
    img= cv2.imread(outfit_2.photo2)
    img = Image.fromarray(img, 'RGB')
    print(img.show())

elif score_list[0] == outfit_3.score:
    print(f"The FASHION BOT suggests this outfit:\n {outfit_3.name}. {outfit_3.description}. Here is the link(s){outfit_3.link}.")
    img= cv2.imread(outfit_3.photo)
    img = Image.fromarray(img, 'RGB')
    print(img.show())
    img= cv2.imread(outfit_3.photo2)
    img = Image.fromarray(img, 'RGB')
    print(img.show())

elif score_list[0] == score_list[1]:
    random_choice = random.choice(outfit_1, outfit_2, outfit_3)
    print(random_choice)

else:
    print("No outfit match")




