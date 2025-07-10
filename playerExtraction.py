from bs4 import BeautifulSoup
import requests

    # soup = BeautifulSoup(open("testDoc.html"))
    # soup = BeautifulSoup("<p>Test</p>")
def find_player(specific_name):
    """
    """
    url = "https://cmsathletics.org/sports/softball/roster"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the player's name
        #specific_name = "Emma Suh"
        # Find all name tags
        name_containers = soup.find_all('div', class_='sidearm-roster-player-name')
        found = False
        for container in name_containers:
            # Look for the <h3> tag inside the container
            h3_tag = container.find('h3')
            if h3_tag:
                # Look for the <a> tag inside the <h3> tag
                a_tag = h3_tag.find('a')
                if a_tag:
                    player_name = a_tag.get_text(strip=True)
                    if player_name == specific_name:
                        found = True
                        # print(f"Found Player: {player_name}")
                        # break
                        return f"Found Player: {player_name}"

        if not found:
            #print(f"Player '{specific_name}' not found in the roster.")
            return f"Player '{specific_name}' not found in the roster."

    
    
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")