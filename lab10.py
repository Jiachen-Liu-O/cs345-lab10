import tracery

rules = {
    
"area": ["mountain","small island","jungle"],
"buildings": ["a palace", "a tample", "a magic school"],
"creations":["people", "lion", "shaman", "cat", "fox"],
"text" : [ "there's a #bigArea#; There's #building# at the #bigArea#; There's an old #creation# and a small #creation#; The old #creation# told a #tale# to the small #creation#: #origin#", "A cow said: \"Hey buddy, did you heard that? Mad cow disease can kill us!\" The other cow said: \"No worry dude, we are kangaroo~\""],
"story": ["#[bigArea:#area#][building:#buildings#][creation:#creations#]text#"],
"origin": ["Once upon a time, #[#setCharacter#]story#"],
"tale": ["story","tale"]

}

grammar = tracery.Grammar(rules)
print(grammar.flatten("#origin#"))
