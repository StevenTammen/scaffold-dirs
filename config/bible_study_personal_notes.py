from .classes import *
from .utility_functions import *

subdirs_dict = {
    'Genesis': 50,
    'Exodus': 40,
    'Leviticus': 27,
    'Numbers': 36,
    'Deuteronomy': 34,
    'Joshua': 24,
    'Judges': 21,
    'Ruth': 4,
    '1 Samuel': 31,
    '2 Samuel': 24,
    '1 Kings': 22,
    '2 Kings': 25,
    '1 Chronicles': 29,
    '2 Chronicles': 36,
    'Ezra': 10,
    'Nehemiah': 13,
    'Esther': 10,
    'Job': 42,
    'Psalms': 150,
    'Proverbs': 31,
    'Ecclesiastes': 12,
    'Song of Solomon': 8,
    'Isaiah': 66,
    'Jeremiah': 52,
    'Lamentations': 5,
    'Ezekiel': 48,
    'Daniel': 12,
    'Hosea': 14,
    'Joel': 3,
    'Amos': 9,
    'Obadiah': 1,
    'Jonah': 4,
    'Micah': 7,
    'Nahum': 3,
    'Habakkuk': 3,
    'Zephaniah': 3,
    'Haggai': 2,
    'Zechariah': 14,
    'Malachi': 4,
    'Matthew': 28,
    'Mark': 16,
    'Luke': 24,
    'John': 21,
    'Acts': 28,
    'Romans': 16,
    '1 Corinthians': 16,
    '2 Corinthians': 13,
    'Galatians': 6,
    'Ephesians': 6,
    'Philippians': 4,
    'Colossians': 4,
    '1 Thessalonians': 5,
    '2 Thessalonians': 3,
    '1 Timothy': 6,
    '2 Timothy': 4,
    'Titus': 3,
    'Philemon': 1,
    'Hebrews': 13,
    'James': 5,
    '1 Peter': 5,
    '2 Peter': 3,
    '1 John': 5,
    '2 John': 1,
    '3 John': 1,
    'Jude': 1,
    'Revelation': 22
}

base_dir = Dir('personal-notes')
base_dir.subdirs = build_parallel_subdirs(subdirs_dict, 'chapter-notes', 'Personal Notes')



# # This is if you want things to be prefixed with the book sequence number (not recommended really, but this is how you'd do it)

# subdirs_list = [
#     ('Genesis', 50),
#     ('Exodus', 40),
#     ('Leviticus', 27),
#     ('Numbers', 36),
#     ('Deuteronomy', 34),
#     ('Joshua', 24),
#     ('Judges', 21),
#     ('Ruth', 4),
#     ('1 Samuel', 31),
#     ('2 Samuel', 24),
#     ('1 Kings', 22),
#     ('2 Kings', 25),
#     ('1 Chronicles', 29),
#     ('2 Chronicles', 36),
#     ('Ezra', 10),
#     ('Nehemiah', 13),
#     ('Esther', 10),
#     ('Job', 42),
#     ('Psalms', 150),
#     ('Proverbs', 31),
#     ('Ecclesiastes', 12),
#     ('Song of Solomon', 8),
#     ('Isaiah', 66),
#     ('Jeremiah', 52),
#     ('Lamentations', 5),
#     ('Ezekiel', 48),
#     ('Daniel', 12),
#     ('Hosea', 14),
#     ('Joel', 3),
#     ('Amos', 9),
#     ('Obadiah', 1),
#     ('Jonah', 4),
#     ('Micah', 7),
#     ('Nahum', 3),
#     ('Habakkuk', 3),
#     ('Zephaniah', 3),
#     ('Haggai', 2),
#     ('Zechariah', 14),
#     ('Malachi', 4),
#     ('Matthew', 28),
#     ('Mark', 16),
#     ('Luke', 24),
#     ('John', 21),
#     ('Acts', 28),
#     ('Romans', 16),
#     ('1 Corinthians', 16),
#     ('2 Corinthians', 13),
#     ('Galatians', 6),
#     ('Ephesians', 6),
#     ('Philippians', 4),
#     ('Colossians', 4),
#     ('1 Thessalonians', 5),
#     ('2 Thessalonians', 3),
#     ('1 Timothy', 6),
#     ('2 Timothy', 4),
#     ('Titus', 3),
#     ('Philemon', 1),
#     ('Hebrews', 13),
#     ('James', 5),
#     ('1 Peter', 5),
#     ('2 Peter', 3),
#     ('1 John', 5),
#     ('2 John', 1),
#     ('3 John', 1),
#     ('Jude', 1),
#     ('Revelation', 22),
# ]

# base_dir = Dir('personal-notes')
# base_dir.subdirs = build_ordered_parallel_subdirs(subdirs_list, 'chapter-notes')



# # This is the manual way. REALLY not recommended

# genesis = Dir('genesis')
# genesis.leaves = build_parameterized_leaves(string_list(range_count(1, 50)), 'genesis-[id]', 'Genesis [id]', 'chapter-notes')

# exodus = Dir('exodus')
# exodus.leaves = build_parameterized_leaves(string_list(range_count(1, 40)), 'exodus-[id]', 'Exodus [id]', 'chapter-notes')

# leviticus = Dir('leviticus')
# leviticus.leaves = build_parameterized_leaves(string_list(range_count(1, 27)), 'leviticus-[id]', 'Leviticus [id]', 'chapter-notes')

# numbers = Dir('numbers')
# numbers.leaves = build_parameterized_leaves(string_list(range_count(1, 36)), 'numbers-[id]', 'Numbers [id]', 'chapter-notes')

# deuteronomy = Dir('deuteronomy')
# deuteronomy.leaves = build_parameterized_leaves(string_list(range_count(1, 34)), 'deuteronomy-[id]', 'Deuteronomy [id]', 'chapter-notes')

# joshua = Dir('joshua')
# joshua.leaves = build_parameterized_leaves(string_list(range_count(1, 24)), 'joshua-[id]', 'Joshua [id]', 'chapter-notes')

# judges = Dir('judges')
# judges.leaves = build_parameterized_leaves(string_list(range_count(1, 21)), 'judges-[id]', 'Judges [id]', 'chapter-notes')

# ruth = Dir('ruth')
# ruth.leaves = build_parameterized_leaves(string_list(range_count(1, 4)), 'ruth-[id]', 'Ruth [id]', 'chapter-notes')

# first_samuel = Dir('1-samuel')
# first_samuel.leaves = build_parameterized_leaves(string_list(range_count(1, 31)), '1-samuel-[id]', '1 Samuel [id]', 'chapter-notes')

# second_samuel = Dir('2-samuel')
# second_samuel.leaves = build_parameterized_leaves(string_list(range_count(1, 24)), '2-samuel-[id]', '2 Samuel [id]', 'chapter-notes')

# first_kings = Dir('1-kings')
# first_kings.leaves = build_parameterized_leaves(string_list(range_count(1, 22)), '1-kings-[id]', '1 Kings [id]', 'chapter-notes')

# second_kings = Dir('2-kings')
# second_kings.leaves = build_parameterized_leaves(string_list(range_count(1, 25)), '2-kings-[id]', '2 Kings [id]', 'chapter-notes')

# first_chronicles = Dir('1-chronicles')
# first_chronicles.leaves = build_parameterized_leaves(string_list(range_count(1, 29)), '1-chronicles-[id]', '1 Chronicles [id]', 'chapter-notes')

# second_chronicles = Dir('2-chronicles')
# second_chronicles.leaves = build_parameterized_leaves(string_list(range_count(1, 36)), '2-chronicles-[id]', '2 Chronicles [id]', 'chapter-notes')

# ezra = Dir('ezra')
# ezra.leaves = build_parameterized_leaves(string_list(range_count(1, 10)), 'ezra-[id]', 'Ezra [id]', 'chapter-notes')

# nehemiah = Dir('nehemiah')
# nehemiah.leaves = build_parameterized_leaves(string_list(range_count(1, 13)), 'nehemiah-[id]', 'Nehemiah [id]', 'chapter-notes')

# esther = Dir('esther')
# esther.leaves = build_parameterized_leaves(string_list(range_count(1, 10)), 'esther-[id]', 'Esther [id]', 'chapter-notes')

# job = Dir('job')
# job.leaves = build_parameterized_leaves(string_list(range_count(1, 42)), 'job-[id]', 'Job [id]', 'chapter-notes')

# psalms = Dir('psalms')
# psalms.leaves = build_parameterized_leaves(string_list(range_count(1, 150)), 'psalms-[id]', 'Psalms [id]', 'chapter-notes')

# proverbs = Dir('proverbs')
# proverbs.leaves = build_parameterized_leaves(string_list(range_count(1, 31)), 'proverbs-[id]', 'Proverbs [id]', 'chapter-notes')

# ecclesiastes = Dir('ecclesiastes')
# ecclesiastes.leaves = build_parameterized_leaves(string_list(range_count(1, 12)), 'ecclesiastes-[id]', 'Ecclesiastes [id]', 'chapter-notes')

# song_of_solomon = Dir('song-of-solomon')
# song_of_solomon.leaves = build_parameterized_leaves(string_list(range_count(1, 8)), 'song-of-solomon-[id]', 'Song of Solomon [id]', 'chapter-notes')

# isaiah = Dir('isaiah')
# isaiah.leaves = build_parameterized_leaves(string_list(range_count(1, 66)), 'isaiah-[id]', 'Isaiah [id]', 'chapter-notes')

# jeremiah = Dir('jeremiah')
# jeremiah.leaves = build_parameterized_leaves(string_list(range_count(1, 52)), 'jeremiah-[id]', 'Jeremiah [id]', 'chapter-notes')

# lamentations = Dir('lamentations')
# lamentations.leaves = build_parameterized_leaves(string_list(range_count(1, 5)), 'lamentations-[id]', 'Lamentations [id]', 'chapter-notes')

# ezekiel = Dir('ezekiel')
# ezekiel.leaves = build_parameterized_leaves(string_list(range_count(1, 48)), 'ezekiel-[id]', 'Ezekiel [id]', 'chapter-notes')

# daniel = Dir('daniel')
# daniel.leaves = build_parameterized_leaves(string_list(range_count(1, 12)), 'daniel-[id]', 'Daniel [id]', 'chapter-notes')

# hosea = Dir('hosea')
# hosea.leaves = build_parameterized_leaves(string_list(range_count(1, 14)), 'hosea-[id]', 'Hosea [id]', 'chapter-notes')

# joel = Dir('joel')
# joel.leaves = build_parameterized_leaves(string_list(range_count(1, 3)), 'joel-[id]', 'Joel [id]', 'chapter-notes')

# amos = Dir('amos')
# amos.leaves = build_parameterized_leaves(string_list(range_count(1, 9)), 'amos-[id]', 'Amos [id]', 'chapter-notes')

# obadiah = Dir('obadiah')
# obadiah.leaves = build_parameterized_leaves(string_list(range_count(1, 1)), 'obadiah-[id]', 'Obadiah [id]', 'chapter-notes')

# jonah = Dir('jonah')
# jonah.leaves = build_parameterized_leaves(string_list(range_count(1, 4)), 'jonah-[id]', 'Jonah [id]', 'chapter-notes')

# micah = Dir('micah')
# micah.leaves = build_parameterized_leaves(string_list(range_count(1, 7)), 'micah-[id]', 'Micah [id]', 'chapter-notes')

# nahum = Dir('nahum')
# nahum.leaves = build_parameterized_leaves(string_list(range_count(1, 3)), 'nahum-[id]', 'Nahum [id]', 'chapter-notes')

# habakkuk = Dir('habakkuk')
# habakkuk.leaves = build_parameterized_leaves(string_list(range_count(1, 3)), 'habakkuk-[id]', 'Habakkuk [id]', 'chapter-notes')

# zephaniah = Dir('zephaniah')
# zephaniah.leaves = build_parameterized_leaves(string_list(range_count(1, 3)), 'zephaniah-[id]', 'Zephaniah [id]', 'chapter-notes')

# haggai = Dir('haggai')
# haggai.leaves = build_parameterized_leaves(string_list(range_count(1, 2)), 'haggai-[id]', 'Haggai [id]', 'chapter-notes')

# zechariah = Dir('zechariah')
# zechariah.leaves = build_parameterized_leaves(string_list(range_count(1, 14)), 'zechariah-[id]', 'Zechariah [id]', 'chapter-notes')

# malachi = Dir('malachi')
# malachi.leaves = build_parameterized_leaves(string_list(range_count(1, 4)), 'malachi-[id]', 'Malachi [id]', 'chapter-notes')

# matthew = Dir('matthew')
# matthew.leaves = build_parameterized_leaves(string_list(range_count(1, 28)), 'matthew-[id]', 'Matthew [id]', 'chapter-notes')

# mark = Dir('mark')
# mark.leaves = build_parameterized_leaves(string_list(range_count(1, 16)), 'mark-[id]', 'Mark [id]', 'chapter-notes')

# luke = Dir('luke')
# luke.leaves = build_parameterized_leaves(string_list(range_count(1, 24)), 'luke-[id]', 'Luke [id]', 'chapter-notes')

# john = Dir('john')
# john.leaves = build_parameterized_leaves(string_list(range_count(1, 21)), 'john-[id]', 'John [id]', 'chapter-notes')

# acts = Dir('acts')
# acts.leaves = build_parameterized_leaves(string_list(range_count(1, 28)), 'acts-[id]', 'Acts [id]', 'chapter-notes')

# romans = Dir('romans')
# romans.leaves = build_parameterized_leaves(string_list(range_count(1, 16)), 'romans-[id]', 'Romans [id]', 'chapter-notes')

# first_corinthians = Dir('1-corinthians')
# first_corinthians.leaves = build_parameterized_leaves(string_list(range_count(1, 16)), '1-corinthians-[id]', '1 Corinthians [id]', 'chapter-notes')

# second_corinthians = Dir('2-corinthians')
# second_corinthians.leaves = build_parameterized_leaves(string_list(range_count(1, 13)), '2-corinthians-[id]', '2 Corinthians [id]', 'chapter-notes')

# galatians = Dir('galatians')
# galatians.leaves = build_parameterized_leaves(string_list(range_count(1, 6)), 'galatians-[id]', 'Galatians [id]', 'chapter-notes')

# ephesians = Dir('ephesians')
# ephesians.leaves = build_parameterized_leaves(string_list(range_count(1, 6)), 'ephesians-[id]', 'Ephesians [id]', 'chapter-notes')

# philippians = Dir('philippians')
# philippians.leaves = build_parameterized_leaves(string_list(range_count(1, 4)), 'philippians-[id]', 'Philippians [id]', 'chapter-notes')

# colossians = Dir('colossians')
# colossians.leaves = build_parameterized_leaves(string_list(range_count(1, 4)), 'colossians-[id]', 'Colossians [id]', 'chapter-notes')

# first_thessalonians = Dir('1-thessalonians')
# first_thessalonians.leaves = build_parameterized_leaves(string_list(range_count(1, 5)), '1-thessalonians-[id]', '1 Thessalonians [id]', 'chapter-notes')

# second_thessalonians = Dir('2-thessalonians')
# second_thessalonians.leaves = build_parameterized_leaves(string_list(range_count(1, 3)), '2-thessalonians-[id]', '2 Thessalonians [id]', 'chapter-notes')

# first_timothy = Dir('1-timothy')
# first_timothy.leaves = build_parameterized_leaves(string_list(range_count(1, 6)), '1-timothy-[id]', '1 Timothy [id]', 'chapter-notes')

# second_timothy = Dir('2-timothy')
# second_timothy.leaves = build_parameterized_leaves(string_list(range_count(1, 4)), '2-timothy-[id]', '2 Timothy [id]', 'chapter-notes')

# titus = Dir('titus')
# titus.leaves = build_parameterized_leaves(string_list(range_count(1, 3)), 'titus-[id]', 'Titus [id]', 'chapter-notes')

# philemon = Dir('philemon')
# philemon.leaves = build_parameterized_leaves(string_list(range_count(1, 1)), 'philemon-[id]', 'Philemon [id]', 'chapter-notes')

# hebrews = Dir('hebrews')
# hebrews.leaves = build_parameterized_leaves(string_list(range_count(1, 13)), 'hebrews-[id]', 'Hebrews [id]', 'chapter-notes')

# james = Dir('james')
# james.leaves = build_parameterized_leaves(string_list(range_count(1, 5)), 'james-[id]', 'James [id]', 'chapter-notes')

# first_peter = Dir('1-peter')
# first_peter.leaves = build_parameterized_leaves(string_list(range_count(1, 5)), '1-peter-[id]', '1 Peter [id]', 'chapter-notes')

# second_peter = Dir('2-peter')
# second_peter.leaves = build_parameterized_leaves(string_list(range_count(1, 3)), '2-peter-[id]', '2 Peter [id]', 'chapter-notes')

# first_john = Dir('1-john')
# first_john.leaves = build_parameterized_leaves(string_list(range_count(1, 5)), '1-john-[id]', '1 John [id]', 'chapter-notes')

# second_john = Dir('2-john')
# second_john.leaves = build_parameterized_leaves(string_list(range_count(1, 1)), '2-john-[id]', '2 John [id]', 'chapter-notes')

# third_john = Dir('3-john')
# third_john.leaves = build_parameterized_leaves(string_list(range_count(1, 1)), '3-john-[id]', '3 John [id]', 'chapter-notes')

# jude = Dir('jude')
# jude.leaves = build_parameterized_leaves(string_list(range_count(1, 1)), 'jude-[id]', 'Jude [id]', 'chapter-notes')

# revelation = Dir('revelation')
# revelation.leaves = build_parameterized_leaves(string_list(range_count(1, 22)), 'revelation-[id]', 'Revelation [id]', 'chapter-notes')

# base_dir = Dir('personal-notes')
# base_dir.subdirs = [
#     genesis,
#     exodus,
#     leviticus,
#     numbers,
#     deuteronomy,
#     joshua,
#     judges,
#     ruth,
#     first_samuel,
#     second_samuel,
#     first_kings,
#     second_kings,
#     first_chronicles,
#     second_chronicles,
#     ezra,
#     nehemiah,
#     esther,
#     job,
#     psalms,
#     proverbs,
#     ecclesiastes,
#     song_of_solomon,
#     isaiah,
#     jeremiah,
#     lamentations,
#     ezekiel,
#     daniel,
#     hosea,
#     joel,
#     amos,
#     obadiah,
#     jonah,
#     micah,
#     nahum,
#     habakkuk,
#     zephaniah,
#     haggai,
#     zechariah,
#     malachi,
#     matthew,
#     mark,
#     luke,
#     john,
#     acts,
#     romans,
#     first_corinthians,
#     second_corinthians,
#     galatians,
#     ephesians,
#     philippians,
#     colossians,
#     first_thessalonians,
#     second_thessalonians,
#     first_timothy,
#     second_timothy,
#     titus,
#     philemon,
#     hebrews,
#     james,
#     first_peter,
#     second_peter,
#     first_john,
#     second_john,
#     third_john,
#     jude,
#     revelation
# ]