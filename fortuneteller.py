import random
from enum import Enum, unique
from typing import List

def magicConchShell():

    answer = random.randint(1,8)

    match answer:
        case 1:
            return "Maybe someday."
        case 2:
            return "I don't think so."
        case 3:
            return "Yes"
        case 4:
            return "Try asking again."
        case 5:
            return "Nooooooooo!"
        case _:
            return "No"

@unique
class Decks(Enum):
    def __new__(cls, shortname, label, longname, global_d = True):
        obj = object.__new__(cls)
        obj._value_ = shortname
        obj.shortname = shortname
        obj.label = label
        obj.longname = longname
        if global_d:
            cls.global_decks = cls.__dict__.get('global_decks', [])
            cls.global_decks.append(obj)
        return obj

    DEFAULT = ("default", "Default", "Default cards")
    SWISS = ("swiss", "Swiss", "IJJ Swiss cards")

@unique
class MajorMinor(Enum):
    MAJOR_ONLY = "major"
    MINOR_ONLY = "minor"
    BOTH = "both"

class Card:
    """A class used to represent a tarot card.
    Attributes:
        name: The name of the card
        upright: Three-word description of a card's upright meaning
        reversed: Three-word description of a card's reversed meaning
        code: A short string representing the card's suit and rank
        up: True if a card is upright, False if inverted
    """

    def __init__(self, name: str, upright: str,
                 reverse: str, code: str, up=True):
        self.name = name
        self.upright = upright
        self.reverse = reverse
        self.code = code
        self.up = True

    def description(self) -> str:
        """Returns the card name and its meaning, depending on its orientation.
        Example:
            King of Cups (upright): compassion, control, balance
        """
        if (self.up):
            descr = self.name + " (upright): " + self.upright
        else:
            descr = self.name + " (reversed): " + self.reverse
        return descr

    def get_name(self) -> str:
        return "{} ({})".format(self.name, "upright" if self.up else "reversed")

    def get_desc(self) -> str:
        if self.up:
            return self.upright
        else:
            return self.reverse

def make_deck(majorminor: MajorMinor) -> List[Card]:
    """Returns a full deck of tarot cards."""
    major = [
        Card("The World",
             "fulfillment, harmony, completion",
             "incompletion, no closure", "21M"),
        Card("Judgement",
             "reflection, reckoning, awakening",
             "lack of self awareness, doubt, self loathing", "20M"),
        Card("The Sun",
             "joy, success, celebration, positivity",
             "negativity, depression, sadness", "19M"),
        Card("The Moon",
             "unconscious, illusions, intuition",
             "confusion, fear, misinterpretation", "18M"),
        Card("The Star",
             "hope, faith, rejuvenation",
             "faithlessness, discouragement, insecurity", "17M"),
        Card("The Tower",
             "sudden upheaval, broken pride, disaster",
             "disaster avoided, delayed disaster, fear of suffering", "16M"),
        Card("The Devil",
             "addiction, materialism, playfulness",
             "freedom, release, restoring control", "15M"),
        Card("Temperance",
             "middle path, patience, finding meaning",
             "extremes, excess, lack of balance", "14M"),
        Card("Death",
             "end of cycle, beginnings, change, metamorphosis",
             "fear of change, holding on, stagnation, decay", "13M"),
        Card("The Hanged Man",
             "sacrifice, release, martyrdom",
             "stalling, needless sacrifice, fear of sacrifice", "12M"),
        Card("Justice",
             "cause and effect, clarity, truth",
             "dishonesty, unaccountability, unfairness", "11M"),
        Card("The Wheel of Fortune",
             "change, cycles, inevitable fate",
             "no control, clinging to control, bad luck", "10M"),
        Card("The Hermit",
             "contemplation, search for truth, inner guidance",
             "loneliness, isolation, lost your way", "9M"),
        Card("Strength",
             "inner strength, bravery, compassion, focus",
             "self doubt, weakness, insecurity", "8M"),
        Card("The Chariot",
             "direction, control, willpower",
             "lack of control, lack of direction, aggression", "7M"),
        Card("The Lovers",
             "partnerships, duality, union",
             "loss of balance, one-sidedness, disharmony", "6M"),
        Card("The Hierophant",
             "tradition, conformity, morality, ethics",
             "rebellion, subversiveness, new approaches", "5M"),
        Card("The Emperor",
             "authority, structure, control, fatherhood",
             "tyranny, rigidity, coldness", "4M"),
        Card("The Empress",
             "motherhood, fertility, nature",
             "dependence, smothering, emptiness, nosiness", "3M"),
        Card("The High Priestess",
             "intuitive, unconscious, inner voice",
             "lack of center, lost inner voice, repressed feelings", "2M"),
        Card("The Magician",
             "willpower, desire, creation, manifestation",
             "trickery, illusions, out of touch", "1M"),
        Card("The Fool",
             "innocence, new beginnings, free spirit",
             "recklessness, taken advantage of, inconsideration", "0M")
    ]
    minor = [
        Card("Seven of Wands",
             "perseverance, defensive, maintaining control",
             "give up, destroyed confidence, overwhelmed", "7W"),
        Card("Four of Wands",
             "community, home, celebration",
             "lack of support, transience, home conflicts", "4W"),
        Card("Ace of Wands",
             "creation, willpower, inspiration, desire",
             "lack of energy, lack of passion, boredom", "AW"),
        Card("Ten of Wands",
             "accomplishment, responsibility, burden",
             "inability to delegate, overstressed, burnt out", "10W"),
        Card("Nine of Wands",
             "resilience, grit, last stand",
             "exhaustion, fatigue, questioning motivations", "9W"),
        Card("Eight of Wands",
             "rapid action, movement, quick decisions",
             "panic, waiting, slowdown", "8W"),
        Card("Six of Wands",
             "victory, success, public reward",
             "excess pride, lack of recognition, punishment", "6W"),
        Card("Five of Wands",
             "competition, rivalry, conflict",
             "avoiding conflict, respecting differences", "5W"),
        Card("Three of Wands",
             "looking ahead, expansion, rapid growth",
             "obstacles, delays, frustration", "3W"),
        Card("Two of Wands",
             "planning, making decisions, leaving home",
             "fear of change, playing safe, bad planning", "2W"),
        Card("Page of Wands",
             "exploration, excitement, freedom",
             "lack of direction, procrastination, creating conflict", "PW"),
        Card("Queen of Wands",
             "courage, determination, joy",
             "selfishness, jealousy, insecurities", "QW"),
        Card("King of Wands",
             "big picture, leader, overcoming challenges",
             "impulsive, overbearing, unachievable expectations", "KW"),
        Card("Knight of Wands",
             "action, adventure, fearlessness",
             "anger, impulsiveness, recklessness", "KNW"),
        Card("King of Cups",
             "compassion, control, balance",
             "coldness, moodiness, bad advice", "KC"),
        Card("Queen of Cups",
             "compassion, calm, comfort",
             "martyrdom, insecurity, dependence", "QC"),
        Card("Knight of Cups",
             "following the heart, idealist, romantic",
             "moodiness, disappointment", "KNC"),
        Card("Page of Cups",
             "happy surprise, dreamer, sensitivity",
             "emotional immaturity, insecurity, disappointment", "PC"),
        Card("Ten of Cups",
             "inner happiness, fulfillment, dreams coming true",
             "shattered dreams, broken family, domestic disharmony", "10C"),
        Card("Nine of Cups",
             "satisfaction, emotional stability, luxury",
             "lack of inner joy, smugness, dissatisfaction", "9C"),
        Card("Eight of Cups",
             "walking away, disillusionment, leaving behind",
             "avoidance, fear of change, fear of loss", "8C"),
        Card("Seven of Cups",
             "searching for purpose, choices, daydreaming",
             "lack of purpose, diversion, confusion", "7C"),
        Card("Six of Cups",
             "familiarity, happy memories, healing",
             "moving forward, leaving home, independence", "6C"),
        Card("Five of Cups",
             "loss, grief, self-pity",
             "acceptance, moving on, finding peace", "5C"),
        Card("Four of Cups",
             "apathy, contemplation, disconnectedness",
             "sudden awareness, choosing happiness, acceptance", "4C"),
        Card("Three of Cups",
             "friendship, community, happiness",
             "overindulgence, gossip, isolation", "3C"),
        Card("Two of Cups",
             "unity, partnership, connection",
             "imbalance, broken communication, tension", "2C"),
        Card("Ace of Cups",
             "new feelings, spirituality, intuition",
             "emotional loss, blocked creativity, emptiness", "AC"),
        Card("King of Swords",
             "head over heart, discipline, truth",
             "manipulative, cruel, weakness", "KS"),
        Card("Knight of Swords",
             "action, impulsiveness, defending beliefs",
        "no direction, disregard for consequences, unpredictability", "KNS"),
        Card("Queen of Swords",
             "complexity, perceptiveness, clear mindedness",
             "cold hearted, cruel, bitterness", "QS"),
        Card("Page of Swords",
             "curiosity, restlessness, mental energy",
             "deception, manipulation, all talk", "PS"),
        Card("Ten of Swords",
             "failure, collapse, defeat",
             "can't get worse, only upwards, inevitable end", "10S"),
        Card("Nine of Swords",
             "anxiety, hopelessness, trauma",
             "hope, reaching out, despair", "9S"),
        Card("Eight of Swords",
             "imprisonment, entrapment, self-victimization",
             "self acceptance, new perspective, freedom", "8S"),
        Card("Seven of Swords",
             "deception, trickery, tactics and strategy",
             "coming clean, rethinking approach, deception", "7S"),
        Card("Six of Swords",
             "transition, leaving behind, moving on",
             "emotional baggage, unresolved issues, resisting transition", "6S"),
        Card("Five of Swords",
             "unbridled ambition, win at all costs, sneakiness",
             "lingering resentment, desire to reconcile, forgiveness", "5S"),
        Card("Three of Swords",
             "heartbreak, suffering, grief",
             "recovery, forgiveness, moving on", "3S"),
        Card("Four of Swords",
             "rest, restoration, contemplation",
             "restlessness, burnout, stress", "4S"),
        Card("Two of Swords",
             "difficult choices, indecision, stalemate",
             "lesser of two evils, no right choice, confusion", "2S"),
        Card("Ace of Swords",
             "breakthrough, clarity, sharp mind",
             "confusion, brutality, chaos", "AS"),
        Card("King of Pentacles",
             "abundance, prosperity, security",
             "greed, indulgence, sensuality", "KP"),
        Card("Queen of Pentacles",
             "practicality, creature comforts, financial security",
             "self-centeredness, jealousy, smothering", "QP"),
        Card("Knight of Pentacles",
             "efficiency, hard work, responsibility",
             "laziness, obsessiveness, work without reward", "KNP"),
        Card("Page of Pentacles",
             "ambition, desire, diligence",
             "lack of commitment, greediness, laziness", "PP"),
        Card("Ten of Pentacles",
             "legacy, culmination, inheritance",
             "fleeting success, lack of stability, lack of resources", "10P"),
        Card("Nine of Pentacles",
             "fruits of labor, rewards, luxury",
             "reckless spending, living beyond means, false success", "9P"),
        Card("Eight of Pentacles",
             "apprenticeship, passion, high standards",
             "lack of passion, uninspired, no motivation", "8P"),
        Card("Seven of Pentacles",
             "hard work, perseverance, diligence",
             "work without results, distractions, lack of rewards", "7P"),
        Card("Six of Pentacles",
             "charity, generosity, sharing",
             "strings attached, stinginess, power and domination", "6P"),
        Card("Five of Pentacles",
             "need, poverty, insecurity",
             "recovery, charity, improvement", "5P"),
        Card("Four of Pentacles",
             "conservation, frugality, security",
             "greediness, stinginess, possessiveness", "4P"),
        Card("Three of Pentacles",
             "teamwork, collaboration, building",
             "lack of teamwork, disorganized, group conflict", "3P"),
        Card("Two of Pentacles",
             "balancing decisions, priorities, adapting to change",
             "loss of balance, disorganized, overwhelmed", "2P"),
        Card("Ace of Pentacles",
             "opportunity, prosperity, new venture",
             "lost opportunity, missed chance, bad investment", "AP")
        ]
    if majorminor == MajorMinor.MAJOR_ONLY:
        return major
    elif majorminor == MajorMinor.MINOR_ONLY:
        return minor
    else:
        return major + minor

def draw(n: int, invert=True, majorminor: MajorMinor = MajorMinor.BOTH) -> List[Card]:
    """Returns a list of n random cards from a full deck of cards.
        Args:
            n: the number of cards to draw
            invert: If True, cards have a 1/5 chance of being inverted.
                    Otherwise, no cards will be inverted.
            major_only: If True, only major arcana cards will be drawn
            minor_only: If True, only minor arcana cards will be drawn
    """
    deck = make_deck(majorminor)
    hand = []
    for i in range(n):
        mycard = deck[random.randrange(len(deck))]
        if invert and (random.randrange(5) == 0):
            mycard.up = False
        deck.remove(mycard)
        hand.append(mycard)
    return hand

def cardtxt(cards: List[Card]):
    """Returns a list of tuples containing descriptions of a list of cards."""
    return list(map(lambda card: (card.get_name(), card.get_desc()), cards))

fortunes =[
     'A day for firm decisions!!!!!  Or is it?', 
     'A few hours grace before the madness begins again.', 
     'A gift of a flower will soon be made to you.', 
     'A long-forgotten loved one will appear soon.', 
     'Buy the negatives at any price.', 
     'A tall, dark stranger will have more fun than you.', 
     'A visit to a fresh place will bring strange work.', 
     'A visit to a strange place will bring fresh work.', 
     'Abandon the search for Truth; settle for a good fantasy.', 
     'After your lover has gone you will still have PEANUT BUTTER!', 
     'Afternoon very favorable for romance. Try a single person for a change.', 
     'Alimony and bribes will engage a large share of your wealth.', 
     'All the troubles you have will pass away very quickly.', 
     'Among the lucky, you are the chosen one.', 
     'An exotic journey in downtown Newark is in your future.', 
     'Another good night not to sleep in a eucalyptus tree.', 
     'Artistic ventures highlighted. Rob a museum.', 
     'Avoid gunfire in the bathroom tonight.', 
     'Avoid reality at all costs.', 
     'Bank error in your favor. Collect $200.', 
     'Be careful! Is it classified?', 
     'Be cautious in your daily affairs.', 
     'Be different: conform.', 
     "Be free and open and breezy! Enjoy! Things won't get any better so get used to it.", 
     'Be security conscious -- National defense is at stake.', 
     'Beware of a dark-haired man with a loud tie.', 
     'Beware of a tall blond man with one black shoe.', 
     'Beware of Bigfoot!', 
     'Beware of low-flying butterflies.', 
     'Beware the one behind you.', 
     'Bridge ahead. Pay troll.', 
     'Caution: breathing may be hazardous to your health.', 
     'Caution: Keep out of reach of children.', 
     'Chess tonight.', 
     'Day of inquiry.  You will be subpoenaed.', 
     'Do not sleep in a eucalyptus tree tonight.', 
     'Do nothing unless you must, and when you must act -- hesitate.', 
     "Don't feed the bats tonight.", 
     "Don't get to bragging.", 
     "Don't go surfing in South Dakota for a while.", 
     "Don't kiss an elephant on the lips today.", 
     "Don't look back, the lemmings are gaining on you.", 
     "Don't look now, but the man in the moon is laughing at you.", 
     "Don't plan any hasty moves. You'll be evicted soon anyway.", 
     "Don't read any sky-writing for the next two weeks.", 
     "Don't tell any big lies today. Small ones can be just as effective.", 
     'Everything will be just tickety-boo today.', 
     'Excellent day for putting Slinkies on an escalator.', 
     'Exercise caution in your daily affairs.', 
     'Expect a letter from a friend who will ask a favor of you.', 
     "Expect the worst, it's the least you can do.", 
     'Fine day for friends. So-so day for you.', 
     'Fine day to work off excess energy. Steal something heavy.', 
     'Fortune: You will be attacked next Wednesday at 3:15 p.m. by six samurai sword wielding purple fish glued to Harley-Davidson motorcycles.', 
     'Future looks spotty. You will spill soup in late evening.', 
     'Generosity and perfection are your everlasting goals.', 
     'Give him an evasive answer.', 
     'Give thought to your reputation. Consider changing name and moving to a new town.', 
     "Give your very best today. Heaven knows it's little enough.", 
     'Go to a movie tonight. Darkness becomes you.', 
     'Good day for a change of scene. Repaper the bedroom wall.', 
     'Good day for overcoming obstacles. Try a steeplechase.', 
     'Good news from afar can bring you a welcome visitor.', 
     'Good news. Ten weeks from Friday will be a pretty good day.', 
     'Green light in A.M. for new projects. Red light in P.M. for traffic tickets.', 
     'It may or may not be worthwhile, but it still has to be done.', 
     'Just because the message may never be received does not mean it isnot worth sending.', 
     'Lady Luck brings added income today.', 
     'Let me put it this way: today is going to be a learning experience.', 
     'Long life is in store for you.', 
     'Love is in the offing. Be affectionate to one who adores you.', 
     'Many changes of mind and mood; do not hesitate too long.', 
     'Next Friday will not be your lucky day.', 
     'Perfect day for scrubbing the floor and other exciting things.', 
     'Questionable day.', 'Ask somebody something.', 
     'Reply hazy, ask again later.', 
     'Save energy: be apathetic.', 
     'Ships are safe in harbor, but they were never meant to stay there.', 
     'Slow day. Practice crawling.', 
     'Snow Day -- stay home.', 
     'Someone whom you reject today, will reject you tomorrow.', 
     'Stay away from flying saucers today.', 
     'Stay away from hurricanes for a while.', 
     'Stay the curse.', 
     "That secret you've been guarding, isn't.", 
     'The time is right to make new friends.', 
     'There will be big changes for you, but you will be happy.', 
     'This will be a memorable month -- no matter how hard you try to forget it.', 
     'Time to be aggressive. Go after a tattooed Virgo.', 
     'Today is the first day of the rest of the mess.', 
     'Today is the first day of the rest of your life.', 
     'Today is the last day of your life so far.', 
     'Today is the tomorrow you worried about yesterday.', 
     'Today is what happened to yesterday.', 
     'Tomorrow will be cancelled due to lack of interest.', 
     'Tomorrow, this will be part of the unchangeable past but fortunately, it can still be changed today.', 
     'Tomorrow, you can be anywhere.', 
     "Tonight you will pay the wages of sin; Don't forget to leave a tip.", 
     "Tonight's the night: Sleep in a eucalyptus tree.", 
     'Truth will out this morning.  (Which may really mess things up.)', 
     'Try to get all of your posthumous medals in advance.', 
     'Try to have as good a life as you can under the circumstances.', 
     'Try to value useful qualities in one who loves you.', 
     'Tuesday After Lunch is the cosmic time of the week.', 
     'Tuesday is the Wednesday of the rest of your life.', 
     'What happened last night can happen again.', 
     "While you recently had your problems on the run, they've regrouped and are making another attack.", 
     'Write yourself a threatening letter and pen a defiant reply.', 
     'You are destined to become the commandant of the fighting men of the department of transportation.', 
     'You are going to have a new love affair.', 
     'You are not dead yet. But watch for further reports.', 
     'You are number 6!  Who is number one?', 
     'You are only young once, but you can stay immature indefinitely.', 
     'You are taking yourself far too seriously.', 
     'You are wise, witty, and wonderful, but you spend too much time reading this sort of trash.', 
     'You can create your own opportunities this week. Blackmail a senior executive.', 
     'You can do very well in speculation where land or anything to do with dirtis concerned.', 
     'You can rent this space for only $5 a week.', 
     'You could live a better life, if you had a better mind and a better body.', 
     "You don't become a failure until you're satisfied with being one.", 
     'You have an ambitious nature and may make a name for yourself.', 
     'You have an unusual equipment for success. Be sure to use it properly.', 
     "You have an unusual magnetic personality.  Don't walk too close to metal objects which are not fastened down.", 
     'You have been selected for a secret mission.', 
     'You may be recognized soon. Hide.', 
     'You may get an opportunity for advancement today. Watch it!', 
     'You may worry about your hair-do today, but tomorrow much peanut butter willbe sold.', 
     'You need more time; and you probably always will.', 
     "You need no longer worry about the future.  This time tomorrow you'll be dead.", 
     'You own a dog, but you can only feed a cat.', 
     'You shall be rewarded for a dastardly deed.', 
     "You should emulate your heroes, but don't carry it too far. Especially if they are dead.", 
     'You should go home.', 
     'You too can wear a nose mitten.', 
     'You ought to be more careful--your love could drag on for years and years.', 
     'You will always get the greatest recognition for the job you least like.', 
     'You will always have good luck in your personal affairs.', 
     'You will attract cultured and artistic people to your home.', 
     'You will be a winner today.  Pick a fight with a four-year-old.', 
     'You will be advanced socially, without any special effort on your part.', 
     'You will be aided greatly by a person whom you thought to be unimportant.', 
     'You will be attacked by a beast who has the body of a wolf, the tail of a lion, and the face of Donald Duck.', 
     'You will be audited by the Internal Revenue Service.', 
     'You will be awarded a medal for disregarding safety in saving someone.', 
     'You will be awarded some great honor.', 
     'You will be awarded the Nobel Peace Prize... posthumously.', 
     'You will be called upon to help a friend in trouble.', 
     'You will be divorced within a year.', 
     'You will be given a post of trust and responsibility.', 
     'You will be held hostage by a radical group.', 
     'You will be honored for contributing your time and skill to a worthy cause.', 
     'You will be imprisoned for contributing your time and skill to a bank robbery.', 
     'You will be married within a year, and divorced within two.', 
     'You will be married within a year.', 
     'You will be misunderstood by everyone.', 
     'You will be recognized and honored as a community leader.', 
     'You will be reincarnated as a toad; and you will be much happier.', 
     'You will be run over by a beer truck.', 
     'You will be run over by a bus.', 
     'You will be singled out for promotion in your work.', 
     'You will be successful in love.', 
     'You will be surprised by a loud noise.', 
     'You will be surrounded by luxury.', 
     'You will be the last person to buy a Chrysler.', 
     'You will be the victim of a bizarre joke.', 
     'You will be Told about it Tomorrow. Go Home and Prepare Thyself.', 
     'You will be traveling and coming into a fortune.', 
     'You will be winged by an anti-aircraft battery.', 
     "You will become rich and famous unless you don't.", 
     'You will contract a rare disease.', 
     'You will engage in a profitable business activity.', 
     'You will experience a strong urge to do good; but it will pass.', 
     'You will feel hungry again in another hour.', 
     'You will forget that you ever knew me.', 
     'You will gain money by a fattening action.', 
     'You will gain money by a speculation or lottery.', 
     'You will gain money by an illegal action.', 
     'You will gain money by an immoral action.', 
     'You will get what you deserve.', 
     'You will give someone a piece of your mind, which you can ill afford.', 
     'You will have a long and boring life.', 
     'You will have a long and unpleasant discussion with your supervisor.', 
     'You will have domestic happiness and faithful friends.', 
     'You will have good luck and overcome many hardships.', 
     'You will have long and healthy life.', 
     'You will hear good news from one you thought unfriendly to you.', 
     'You will inherit millions of dollars.', 
     'You will inherit some money or a small piece of land.', 
     'You will live a long, healthy, happy life and make bags of money.', 
     'You will live to see your grandchildren.', 
     'You will lose your present job and have to become a door to door mayonnaise salesman.', 
     'You will meet an important person who will help you advance professionally.', 
     'You will not be elected to public office this year.',
     'You will obey or molten silver will be poured into your ears.',
     'You will overcome the attacks of jealous associates.',
     'You will pay for your sins. If you have already paid, please disregard this message.', 
     'You will pioneer the first Martian colony.', 
     'You will probably marry after a very brief courtship.', 
     'You will reach the highest possible point in your business or profession.', 
     'You will receive a legacy which will place you above want.', 
     'You will remember something that you should not have forgotten.', 
     'You will soon forget this.', 
     'You will soon meet a person who will play an important role in your life.', 
     'You will step on the night soil of many countries.', 
     'You will stop at nothing to reach your objective, but only because your brakes are defective.', 
     'You will triumph over your enemy.', 
     'You will visit the Dung Pits of Glive soon.', 
     'You will win success in whatever calling you adopt.', 
     "You will wish you hadn't.", 
     "You work very hard. Don't try to think as well.", 
     'You worry too much about your job. Stop it. You are not paid enough to worry.', 
     "You would if you could but you can't so you won't.", 
     "You'll be called to a post requiring ability in handling groups of people.", 
     "You'll be sorry...", 
     "You'll feel devilish tonight. Be gay. Do crime.",  
     "You'll never see all the places, or read all the books, but fortunately, they're not all recommended.", 
     "You'll wish that you had done some of the hard things when they were easier to do.", 
     "You're a card which will have to be dealt with.", 
     "You're at the end of the road again.", 
     "You're being followed. Cut out the hanky-panky for a few days.", 
     'You\'re currently going through a difficult transition period called "Life."', 
     "You're definitely on their list. The question to ask next is what list it is.", 
     "You're growing out of some of your problems, but there are others that you're growing into.", 
     "You've been leading a dog's life. Stay off the furniture.",  
     'Your business will assume vast proportions.', 
     'Your business will go through a period of considerable expansion.', 
     "Your fly might be open (but don't check it just now).", 
     'Your goose is cooked. (Your dinner is burned up too!)', 
     'Your love life will be happy and harmonious.', 
     'Your love life will be... interesting.', 
     'Your lover will never wish to leave you.', 
     'Your lucky color has faded.', 
     'Your lucky number is 3552664958674928.  Watch for it everywhere.', 
     'Your mode of life will be changed for the better because of good news soon.', 
     'Your mode of life will be changed for the better because of new developments.', 
     'Your motives for doing whatever good deed you may have in mind will be misinterpreted by somebody.', 
     'Your present plans will be successful.', 
     'Your society will be sought by people of taste and refinement.', 
     'Your step will soil many countries.', 
     'Your talents will be recognized and suitably rewarded.', 
     'Your temporary financial embarrassment will be relieved in a surprising manner.']

def getFortune():
    fortune = fortunes[random.randint(0,240)]
    return fortune