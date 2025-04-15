
image hana = im.Scale("hana.png", 500, 650)  # Scaled to 500x650 pixels
image mika = im.Scale("mika.png", 350, 650)  # Scaled to 350x650 pixels
image dr_vex = im.Scale("dr_vex.png", 450, 650)  # Scaled to 450x650 pixels


image village_day = "village_day.png"  # Daytime village background
image village_sunset = "village_sunset.png"  # Sunset village background

# Define characters with their names and dialogue colors
define h = Character("Hana", color="#ff69b4")  # Pink for Hana's playful personality
define m = Character("Mika", color="#87ceeb")  # Light blue for Mika's shy nature
define v = Character("Dr. Vex", color="#00ff00")  # Green for Dr. Vex's sci-fi vibe
define unknown = Character("???", color="#ffffff")  # For mysterious moments (e.g., Mika's mom)

# Variables to track player choices
default trust_vex = 0  # Tracks how much the player trusts Dr. Vex (affects interactions and endings)


label start:
    # Scene 1: Arrival in Elderglow (Daytime)
    play music "village_ambience.mp3" fadein 1.0 loop  # Play calm village music
    scene village_day with fade
    "You arrive in the quaint village of Elderglow, a peaceful place surrounded by lush greenery and traditional houses. The sun is high, casting a warm glow over the village."

    show hana at left with dissolve
    h "Ugh, no signal? Seriously? How am I supposed to live without my chat? This ‘digital detox’ better be worth it…"

    show mika at right with dissolve
    m "Oh… um, hello! Are you… new here? We don’t get many visitors in Elderglow."

    h "Yeah, I’m Hana. I’m here to ‘find myself’ or whatever. You’re a local, huh? Got any tips for surviving this place?"

    m "I-I’m Mika… I live here with my mom. It’s usually quiet, but… lately, things have been a little strange."

    h "Strange how? Like, ‘haunted village’ strange? ‘Cause I’m totally down for some spooky vibes!"

    m "N-not exactly… People have been seeing lights in the forest at night, and… some villagers haven’t come back after going to investigate."

    
    menu:
        "Let’s go check out the forest tonight! I’m not scared of some glowy lights.":
            h "Let’s go check out the forest tonight! I’m not scared of some glowy lights."
            jump forest_night
        "Maybe we should ask around the village first. Someone might know more.":
            h "Maybe we should ask around the village first. Someone might know more."
            jump village_investigate


label forest_night:
    stop music fadeout 1.0  # Fade out the village music
    play music "sunset_mystery.mp3" fadein 1.0 loop  # Play suspenseful music for the forest
    play sound "forest_noise.mp3"  # Play ambient forest sounds
    scene village_sunset with fade
    "As the sun sets, the village takes on a melancholic hue. You and Mika head toward the forest, following the dirt path. The air grows colder, and a faint green glow pulses in the distance."

    show hana at left with dissolve
    show mika at right with dissolve
    h "Look, there’s a glow over there! Let’s check it out, Mika!"

    m "W-wait, Hana! What if it’s dangerous? I… I’m not sure about this…"

    show dr_vex at center with moveinleft
    v "Intruders… I should’ve known the villagers would start snooping. Who are you, and why are you here?"

    h "Whoa, cool robot arms! I’m Hana, and this is Mika. We’re just trying to figure out what’s going on with the glowy stuff. You’re not, like, kidnapping people, are you?"

    v "Kidnapping? No… but my experiments may have… unintended consequences. The serum I’ve created enhances strength and speed, but it’s unstable. Some villagers who volunteered to test it… they’ve changed."

    m "C-changed? What do you mean? Are they okay?"

    v "They’ve become… aggressive. I’ve been trying to reverse the effects, but I need more time. You two should leave before you get hurt."

    # Second choice: How do the girls respond to Dr. Vex?
    menu:
        "We’re not leaving! We can help you fix this.":
            $ trust_vex += 1  # Increase trust in Dr. Vex
            h "We’re not leaving! We can help you fix this."
            m "Y-yes… I want to help the villagers. They’re my friends…"
            jump teamwork_path
        "This sounds dangerous… Let’s go back to the village and warn everyone.":
            h "This sounds dangerous… Let’s go back to the village and warn everyone."
            m "I-I agree… We need to tell my mom and the others!"
            jump warn_village_path


label village_investigate:
    stop music fadeout 1.0  # Fade out any previous music
    play music "village_ambience.mp3" fadein 1.0 loop  # Play calm village music again
    scene village_day with fade
    "You decide to ask around the village for more information. The villagers are busy with their daily tasks, but they seem uneasy when you mention the forest lights."

    show hana at left with dissolve
    show mika at right with dissolve
    h "Okay, let’s play it safe and talk to some locals. Anyone in this village know about the forest lights?"

    m "M-my mom might know something… She’s been worried about the disappearances. Let’s go to my house."

    "You follow Mika to her small house near the village square. Her mother, a kind but stern woman, greets you at the door."

    show mika at center with move
    m "Mom, this is Hana. We’re trying to find out what’s happening with the forest lights and the missing villagers."

    show mika at right with move
    unknown "I’ve heard rumors… There’s a scientist living on the outskirts of the village. People say she’s been conducting strange experiments in the forest."

    h "A scientist, huh? Sounds like a lead! Let’s go check out the forest tonight and see if we can find her."

    m "B-but… what if it’s dangerous?"

    h "Don’t worry, Mika! I’ve got your back. Let’s do this!"

    jump forest_night  # Loops back to the forest investigation


label teamwork_path:
    stop music fadeout 1.0  # Fade out the forest music
    play music "sunset_mystery.mp3" fadein 1.0 loop  # Continue the mysterious music
    play sound "lab_hum.mp3"  # Play a sci-fi lab sound effect
    scene village_sunset with fade
    "You and Mika decide to help Dr. Vex find a cure for the affected villagers. She leads you to her hidden lab in the forest, a cluttered space filled with glowing vials and strange machinery."

    show hana at left with dissolve
    show mika at right with dissolve
    show dr_vex at center with dissolve
    h "Alright, Doc, let’s fix this mess! I’m good with puzzles—hit me with what you’ve got!"

    m "I-I’ll help too… I noticed some of the plants in the forest looked strange. Maybe they can help with the antidote?"

    v "…Very well. Your assistance might just save this village. Let’s get to work."

    "You spend the night working together. Hana uses her gaming skills to solve a complex chemical equation on Dr. Vex’s computer, while Mika collects rare herbs from the forest to stabilize the serum."

    v "Impressive… With your help, I’ve created an antidote. We can administer it to the affected villagers and bring them back to normal."

    
    menu:
        "Let’s go to the village and give the antidote to the families first.":
            $ trust_vex += 1  # Further increase trust in Dr. Vex
            h "Let’s go to the village and give the antidote to the families first. They deserve to know their loved ones are safe."
            jump teamwork_ending
        "We should find the affected villagers in the forest and cure them directly.":
            h "We should find the affected villagers in the forest and cure them directly. No time to waste!"
            jump forest_cure


label warn_village_path:
    stop music fadeout 1.0  # Fade out the forest music
    play music "village_ambience.mp3" fadein 1.0 loop  # Play calm music for the village
    scene village_day with fade
    "You and Mika return to the village at dawn, determined to warn the others about Dr. Vex’s experiments. The villagers gather in the square, their faces filled with worry."

    show hana at left with dissolve
    show mika at right with dissolve
    h "We need to tell everyone what’s going on! That crazy scientist is trouble!"

    m "Y-you’re right… Let’s go to the village square. My mom will know what to do."

    "Mika’s mother organizes the villagers, and they form a group to confront Dr. Vex. You lead them back to the forest, where Dr. Vex is waiting."

    stop music fadeout 1.0  # Fade out the village music
    play music "sunset_mystery.mp3" fadein 1.0 loop  # Play suspenseful music for the confrontation
    show dr_vex at center with moveinleft
    v "So, you’ve turned the village against me… I only wanted to help humanity evolve. You’ll regret this."

    "The villagers demand that Dr. Vex leave Elderglow. She reluctantly agrees, but not before warning you of the consequences."

    v "The affected villagers are still out there… Without my help, they’ll remain monsters. You’ve doomed them."

    jump confrontation_ending


label teamwork_ending:
    stop music fadeout 1.0  # Fade out the previous music
    play music "hopeful_ending.mp3" fadein 1.0 loop  # Play uplifting music for the happy ending
    scene village_day with fade
    "With Dr. Vex’s antidote, you and Mika distribute it to the families of the affected villagers. Slowly, the villagers return to normal, and the village is filled with tearful reunions."

    show hana at left with dissolve
    show mika at right with dissolve
    show dr_vex at center with dissolve
    h "Well, that was wild! I guess this detox wasn’t so boring after all. Hey, Mika, you should totally come visit me in the city sometime!"

    m "M-me? In the city? I… I think I’d like that. Thank you, Hana, for everything."

    v "You two have potential… I’ll continue my research elsewhere, but I’ll never forget your help. Perhaps our paths will cross again."

    "The sun rises over Elderglow, and a sense of peace returns to the village. You’ve made a new friend in Mika and helped Dr. Vex find redemption."

    "The End - Teamwork Ending"
    stop music fadeout 2.0  # Fade out the music at the end
    return


label forest_cure:
    stop music fadeout 1.0  # Fade out the lab music
    play music "tense_action.mp3" fadein 1.0 loop  # Play tense music for the action scene
    play sound "forest_noise.mp3"  # Play ambient forest sounds
    scene village_sunset with fade
    "You, Mika, and Dr. Vex venture into the forest to find the affected villagers. The green glow intensifies, and you hear growls in the distance."

    show hana at left with dissolve
    show mika at right with dissolve
    show dr_vex at center with dissolve
    h "Alright, let’s do this! We’ve got the antidote—time to play hero!"

    m "I-I’m scared… but I trust you, Hana."

    v "Be careful. The serum has made them unpredictable. We need to approach with caution."

    play sound "growl.mp3"  # Play a growl sound effect
    "You find a group of affected villagers, their eyes glowing green. You try to administer the antidote, but they attack before you can get close."

    h "Whoa, back off! We’re trying to help you!"

    play sound "glass_shatter.mp3"  # Play a glass shattering sound effect
    "In the chaos, Dr. Vex is injured, and the antidote vials are shattered. The affected villagers escape deeper into the forest, leaving you with no way to cure them."

    v "…I warned you. Without the antidote, they’ll remain like this… and they’ll come for the village next."

    m "N-no… What have we done?"

    jump tragic_ending


label confrontation_ending:
    stop music fadeout 1.0  # Fade out the confrontation music
    play music "bittersweet_ending.mp3" fadein 1.0 loop  # Play somber music for the bittersweet ending
    scene village_day with fade
    "Dr. Vex leaves Elderglow, but the affected villagers remain lost in the forest. The village is safe for now, but the families of the missing villagers are heartbroken."

    show hana at left with dissolve
    show mika at right with dissolve
    h "We did what we had to do, Mika. That scientist was bad news."

    m "I… I know, but… what about the people who are still out there? My friends… they’re gone…"

    "The village tries to move on, but a shadow hangs over Elderglow. You’ve protected the village, but at a great cost."

    "The End - Confrontation Ending"
    stop music fadeout 2.0  # Fade out the music at the end
    return


label tragic_ending:
    stop music fadeout 1.0  # Fade out the previous music
    play music "tragic_ending.mp3" fadein 1.0 loop  # Play dark music for the tragic ending
    play sound "village_chaos.mp3"  # Play sounds of chaos
    scene village_sunset with fade
    "Without the antidote, the affected villagers attack Elderglow in the night. The village is unprepared, and chaos ensues."

    show hana at left with dissolve
    show mika at right with dissolve
    h "This is bad… We messed up, Mika!"

    m "I-I should’ve done more… I’m so sorry…"

    "The village is overrun, and you and Mika barely escape with your lives. Dr. Vex disappears into the night, her warnings unheeded."

    "The End - Tragic Ending"
    stop music fadeout 2.0  # Fade out the music at the end
    stop sound fadeout 1.0  # Stop any remaining sound effects
    return