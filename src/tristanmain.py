from UI.mainUI import UImain

class DummyLL:
    """A placeholder Logic Layer for testing the UI."""
    pass

def main():
    ll = DummyLL()  # fake logic layer
    ui = UImain(ll)
    ui.run()

if __name__ == "__main__":
    main()
