from .classes import *

# To quickly get things in the right format:
#   - Copy-paste study titles into a text file
#   - Use multiple cursors to quickly process all of them at the same time to remove everything but the main title part
#     - In VSCode, for example, you can put the cursor at the beginning of a line, and use Ctrl + Alt + Down to make multiple
#       cursors at the beginning of each following line
#     - Then use (Ctrl) + Left/Right to move, and (Ctrl) + Shift + Left/Right to select things to delete
#   - After cleaning up the titles, paste them into a spreadsheet program. Scaffold id column in the spreadsheet
#     using a formula like A2 = A1 + 1, if it is strictly numerical. Otherwise (if it is something more like
#     1a, 1b, 2a, ..., etc.), hand create this column
#   - Get the lower kabob-case form of the titles by processing your title list with
#     https://atakanau.blogspot.com/2019/03/convert-multiline-text-to-slug.html
#   - Then paste your slugified titles into another column in your spreadsheet
#   - Then use the & operator in your spreadsheet to build the LeafFile lines. The formula will look something like
#     = "LeafFile('"&A1&"', '"&A1&"-"&B1&"', '"&A1&" - "&C1&"', 'study'),"
#   - Then past the lines into this file, delete the trailing comma, and use Tab to indent as necessary
#   - Backslash escape any apostrophes, if necessary


peter_series = Dir('peter-series')
peter_series.leaves = [
    LeafFile('pet1', 'pet1-introduction', 'PET1 - Introduction', 'study'),
    LeafFile('pet2', 'pet2-peter-the-apostle-of-suffering', 'PET2 - Peter the Apostle of Suffering', 'study'),
    LeafFile('pet3', 'pet3-the-plan-of-god', 'PET3 - The Plan of God', 'study'),
    LeafFile('pet4', 'pet4-categories-of-suffering', 'PET4 - Categories of Suffering', 'study'),
    LeafFile('pet5', 'pet5-reasons-for-suffering', 'PET5 - Reasons for Suffering', 'study'),
    LeafFile('pet6', 'pet6-grace-in-suffering', 'PET6 - Grace in Suffering', 'study'),
    LeafFile('pet7', 'pet7-the-ministry-of-the-holy-spirit', 'PET7 - The Ministry of the Holy Spirit', 'study'),
    LeafFile('pet8', 'pet8-results-of-our-election', 'PET8 - Results of our Election', 'study'),
    LeafFile('pet9', 'pet9-faith-and-the-blood-of-christ', 'PET9 - Faith and the Blood of Christ', 'study'),
    LeafFile('pet10', 'pet10-spiritual-growth', 'PET10 - Spiritual Growth', 'study'),
    LeafFile('pet11', 'pet11-natural-and-special-revelation', 'PET11 - Natural and Special Revelation', 'study'),
    LeafFile('pet12', 'pet12-the-parable-of-the-sower', 'PET12 - The Parable of the Sower', 'study'),
    LeafFile('pet13', 'pet13-sanctification', 'PET13 - Sanctification', 'study'),
    LeafFile('pet14', 'pet14-faith-and-spiritual-growth', 'PET14 - Faith and Spiritual Growth', 'study'),
    LeafFile('pet15', 'pet15-confession-of-sin', 'PET15 - Confession of Sin', 'study'),
    LeafFile('pet16', 'pet16-leadership-of-the-spirit', 'PET16 - Leadership of the Spirit', 'study'),
    LeafFile('pet17', 'pet17-imitating-christ', 'PET17 - Imitating Christ', 'study'),
    LeafFile('pet18', 'pet18-eternal-rewards', 'PET18 - Eternal Rewards', 'study'),
    LeafFile('pet19', 'pet19-spiritual-rebirth', 'PET19 - Spiritual Rebirth', 'study'),
    LeafFile('pet20', 'pet20-resurrection', 'PET20 - Resurrection', 'study'),
    LeafFile('pet21', 'pet21-perseverance-of-faith', 'PET21 - Perseverance of Faith', 'study'),
    LeafFile('pet22', 'pet22-testing-of-faith', 'PET22 - Testing of Faith', 'study'),
    LeafFile('pet23', 'pet23-seeing-with-faith', 'PET23 - Seeing with Faith', 'study'),
    LeafFile('pet24', 'pet24-faith-dynamics', 'PET24 - Faith Dynamics', 'study'),
    LeafFile('pet25', 'pet25-personal-tribulation', 'PET25 - Personal Tribulation', 'study'),
    LeafFile('pet26', 'pet26-reacting-to-tribulation', 'PET26 - Reacting to Tribulation', 'study'),
    LeafFile('pet27', 'pet27-three-false-doctrines', 'PET27 - Three False Doctrines', 'study'),
    LeafFile('pet28', 'pet28-personal-salvation-and-progressive-revelation', 'PET28 - Personal Salvation and Progressive Revelation', 'study'),
    LeafFile('pet29', 'pet29-maintaining-a-sound-christian-offense-in-our-spiritual-warfare', 'PET29 - Maintaining a Sound Christian Offense in our Spiritual Warfare', 'study'),
    LeafFile('pet30', 'pet30-sanctification-in-time:-christian-defense-in-our-spiritual-warfare', 'PET30 - Sanctification in Time: Christian Defense in our Spiritual Warfare', 'study'),
    LeafFile('pet31', 'pet31-basic-christian-orientation-to-life-and-eternity', 'PET31 - Basic Christian Orientation to Life and Eternity', 'study'),
    LeafFile('pet32', 'pet32-a-challenge-to-grow-spiritually', 'PET32 - A Challenge to Grow Spiritually', 'study'),
    LeafFile('pet33', 'pet33-three-analogies-for-the-christian-life', 'PET33 - Three Analogies for the Christian Life', 'study'),
    LeafFile('pet34', 'pet34-a-christian-code-of-conduct', 'PET34 - A Christian Code of Conduct', 'study'),
    LeafFile('pet35', 'pet35-undeserved-suffering-in-marriage-and-in-life-and-the-example-of-christ', 'PET35 - Undeserved Suffering in Marriage and in Life – and the Example of Christ', 'study'),
    LeafFile('pet36', 'pet36-undeserved-suffering-on-the-cusp-of-the-end-times', 'PET36 - Undeserved Suffering on the Cusp of the End Times', 'study'),
    LeafFile('pet37', 'pet37-shepherding-the-flock-and-resisting-the-devil', 'PET37 - Shepherding the Flock and Resisting the Devil', 'study'),
    LeafFile('pet38', 'pet38-the-primacy-of-the-word-of-god', 'PET38 - The Primacy of the Word of God', 'study'),
    LeafFile('pet39', 'pet39-false-teachers-false-teaching-and-false-organizations-a-preface-to-2-peter-chapter-two', 'PET39 - False Teachers, False Teaching, and False Organizations - a Preface to 2 Peter chapter two', 'study'),
    LeafFile('pet40', 'pet40-false-teachers-and-false-teaching', 'PET40 - False Teachers and False Teaching', 'study'),
    LeafFile('pet41', 'pet41-the-day-of-the-lord-perspective', 'PET41 - The Day of the Lord Perspective', 'study')
]

bible_basics = Dir('bible-basics')
bible_basics.leaves = [
    LeafFile('bb1', 'bb1-theology', 'BB1 - Theology', 'study'),
    LeafFile('bb2a', 'bb2a-angelology', 'BB2A - Angelology', 'study'),
    LeafFile('bb2b', 'bb2b-eschatology', 'BB2B - Eschatology', 'study'),
    LeafFile('bb3a', 'bb3a-anthropology', 'BB3A - Anthropology', 'study'),
    LeafFile('bb3b', 'bb3b-hamartiology', 'BB3B - Hamartiology', 'study'),
    LeafFile('bb4a', 'bb4a-christology', 'BB4A - Christology', 'study'),
    LeafFile('bb4b', 'bb4b-soteriology', 'BB4B - Soteriology', 'study'),
    LeafFile('bb5', 'bb5-pneumatology', 'BB5 - Pneumatology', 'study'),
    LeafFile('bb6a', 'bb6a-peripateology', 'BB6A - Peripateology', 'study'),
    LeafFile('bb6b', 'bb6b-ecclesiology', 'BB6B - Ecclesiology', 'study'),
    LeafFile('bb7', 'bb7-bibliology', 'BB7 - Bibliology', 'study')
]

satanic_rebellion = Dir('satanic-rebellion')
satanic_rebellion.leaves = [
    LeafFile('sr1', 'sr1-satans-rebellion-and-fall', 'SR1 - Satan\'s Rebellion and Fall', 'study'),
    LeafFile('sr2', 'sr2-the-genesis-gap', 'SR2 - The Genesis Gap', 'study'),
    LeafFile('sr3', 'sr3-the-purpose-creation-and-fall-of-man', 'SR3 - The Purpose, Creation, and Fall of Man', 'study'),
    LeafFile('sr4', 'sr4-satans-world-system', 'SR4 - Satan\'s World System', 'study'),
    LeafFile('sr5', 'sr5-judgment-restoration-and-replacement', 'SR5 - Judgment, Restoration, and Replacement', 'study')
]

coming_tribulation = Dir('coming-tribulation')
coming_tribulation.leaves = [
    LeafFile('ct1', 'ct1-introduction', 'CT1 - Introduction', 'study'),
    LeafFile('ct2a', 'ct2a-the-seven-churches', 'CT2A - The Seven Churches', 'study'),
    LeafFile('ct2b', 'ct2b-the-heavenly-prelude', 'CT2B - The Heavenly Prelude', 'study'),
    LeafFile('ct3a', 'ct3a-the-tribulation-begins', 'CT3A - The Tribulation Begins', 'study'),
    LeafFile('ct3b', 'ct3b-antichrist-and-his-kingdom', 'CT3B - Antichrist and His Kingdom', 'study'),
    LeafFile('ct4', 'ct4-the-great-tribulation', 'CT4 - The Great Tribulation', 'study'),
    LeafFile('ct5', 'ct5-the-2nd-advent-and-armageddon', 'CT5 - The 2nd Advent and Armageddon', 'study'),
    LeafFile('ct6', 'ct6-last-things', 'CT6 - Last Things', 'study'),
    LeafFile('ct7', 'ct7-preparing-for-the-tribulation', 'CT7 - Preparing for Tribulation', 'study')
]

hebrews_series = Dir('hebrews-series')
hebrews_series.leaves = [
    LeafFile('heb0', 'heb0-introduction', 'Hebrews - Introduction', 'study'),
    LeafFile('heb1', 'heb1-the-son-of-god-superior-to-angels', 'Hebrews Chapter 1 - The Son of God Superior to Angels', 'study'),
    LeafFile('heb2', 'heb2-the-purpose-of-the-incarnation-of-the-son', 'Hebrews Chapter 2 - The Purpose of the Incarnation of the Son', 'study'),
    LeafFile('heb3', 'heb3-jesus-superiority-to-moses-and-the-negative-example-of-the-exodus-generation', 'Hebrews Chapter 3 - Jesus\' Superiority to Moses and the Negative Example of the Exodus Generation', 'study'),
    LeafFile('heb4', 'heb4-the-true-sabbath-rest-the-word-and-our-new-high-priest', 'Hebrews Chapter 4 - The True Sabbath Rest, the Word, and our New High Priest', 'study'),
    LeafFile('heb5', 'heb5-jesus-christ-our-true-high-priest-his-sacrifice-for-us-and-the-reversion-of-the-jerusalem-church', 'Hebrews Chapter 5 - Jesus Christ Our True High Priest, His Sacrifice for Us, and the Reversion of the Jerusalem Church', 'study'),
    LeafFile('heb6', 'heb6-the-hope-that-anchors-us', 'Hebrews Chapter 6 - The Hope that Anchors Us', 'study'),
    LeafFile('heb7', 'heb7-our-new-high-priest-jesus-christ', 'Hebrews Chapter 7 - Our New High Priest: Jesus Christ', 'study'),
    LeafFile('heb8', 'heb8-jesus-christ-high-priest-of-a-better-covenant', 'Hebrews Chapter 8 - Jesus Christ: High Priest of a Better Covenant', 'study')
]

base_dir = Dir('ichthys-study-notes')
base_dir.subdirs = [
    peter_series,
    bible_basics,
    satanic_rebellion,
    coming_tribulation,
    hebrews_series
]
