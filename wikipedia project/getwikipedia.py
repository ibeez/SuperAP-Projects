from bs4 import BeautifulSoup 
import requests 
from link import link
#print out formatted code
#print(catchurch.prettify())

endLinks = []
finishlinks = []
endLinks2 = []
finishlinks2 = []
def linksToAssistClass(whatlinkshere2):
    whatlinkshere2a = requests.get(whatlinkshere2)
    links1a = BeautifulSoup(whatlinkshere2a.content, 'html.parser')
    for links2 in links1a.find_all(id = "mw-whatlinkshere-list"):
        for linky in links2.find_all('a'):
            #filters out: links that are 'copies' of others or not actual valid pages; links that are special versions of others; links that are 'lists of others' - generally, those only ever link to other lists, which isn't very handy. hooray for cleaning data 
            if linky.get('href')[0 : 6] == '/wiki/' and linky.get('href').find(':') == -1 and linky.get('href').find('List_of') == -1:
                #print(link.get('href'))
                placeholder = link('end', 'https://en.wikipedia.org/' + linky.get('href'))
                finishlinks.append('https://en.wikipedia.org/' + linky.get('href'))   
#####################################################################################################################################################
def getAllUsableLinksTo(whatlinkshere):
    finishlinks.append(whatlinkshere)
    #get raw data from a webpage 
    page = requests.get(whatlinkshere)
    #convert data into usable text of html code
    hamer = BeautifulSoup(page.content, 'html.parser')
    #finds the temporary link to the next one from the "root" original page. this may not be what root actually should mean in this context 
    tempfromroot = hamer.find(accesskey="j").get('href')
    #bizarrely and inelegantly, this is the simplest way I've been able to find to switch to a version of the page that displays more than the default 50 links
    links1 = requests.get('https://en.wikipedia.org/w/index.php?title='+tempfromroot[tempfromroot.find('Special'):]+'&limit=500')
    links1a = BeautifulSoup(links1.content, 'html.parser')
    for links2 in links1a.find_all(id = "mw-whatlinkshere-list"):
        for linky in links2.find_all('a'):
            #filters out: links that are 'copies' of others or not actual valid pages; links that are special versions of others; links that are 'lists of others' - generally, those only ever link to other lists, which isn't very handy. hooray for cleaning data 
            if linky.get('href')[0 : 6] == '/wiki/' and linky.get('href').find(':') == -1 and linky.get('href').find('List_of') == -1:
                #print(link.get('href'))
                placeholder = link('end', 'https://en.wikipedia.org/' + linky.get('href'))
                finishlinks2.append(placeholder)
                finishlinks.append('https://en.wikipedia.org/' + linky.get('href'))
    while True:
        nextset = links2.find('a', text = 'next 500')
        if type(nextset) is None:
            linksToAssistClass('https://en.wikipedia.org/'+nextset.get('href'))
        else:
            break
        
    #for link in hamer.find_all('a'):
    #     print(link.get('href'))
#############################################################################################################################################



#############################################################################################################################################
def getAllUsableLinksFrom(whatsThisLinkTo):
    page1 = requests.get(whatsThisLinkTo)
    tobegotten = BeautifulSoup(page1.content, 'html.parser')
    for links in tobegotten.find_all(id = "bodyContent"):
        for link3 in links.find_all('a'):
            #for some reason, some of the links found in articles aren't strings, but most of them are 
            if isinstance(link3.get('href'), str):
                #filters out lists, articles that have no actual text, links to exterior sites(like sources), and links to files and images
                if link3.get('href').find('Category') == -1 and link3.get('href').find('File') == -1 and link3.get('href').find('#') == -1 and link3.get('href').find('/wiki/') != -1 and link3.get('href').find(":") == -1 and link3.get('href').find('identifier') == -1:
                    #print(link3.get('href'))
                   
                    endLinks2.append(link(whatsThisLinkTo, 'https://en.wikipedia.org/'+link3.get('href')))
                    endLinks.append('https://en.wikipedia.org'+link3.get('href'))
#############################################################################################################################################


#endLinks2 = [link('none','fee'),link(99,"tree"),link(0,'fi'),link(999999,"humboldt"),link(2,'fo'),link(4,'fum')]

#######################################################################################################################
sources = []
def getSource(final):
    linkat = endLinks2[final]
    while True: 
        if linkat.source == 'none':
            sources.append(linkat.linkstothis)
            break
        else:
            sources.append(linkat.linkstothis)
            print(linkat.linkstothis)
            linkat = endLinks2[linkat.source]
    

def printSource():
    sourceList = ''
    sources.reverse()
    for i in sources:
        print(i)
        sourceList = sourceList + '=====>' + i
    print(sourceList[6:])
######################################################################################################################   


#getSource(5)
#printSource()



def findAMatch(start, end):
    endLinks2.append(link('none',start))
    finishlinks2.append(link('none',end))
# #print(findAMatch("https://en.wikipedia.org/wiki/Anatomical_terms_of_location","https://en.wikipedia.org/wiki/Padarn_Beisrudd"))
# print(findAMatch("https://en.wikipedia.org/wiki/Cat","https://en.wikipedia.org/wiki/Deciduous_teeth"))
