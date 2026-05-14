from functools import reduce

#1.
pts1 = [(6, -1), (8, 4), (7.5, -3), (4.4, 12), (7, 2)]

#a) 
max_x = max(map(lambda p: p[0], pts1))
print("1.a) Maior valor de x:", max_x)

#b)
max_point = max(pts1, key=lambda p: p[0])
print("1.b) Coordenada com maior x:", max_point)


#2.
first_quadrant = list(filter(lambda p: p[0] >= 0 and p[1] >= 0, pts1))
print("2) Primeiro quadrante:", first_quadrant)


#3.
pts2 = [(2, 5), (12, 3), (12, 1), (6, 5),
        (14, 10), (12, 10), (8, 12), (5, 3)]

sorted_pts = sorted(pts2, key=lambda p: (p[1], p[0]), reverse=True)
print("3) Coordenadas ordenadas:", sorted_pts)


#4.
def apply_function(func, items):
    return list(map(func, items))

strings = ["Ola Mundo", "Python Funcional"]
numbers = ["10", "25", "300"]

#a) 
print("4.a)", apply_function(str.lower, strings))

#b)
print("4.b)", apply_function(int, numbers))

#c) 
print("4.c)", apply_function(lambda s: s.replace(" ", "-"), strings))

#d)
print("4.d)", apply_function(str.title, strings))


#5.
def toCamelCase(strings):
    return list(map(str.title, strings))


print("5)", toCamelCase(strings))


#6.
def expand_words(strings):
    return [word for s in strings for word in s.split()]

def filter_words(words):
    return list(filter(lambda w: len(w) >= 4, words))

phrases = [
    "programacao funcional em python",
    "linguagens de programacao"
]

expanded = expand_words(phrases)
filtered = filter_words(expanded)

print("6.a) Palavras expandidas:", expanded)
print("6.b) Palavras filtradas:", filtered)


#7.
def toCamelCaseString(strings):
    words = expand_words(strings)
    words = filter_words(words)
    words = map(str.title, words)

    return reduce(lambda acc, w: acc + w, words, "")

result = toCamelCaseString(phrases)
print("7) String CamelCase:", result)