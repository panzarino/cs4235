import hashlib
import json
import math
import os
import random
# You may NOT alter the import list!!!!
# Or import anything else!!!


class CryptoProject(object):

    def __init__(self):
        # TODO: Change this to YOUR Georgia Tech student ID!!!
        # Note that this is NOT your 9-digit Georgia Tech ID
        # self.student_id = 'bdornier3'  # for test_crypto_proj_1.py
        # self.student_id = 'ctaylor308'  # for test_crypto_proj_2.py
        self.student_id = 'zpanzarino3'

    def get_student_id_hash(self):
        return hashlib.sha224(self.student_id.encode('UTF-8')).hexdigest()

    def get_all_data_from_json(self, filename):
        data = None
        base_dir = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(base_dir, filename), 'r') as f:
            data = json.load(f)
        return data

    def get_data_from_json_for_student(self, filename):
        data = self.get_all_data_from_json(filename)
        name = self.get_student_id_hash()
        if name not in data:
            print(self.student_id + ' not in file ' + filename)
            return None
        else:
            return data[name]

    # TODO: OPTIONAL - Add helper functions below
    # BEGIN HELPER FUNCTIONS

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcde(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.gcde(b % a, a)
            return g, x - (b // a) * y, y

    def modinv(self, a, b):
        g, x, y = self.gcde(b, a)
        return x % a

    def root3(self, x):
        h = 1
        while h ** 3 <= x:
            h *= 2
        l = h // 2
        m = 0
        while l < h:
            m = (l + h) // 2
            if m ** 3 < x and l < m:
                l = m
            elif m ** 3 > x and h > m:
                h = m
            else:
                return m
        return m + 1

    # END HELPER FUNCTIONS

    def decrypt_message(self, N, e, d, c):
        # TODO: Implement this function for Task 1
        m = pow(c, d, N)

        return hex(m).rstrip('L')

    def crack_password_hash(self, password_hash, weak_password_list):
        # TODO: Implement this function for Task 2
        for password in weak_password_list:
            for salt in weak_password_list:
                hashed_password = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
                if (password_hash == hashed_password):
                    return password, salt
        return '', ''

    def get_factors(self, n):
        # TODO: Implement this function for Task 3
        p = int(n ** 0.5)
        if p % 2 == 0:
            p -= 1
        while (p > 0 and n % p != 0):
            p -= 2
            if (p == 1):
                p = 2
        q = n // p

        return p, q

    def get_private_key_from_p_q_e(self, p, q, e):
        # TODO: Implement this function for Task 3
        phi = (p - 1) * (q - 1)
        x = 1
        while (x % e != 0):
            x += phi
        d = x // e

        return d

    def is_waldo(self, n1, n2):
        # TODO: Implement this function for Task 4
        result = self.gcd(n1, n2) != 1

        return result

    def get_private_key_from_n1_n2_e(self, n1, n2, e):
        # TODO: Implement this function for Task 4
        p = self.gcd(n1, n2)
        q = n1 // p
        d = self.get_private_key_from_p_q_e(p, q, e)

        return d

    def recover_msg(self, N1, N2, N3, C1, C2, C3):
        # TODO: Implement this function for Task 5
        a = self.modinv(N1, N2 * N3) * N2 * N3
        b = self.modinv(N2, N1 * N3) * N1 * N3
        c = self.modinv(N3, N1 * N2) * N1 * N2
        m3 = (a * C1 + b * C2 + c * C3) % (N1 * N2 * N3)
        m = self.root3(m3)

        return m

    def task_1(self):
        data = self.get_data_from_json_for_student('keys4student_task_1.json')
        N = int(data['N'], 16)
        e = int(data['e'], 16)
        d = int(data['d'], 16)
        c = int(data['c'], 16)

        m = self.decrypt_message(N, e, d, c)
        return m

    def task_2(self):
        data = self.get_data_from_json_for_student('hashes4student_task_2.json')
        password_hash = data['password_hash']

        # The password list is prepopulated for your convenience
        weak_password_list = ['123456', '12345', '123456789', 'password', 'iloveyou', 'princess', '1234567', 'rockyou',
                              '12345678', 'abc123', 'nicole', 'daniel', 'babygirl', 'monkey', 'lovely', 'jessica',
                              '654321', 'michael', 'ashley', 'qwerty', '111111', 'iloveu', '0', 'michelle', 'tigger',
                              'sunshine', 'chocolate', 'password1', 'soccer', 'anthony', 'friends', 'butterfly',
                              'purple', 'angel', 'jordan', 'liverpool', 'justin', 'loveme', 'fuckyou', '123123',
                              'football', 'secret', 'andrea', 'carlos', 'jennifer', 'joshua', 'bubbles', '1234567890',
                              'superman', 'hannah', 'amanda', 'loveyou', 'pretty', 'basketball', 'andrew', 'angels',
                              'tweety', 'flower', 'playboy', 'hello', 'elizabeth', 'hottie', 'tinkerbell', 'charlie',
                              'samantha', 'barbie', 'chelsea', 'lovers', 'teamo', 'jasmine', 'brandon', '666666',
                              'shadow', 'melissa', 'eminem', 'matthew', 'robert', 'danielle', 'forever', 'family',
                              'jonathan', '987654321', 'computer', 'whatever', 'dragon', 'vanessa', 'cookie', 'naruto',
                              'summer', 'sweety', 'spongebob', 'joseph', 'junior', 'softball', 'taylor', 'yellow',
                              'daniela', 'lauren', 'mickey', 'princesa', 'alexandra', 'alexis', 'jesus', 'estrella',
                              'miguel', 'william', 'thomas', 'beautiful', 'mylove', 'angela', 'poohbear', 'patrick',
                              'iloveme', 'sakura', 'adrian', 'alexander', 'destiny', 'christian', '121212', 'sayang',
                              'america', 'dancer', 'monica', 'richard', '112233', 'princess1', '555555', 'diamond',
                              'carolina', 'steven', 'rangers', 'louise', 'orange', '789456', '999999', 'shorty',
                              '11111', 'nathan', 'snoopy', 'gabriel', 'hunter', 'cherry', 'killer', 'sandra',
                              'alejandro', 'buster', 'george', 'brittany', 'alejandra', 'patricia', 'rachel',
                              'tequiero', '7777777', 'cheese', '159753', 'arsenal', 'dolphin', 'antonio', 'heather',
                              'david', 'ginger', 'stephanie', 'peanut', 'blink182', 'sweetie', '222222', 'beauty',
                              '987654', 'victoria', 'honey', '0', 'fernando', 'pokemon', 'maggie', 'corazon', 'chicken',
                              'pepper', 'cristina', 'rainbow', 'kisses', 'manuel', 'myspace', 'rebelde', 'angel1',
                              'ricardo', 'babygurl', 'heaven', '55555', 'baseball', 'martin', 'greenday', 'november',
                              'alyssa', 'madison', 'mother', '123321', '123abc', 'mahalkita', 'batman', 'september',
                              'december', 'morgan', 'mariposa', 'maria', 'gabriela', 'iloveyou2', 'bailey', 'jeremy',
                              'pamela', 'kimberly', 'gemini', 'shannon', 'pictures', 'asshole', 'sophie', 'jessie',
                              'hellokitty', 'claudia', 'babygirl1', 'angelica', 'austin', 'mahalko', 'victor', 'horses',
                              'tiffany', 'mariana', 'eduardo', 'andres', 'courtney', 'booboo', 'kissme', 'harley',
                              'ronaldo', 'iloveyou1', 'precious', 'october', 'inuyasha', 'peaches', 'veronica', 'chris',
                              '888888', 'adriana', 'cutie', 'james', 'banana', 'prince', 'friend', 'jesus1', 'crystal',
                              'celtic', 'zxcvbnm', 'edward', 'oliver', 'diana', 'samsung', 'freedom', 'angelo',
                              'kenneth', 'master', 'scooby', 'carmen', '456789', 'sebastian', 'rebecca', 'jackie',
                              'spiderman', 'christopher', 'karina', 'johnny', 'hotmail', '123456789', 'school',
                              'barcelona', 'august', 'orlando', 'samuel', 'cameron', 'slipknot', 'cutiepie', 'monkey1',
                              '50cent', 'bonita', 'kevin', 'bitch', 'maganda', 'babyboy', 'casper', 'brenda', 'adidas',
                              'kitten', 'karen', 'mustang', 'isabel', 'natalie', 'cuteako', 'javier', '789456123',
                              '123654', 'sarah', 'bowwow', 'portugal', 'laura', '777777', 'marvin', 'denise', 'tigers',
                              'volleyball', 'jasper', 'rockstar', 'january', 'fuckoff', 'alicia', 'nicholas', 'flowers',
                              'cristian', 'tintin', 'bianca', 'chrisbrown', 'chester', '101010', 'smokey', 'silver',
                              'internet', 'sweet', 'strawberry', 'garfield', 'dennis', 'panget', 'francis', 'cassie',
                              'benfica', 'love123', '696969', 'asdfgh', 'lollipop', 'olivia', 'cancer', 'camila',
                              'qwertyuiop', 'superstar', 'harrypotter', 'ihateyou', 'charles', 'monique', 'midnight',
                              'vincent', 'christine', 'apples', 'scorpio', 'jordan23', 'lorena', 'andreea', 'mercedes',
                              'katherine', 'charmed', 'abigail', 'rafael', 'icecream', 'mexico', 'brianna', 'nirvana',
                              'aaliyah', 'pookie', 'johncena', 'lovelove', 'fucker', 'abcdef', 'benjamin', '131313',
                              'gangsta', 'brooke', '333333', 'hiphop', 'aaaaaa', 'mybaby', 'sergio', 'welcome',
                              'metallica', 'julian', 'travis', 'myspace1', 'babyblue', 'sabrina', 'michael1', 'jeffrey',
                              'stephen', 'love', 'dakota', 'catherine', 'badboy', 'fernanda', 'westlife', 'blondie',
                              'sasuke', 'smiley', 'jackson', 'simple', 'melanie', 'steaua', 'dolphins', 'roberto',
                              'fluffy', 'teresa', 'piglet', 'ronald', 'slideshow', 'asdfghjkl', 'minnie', 'newyork',
                              'jason', 'raymond', 'santiago', 'jayson', '88888888', '5201314', 'jerome', 'gandako',
                              'muffin', 'gatita', 'babyko', '246810', 'sweetheart', 'chivas', 'ladybug', 'kitty',
                              'popcorn', 'alberto', 'valeria', 'cookies', 'leslie', 'jenny', 'nicole1', '12345678910',
                              'leonardo', 'jayjay', 'liliana', 'dexter', 'sexygirl', '232323', 'amores', 'rockon',
                              'christ', 'babydoll', 'anthony1', 'marcus', 'bitch1', 'fatima', 'miamor', 'lover',
                              'chris1', 'single', 'eeyore', 'lalala', '252525', 'scooter', 'natasha', 'skittles',
                              'brooklyn', 'colombia', '159357', 'teddybear', 'winnie', 'happy', 'manutd', '123456a',
                              'britney', 'katrina', 'christina', 'pasaway', 'cocacola', 'mahal', 'grace', 'linda',
                              'albert', 'tatiana', 'london', 'cantik', '123456', 'lakers', 'marie', 'teiubesc',
                              '147258369', 'charlotte', 'natalia', 'francisco', 'amorcito', 'smile', 'paola',
                              'angelito', 'manchester', 'hahaha', 'elephant', 'mommy1', 'shelby', '147258', 'kelsey',
                              'genesis', 'amigos', 'snickers', 'xavier', 'turtle', 'marlon', 'linkinpark', 'claire',
                              'stupid', '147852', 'marina', 'garcia', 'fuckyou1', 'diego', 'brandy', 'letmein',
                              'hockey', '444444', 'sharon', 'bonnie', 'spider', 'iverson', 'andrei', 'justine',
                              'frankie', 'pimpin', 'disney', 'rabbit', '54321', 'fashion', 'soccer1', 'red123',
                              'bestfriend', 'england', 'hermosa', '456123', 'qazwsx', 'bandit', 'danny', 'allison',
                              'emily', '102030', 'lucky1', 'sporting', 'miranda', 'dallas', 'hearts', 'camille',
                              'wilson', 'potter', 'pumpkin', 'iloveu2', 'number1', 'katie', 'guitar', '212121',
                              'truelove', 'jayden', 'savannah', 'hottie1', 'phoenix', 'monster', 'player', 'ganda',
                              'people', 'scotland', 'nelson', 'jasmin', 'timothy', 'onelove', 'ilovehim', 'shakira',
                              'estrellita', 'bubble', 'smiles', 'brandon1', 'sparky', 'barney', 'sweets', 'parola',
                              'evelyn', 'familia', 'love12', 'nikki', 'motorola', 'florida', 'omarion', 'monkeys',
                              'loverboy', 'elijah', 'joanna', 'canada', 'ronnie', 'mamita', 'emmanuel', 'thunder',
                              '999999999', 'broken', 'rodrigo', 'maryjane', 'westside', 'california', 'lucky',
                              'mauricio', 'yankees', 'jackass', 'jamaica', 'justin1', 'amigas', 'preciosa', 'shopping',
                              'flores', 'mariah', 'matrix', 'isabella', 'tennis', 'trinity', 'jorge', 'sunflower',
                              'kathleen', 'bradley', 'cupcake', 'hector', 'martinez', 'elaine', 'robbie', 'friendster',
                              'cheche', 'gracie', 'connor', 'hello1', 'valentina', 'melody', 'darling', 'sammy',
                              'jamie', 'santos', 'abcdefg', 'joanne', 'candy', 'fuckyou2', 'loser', 'dominic',
                              'pebbles', 'sunshine1', 'swimming', 'millie', 'loving', 'gangster', 'blessed', 'compaq',
                              'taurus', 'gloria', 'tyler', 'aaron', 'darkangel', 'kitkat', 'megan', 'dreams',
                              'sweetpea', 'bettyboop', 'jessica1', 'cynthia', 'cheyenne', 'ferrari', 'dustin', 'iubire',
                              'a123456', 'snowball', 'purple1', 'violet', 'darren', 'starwars', 'bestfriends', 'inlove',
                              'kelly', 'batista', 'karla', 'sophia', 'chacha', 'biteme', 'marian', 'sydney', 'sexyme',
                              'pogiako', 'gerald', 'jordan1', '10203', 'daddy1', 'zachary', 'daddysgirl', 'billabong',
                              'carebear', 'froggy', 'pinky', 'erika', 'oscar', 'skater', 'raiders', 'nenita', 'tigger1',
                              'ashley1', 'charlie1', 'gatito', 'lokita', 'maldita', 'buttercup', 'nichole', 'bambam',
                              'nothing', 'glitter', 'bella', 'amber', 'apple', '123789', 'sister', 'zacefron',
                              'tokiohotel', 'loveya', 'lindsey', 'money', 'lovebug', 'bubblegum', 'marissa', 'dreamer',
                              'darkness', 'cecilia', 'lollypop', 'nicolas', 'google', 'lindsay', 'cooper', 'passion',
                              'kristine', 'green', 'puppies', 'ariana', 'fuckme', 'chubby', 'raquel', 'lonely',
                              'anderson', 'sammie', 'sexybitch', 'mario', 'butter', 'willow', 'roxana', 'mememe',
                              'caroline', 'susana', 'kristen', 'baller', 'hotstuff', 'carter', 'stacey', 'babylove',
                              'angelina', 'miller', 'scorpion', 'sierra', 'playgirl', 'sweet16', '12345', 'rocker',
                              'bhebhe', 'gustavo', 'marcos', 'chance', '123qwe', 'kayla', 'james1', 'football1',
                              'eagles', 'loveme1', 'milagros', 'stella', 'lilmama', 'beyonce', 'lovely1', 'rocky',
                              'daddy', 'catdog', 'armando', 'margarita', '151515', 'loves', 'lolita', '202020',
                              'gerard', 'undertaker', 'amistad', 'williams', 'qwerty1', 'freddy', 'capricorn',
                              'caitlin', 'bryan', 'delfin', 'dance', 'cheerleader', 'password2', 'PASSWORD', 'martha',
                              'lizzie', 'georgia', 'matthew1', 'enrique', 'zxcvbn', 'badgirl', 'andrew1', '141414',
                              '11111111', 'dancing', 'cuteme', 'booger', 'amelia', 'vampire', 'skyline', 'chiquita',
                              'angeles', 'scoobydoo', 'janine', 'tamara', 'carlitos', 'money1', 'sheila', 'justme',
                              'ireland', 'kittycat', 'hotdog', 'yamaha', 'tristan', 'harvey', 'israel', 'legolas',
                              'michelle1', 'maddie', 'angie', 'cinderella', 'jesuschrist', 'lester', 'ashton',
                              'ilovejesus', 'tazmania', 'remember', 'xxxxxx', 'tekiero', 'thebest', 'princesita',
                              'lucky7', 'jesucristo', 'peewee', 'paloma', 'buddy1', 'deedee', 'miriam', 'april',
                              'patches', 'regina', 'janice', 'cowboys', 'myself', 'lipgloss', 'jazmin', 'rosita',
                              'happy1', 'felipe', 'chichi', 'pangit', 'mierda', 'genius', '741852963', 'hernandez',
                              'awesome', 'walter', 'tinker', 'arturo', 'silvia', 'melvin', 'celeste', 'pussycat',
                              'gorgeous', 'david1', 'molly', 'honeyko', 'mylife', 'animal', 'penguin', 'babyboo',
                              'loveu', 'simpsons', 'lupita', 'boomer', 'panthers', 'hollywood', 'alfredo', 'musica',
                              'johnson', 'ilovegod', 'hawaii', 'sparkle', 'kristina', 'sexymama', 'crazy', 'valerie',
                              'spencer', 'scarface', 'hardcore', '98765', '0', 'winter', 'hailey', 'trixie', 'hayden',
                              'micheal', 'wesley', '242424', '987654321', 'marisol', 'nikita', 'daisy', 'jeremiah',
                              'pineapple', 'mhine', 'isaiah', 'christmas', 'cesar', 'lolipop', 'butterfly1', 'chloe',
                              'lawrence', 'xbox360', 'sheena', 'murphy', 'madalina', 'anamaria', 'gateway', 'debbie',
                              'yourmom', 'blonde', 'jasmine1', 'please', 'bubbles1', 'jimmy', 'beatriz', 'poopoo',
                              'diamonds', 'whitney', 'friendship', 'sweetness', 'pauline', 'desiree', 'trouble',
                              '741852', 'united', 'marley', 'brian', 'barbara', 'hannah1', 'bananas', 'julius',
                              'leanne', 'sandy', 'marie1', 'anita', 'lover1', 'chicago', 'twinkle', 'pantera',
                              'february', 'birthday', 'shadow1', 'qwert', 'bebita', '87654321', 'twilight', 'imissyou',
                              'pollito', 'ashlee', 'tucker', 'cookie1', 'shelly', 'catalina', '147852369', 'beckham',
                              'simone', 'nursing', 'iloveyou!', 'eugene', 'torres', 'damian', '123123123', 'joshua1',
                              'bobby', 'babyface', 'andre', 'donald', 'daniel1', 'panther', 'dinamo', 'mommy',
                              'juliana', 'cassandra']

        password, salt = self.crack_password_hash(password_hash, weak_password_list)

        return password, salt

    def task_3(self):
        data = self.get_data_from_json_for_student('keys4student_task_3.json')
        n = int(data['N'], 16)
        e = int(data['e'], 16)

        p, q = self.get_factors(n)
        d = self.get_private_key_from_p_q_e(p, q, e)

        return hex(d).rstrip('L')

    def task_4(self):
        all_data = self.get_all_data_from_json('keys4student_task_4.json')
        student_data = self.get_data_from_json_for_student('keys4student_task_4.json')
        n1 = int(student_data['N'], 16)
        e = int(student_data['e'], 16)

        d = 0
        waldo = 'Dolores'

        for classmate in all_data:
            if classmate == self.get_student_id_hash():
                continue
            n2 = int(all_data[classmate]['N'], 16)

            if self.is_waldo(n1, n2):
                waldo = classmate
                d = self.get_private_key_from_n1_n2_e(n1, n2, e)
                break

        return hex(d).rstrip("L"), waldo

    def task_5(self):
        data = self.get_data_from_json_for_student('keys4student_task_5.json')
        N1 = int(data['N0'], 16)
        N2 = int(data['N1'], 16)
        N3 = int(data['N2'], 16)
        C1 = int(data['C0'], 16)
        C2 = int(data['C1'], 16)
        C3 = int(data['C2'], 16)

        m = self.recover_msg(N1, N2, N3, C1, C2, C3)
        # Convert the int to a message string
        msg = bytes.fromhex(hex(m).rstrip('L')[2:]).decode('UTF-8')

        return msg
