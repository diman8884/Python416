import re

st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
reg = r"\+?7\d{10}"
print(re.findall(reg, st))