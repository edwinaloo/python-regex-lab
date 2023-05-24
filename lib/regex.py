import re

my_pattern = r"({})".format("|".join(map(re.escape, ["It's", "such a", "lovely day", "today", "Some weather we're having today, huh?", "Maybe today's just not my day."])))
my_regex = re.compile(my_pattern)

# Test the regular expression pattern
string1 = "It's such a lovely day today."
string2 = "Some weather we're having today, huh?"
string3 = "Maybe today's just not my day."

assert my_regex.findall(string1) == ["It's", "such a", "lovely day", "today"]
assert my_regex.findall(string2) == ["Some weather we're having today, huh?"]
assert my_regex.findall(string3) == ["Maybe today's just not my day."]
