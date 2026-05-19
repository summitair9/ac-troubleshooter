def ac_troubleshooter():
    print("=" * 50)
    print("   AC SERVICE CALL TROUBLESHOOTER")
    print("   (Helps decide if tech is needed)")
    print("=" * 50)
    print()

    print("What is the main problem?")
    print("1. No power / unit not turning on")
    print("2. Running but not cooling")
    print("3. Frozen / ice on pipes")
    print("4. Weak or no airflow")
    print("5. Strange noises, smells, or leaks")
    print("6. Other")
    
    choice = input("\nEnter number (1-6): ").strip()

    if choice == "1":
        print("\n✅ Check: Thermostat batteries, breakers, air filter.")
        print("If still no power after these → Schedule tech.")
    
    elif choice == "2":
        print("\n✅ Step 1: Replace air filter")
        print("Step 2: Clear debris around outdoor unit")
        print("Step 3: Check for ice")
        print("If no improvement → Schedule tech.")
    
    elif choice == "3":
        print("\n✅ Customer instructions:")
        print("1. Turn thermostat OFF")
        print("2. Set fan to ON")
        print("3. Replace air filter")
        print("4. Wait until fully thawed (2-6 hours)")
        print("If it freezes again → Schedule tech.")
    
    elif choice == "4":
        print("\n✅ Replace air filter + check vents")
        print("If indoor fan not running → Schedule tech.")
    
    elif choice == "5":
        print("\n⚠️  Turn system OFF and schedule tech immediately.")
    
    else:
        print("\nPlease describe the issue to the customer service team.")

    print("\n✅ Done. Would you like to run again? (y/n)")

# Run the program
if __name__ == "__main__":
    while True:
        ac_troubleshooter()
        again = input().strip().lower()
        if again != "y":
            print("Thank you! Stay cool 😎")
            break
