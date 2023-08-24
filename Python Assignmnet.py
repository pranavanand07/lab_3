class PythonAssignmnet:
    def init(self):
        self.data = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]

    def search_by_team(self, team_name):
        matches = []
        for match in self.data:
            if team_name in [match["Team 01"], match["Team 02"]]:
                matches.append(match)
        return matches

    def search_by_location(self, location_name):
        matches = []
        for match in self.data:
            if match["Location"] == location_name:
                matches.append(match)
        return matches

    def search_by_timing(self, timing):
        matches = []
        for match in self.data:
            if match["Timing"] == timing:
                matches.append(match)
        return matches


def main():
    flight_table =PythonAssignmnet()

    while True:
        print("\nChoose a search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            team_name = input("Enter the team name: ")
            team_matches = flight_table.search_by_team(team_name)
            if team_matches:
                print("Matches for Team", team_name)
                for match in team_matches:
                    print(match)
            else:
                print("No matches found for Team", team_name)

        elif choice == "2":
            location_name = input("Enter the location: ")
            location_matches = flight_table.search_by_location(location_name)
            if location_matches:
                print("Matches at Location", location_name)
                for match in location_matches:
                    print(match)
            else:
                print("No matches found at Location", location_name)

        elif choice == "3":
            timing = input("Enter the timing: ")
            timing_matches = flight_table.search_by_timing(timing)
            if timing_matches:
                print("Matches with Timing", timing)
                for match in timing_matches:
                    print(match)
            else:
                print("No matches found with Timing", timing)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
   main()