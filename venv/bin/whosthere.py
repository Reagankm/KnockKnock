#!/home/reagan/Development/NLTK/venv/bin/python
import random
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, word_tokenize


def getTexts():
    #Create a list of texts to search

    print("\nExcuse me just a moment while I get all of my books in order...\n")
    
    corpusRoot = '.'
    textList = PlaintextCorpusReader(corpusRoot, r'.*.txt')
    
    
    return [sent_tokenize(nltk.corpus.webtext.raw('overheard.txt')), 
            sent_tokenize(nltk.corpus.gutenberg.raw('austen-emma.txt')), 
            sent_tokenize(nltk.corpus.gutenberg.raw('austen-persuasion.txt')), 
            sent_tokenize(nltk.corpus.gutenberg.raw('austen-sense.txt')), 
            sent_tokenize(nltk.corpus.gutenberg.raw('bryant-stories.txt')), 
            sent_tokenize(nltk.corpus.gutenberg.raw('burgess-busterbrown.txt')), 
            sent_tokenize(nltk.corpus.gutenberg.raw('carroll-alice.txt')), 
            sent_tokenize(nltk.corpus.gutenberg.raw('chesterton-ball.txt')),
            sent_tokenize(nltk.corpus.gutenberg.raw('chesterton-brown.txt')), 
            sent_tokenize(nltk.corpus.gutenberg.raw('chesterton-thursday.txt')), 
            sent_tokenize(nltk.corpus.gutenberg.raw('edgeworth-parents.txt')), 
            sent_tokenize(nltk.corpus.nps_chat.raw()), 
            sent_tokenize(nltk.corpus.brown.raw(categories=['adventure', 'belles_lettres', 'fiction', 'humor',  
                                                          'lore', 'mystery', 'romance', 'science_fiction'])), 
            #sent_tokenize(nltk.corpus.switchboard.raw()),      
            sent_tokenize(textList.raw('corpuses/auto_girls.txt')), 
            sent_tokenize(textList.raw('corpuses/birthday_party.txt')), 
            sent_tokenize(textList.raw('corpuses/bobsey_city.txt')), 
            sent_tokenize(textList.raw('corpuses/bobsey_home.txt')), 
            sent_tokenize(textList.raw('corpuses/bobsey_indoors.txt')), 
            sent_tokenize(textList.raw('corpuses/bobsey_meadow.txt')), 
            sent_tokenize(textList.raw('corpuses/bonnie_charlie.txt')), 
            sent_tokenize(textList.raw('corpuses/boys_and_girls_bookshelf.txt')), 
            sent_tokenize(textList.raw('corpuses/bunny_brown.txt')), 
            sent_tokenize(textList.raw('corpuses/buster_bear.txt')), 
            sent_tokenize(textList.raw('corpuses/charlie_rescue.txt')), 
            sent_tokenize(textList.raw('corpuses/childhoods_favorites.txt')), 
            sent_tokenize(textList.raw('corpuses/childrens_hour.txt')), 
            sent_tokenize(textList.raw('corpuses/childrens_old_favorites.txt')), 
            sent_tokenize(textList.raw('corpuses/child_stories_from_masters.txt')), 
            sent_tokenize(textList.raw('corpuses/curlytops.txt')), 
            sent_tokenize(textList.raw('corpuses/daddy_garden.txt')), 
            sent_tokenize(textList.raw('corpuses/dorothy_dale.txt')),
            sent_tokenize(textList.raw('corpuses/double_dare.txt')), 
            sent_tokenize(textList.raw('corpuses/enchanted_castle.txt')), 
            sent_tokenize(textList.raw('corpuses/errand_boy.txt')), 
            sent_tokenize(textList.raw('corpuses/etheldreda.txt')), 
            sent_tokenize(textList.raw('corpuses/fairy_tales_every_child.txt')), 
            sent_tokenize(textList.raw('corpuses/favorite_stories_every_child.txt')), 
            sent_tokenize(textList.raw('corpuses/friend_smith.txt')), 
            sent_tokenize(textList.raw('corpuses/girl_commune.txt')), 
            sent_tokenize(textList.raw('corpuses/girlhood.txt')), 
            sent_tokenize(textList.raw('corpuses/girl_in_ten_thousand.txt')), 
            sent_tokenize(textList.raw('corpuses/golden_moments.txt')), 
            sent_tokenize(textList.raw('corpuses/henrietta_hen.txt')), 
            sent_tokenize(textList.raw('corpuses/honorable_miss.txt')), 
            sent_tokenize(textList.raw('corpuses/houseful_girls.txt')), 
            sent_tokenize(textList.raw('corpuses/jolly_fellowship.txt')), 
            sent_tokenize(textList.raw('corpuses/jos_boys.txt')), 
            sent_tokenize(textList.raw('corpuses/junior_classics.txt')), 
            sent_tokenize(textList.raw('corpuses/kates_ordeal.txt')), 
            sent_tokenize(textList.raw('corpuses/laugh_and_play.txt')), 
            sent_tokenize(textList.raw('corpuses/lightfoot_deer.txt')), 
            sent_tokenize(textList.raw('corpuses/little_maid.txt')), 
            sent_tokenize(textList.raw('corpuses/little_marian.txt')), 
            sent_tokenize(textList.raw('corpuses/little_mother.txt')), 
            sent_tokenize(textList.raw('corpuses/luckiest_girl.txt')), 
            sent_tokenize(textList.raw('corpuses/magic_pudding.txt')), 
            sent_tokenize(textList.raw('corpuses/maida_shop.txt')), 
            sent_tokenize(textList.raw('corpuses/marjie_busy.txt')), 
            sent_tokenize(textList.raw('corpuses/mary_louse.txt')), 
            sent_tokenize(textList.raw('corpuses/modern_tomboy.txt')), 
            sent_tokenize(textList.raw('corpuses/mrs_quack.txt')), 
            sent_tokenize(textList.raw('corpuses/mystery_putnam.txt')), 
            sent_tokenize(textList.raw('corpuses/navy_girl.txt')), 
            sent_tokenize(textList.raw('corpuses/patty_and_azalea.txt')), 
            sent_tokenize(textList.raw('corpuses/patty_social.txt')), 
            sent_tokenize(textList.raw('corpuses/patty_suitor.txt')), 
            sent_tokenize(textList.raw('corpuses/peck_bad.txt')), 
            sent_tokenize(textList.raw('corpuses/phoenix_and_carpet.txt')), 
            sent_tokenize(textList.raw('corpuses/plebe_year.txt')), 
            sent_tokenize(textList.raw('corpuses/polite_princes.txt')), 
            sent_tokenize(textList.raw('corpuses/polly.txt')), 
            sent_tokenize(textList.raw('corpuses/poor_proud.txt')), 
            sent_tokenize(textList.raw('corpuses/railway_kids.txt')), 
            sent_tokenize(textList.raw('corpuses/rollo_play.txt')), 
            sent_tokenize(textList.raw('corpuses/rusty_wren.txt')), 
            sent_tokenize(textList.raw('corpuses/sailor_girl.txt')), 
            sent_tokenize(textList.raw('corpuses/sara_crewe.txt')), 
            sent_tokenize(textList.raw('corpuses/snowball_lamb.txt')), 
            sent_tokenize(textList.raw('corpuses/sweet_maid.txt')), 
            sent_tokenize(textList.raw('corpuses/ted_and_phone.txt')), 
            sent_tokenize(textList.raw('corpuses/three_towers.txt')), 
            sent_tokenize(textList.raw('corpuses/tim_turtle.txt')), 
            sent_tokenize(textList.raw('corpuses/uncle_ike.txt')), 
            sent_tokenize(textList.raw('corpuses/west_wind.txt')), 
            sent_tokenize(textList.raw('corpuses/white_feather.txt')), 
            sent_tokenize(textList.raw('corpuses/young_folks_treasury.txt')),
            sent_tokenize(textList.raw('corpuses/works_of_fielding.txt')), 
            sent_tokenize(textList.raw('corpuses/useful_phrases.txt')), 
            sent_tokenize(textList.raw('corpuses/tudor_conversation.txt')), 
            sent_tokenize(textList.raw('corpuses/phrases_for_speakers.txt')), 
            sent_tokenize(textList.raw('corpuses/bequest.txt')),
            sent_tokenize(textList.raw('corpuses/english_spoke.txt')), 
            sent_tokenize(textList.raw('corpuses/phrase_book.txt'))
            ]
    # return [nltk.ConcordanceIndex(nltk.corpus.webtext.words('overheard.txt')), 
    #         nltk.ConcordanceIndex(nltk.corpus.gutenberg.words('austen-emma.txt')), 
    #         nltk.ConcordanceIndex(nltk.corpus.gutenberg.words('austen-persuasion.txt')), 
    #         nltk.ConcordanceIndex(nltk.corpus.gutenberg.words('austen-sense.txt')), 
    #         nltk.ConcordanceIndex(nltk.corpus.gutenberg.words('bryant-stories.txt')), 
    #         nltk.ConcordanceIndex(nltk.corpus.gutenberg.words('burgess-busterbrown.txt')), 
    #         nltk.ConcordanceIndex(nltk.corpus.gutenberg.words('carroll-alice.txt')), 
    #         nltk.ConcordanceIndex(nltk.corpus.gutenberg.words('chesterton-ball.txt')),
    #         nltk.ConcordanceIndex(nltk.corpus.gutenberg.words('chesterton-brown.txt')), 
    #         nltk.ConcordanceIndex(nltk.corpus.gutenberg.words('chesterton-thursday.txt')), 
    #         nltk.ConcordanceIndex(nltk.corpus.gutenberg.words('edgeworth-parents.txt')), 
    #         nltk.ConcordanceIndex(nltk.corpus.nps_chat.words()), 
    #         nltk.ConcordanceIndex(nltk.corpus.brown.words(categories=['adventure', 'belles_lettres', 'fiction', 'humor',  
    #                                                       'lore', 'mystery', 'romance', 'science_fiction'])), 
    #         nltk.ConcordanceIndex(nltk.corpus.switchboard.words()),      
    #         nltk.ConcordanceIndex(textList.words('corpuses/auto_girls.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/birthday_party.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/bobsey_city.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/bobsey_home.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/bobsey_indoors.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/bobsey_meadow.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/bonnie_charlie.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/boys_and_girls_bookshelf.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/bunny_brown.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/buster_bear.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/charlie_rescue.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/childhoods_favorites.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/childrens_hour.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/childrens_old_favorites.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/child_stories_from_masters.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/curlytops.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/daddy_garden.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/dorothy_dale.txt')),
    #         nltk.ConcordanceIndex(textList.words('corpuses/double_dare.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/enchanted_castle.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/errand_boy.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/etheldreda.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/fairy_tales_every_child.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/favorite_stories_every_child.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/friend_smith.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/girl_commune.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/girlhood.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/girl_in_ten_thousand.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/golden_moments.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/henrietta_hen.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/honorable_miss.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/houseful_girls.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/jolly_fellowship.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/jos_boys.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/junior_classics.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/kates_ordeal.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/laugh_and_play.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/lightfoot_deer.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/little_maid.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/little_marian.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/little_mother.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/luckiest_girl.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/magic_pudding.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/maida_shop.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/marjie_busy.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/mary_louse.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/modern_tomboy.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/mrs_quack.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/mystery_putnam.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/navy_girl.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/patty_and_azalea.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/patty_social.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/patty_suitor.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/peck_bad.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/phoenix_and_carpet.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/plebe_year.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/polite_princes.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/polly.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/poor_proud.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/railway_kids.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/rollo_play.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/rusty_wren.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/sailor_girl.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/sara_crewe.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/snowball_lamb.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/sweet_maid.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/ted_and_phone.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/three_towers.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/tim_turtle.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/uncle_ike.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/west_wind.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/white_feather.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/young_folks_treasury.txt')),
    #         nltk.ConcordanceIndex(textList.words('corpuses/works_of_fielding.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/useful_phrases.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/tudor_conversation.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/phrases_for_speakers.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/bequest.txt')),
    #         nltk.ConcordanceIndex(textList.words('corpuses/english_spoke.txt')), 
    #         nltk.ConcordanceIndex(textList.words('corpuses/phrase_book.txt'))
    #         ]

def getGuest():
    print("Welcome to the Knock Knock Joke Generator!")
    guest = input("Who do you want to be there? ")
    return guest

    

def getPunchline(guest, corpusList):
    readingPic = reading()
    readingInd = 0
    
    #Append oo sounds and look for concordances
    ooSounds = ["who", "oo", "ew", "ough", "ue", "eau"]
    ooList = []
    for sound in ooSounds:
        if guest.endswith(sound[0]):
            ooList.append(guest + sound[1:len(sound)])
        else:
            ooList.append(guest + sound)
            
#            ooList = [guest + "who", guest + "oo", guest + "ew", guest + "ough", guest + "ue"]
        
    workingList = ooList.copy()
    #Look for similar words and add them to the list
    for word in workingList:
        syn = wn.synsets(word)
        for i in range(0, len(syn)):
            current = syn[i]
            lems = current.lemmas()
            for j in range(0, len(lems)):
                name = lems[j].name()
                if len(word_tokenize(name)) is 1:
                  ooList.append(name)

    print(ooList)
    
    # for word in ooList:
    #     #Prints any found concordances (the word sought plus context on either side)
    #     for text in corpusList:
    #         for s in range(0, len(text)):
    #             if s == 0:
    #                 sent = text[s]
    #                 length = len(sent)
    #                 if length > 25:
    #                     length = 25
    #                 print("From: " + sent[0:25])
    #                 print("RESULTS:")
    #             wds = word_tokenize(text[s])
    #             for w in range(0, len(wds)):
    #                 if wds[w] == word:
    #                     print(text[s])
    #                     break
                    
    results = []
    for text in corpusList:
        print(readingPic[readingInd])
        readingInd = (readingInd + 1) % len(readingPic)
        #Prints any found concordances (the word sought plus context on either side)
        for s in range(0, len(text)):
            if s == 0:
                #sent = text[s].strip().stripWhitespace()
                sent = " ".join(text[s].split())
                length = len(sent)
                if length > 25:
                    length = 25
                #print("From: " + sent[0:25])
                #print("RESULTS:")
            #wds = word_tokenize(text[s])
            ci = nltk.ConcordanceIndex(word_tokenize(text[s]))
            
            for word in ooList:
                if ci.offsets(word):
                    #print(text[s])
                    results.append(text[s])
                    break
    
    
            #if text.offsets(word):
            #    text.print_concordance(word)
            #    print(text)
    print("Final result list:")
    for r in results:
        print(r)
    #s.startswith(t) 	test if string s starts with t
    
    if len(results) is 0:
        return "There's nothing funny about " + guest
    else:
        return results[random.randrange(0, len(results))]

def isValidWhosThere(whosThere):
    whosThere = whosThere.lower()
    if whosThere == "who's there?" or whosThere == "whos there?" or whosThere == "who's there" or whosThere == "whos there":
        return True
    else:
        return False

def isValidGuestWho(guest, guestWho):
    guestWho = guestWho.lower()
    guest = guest.lower()

    if guestWho == (guest + " who?") or guestWho == (guest + " who"):
        return True
    else:
        return False

def printJoke(guest, punchline):
    print("\nOkay, now I'm going to tell you a hilarious joke. Be ready to do your part.\n")

    whosThere = input("Knock knock\n")
    while not isValidWhosThere(whosThere):
        print("No, no, you're supposed to say 'Who's there?'. Let's try again.\n")
        whosThere = input("Knock knock\n")

    guestWho = input(guest + "\n")
    while not isValidGuestWho(guest, guestWho):
        print("No, no, you're supposed to say '" + guest + " who?' Let's try again.\n")
        guestWho = input(guest)

    print(punchline)

def noInputJoke(guest, punchline):
    divider = "******************************************************************************************************"
    print(divider)
    print(divider)
    print("\nOkay, now I'm going to tell you a hilarious joke.\n")
    print("Knock knock\n")
    print("Who's there?\n")
    print(guest + "\n")
    print(guest + " who?\n")
    print(punchline + "\n")
    print(divider)

def playAnother():
    answer = input("Would you like to play again? (Y for yes, N for no): ").lower()
    while (answer != "y" and answer != "n"):
        answer = input("I didn't understand that. Would you like to play again? (Y for yes, N for no): ").lower()

    if answer == "y":
        return True
    else:
        return False
                   

def reading():
    return ["              .__=\\__                  .__==__,",
            "            jf\'      ~~=\\,         _=/~\'      `\\,", 
            "        ._jZ\'            `\\q,   /=~             `\\__",
            "       j5(/                 `\\./                  V\\\\,",
            "     .Z))\' _____              |             .____, \\)/\\", 
            "    j5(K=~~     ~~~~\\=_,      |      _/=~~~~\'    `~~+K\\\\,",
            "  .Z)\\/                `~=L   |  _=/~                 t\\ZL"
            , " j5(_/.__/===========\\__   ~q |j/   .__============___/\\J(N,",
            "4L#XXXL_________________XGm, \\P  .mXL_________________JXXXW8L", 
            "~~~~~~~~~~~~~~~~~~~~~~~~~YKWmmWmmW@~~~~~~~~~~~~~~~~~~~~~~~~~~", ""]

    
def main():

    corpusList = getTexts()

    playAgain = True

    while (playAgain):
        guest = getGuest()
        punchline = getPunchline(guest, corpusList)
        #printJoke(guest, punchline)
        guest = guest.capitalize()
        noInputJoke(guest, punchline)
        playAgain = playAnother()


main()
        
    

