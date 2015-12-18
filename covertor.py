import os
import json
import sys
import collections
# in makeJSON function
# metadata = {} from earlier


def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def getTitle(path):
    p = os.path.join(path, '__title__')
    if os.path.isfile(p):
        f = open(path + '\__title__')
        temp = []
        for line in f:
            temp.append(str(line.rstrip('\n')))
        f.close
        return temp[0]
    return ""


def getCategory(path):
    p = os.path.join(path, '__Category__')
    if os.path.isfile(p):
        f = open(path + '\__Category__')
        temp = []
        for line in f:
            temp.append(str(line.rstrip('\n')))
        f.close
        return temp[0]
    return ""


def getArtist(path):
    p = os.path.join(path, '__Artist__')
    if os.path.isfile(p):
        f = open(path + '\__Artist__')
        temp = []
        for line in f:
            temp.append(str(line.rstrip('\n')))
        f.close
        return temp[:]
    return [""]

def getCharacters(path):
    p = os.path.join(path, '__Characters__')
    if os.path.isfile(p):
        f = open(path + '\__Characters__')
        temp = []
        for line in f:
            temp.append(str(line.rstrip('\n')))
        f.close
        return temp[:]
    return [""]

def getContents(path):
    p = os.path.join(path, '__Contents__')
    if os.path.isfile(p):
        f = open(path + '\__Contents__')
        temp = []
        for line in f:
            temp.append(str(line.rstrip('\n')))
        f.close
        return temp[:]
    return [""]


def getGroup(path):
    p = os.path.join(path, '__Circle__')
    if os.path.isfile(p):
        f = open(path + '\__Circle__')
        temp = []
        for line in f:
            temp.append(str(line.rstrip('\n')))
        f.close
        return temp[:]
    return [""]


def getLanguage(path):
    p = os.path.join(path, '__Language__')
    if os.path.isfile(p):
        f = open(path + '\__Language__')
        temp = []
        for line in f:
            temp.append(str(line.rstrip('\n')))
        f.close
        return temp[:]
    return [""]


def getParody(path):
    p = os.path.join(path, '__Parody__')
    if os.path.isfile(p):
        f = open(path + '\__Parody__')
        temp = []
        for line in f:
            temp.append(str(line.rstrip('\n')))
        f.close
        return temp[:]
    return [""]


def deleteOld(path):
    files = ["__Artist__", "__Category__", "__Characters__", "__Circle__", "__Contents__", "__Convention__",
         "__Description__", "__Language__", "__oid__", "__Parody__", "__title__", "__Scanlator__", "__Copy__", "__Chapters__"]
    for f in files:
         p = os.path.join(path, f)
         if os.path.isfile(p):
              os.remove(p)


def makeJSON(path):
    # initialize
        metadata ={
        "gallery_info":collections.OrderedDict( {}),  # this is the key you put data in
        # these last two keys need to be present or else Happypanda won't accept
        # this file (just leave them empty)
        "image_api_key": "",
        "image_info": ""
        }
        gallery_info = metadata['gallery_info']
        gallery_info['title'] = getTitle(path)
        gallery_info['title_original'] = getTitle(path)
        gallery_info['category'] = getCategory(path)
        gallery_info['tags'] =collections.OrderedDict( {})
        gallery_tags = gallery_info['tags']
        gallery_tags['language'] = getLanguage(path) # should return a list
        gallery_tags['parody'] = getParody(path) # should return a list
        gallery_tags['character'] = getCharacters(path) # should return a list
        gallery_tags['group'] = getGroup(path) # should return a list
        gallery_tags['artist'] = getArtist(path) # should return a list
        gallery_tags['misc'] = getContents(path) # should return a list
        #extra stuff that is needed but not used
        gallery_info['language'] = getLanguage(path)[0]
        gallery_info['translated'] = "true"
        gallery_info['favorite_category'] = "null"
        gallery_info['upload_date'] =[2015, 12, 12, 14, 2, 0]
        gallery_info['source'] =collections.OrderedDict( {})
        gallery_source = gallery_info['source']
        gallery_source['site'] = "e-hentai"
        gallery_source['gid'] = 55
        gallery_source['token'] = "e23b5c3ed"
        gallery_source['parent_gallery'] = "null"
        gallery_source['newer_versions'] = []
        fileloc = os.path.join(path, "info.json")
        with open(fileloc, "w", encoding="utf-8") as infofile:
            json.dump(metadata,infofile, indent = 2)
        deleteOld(path)

def convertAll(path):    
	for root, dirs, files in os.walk(path):     
		for dir in dirs:
				makeJSON(os.path.join(path, dir))
def main():
    PATH = getScriptPath()
    curPath = ""
    #for each folder
    for item in os.listdir(PATH):
        if os.path.isdir(os.path.join(PATH, item)):
            curPath = os.path.join(PATH, item)
            convertAll(curPath)

main()
