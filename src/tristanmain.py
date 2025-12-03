"""
Test runner for the UI layer with MockLL
Run this to manually test the create_tournament flow
"""
import sys
sys.path.insert(0, 'src')


from UI.mainUI import UImain

def main():
    """Run the UI with a mock logic layer for testing."""
    print("=" * 50)
    print("UI TEST MODE - Using MockLL")
    print("=" * 50)
    print()
    # Create and run the UI (no LL needed for UI navigation testing)
    ui = UImain(ll_wrapper=None)
    ui.run()

if __name__ == "__main__":
    main()