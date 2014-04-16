formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ('whyyyy', "two", "three", "four")
#no need to put "" around true and false because they are recognized, doing so would turn them into strings
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight.")

#why is the parentesis so far down in the example?
#why in line 4 does it not matter if its 1 ' or 2 "..always prints with 1 '