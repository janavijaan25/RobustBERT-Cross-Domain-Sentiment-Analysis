import pandas as pd
import random

# Set seed for reproducibility
random.seed(42)

print("Initializing dataset generation...")

# ==============================================================================
# DATASET 1: IMDb REVIEWS (Source Domain)
# ==============================================================================
# Requirements: 5000 samples (4000 train, 1000 test), Balanced (2500 pos, 2500 neg)
# Style: Formal, detailed movie reviews, 150-300 words.

imdb_pos_templates = [
    "{movie} is an absolute masterpiece. The {aspect1} is stunning and the {aspect2} is brilliant. The lead actor delivers an outstanding performance that will be remembered for years. The screenplay is tightly written, with every scene serving a purpose. The emotional depth of the story resonates long after the credits roll. I cannot recommend this film highly enough.",
    "I was deeply moved by {movie}. From the opening scene to the final moment, this film exceeded my expectations. The {aspect1} is exceptional and the {aspect2} elevates the entire experience. This is cinema at its finest. A must-watch for anyone who appreciates {genre}.",
    "Rarely does a film come along that delivers on so many levels. {movie} is a remarkable achievement in {genre} filmmaking. The {aspect1} is superb, the {aspect2} is phenomenal, and the {aspect3} is simply extraordinary. I left the theater feeling thoroughly entertained. This is one I will definitely watch again."
]

imdb_neg_templates = [
    "What a disaster. {movie} is a terrible mess from start to finish. The {aspect1} is confusing and the {aspect2} is dreadful. The acting feels atrocious, as if the cast knew they were in a bad movie. Save your money and skip this one. It's not even worth a streaming rental.",
    "I had low expectations and still was disappointed. The {aspect1} is awful and the {aspect2} makes no sense. {movie} wastes a talented cast on a boring script. The {aspect3} is horrendous. This is easily one of the worst films I've seen this year.",
    "Where to begin with this trainwreck? The {aspect1} is dreadful, the {aspect2} is abysmal, and don't get me started on the {aspect3}. I checked my watch multiple times during the painfully long runtime. {movie} is a complete waste of time and money."
]

movies = ["The Shawshank Redemption", "The Godfather", "Pulp Fiction", "The Dark Knight", "Forrest Gump", "Inception", "The Matrix", "Goodfellas", "Schindler's List", "Fight Club", "Interstellar", "The Silence of the Lambs", "Saving Private Ryan", "Gladiator"]
aspects_pos = ["acting", "plot", "direction", "cinematography", "screenplay", "dialogue", "pacing", "score", "visual effects", "editing", "character development"]
aspects_neg = ["plot", "direction", "screenplay", "dialogue", "pacing", "editing", "character development"]
genres = ["drama", "thriller", "action", "comedy", "romance", "sci-fi", "horror", "mystery"]

imdb_data = []
for i in range(2500):
    template = random.choice(imdb_pos_templates)
    text = template.format(
        movie=random.choice(movies),
        aspect1=random.choice(aspects_pos),
        aspect2=random.choice(aspects_pos),
        aspect3=random.choice(aspects_pos),
        genre=random.choice(genres)
    )
    split = "train" if i < 2000 else "test"
    imdb_data.append({"text": text, "label": 1, "split": split})

for i in range(2500):
    template = random.choice(imdb_neg_templates)
    text = template.format(
        movie=random.choice(movies),
        aspect1=random.choice(aspects_neg),
        aspect2=random.choice(aspects_neg),
        aspect3=random.choice(aspects_neg)
    )
    split = "train" if i < 2000 else "test"
    imdb_data.append({"text": text, "label": 0, "split": split})

df_imdb = pd.DataFrame(imdb_data).sample(frac=1, random_state=42).reset_index(drop=True)
df_imdb.to_csv("imdb_reviews.csv", index=False)
print(f"✅ Generated imdb_reviews.csv ({len(df_imdb)} rows)")


# ==============================================================================
# DATASET 2: TWITTER SENTIMENT (Target Domain)
# ==============================================================================
# Requirements: 3000 samples, Balanced (1500 pos, 1500 neg)
# Style: Informal, slang, emojis, hashtags, 10-30 words.

tw_pos_templates = [
    "Just watched {movie} and OMG it's {slang}! {emoji} {hashtag}",
    "{movie} is straight {slang}. No cap, {phrase} {emoji}",
    "I'm {emotion} with {movie}! {phrase} {emoji} #MustWatch",
    "This {product} is {slang}! {phrase} {emoji} {hashtag}",
    "Lowkey {movie} is the best film of the year {emoji} #MovieNight",
    "Just got my {product} and I'm {emotion}! {phrase} {emoji}",
    "This {product} is straight {slang} fr fr. {phrase} 💯"
]

tw_neg_templates = [
    "Worst movie ever. Complete {slang}. Wasted 2 hours {emoji} {hashtag}",
    "{movie} is {slang}. Don't waste your time {emoji}",
    "I can't even. {movie} is so bad it hurts {emoji} {hashtag}",
    "This {product} is {slang}. Don't waste your money tbh {emoji}",
    "Big regret buying this {product}. {phrase} {emoji} {hashtag}",
    "{movie} is mid at best. {phrase} {emoji}",
    "Big yikes. {movie} is a total {slang} {emoji} #SkipIt"
]

tw_movies = ["this movie", "the film", "this new release", "that sequel", "the remake", "this documentary"]
tw_products = ["phone", "laptop", "headphones", "coffee maker", "vacuum", "smartwatch", "camera", "tablet"]
tw_slang_pos = ["fire", "lit", "bussin", "goat", "slaps", "hits different", "immaculate", "chef's kiss", "top tier", "elite"]
tw_slang_neg = ["trash", "mid", "garbage", "a mess", "a flop", "cringe", "a snooze fest", "not it", "giving flop", "dead"]
tw_phrase_pos = ["Best thing ever!", "Highly recommend!", "So good!", "Can't stop thinking about it!", "Absolutely loved it!", "10/10 would recommend", "Must watch!"]
tw_phrase_neg = ["Don't waste your time.", "Save your money.", "Skip it.", "So disappointed.", "What a waste.", "Never again.", "0/10 would not recommend"]
tw_emoji_pos = ["😍", "🔥", "💯", "😊", "❤️", "👏", "🙌", "✨", "💪", "🎉"]
tw_emoji_neg = ["😡", "👎", "🤮", "💩", "😤", "🙄", "😑", "💔", "😒", "🤦"]
tw_hashtags_pos = ["#MustWatch", "#MovieNight", "#BestEver", "#WorthIt", "#HighlyRecommend"]
tw_hashtags_neg = ["#Disappointed", "#WorstPurchase", "#NeverAgain", "#SkipIt", "#NotWorthIt"]
tw_emotions_pos = ["obsessed", "in love", "so happy", "thrilled", "amazed"]
tw_emotions_neg = ["disappointed", "frustrated", "annoyed", "upset", "angry"]

tw_data = []
for i in range(1500):
    template = random.choice(tw_pos_templates)
    text = template.format(
        movie=random.choice(tw_movies),
        product=random.choice(tw_products),
        slang=random.choice(tw_slang_pos),
        phrase=random.choice(tw_phrase_pos),
        emoji=random.choice(tw_emoji_pos),
        hashtag=random.choice(tw_hashtags_pos),
        emotion=random.choice(tw_emotions_pos)
    )
    tw_data.append({"text": text, "label": 1, "category": "positive"})

for i in range(1500):
    template = random.choice(tw_neg_templates)
    text = template.format(
        movie=random.choice(tw_movies),
        product=random.choice(tw_products),
        slang=random.choice(tw_slang_neg),
        phrase=random.choice(tw_phrase_neg),
        emoji=random.choice(tw_emoji_neg),
        hashtag=random.choice(tw_hashtags_neg)
    )
    tw_data.append({"text": text, "label": 0, "category": "negative"})

df_twitter = pd.DataFrame(tw_data).sample(frac=1, random_state=42).reset_index(drop=True)
df_twitter.to_csv("twitter_sentiment.csv", index=False)
print(f"✅ Generated twitter_sentiment.csv ({len(df_twitter)} rows)")


# ==============================================================================
# DATASET 3: CHALLENGE SET (Nuanced Language)
# ==============================================================================
# Requirements: 200 samples. 50 per category. Exactly 25 pos, 25 neg per category.

data = []

# 1. Sarcasm (25 Neg, 25 Pos)
sarcasm_neg = [
    "Oh great, another sequel. Just what we needed.", "Wow, what a surprise. The ending was so predictable.",
    "Fantastic. Another two hours of my life wasted.", "Brilliant idea to cast him. He only ruined the entire film.",
    "I just love waiting three hours for a plot twist. Amazing.", "Perfect. Now I remember why I stopped watching this series.",
    "Great, more CGI and less story. Just what cinema needs.", "Oh joy, another remake. Because originality is overrated.",
    "Wonderful. The sound mixing made dialogue completely inaudible.", "Superb casting choice. If they wanted someone with zero expressions.",
    "Thank goodness for the intermission. I needed a break from boredom.", "Amazing how they made a 90-minute film feel like 5 hours.",
    "What a cliffhanger. Can't wait for the sequel nobody asked for.", "Loved the part where nothing happened for 30 minutes. Riveting.",
    "Brilliant writing. The characters had the depth of a puddle.", "So glad I paid full price for this. Totally worth it. Not.",
    "The special effects were so good I forgot there was no plot.", "Great, another movie that thinks explosions equal entertainment.",
    "Just what I needed after a long week. More disappointment.", "Bravo! You managed to make a boring movie about space battles.",
    "Finally, a film that answers the question: what if nothing made sense?", "Superb. The lead actor's range spans from A to A.",
    "Thrilling. I was on the edge of my seat trying to stay awake.", "Amazing. They turned a great book into whatever this was.",
    "What a masterpiece. Said no one who watched it."
]
sarcasm_pos = [
    "I guess it wasn't the worst thing I've ever seen. High praise, I know.", "Well, at least the credits rolled eventually.",
    "I'll give them this: they managed to release it.", "It's a movie. That's for sure.",
    "I've seen worse. But not much worse.", "At least I got a nap in the theater.",
    "The popcorn was good. Can't say the same for the movie.", "If you like watching paint dry, this is your Citizen Kane.",
    "Truly a cinematic experience. By which I mean I experienced regret.", "I laughed. Not at the jokes, but at how bad it was.",
    "So bad it's almost good. Almost.", "A triumph of marketing over substance.",
    "They really outdid themselves. In what way, I'm not sure.", "I can't wait to forget I ever watched this.",
    "It's definitely a film that was made.", "The best part was when it ended.",
    "I'm sure the director tried their best. Or at least showed up.", "A bold experiment in testing audience patience.",
    "Congratulations to everyone involved. I hope you got paid well.", "This will definitely win an award. Maybe a Razzie.",
    "I'm speechless. And not in a good way.", "Wow. Just... wow. That was something.",
    "It's an experience. I wouldn't call it a good one.", "Well, they can't all be winners.",
    "I suppose it could have been worse. If it was longer."
]

# 2. Negation (25 Neg, 25 Pos)
negation_neg = [
    "Not a good movie. Don't waste your time.", "I don't recommend this to anyone.",
    "This isn't worth watching. Skip it.", "I wouldn't say it's great. Far from it.",
    "It's not enjoyable at all. Very disappointing.", "Not happy with this purchase. Regret it.",
    "Can't say I liked it. It was terrible.", "This isn't entertaining. It's just boring.",
    "Not worth the money. Don't buy it.", "I don't want to see it again. Once was enough.",
    "It's not even funny. Just cringeworthy.", "Never going to watch this again.",
    "Not a single good thing about it.", "Can't believe I wasted two hours on this.",
    "Not what I expected, and not in a good way.", "I don't understand the hype. It's bad.",
    "It's not a masterpiece. It's a mess.", "Not recommended. Avoid at all costs.",
    "Couldn't wait for it to end. So boring.", "Never been so disappointed in a movie.",
    "Not worth your time. Trust me.", "I can't find anything good to say. Terrible.",
    "Don't bother watching. It's awful.", "Not going to lie, it was bad.",
    "Isn't it terrible? Yes, yes it is."
]
negation_pos = [
    "Not a bad movie at all. Actually quite enjoyable.", "I don't hate it. It's actually pretty good.",
    "This is not without its merits. A solid effort.", "I wouldn't say it's terrible. It has some good moments.",
    "It's not the worst thing I've ever seen. Decent enough.", "Not disappointed at all. Really liked it.",
    "Can't say I disliked it. Pretty entertaining.", "This isn't boring. It kept me engaged throughout.",
    "Not bad, not bad at all. I enjoyed it.", "I don't regret watching it. Time well spent.",
    "It's not without flaws, but overall a good watch.", "Never felt bored. The pacing was excellent.",
    "Not a single dull moment. Thoroughly enjoyed it.", "Can't complain about anything. It was great.",
    "Not what I expected, but in a good way.", "I don't usually like this genre, but this one got me.",
    "It's not your typical blockbuster. And that's a good thing.", "Not overrated at all. Deserves all the praise.",
    "Couldn't stop watching. Absolutely captivating.", "Never thought I'd say this, but it was excellent.",
    "Not a waste of time. Actually quite rewarding.", "I can't find anything to criticize. Brilliant work.",
    "Don't miss this one. It's really good.", "Not going to lie, I loved every second.",
    "Isn't it amazing? Yes, yes it is."
]

# 3. Mixed Sentiment (25 Neg, 25 Pos)
mixed_neg = [
    "Great acting, but the plot was weak.", "Visually stunning, but emotionally hollow.",
    "Good performances wasted on poor script.", "Started strong but fell apart in the second half.",
    "Amazing soundtrack, terrible story.", "Brilliant concept, poor execution.",
    "The cast was excellent, but the direction was lacking.", "Some scenes were great, but overall it was disappointing.",
    "Good first act, boring second act, decent third act.", "Technically impressive but emotionally empty.",
    "The acting saved it from being a complete disaster.", "Beautiful cinematography, forgettable everything else.",
    "It had potential but failed to deliver.", "Enjoyed parts of it, but wouldn't watch again.",
    "Strong start, weak finish.", "The visuals were stunning but the story was predictable.",
    "Good effort, but something was missing.", "Not terrible, not great. Just okay.",
    "Moments of brilliance in an otherwise average film.", "Great ideas, poor execution.",
    "Loved the first half, hated the second.", "The performances were good but the writing was weak.",
    "Some good moments, but mostly forgettable.", "Ambitious but flawed.",
    "It tried too hard and fell short."
]
mixed_pos = [
    "Despite some flaws, it was an enjoyable watch.", "The plot was messy, but the acting was fantastic.",
    "Slow start, but it really picked up later.", "A bit too long, but overall a good movie.",
    "Some cheesy dialogue, but the action was great.", "Not perfect, but definitely worth watching.",
    "It has its issues, but I still liked it.", "The ending was weird, but I enjoyed the journey.",
    "Flawed but entertaining.", "A bit confusing, but visually beautiful.",
    "The story was predictable, but the cast was charming.", "Too many characters, but the main one was great.",
    "Some jokes fell flat, but I laughed a lot.", "It was a bit dark, but I appreciated the tone.",
    "The CGI was bad, but the practical effects were good.", "Not the best, but far from the worst.",
    "I had low expectations, but it surprised me.", "Messy plot, but great vibes.",
    "It has problems, but I can't help liking it.", "A bit slow, but the payoff was worth it.",
    "The writing was weak, but the performances carried it.", "Overrated, but still a fun ride.",
    "It didn't make sense, but it was fun.", "Flawed, but I respect the ambition.",
    "A bumpy ride, but I'm glad I took it."
]

# 4. Slang (25 Neg, 25 Pos)
slang_neg = [
    "This film is mid at best. Don't believe the hype.", "It's giving flop energy.",
    "This movie is trash. Total waste.", "I can't even. So bad it hurts.",
    "This is not it, chief.", "Big yikes. Skip this one.",
    "This film is a snooze fest. Literally.", "It's giving bored. So boring.",
    "Deadass the worst movie I've seen.", "This ain't it. Periodt.",
    "Absolute L. Don't watch it.", "This movie is garbage. Fr fr.",
    "It's a whole mess. Not in a good way.", "I'm pressed. It was so bad.",
    "That was cringe. Pure cringe.", "This movie is a flop. Big time.",
    "I want my time back. Deadass.", "This film is sus. Very sus.",
    "It's giving trash. Nothing else.", "The acting was mid.",
    "This is a massive L.", "I'm crying. It's so bad.",
    "This movie is bottom tier.", "No cap, it was awful.",
    "This film is a joke."
]
slang_pos = [
    "This movie is sick! In the best way possible.", "That plot twist was fire! 🔥",
    "This film is straight bussin, no cap.", "Lowkey the best movie of the year.",
    "I'm dead. This movie killed me. So good! 💀", "This is giving everything! Absolutely slayed.",
    "No lie, this movie hits different.", "Fr fr, this is a masterpiece.",
    "This film understood the assignment. 10/10.", "It's giving cinema. Pure art.",
    "This movie eats. And leaves no crumbs.", "Periodt. Best film ever.",
    "I'm obsessed. This is my Roman Empire.", "It slaps so hard. Must watch!",
    "This movie is a whole vibe.", "Rent free in my head. Can't stop thinking about it.",
    "This is the GOAT of movies.", "Absolutely goated. No cap.",
    "Sheesh, this movie is too good.", "It's a W for sure.",
    "The acting was top tier.", "This movie is a chef's kiss. 🤌",
    "I'm screaming. It's so good.", "Pure immaculate vibes.",
    "This film is elite."
]

# Assemble Challenge Set
for t in sarcasm_neg: data.append({"text": t, "label": 0, "category": "sarcasm"})
for t in sarcasm_pos: data.append({"text": t, "label": 1, "category": "sarcasm"})
for t in negation_neg: data.append({"text": t, "label": 0, "category": "negation"})
for t in negation_pos: data.append({"text": t, "label": 1, "category": "negation"})
for t in mixed_neg: data.append({"text": t, "label": 0, "category": "mixed_sentiment"})
for t in mixed_pos: data.append({"text": t, "label": 1, "category": "mixed_sentiment"})
for t in slang_neg: data.append({"text": t, "label": 0, "category": "slang"})
for t in slang_pos: data.append({"text": t, "label": 1, "category": "slang"})

df_challenge = pd.DataFrame(data).sample(frac=1, random_state=42).reset_index(drop=True)

# Validate before saving
assert len(df_challenge) == 200, "Challenge set must have exactly 200 rows."
for cat in df_challenge['category'].unique():
    pos_count = len(df_challenge[(df_challenge['category'] == cat) & (df_challenge['label'] == 1)])
    neg_count = len(df_challenge[(df_challenge['category'] == cat) & (df_challenge['label'] == 0)])
    assert pos_count == 25 and neg_count == 25, f"Category {cat} is not balanced."

df_challenge.to_csv("challenge_set.csv", index=False)
print(f"✅ Generated challenge_set.csv ({len(df_challenge)} rows)")
print("\n🎉 ALL DATASETS GENERATED SUCCESSFULLY!")
print("You now have exactly what you need for the Adaptive BERT project.")