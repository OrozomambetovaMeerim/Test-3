# Что будет выведено на экран в результате исполнения следующего кода:

class English:

    def thank_you(self):

        print("Thank you")

 

 

class French(English):

    def thank_you(self):

        print("Merci")

 

 

class Italian(English):

    def thank_you(self):

        print("Grazie")

 

 

class German(Italian):

    def thank(self):

        print("Danke")

 

class NewLanguage(German, English):

    pass lang = NewLanguage() lang.thank_you()


# Thank you


# Merci


# Grazie


# Danke