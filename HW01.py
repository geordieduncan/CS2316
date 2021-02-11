'''
This is the shell file for HW01. Be sure to replace the "pass" statements with the functions
See the HW01 prompt for detailed descriptions on the questions. Some test cases from the prompt
are provided at the bottom of the document. It is recommended to try all test cases from the prompt,
not just the ones provided at the bottom.
'''

# PART 1

def add_floats(num_list):
    tot = 0.0
    for n in num_list:
        try:
            if int(float(n)) == float(n):
                continue
            else:
                tot += float(n)
        except TypeError:
            pass
    return tot




def string_modifier(str_list):
    l = [s for s in str_list if s.isalpha()]
    return [i * l.index(i) for i in l]

def zip_counter(zip_list):
    return len(set([''.join([c for c in z if c.isdigit()]) for z in zip_list if len([c for c in z if c.isdigit()]) == 5]))

def directory(name_list, wanted):
    return [(c.split(' ')[-1], c.split(' ')[0]) for c in name_list if c.split(' ')[-1] in wanted]


def freezing(city, celsius):
    return {city[i]: celsius[i] * 1.8 + 32.0 for i in range(len(city)) if celsius[i] > 0}


def bill(foods, discounts):
    return {list(foods.keys())[i]: foods[list(foods.keys())[i]] * (1 - (0.01 * discounts[i])) for i in range(len(foods.keys()))}


#Part 2 - Classes and Objects

#######################################
#DO NOT EDIT THE FOLLOWING MOVIE CLASS#
#######################################
class Movie:

    def __init__(self, title, genre, length, rating):
        self.title = title
        self.genre = genre
        self.length = length
        self.rating = rating


    def __repr__(self):
        return f"{self.title}, a {self.genre} movie rated {self.rating}."


    def __eq__(self, other):
        return self.title == other.title and self.genre == other.genre

# Write the Streaming_Service class below as directed in the HW01 prompt


class Streaming_Service:

    def __init__(self, name, num_subs, movie_list):
        self.name = name
        self.num_subs = num_subs
        self.movie_list = [Movie(m[0], m[1], m[2], m[3]) for m in movie_list]
        self.avg_rating = round(sum([m.rating for m in self.movie_list]) / len(self.movie_list), 1)

    def __str__(self):
        return '{} is a streaming service with {} million users and an average movie rating of {}.'.format(self.name, self.num_subs, self.avg_rating)

    def __lt__(self, other):
        return self.num_subs < other.num_subs

    def add_subs(self, s_int):
        self.num_subs += s_int

    def genre_count_dict(self):
        res = {}
        for m in self.movie_list:
            if m.genre in res.keys():
                res[m.genre] += 1
            else:
                res[m.genre] = 1
        return res

    def add_movie(self, M):
        self.movie_list.append(M)
        self.avg_rating = round(sum([m.rating for m in self.movie_list]) / len(self.movie_list),1)





####################################
########## Test Cases ##############
####################################
'''
in order to use these, uncomment the necessary parameters and print statement
and then run your file through the command line
re-comment the test cases when your function is working properly
note: to test the other cases given in the prompt, simply copy and paste in the changed paramater
we recommend testing all test cases given in the prompt before submitting any function to gradescope
'''

if __name__ == '__main__':

    num_list = [1, 3.2, '2.8', '3']
    print(add_floats(num_list))

    str_list = ['a', 'b', 'c', '4']
    print(string_modifier(str_list))

    zip_list = ['30-328', '200aaa1+++5', '303%@%15', '30328', '3039,,,,,4', '99$)552', '-/-/3-/03++12']
    print(zip_counter(zip_list))

    print(directory(['Johnson Lopez', 'Shaka Johnson', 'Dennis Ott'], ['Johnson']))

    print(freezing(["Atlanta", "Portland", "Mobile", "Fargo"],[4,-1, 14, -10]))

    print(bill({"Burger" : 10, "Salmon" : 100, "Fries" : 50}, [10, 50, 25]))

    movie_list = [['Inception', 'Action', 162.6, 9.6], ['National Treasure', 'Mystery', 131.0, 10.0], ['The Notebook', 'Romance', 145.0, 7.3]]
    netflix = Streaming_Service('Netflix', 61.0, movie_list)
    print(netflix)

    mov1 = Movie('Elf', 'Comedy', 129, 9.8)
    netflix.add_movie(mov1)
    print(netflix.avg_rating)

    netflix.add_subs(1.5)
    print(netflix.num_subs)

    print(netflix.genre_count_dict())

    hulu = Streaming_Service('Hulu', 58.0, movie_list)
    print(hulu < netflix)

    ##### Do Not Comment or Delete the pass below #####
    pass
