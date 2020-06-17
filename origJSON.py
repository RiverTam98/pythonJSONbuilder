# your text must be in a block and separated by / for this JSON builder to work

text = input("Paste your block of text here ")

block_text = (text.split('/'))

the_list = []
for items in (block_text):
    the_list.append(items)

sentence_num = (len(the_list))

structure = input(f"You have {sentence_num} sentences in total and the last one should be {the_list[-1]} ")



def count(index):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return index(*args, **kwargs)
    wrapper.counter = -1
    return wrapper
@count
def index():
    pass



#=========DO NOT ALTER ANY TEXT ABOVE HERE============================================


# you will need to alter the following depending on what format you want your json to take

print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")


print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")

index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")




print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")







#====================================================================================





# below is a list of template components to create your json:

# space
# print (f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n")

# norm =
# index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\"\n}},\n")
#
# small =
# index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n")
#
# large =
# index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n")
#
# italics =
# index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true\n}},\n")
#
# bold =
# index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isBold\": true\n}},\n")
#
# combi =
# index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"isItalic\": true,\n\"fontSize\": \"LARGE\",\n\"align\": CENTER\n}},\n")
#
# normCA =
# index(), print (f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[(index.counter)]}\",\n\"align\": true\n}},\n")


# NORMAL TEXT
# index(), print (norm)

# SPACE
# print (space)

# SMALL TEXT
# index(), print (small)

# LARGE TEXT
# index(), print (large)

# ITALICS NORMAL
# index(), print (italics)

# BOLD NORMAL
# index(), print (bold)

# COMBINATION
# index(), print (combi)

# NORMAL CENTER ALIGN  =
# index(), print (normCA)

# space = f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n"
# norm = f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{theList[(index.counter)]}\"\n}},\n"
# small = f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{theList[(index.counter)]}\",\n\"fontSize\": \"SMALL\"\n}},\n"
# large = f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{theList[(index.counter)]}\",\n\"fontSize\": \"LARGE\"\n}},\n"
# italics = f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{theList[(index.counter)]}\",\n\"isItalic\": true\n}},\n"
# bold = f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{theList[(index.counter)]}\",\n\"isBold\": true\n}},\n"
# combi = f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{theList[(index.counter)]}\",\n\"isItalic\": true,\n\"fontSize\": \"LARGE\",\n\"align\": CENTER\n}},\n"
# normCA = f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{theList[(index.counter)]}\",\n\"align\": true\n}},\n"

