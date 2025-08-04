from bs4 import BeautifulSoup
import requests

    # soup = BeautifulSoup(open("testDoc.html"))
    # soup = BeautifulSoup("<p>Test</p>")
def find_player(specific_name):
    """
    """
    base_url = "https://cmsathletics.org"
    softball_roster_url = f"{base_url}/sports/softball/roster"
    response = requests.get(softball_roster_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        name_containers = soup.find_all('div', class_='sidearm-roster-player-name')
  
        for container in name_containers:
            # Look for the <h3> tag inside the container
            h3_tag = container.find('h3')
            if h3_tag:
                # Look for the <a> tag inside the <h3> tag
                a_tag = h3_tag.find('a')
                if a_tag:
                    player_name = a_tag.get_text(strip=True)
                    if player_name == specific_name:
                        player_href = a_tag['href']
                        player_url = f"{base_url}{player_href}"
                        stats = get_player_stats(player_url, player_name)
                      
                        # print(f"Found Player: {player_name}")
                        # break
                        return f"Found Player: {player_name}"
                    


import requests
from bs4 import BeautifulSoup

def get_player_stats(player_url, player_name):
    """
    Fetches 'Hits' and 'Runs Scored' season highs from a player's page.
    Returns a dictionary with the stats.
    """
    response = requests.get(player_url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page for {player_name}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the "Season Highs (Hitting)" table
    caption = soup.find("caption", string="Season Highs (Hitting)")
    if not caption:
        print(f"No hitting stats table found for {player_name}")
        return None

    table = caption.find_parent("table")
    stats = {}

    for row in table.tbody.find_all("tr"):
        cols = row.find_all("td")
        stat_name = cols[0].text.strip()
        stat_value = cols[1].text.strip()
        stat_date = cols[2].text.strip()
        opponent = cols[3].text.strip()
        
        if stat_name in ["Hits", "Runs Scored"]:
            stats[stat_name] = {
                "value": stat_value,
                "date": stat_date,
                "opponent": opponent
            }

    return stats

# Example usage:
# url = "https://example.com/roster.aspx?rp_id=1234"  # Replace with actual player URL
# player_name = "Jane Doe"
# player_stats = get_player_stats(url, player_name)

# if player_stats:
#     for stat, info in player_stats.items():
#         print(f"{player_name} - {stat}: {info['value']} on {info['date']} vs {info['opponent']}")





# def get_player_stats(player_url, player_name):
#     """
#     Fetches player stats from the player's page.
#     """
#     response = requests.get(player_url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # Locate the stats section
#         stats_section = soup.find('section', id='sidearm-roster-player-stats')
    
#         if stats_section:
#             # Locate the stats table within the section
#             stats_table = stats_section.find('table')
#             print(stats_table)
#             if stats_table:
               
#                 stats = {"Player": player_name}
#                 # Iterate through rows in the table
#                 for row in stats_table.find_all('tr'):
#                     cols = row.find_all('td')
#                     if len(cols) >= 2:  # Ensure there are at least two columns
#                         label = cols[0].get_text(strip=True)  # First column is the label
#                         value = cols[1].get_text(strip=True)  # Second column is the value
#                         if label == "Hits":
#                             stats['Hits'] = value
#                         elif label == "Runs":
#                             stats['Runs'] = value
#                         elif label == "Triples":
#                             stats['Triples'] = value
#                         elif label == "Doubles":
#                             stats['Doubles'] = value

#                 if stats:
#                     print(f"Stats for {player_name}: {stats}")
#                     return stats
#                 else:
#                     return f"No relevant stats found for {player_name}."
#             else:
#                 return "Stats table not found in the stats section."
#         else:
#             return "Stats section not found on the player's page."
#     else:
#         return f"Failed to retrieve player stats. Status code: {response.status_code}"