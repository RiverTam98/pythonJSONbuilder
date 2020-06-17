# your text must be in a block and separated by full stops for this JSON builder to work

text = input("what is your block of text please? ")

block_text = (text.split('/'))

the_list = []
for items in (block_text):
    the_list.append(items)

sentence_num = (len(the_list))


structure = input(f"You have {sentence_num} sentences in total and your last index number should be {sentence_num-1} ")

# you can alter the following depending on what format you want your json to take - index starts at 0 and must run in order

print(

    f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n"
    f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[0]}\",\n\"fontSize\": \"LARGE\"\n}},\n"
    f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n"
    f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[1]}\"\n}},\n"
    f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n"
    f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[2]}\"\n}},\n"
    f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n"
    f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[3]}\"\n}},\n"
    f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n"
    f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[4]}\"\n}},\n"
    f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[5]}\",\n\"isItalic\": true\n}},\n"
    f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[6]}\",\n\"isItalic\": true\n}},\n"
    f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n"
    f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[7]}\",\n\"fontSize\": \"LARGE\"\n}},\n"
    f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n"





)

#============================================================================================================

# below is a list of template components to create your json:

# normal
# f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[1]}\"\n}},\n"

# spacer
# f"{{\n\"type\": \"VERTICAL_SPACER_COMPONENT\"\n}},\n"

# text small
# f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[1]}\",\n\"fontSize\": \"SMALL\"\n}},\n"

# text large
# f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[1]}\",\n\"fontSize\": \"LARGE\"\n}},\n"

# normal italic
# f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[1]}\",\n\"isItalic\": true\n}},\n"

# normal bold
# f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[1]}\",\n\"isBold\": true\n}},\n"

# combined
# f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[1]}\",\n\"isItalic\": true,\n\"fontSize\": \"LARGE\",\n\"align\"\n}},\n"

# normal center aligned
# f"{{\n\"type\": \"TEXT_COMPONENT\",\n\"value\": \"{the_list[1]}\",\n\"align\": true\n}},\n"
