label day2:
    scene bg hallway
    show yuuma default:
        xalign 0.35
        yalign 1.0
    y "...I can’t believe I agreed to something like this..."
    y "Kyo really shouldn’t have turned my form in without me."
    y "This is going to be so bad…"
    y "There’s a reason I don’t join clubs, but…"
    y "I know Kyo only wants the best for me. She means well."
    y "She probably just saw that I had some interest in this club and just wanted to give me a push."
    y "She means well. I guess I’m lucky to have someone like her."
    y "I’ve got to try. I can’t just scare myself out of this. I have to make an effort for Kyo."
    y "And maybe, for my own sake...A little change might be good."
    "Yuuma stands outside the club room for a minute, before decisively reaching forward and opening the door."
    scene bg clubroom
    show yuuma default:
        xalign 0.05
        yalign 1.0
    show souji default:
        xalign 0.6
        yalign 1.0
    show taida:
        xalign 0.9
        yalign 1.0
    with changeScene
    s "Alright everyone, quiet down, quiet down!"
    s "Welcome to the cooking club! I’m Souji, the club president, I look forward to cooking with you all!"
    s "Taida sensei here is going to be supervising our club"
    "Taida sensei briefly puts down the box of juice he was drinking and raises his hand in greeting."
    t "‘Sup."
    s "You guys can come to me or Taida sensei if you ever need help. Now without wasting any more time, how about we start our first activity?"
    s "I would like everyone to find a partner, preferably someone you haven’t met yet, and make a tamagoyaki."
    show souji default
    s "Nothing says ‘new friendship’ like a rolled omelet."
    show souji:
        linear 0.75 xpos 1.5
    show taida:
        linear 0.75 xpos 1.5
    hide taida
    "The room quickly divides into pairs, but Yuuma is left with nobody to work with"
    show yuuma default
    y "Maybe I should just leave. There’s no way anybody is going to want to work with me."
    "Yuuma starts walking to the door, wanting to save himself from any awkwardness that would follow."
    "Before Yuuma can leave, he feels somebody grab his arm."
    y "!!!"
    show katsumi default:
        xalign 1.5
        yalign 1.0
    show yuuma:
        linear 0.75 xpos 0.15
    show katsumi:
        linear 0.75 xpos 0.7
    h "You don’t have a partner, right?"
    y "I…"
    y "I don’t."
    show katsumi default
    h "Great! Neither do I! Wanna join up?"
    y "Uh…"
    y "Sure?"
    "Yuuma kicks himself for getting himself in this situation. He couldn’t get away now."
    h "I’m Katsumi Hoshino. Nice to meet you."
    y "Hoshino? I’m Yuuma Fujiwara."
    h "Fujiwara? That’s nice. Well, Fujiwara, there’s an open counter over there."
    show katsumi:
        linear 0.5 xpos 0.7
    show souji default:
        linear 0.5 xpos 0.85
    s "Get to it, guys!"
    show souji default:
        linear 0.75 xpos 1.5
    show katsumi:
        linear 0.5 xpos 0.75
    y "Do you know how to make tamagoyaki, Hoshino?"
    h "What’s there to know? It’s just eggs."
    y "Right…"
    "Katsumi reaches into the minifridge and pulls out a carton of eggs."
    "He reaches down into the cabinet and pulls out a bowl and whisk."
    "Katsumi starts cracking eggs into the bowl and whisking them."
    show yuuma default
    y "You look like you know what you’re doing."
    y "Make sure to put the soy sauce and other stuff in."
    h "Soy sauce and…? Okay."
    "Katsumi opens the minifridge and takes out soy sauce, sour cream, tomato salsa, and barbeque sauce."
    "Katsumi then proceeds to dump everything he grabbed into his eggs all at once."
    show yuuma default
    y "What in the world is he doing..."
    "Katsumi turns the stove on full heat, and dumps all of his egg mix onto a frying pan without putting butter or oil on first."
    y "It’s gonna burn…?"
    y "...Does he know it’s gonna burn?"
    "Yuuma watches in horror as the eggs turn black and start to steam."
    y "Hoshino--"
    show katsumi:
        linear 0.5 xpos 0.7
    show souji default:
        linear 0.5 xpos 0.85
    s "Katsumi, what are you doing?!"
    h "I’m making tamagoyaki. I think it is going pretty well!"
    s "..."
    s "...No, you’re not."
    s "Why don’t you have your partner take over this assignment today?"
    s "Yuuma? Can you make tamagoyaki?"
    show yuuma default
    y "Of course I can. It isn’t that hard."
    "In just a couple minutes, Yuuma proceeds to whip up a flawless plate of tamagoyaki that would put everyone else’s to shame."
    h "Woah! That was so fast! How did you do that?"
    y "It’s just eggs, man."
    h "It looks so good!"
    y "It’s just eggs, man. How low are your standards?"
    s "This looks great! Good job, Yuuma!"
    s "Everyone, come take a look at Yuuma’s tamagoyaki when you have a minute."
    s "Hopefully everyone can make a tamagoyaki that looks this good by the end of the year!"
    "The other classmates come over and marvel at Yuuma’s tamagoyaki."
    h "Yuuma…"
    h "I mean, Fujiwara."
    h "Please teach me how to cook!"
    y "What? Are you kidding me?"
    h "Please! You’re so good at this, couldn’t you help me."
    y "All due respect, but you’re a lost cause, Hoshino."
    y "I don’t know how you’ve made it this far like that."
    show katsumi default
    h "I need to learn, and who could teach me but a pro?"
    y "I can’t, Hoshino. Go find yourself a cookbook."
    "Yuuma grabs his bag and walks out of the club room."
    with changeScene
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
