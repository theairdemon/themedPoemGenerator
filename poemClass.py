import random

class PoemClass:

    def __init__(self, theme):
        self.theme = theme

        self.noun_list = ["love", "nature", "flower", "time", "day", "light"]
        self.verb_list = ["love", "flower", "light", "generic"]

        self.noun_dict = {}
        self.verb_dict = {}

        # list out the themes as NOUNS and their assosciated synonyms
        self.noun_dict["love"] = ["love", "lover", "romance", "passion", "angel", "dearest", "beloved", "flame", "paramour", "spark", "sweetheart", "valentine", "husband", "wife", "beauty", "dear"]
        self.noun_dict["nature"] = ["nature", "land", "world", "cosmos", "country", "forest", "sea", "universe"]
        self.noun_dict["flower"] = ["flower", "blossom", "bud", "rose", "daisy", "lilac", "lily", "iris", "wildflower", "daffodil", "orchid"]
        self.noun_dict["time"] = ["time", "age", "date", "day", "night", "future", "era", "hour", "life", "moment", "season", "space", "year", "clock", "epoch", "eternity", "infinity", "tempo"]
        self.noun_dict["day"] = ["day", "light", "time", "sunshine", "night", "period", "age", "cycle", "epoch"]
        self.noun_dict["light"] = ["light", "candle", "day", "flash", "glare", "glow", "lamp", "lantern", "radiation", "star", "sun", "aurora", "beacon", "blaze", "brilliance", "dawn", "dusk", "flare", "gleam", "glimmer", "glint", "illumination", "luster", "morning", "shine", "sparkle", "spark"]

        # list out the themes as VERBS and their associated synonyms
        self.verb_dict["love"] = ["love", "admire", "cherish", "treasure", "deify", "venerate", "embrace", "adore", "promise"]
        self.verb_dict["flower"] = ["flower", "blossom", "prosper", "thrive", "bloom"]
        self.verb_dict["light"] = ["light", "brighten", "ignite", "kindle", "shine", "sparkle", "fire", "illuminate", "inflame", "ignite"]
        self.verb_dict["generic"] = ["run", "escape", "venture", "explore", "discover", "reveal", "walk", "behold", "dwell"]


    """
    Get Poem - the powerhouse of the class
        This is the part that actually generates the poem structure
    """
    def get_poem(self):
        num_lines = random.randint(4, 20)
        stanza_length = int(random.randint(4, 8) / 2) * 2
        poem = ""

        for line in range(1, num_lines+1):
            # pick a NOUN if the noun is in the dictionary
            if self.theme in self.noun_list:
                # random chance number
                rand_num_noun = random.randint(1, 4)
                # 1 in 4 chance of using an unrelated noun
                if rand_num_noun == 4:
                    noun_name = random.choice(self.noun_list)
                    noun = random.choice(self.noun_dict[noun_name])
                # most of the time, pick a related noun
                else: noun = random.choice(self.noun_dict[self.theme])
            # if noun not in dictionary, pick random noun
            else:
                noun_name = random.choice(self.noun_list)
                noun = random.choice(self.noun_dict[noun_name])

            # pick a VERB
            if self.theme in self.verb_list:
                # random chance number
                rand_verb_num = random.randint(1, 4)
                # 1 in 4 chance of using an unrelated verb
                if rand_verb_num == 4:
                    verb_name = random.choice(self.verb_list)
                    verb = random.choice(self.verb_dict[verb_name])
                # most of the time, pick a related verb
                else: verb = random.choice(self.verb_dict[self.theme])
            # if verb not in dictionary, pick random verb
            else:
                verb_name = random.choice(self.verb_list)
                verb = random.choice(self.verb_dict[verb_name])

            poem += self.sentence_builder(noun, verb)
            if line % stanza_length == 0:
                poem += "\n"

        return poem


    """
    Sentence builder - constructor for the sentence structure
        Very important to maintain diversity here, since the poem needs variance
        in cadence and rhythm
    """
    def sentence_builder(self, noun, verb):
        rand_int = random.randint(1, 9)

        sentence = ""
        if rand_int == 1:
            new_int = random.randint(1, 2)
            if new_int == 1: conj = "The "
            else: conj = "A "

            if verb[len(verb) - 1] == "y":
                verb = verb[:(len(verb)-1)]
                sentence = conj + noun + " " + verb + "s"
            else: sentence = conj + noun + " " + verb + "s"
        elif rand_int == 2: sentence = "And so, the " + noun + " will " + verb
        elif rand_int == 3: sentence = "Now " + verb + ", " + noun
        elif rand_int == 4:
            new_int = random.randint(1, 2)
            if new_int == 1: conj = "The "
            else: conj = "A "

            sentence = conj + noun
        elif rand_int == 5:
            new_int = random.randint(1, 2)
            if new_int == 1: conj = "The "
            else: conj = "A "

            if verb[len(verb) - 1] == "e": sentence = conj + noun + " " + verb + "d"
            elif verb[len(verb) - 1] == "y":
                verb = verb[:(len(verb)-1)]
                sentence = conj + noun + " " + verb + "ied"
            else: sentence = conj + noun + " " + verb + "ed"
        elif rand_int == 6:
            if verb[len(verb) - 1] == "y":
                    verb = verb[:(len(verb)-1)]
                    sentence = "At long last, the " + noun + " " + verb + "ies"
            else: sentence = "At long last, the " + noun + " " + verb + "s"
        elif rand_int == 7:
            new_rand_int = random.randint(1, 2)
            if new_rand_int == 1: conj = "the "
            else: conj = "a "

            new_int = random.randint(1, 2)
            if new_int == 1: place = "here"
            else: place = "there"

            if verb[len(verb) - 1] == "e":
                verb = verb[:(len(verb)-1)]
                sentence = "For " + place + " is " + conj  + noun + ", " + verb + "ing"
            else: sentence = "For " + place + " is " + conj + noun + ", " + verb + "ing"
        elif rand_int == 7:
            new_int = random.randint(1, 2)
            if new_int == 1: conj = "the "
            else: conj = "a "

            if verb[len(verb) - 1] == "e": sentence = "And " + conj + noun + " " + verb + "d"
            elif verb[len(verb) - 1] == "y":
                verb = verb[:(len(verb)-1)]
                sentence = "And " + conj + noun + " " + verb + "ied"
            else: sentence = "And " + conj + noun + " " + verb + "ed"
        else:
            new_int = random.randint(1, 2)
            if new_int == 1: conj = "The "
            else: conj = "A "

            if verb[len(verb) - 1] == "y":
                verb = verb[:(len(verb)-1)]
                sentence = conj + noun + " " + verb + "ies"
            else: sentence = conj + noun + " " + verb + "s"

        sentence += "\n"
        return sentence


    def __str__(self):
        return self.get_poem()
