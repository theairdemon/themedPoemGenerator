import random

class PoemClass:

    def __init__(self, theme):
        self.theme = theme

        self.noun_list = ["love", "nature", "flower", "time", "day", "light"]
        self.verb_list = ["love", "flower", "light"]

        self.noun_dict = {}
        self.verb_dict = {}

        # list out the themes as NOUNS and their assosciated synonyms
        self.noun_dict["love"] = ["love", "Romeo", "passion", "angel", "beau", "dearest", "beloved", "flame", "honey", "paramour", "spark", "sweetheart", "valentine"]
        self.noun_dict["nature"] = ["nature", "land", "world", "cosmos", "country", "forest", "sea", "universe"]
        self.noun_dict["flower"] = ["flower", "blossom", "bud", "rose", "daisy", "lilac", "lily"]
        self.noun_dict["time"] = ["time", "age", "date", "day", "night", "future", "era", "hour", "life", "moment", "season", "space", "year", "clock", "epoch", "eternity", "infinity", "tempo"]
        self.noun_dict["day"] = ["day", "light", "time", "sunshine", "night", "period", "age", "cycle", "epoch"]
        self.noun_dict["light"] = ["light", "candle", "day", "flash", "glare", "glow", "lamp", "lantern", "radiation", "star", "sun", "aurora", "beacon", "blaze", "brilliance", "dawn", "dusk", "flare", "gleam", "glimmer", "glint", "illumination", "luster", "morning", "shine", "sparkle", "spark"]

        # list out the themes as VERBS and their assosciated synonyms
        self.verb_dict["love"] = ["love", "admire", "cherish", "treasure", "deify", "venerate", "embrace", "adore"]
        self.verb_dict["flower"] = ["flower", "blossom", "prosper", "thrive", "bloom"]
        self.verb_dict["light"] = ["light", "brighten", "ignite", "kindle", "shine", "sparkle", "spark", "fire", "illuminate", "inflame", "ignite"]


    """
    Get Poem - the powerhouse of the class
        This is the part that actually generates the poem structure
    """
    def get_poem(self):
        num_lines = random.randint(4, 16)
        stanza_length = random.randint(4, 10)
        poem = ""

        for line in range(1, num_lines+1):
            # pick a NOUN
            if self.theme in self.noun_list:
                noun = random.choice(self.noun_dict[self.theme])
            else:
                noun_name = random.choice(self.noun_list)
                noun = random.choice(self.noun_dict[noun_name])

            # pick a VERB
            if self.theme in self.verb_list:
                verb = random.choice(self.verb_dict[self.theme])
            else:
                verb_name = random.choice(self.verb_list)
                verb = random.choice(self.verb_dict[verb_name])

            if line % stanza_length == 0:
                poem += "\n"
            poem += self.sentence_builder(noun, verb)

        return poem


    """
    Constructor for the sentence structure
    """
    def sentence_builder(self, noun, verb):
        rand_int = random.randint(1, 8)

        sentence = ""
        if rand_int == 1: sentence = "The " + noun + " " + verb + "s"
        elif rand_int == 2: sentence = "And so, the " + noun + " will " + verb
        elif rand_int == 3: sentence = "Now " + verb + ", " + noun
        elif rand_int == 4: sentence = "A " + noun
        elif rand_int == 5:
            if verb[len(verb) - 1] == "e":
                sentence = "Thus, the " + noun + " " + verb + "d"
            else: sentence = "Thus, the " + noun + " " + verb + "ed"
        elif rand_int == 6: sentence = "At long last, the " + noun + " " + verb + "s"
        elif rand_int == 7:
            new_int = random.randint(1, 2)
            if new_int == 1: place = "here"
            else: place = "there"
            if verb[len(verb) - 1] == "e":
                verb = verb[:(len(verb)-1)]
                sentence = "For " + place + " is the " + noun + ", " + verb + "ing"
            else:
                sentence = "For " + place + " is the " + noun + ", " + verb + "ing"
        else: sentence = "The " + noun + " " + verb + "s"

        sentence += "\n"
        return sentence


    def __str__(self):
        return self.get_poem()
