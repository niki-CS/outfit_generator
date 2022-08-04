print("WELCOME!\nI am the Fashion Bot and I will help you make an outfit based on your closest style type. Answer the following 15 questions honestly and I will generate an outfit I think you will look great in!")

question_1 = input("Which of these words best describe you? (adventorous, peaceful, vibrant, creative, intelligant, or expressive): ")
question_2 = input("What is your typical music taste? (pop, rock/alternative, indie, lofi, country): ")
question_3 = input("What do you like to do on a Saturday? (stay inside, go out, neutral): ")

class Outfit:
    def __init__(self, name, description, link, option_1, option_2, option_3):
        self.name = name
        self.description = description
        self.link = link
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3


outfit_1 = Outfit("Casual Outfit", "", "https://www2.hm.com/en_us/productpage.1002471021.html", "peaceful", "pop", "stay inside")
outfit_2 = Outfit("Black Dress", "", "https://us.shein.com/ROMWE-Goth-Solid-Lace-Up-Shirred-Cami-Dress-p-9765265-cat-1727.html?src_identifier=st%3D2%60sc%3Dgoth%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_goods_detail1659469818111&mallCode=1&scici=Search~~EditSearch~~1~~goth~~~~0", "expressive", "rock", "go out")
outfit_3 = Outfit("Argyle Set", "", "https://us.shein.com/SHEIN-Teen-Girls-Argyle-Print-Tank-Top-And-Pleated-Skirt-Set-p-9708356-cat-2016.html?src_identifier=st%3D2%60sc%3Dsoft%20girl%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_search1659635902333&mallCode=1&scici=Search~~EditSearch~~1~~soft_20girl~~~~0", "vibrant", "lofi", "neutral")


# cottagecore= {
#     "outfit_1": "--"
#     "outfit_2": "--"
# }

# indie= {
    
# }

# Cottagecore = Results("Cottagecore", "An aesthetic or style characterized by old-fashioned rural lifestyle.", [])
# Indie = Results("Indie", "An aesthetic or style characterized retro, vintage, and hipster clothing.", [])
# Goth = Results("Goth", "Goth fashion is a style that is marked by dark, mysterious, and homogenous features.", [])
# Normal = Results("Normal", "Normal fashion is described as unpretentious and average-looking clothing.", [])
# Academia = Results("Academia", "Academia fashion is influenced by learning, reading, and writing but with a gothic edge. Think cardigans, tweed pants, and trench coats.", [])
# Soft = Results("Soft", "A style that includes many pastel colors, maximalist accessories, and an overall 'cutesy' look.", [])
# Artsy = Results("Artsy", "A style that includes stripes, loose trousers, and oversized tees. Think graphic tees and corduroy.", [])

