
# if 'cats' in res:
# 	print(True)
# else:
# 	print(False)

def word_count(s):
    # Your code here
    cache = {}
    str = s.split()
    a = 0

    for i in str:
    	if i in str:
    		a = a + 1
    		print(a)
    	# print(i)
    return cache




# if __name__ == "__main__":
print(word_count(""))
print(word_count("Hello"))
print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

