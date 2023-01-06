def find_dog(sound):
    if sound == "멍멍":
        return("개가 짖나?")
    else:
        return("고양이구나")

sound = "야옹"
result = find_dog(sound)

print(result)