can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for i in can_we_count_it:
    if hasattr(i, "count"):
        print(str(type(i)) + " has the count attribute!")