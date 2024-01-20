from PIL import Image
import pytesseract

IdealData = """1.e4 d6 2.d4 c6 3.@f3 Ma5+ 4. M@c3 DaG 5. Hd3 Abs 6. Md2 b5 7. a3
Axd3+ 8. oxd3 bs 9. &d5 fad 10. b3 a6 11. Mc7+ QB 12. Axaé
&xa6 13.0-0 b4 14. Axb4 Bc8 15. We2 Ate 16. Mg5 Ves 17. act h6 18.
Wxc6+ Axcé 19. Mxc6 hxg5 20. Kxa6 Ag4 21. Kct Hha 22. d5 Axh2 23.
c8+ @d7 24. Kacé Ans 25. K6c7# 1-0"""

class GameData:
    def __init__(self, iimagePath, ilanguage):
        self.imagePath = iimagePath
        self.language = ilanguage
        self.textFromImage = IdealData #pytesseract.image_to_string(Image.open(iimagePath), lang=ilanguage)
    
    def BlackAndWhiteSeparation(self):
        movesList = {"white":[], "black":[]}
        alistOfWords = self.textFromImage.split(" ")
        self.score = alistOfWords.pop(-1)
        isWhite = True

        for aword in alistOfWords:
            if "." in aword:
                aword = aword.split(".", 1)[-1]

            if aword != "":
                if "\n" in aword and aword.split("\n")[0] != "":
                    movesList["white"].append(aword.split("\n")[0])
                    movesList["black"].append(aword.split("\n")[1])
                elif "\n" in aword and aword.split("\n")[0] == "":
                    movesList["white"].append(aword.split("\n")[1])
                    isWhite = not isWhite
                elif isWhite:
                    movesList["white"].append(aword)
                    isWhite = not isWhite
                else:
                    movesList["black"].append(aword)
                    isWhite = not isWhite

        self.movesList = movesList
        return movesList

#Main

aObject = GameData("path", "chess")
print(aObject.BlackAndWhiteSeparation())
print("The Score is : " + aObject.score)