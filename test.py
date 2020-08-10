from solution import christmas_tree

# DON'T MODIFY THIS FILE

if __name__ == "__main__":
    with open("result.tree") as file:
        if christmas_tree() and christmas_tree() == "\n".join([line.rstrip('\n') for line in file]):
            print("SUCCESS")
        else:
            print("FAILURE")
