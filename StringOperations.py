from functools import partial

class StringOperations:
    def capitalize_text(self, text):
        return ' '.join(word.capitalize() for word in text.split())

    def replace_substring(self, text, old, new):
        return text.replace(old, new)

# Crear una instancia de StringOperations
string_ops = StringOperations()

# Crear versiones especializadas usando functools.partial
capitalize_first_word = partial(string_ops.capitalize_text)
replace_spaces_with_underscore = partial(string_ops.replace_substring, old=' ', new='_')

# Ejemplos de uso
def main():
    text = "hola mundo"
    
    # Usando capitalize_first_word
    print(capitalize_first_word(text))  # Output: "Hola mundo"
    
    # Usando replace_spaces_with_underscore
    print(replace_spaces_with_underscore(text))  # Output: "hola_mundo"

if __name__ == "__main__":
    main()