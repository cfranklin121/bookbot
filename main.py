def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        #print(file_contents)
        word_count = get_word_count(file_contents)
        #print(word_count)
        char_count = get_character_count(file_contents)
        #print(char_count)

        print_report(word_count, char_count, file_path)



def get_word_count(text):
    words = text.split()
    count = len(words)
    
    return count


def get_character_count(text):
    count = {}
    new_string = text.lower()
    for char in new_string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    return count

def sort_on(dict):
    return dict["count"]

def print_report(word_count, char_count, file_path):
    report = []
    for char in char_count:
        if char.isalpha():
            report.append({"char": char, "count": char_count[char]})
    
    report.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    i = 0
    for char in report:
        print(f"The '{report[i]["char"]}' character was found {report[i]["count"]} times")
        i += 1
    print("--- End report ---")


if __name__ == "__main__":
    main()