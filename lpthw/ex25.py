def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') #将变量按空格分成数组
    return words
	
def sort_words(words):
    """Sorts the words."""
    return sorted(words) #这个对字符串的排序是按字母顺序的吗？
	
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) #返回并删除指定的元素
    print(word)
	
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #pop()默认参数为-1，即数组最后一个元素
    print(word)
	
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) #调用break_words()将sentence处理成数组，赋值给words
    return sort_words(words) #再调用sort_words()对words进行排序
	
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)#调用
    print_last_word(words)
	
def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)#调用
    print_last_word(words)