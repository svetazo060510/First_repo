from contact_book import add_contact, search_contact

def run_tests():
    """Runs a series of tests to check the contact book logic."""
    print("Running tests...")
    
    # Test 1: Start with an empty list
    contacts = []
    assert len(contacts) == 0, "Test 1 Failed: Initial list should be empty"
    
    # Test 2: Add a valid contact
    result = add_contact("Alice Smith, 555-1234, alice@email.com", contacts)
    assert result is True, "Test 2 Failed: add_contact should return True for valid input"
    assert len(contacts) == 1, "Test 2 Failed: List should have 1 contact"
    assert contacts[0]['name'] == "Alice Smith", "Test 2 Failed: Name not stored correctly"
    
    # Test 3: Add another valid contact with extra whitespace to test strip()
    add_contact("  Bob Johnson  ,  555-5678  , bob@email.com ", contacts)
    assert len(contacts) == 2, "Test 3 Failed: List should have 2 contacts"
    assert contacts[1]['name'] == "Bob Johnson", "Test 3 Failed: Name not stripped correctly"
    assert contacts[1]['phone'] == "555-5678", "Test 3 Failed: Phone not stripped correctly"
    
    # Test 4: Try to add a contact with an invalid format
    result = add_contact("Charlie Brown, 555-9999", contacts) # Missing email
    assert result is False, "Test 4 Failed: add_contact should return False for invalid input"
    assert len(contacts) == 2, "Test 4 Failed: Invalid contact should not be added to the list"
    
    # Test 5: Search for an existing contact (case-insensitive)
    found = search_contact("alice smith", contacts)
    assert found is not None, "Test 5 Failed: Should have found Alice"
    assert found['email'] == "alice@email.com", "Test 5 Failed: Found the wrong contact"

    # Test 6: Search for a non-existent contact
    found = search_contact("Zelda", contacts)
    assert found is None, "Test 6 Failed: Should return None for a contact that doesn't exist"

    print("✅ All tests passed!")

# Run the tests when the script is executed
if __name__ == "__main__":
    run_tests()