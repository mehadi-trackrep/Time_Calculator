from main import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))
print(add_time("6:30 PM", "205:12"))


# Run unit tests automatically
main(module='test_module', exit=False)