from time import sleep
from bs4 import BeautifulSoup
from requests import get
from Player import Player

def get_records():
    URL = 'https://www.hltv.org/'

    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    player_list = []

    complete_ranking = bs.find('a', class_='block button text-center')
    ranking_link = get(URL + complete_ranking['href'])
    bs2 = BeautifulSoup(ranking_link.content, 'html.parser')

    for player in bs2.find_all('td', class_='player-holder'):

        player_link = player.find('a')
        page3 = get(URL + player_link['href'])
        bs3 = BeautifulSoup(page3.content, 'html.parser')

        div_team = bs3.find('div', class_='playerTeam')
        team = div_team.find('a').get_text()

        div_nickname = bs3.find('h1', class_='playerNickname').get_text()
        div_name = bs3.find('div', class_='playerRealname').get_text().lstrip()
        div_nationality = bs3.find('img', class_='flag')
        div_age = bs3.find('span', class_='listRight')
        age = div_age.find('span').get_text().replace(' years','')

        #If player has no stats within 3 months we're searching for values in advanced stats [example 'Farlig' from team 'Astralis']
        empty_stats = bs3.find("div", class_='playerpage-container empty-state')
        if empty_stats is not None:
            player_link_complete_stats = bs3.find('a', class_='moreButton')
            page4 = get(URL + player_link_complete_stats['href'])
            bs4 = BeautifulSoup(page4.content, 'html.parser')
            div_kdratio = bs4.find('div', class_='stats-row').findNext('div', class_='stats-row').findNext('div', class_='stats-row').findNext('div', class_='stats-row').find('span').findNext('span').get_text()
            div_headshots = bs4.find('div', class_='stats-row').findNext('div', class_='stats-row').find('span').findNext('span').get_text()
        else:
            div_kdratio = bs3.find('span', class_='statsVal').get_text()
            div_headshots = bs3.find('span', class_='statsVal').findNext('span').findNext('span').get_text().replace('%','')

        #If player has no achievements in achievements tab we're setting it for 0 values [example 'k1to' from team 'BIG']
        empty_major_stats = bs3.find('div', 'playerProfile').find('div', id='achievementBox').find("div", class_='empty-state')
        if empty_major_stats is not None:
            major_won = 0
            major_played = 0
        else:
            div_major = bs3.find('div', class_='sub-tab-content').find('div', class_='highlighted-stats-box')
            major_won = div_major.find('div', class_='stat').get_text()
            major_played = div_major.find('div', class_='stat').findNext('div', class_='stat').get_text()

        #Creating each player and append him to list of players
        player = Player(team, div_nickname, div_name, div_nationality['alt'], age, div_kdratio, div_headshots, major_won, major_played)
        player_list.append(player)
        print(player)
        #print(f"Team {team}, Nick {div_nickname}, Name {div_name}, Nationality {div_nationality['alt']}, Age {age}, K/D Ratio {div_kdratio}, Headshots {div_headshots}, Majors won {major_won}, Majors played {major_played}")
        sleep(0.3)
    
    return player_list

