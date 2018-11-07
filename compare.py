#!/usr/bin/env python3

import configparser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time
import sys
import urllib
import re
import time
import hashlib
#from urlparse3 import parse_qs, urlparse
from urllib.parse import parse_qs, urlparse
import os
import io


import math
import operator
from collections import defaultdict
from PIL import Image, ImageChops, ImageOps, ImageDraw


class urlList():

    def __init__(self):
        self.pages = []
        self.project = ''

    def readFile(self, fname):
        f = open(fname, 'r')
        for line in f:
            if self.project == '':
                self.project = line.rstrip()
            else:
                self.pages.append(line.rstrip())

        print(self.pages)

        return self.pages

    def generateTypo3Links(self, lang = []):
        '''
        pids = [367, 368, 411, 370, 423, 416, 406, 407, 374, 405, 397, 399, 430, 379, 377, 394, 373, 380, 381, 378, 382, 417, 419, 418, 420, 421, 431, 429, 369, 442, 424, 414, 415]
        self.baseurl = 'www.parkingtec.ch'

        self.baseurl = 'www.parkingtec.ch:8081'
        self.lang = [2, 3]

        self.baseurl = 'www.taxomex.ch'
        self.baseurl = 'www.taxomex.ch:8081'
        self.lang = [2, 3]
        pids = [1, 6, 9, 12, 13, 14, 18, 22, 376, 114, 118, 43, 53, 44, 126, 135, 55, 51, 52, 57, 58, 60, 120, 121, 122, 475, 5, 17, 474, 113, 128, 132, 61, 3, 4, 492, 108, 21, 443, 23, 133, 115, 116, 117, 491, 129]

        self.baseurl = 'global.vonballmoos.com'
        self.lang = []
        pids = [284, 285, 286, 287, 324, 325, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 427, 313, 312, 322, 321, 320, 319]

        self.baseurl = 'www.vonballmoos.com'
        self.lang = [2, 3]
        pids = [175, 177, 178, 179, 180, 358, 249, 250, 280, 192, 193, 194, 195, 196, 366, 182, 432, 185, 187, 272, 198, 199, 184, 197, 186, 449, 354, 212, 213, 273, 214, 274, 215, 452, 253, 258, 261, 262, 485, 486, 202, 439, 357, 355, 205, 206, 349, 347, 426, 339, 338, 340, 341, 489, 490, 372, 482, 483, 267, 484, 223, 224, 458, 463, 467, 257, 259, 344, 343, 428, 351, 352, 353, 433, 434, 451, 495, 453, 444, 229, 230, 235, 236, 480, 481, 385, 441, 446, 440, 445, 454, 461, 460, 459, 466, 465, 464, 469, 471, 496]


        self.baseurl = 'www.taywa.ch'
        self.lang = []
        pids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 53, 55, 56, 57, 59, 60, 63, 66, 67, 68, 69, 72, 73, 74, 76, 77, 78, 79, 80, 81, 83, 84, 85]
        self.baseurl = 'www.noelledarbellay.com'
        self.lang = [2, 3]
        #self.lang = []
        pids = [1, 10, 11, 15, 12, 35, 13, 14, 16, 17, 2, 3, 4, 5, 6, 7, 8, 30, 29, 31, 32, 26, 18, 19, 22, 9, 28, 33, 34]
        pids = [13]

        # SELECT CONCAT(uid, ",") FROM `pages` WHERE hidden = 0 and deleted = 0 and doktype = 1
        self.baseurl = 'www.karling.ch:8081'
        pids = [7, 16, 20, 21, 24, 26, 28, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
        self.lang = []
        '''

        pids = [45, 344, 24, 51, 356, 819, 250, 904, 960, 364, 367, 365, 366, 368, 369, 363, 63, 64, 65, 67, 66, 157, 777, 824, 825, 826, 827, 96, 98, 99, 97, 851, 882, 516, 850, 965, 966, 712, 922, 793, 718, 702, 788, 908, 934, 935, 818, 790, 959, 874, 831, 789, 517, 873, 906, 715, 490, 787, 907, 491, 932, 884, 902, 713, 945, 927, 714, 485, 875, 876, 474, 504, 297, 299, 508, 809, 892, 300, 301, 734, 302, 303, 916, 304, 729, 305, 731, 307, 308, 774, 896, 754, 309, 844, 475, 898, 311, 497, 499, 312, 481, 313, 706, 298, 707, 314, 723, 315, 316, 495, 942, 317, 964, 812, 924, 894, 911, 319, 762, 846, 946, 320, 321, 954, 808, 900, 733, 766, 487, 509, 905, 322, 871, 958, 725, 889, 944, 918, 811, 323, 816, 325, 327, 328, 814, 329, 938, 813, 949, 727, 817, 330, 887, 333, 870, 181, 719, 482, 340, 36, 33, 35, 743, 936, 39, 143, 21, 968, 750, 44, 969, 41, 42, 43, 744, 137, 973, 923, 134, 133, 140, 346, 17, 19, 18, 32, 296, 249, 183, 184, 185, 186, 187, 188, 198, 190, 193 ]
        pids = [45, 344, 24, 51, 356, 819, 250, 904, 960]

        # self.project = self.baseurl
        for i in pids:
            self.pages.append('https://%s/index.php?id=%s' % (self.baseurl, i))
            for l in lang:
                self.pages.append('https://%s/index.php?id=%s&L=%s' % (self.baseurl, i, l))
        return self.pages



class Compare():
    def __init__(self, project,  pages, width=1280):
        # profile = webdriver.FirefoxProfile()
        # print (profile
        # profile.set_preference('browser.window.width', 1024)
        # profile.set_preference('browser.window.height', 300)
        # profile.update_preferences()
        self.width = width
        self.viewportonly = True
        self.storage = 'data'
        self.project = project

        self.browser = browser(self.width, self.viewportonly)

        self.fields = []
        self.pages = pages
        self.sleep = 1
        print ('Duration: {}s'.format(len(pages) * self.sleep))

    def loopPages(self):
        for p in self.pages:
            self.url = p
            self.browser.get(self.url)
            time.sleep(self.sleep)
            self.shot()
        # self.close()

    def extractT3Uid(self):
        return True

    def fname(self):
        url = urlparse(self.url)
        par = parse_qs(url.query)

        print (url)

        path = str(url.path)
        path = path.replace('/', '', 1)
        for i in ['.', '/']:
            path = path.replace(i, '_')

        print (path)

        # sys.exit()

        uid = path

        if 'id' in par:
            # pid = par['id'][0]
            uid = '%s_%s' % (uid, par['id'][0].zfill(3))

        if 'L' in par:
            # L =  par['L'][0]
            uid = '%s_%s' % (uid, par['L'][0])
        else:
            uid = '%s_%s' % (uid, 1)


        tstmp = time.strftime("%Y%m%d-%H%M%S")
        md5base = str(url.path + url.query).encode('utf-8')
        md5 = hashlib.md5(md5base)
        md5 = md5.hexdigest()[0:6]
        # self.project = str(url.netloc)
        # self.project = self.project.split(':')[0]
        if url.port:
            port = url.port
        else:
            port = 80

        mkdir = '{}/{}'.format(self.storage, self.project)
        if not os.path.exists(mkdir):
            os.makedirs(mkdir)

        name = '{}/{}/{}-{}_{}.{}'.format(self.storage, self.project, uid, self.width, tstmp, 'png')
        print (name)

        return name

    def shot(self):
        fname = self.fname()
        self.browser.save_screenshot(fname)

    def subscribe(self, fields=[]):

        self.startPage()
        for i in fields:
            print (i)
            elem = self.browser.find_element_by_id(i)
            if i == 'mailformemail':
                elem.send_keys('ft@taywa.ch')
            else:
                elem.send_keys(i)
        self.fillMail()
        # elem = self.browser.find_element_by_id('email')
        # mail = self.mail()
        # elem.send_keys(mail)
        elem = self.browser.find_elements_by_xpath('.//input[@type="submit"]')
        elem[0].click()

    def mail(self):
        name = time.strftime("%Y%m%d%H%M")
        mail = name+"@icy.ch"
        print (mail)
        return mail

    def fillMail(self):
        elem = self.browser.find_element_by_id('email')
        mail = self.mail()
        elem.send_keys(mail)

    def close(self):
        self.browser.close()


class browser():

    def __init__(self, width=1200, viewportonly=True):
        self.temppath = '/tmp/'
        self.viewportonly = viewportonly
        profile = webdriver.FirefoxProfile('/home/m/.mozilla/firefox/7opu4o1o.silenium/')
        self.browser = webdriver.Firefox(profile)
        self.width = width
        self.height = 1100
        self.browser.set_window_position(0, 0)
        self.browser.set_window_size(self.width, self.height)
        self.verbose = 0

    def get(self, url):
        self.browser.get(url)

    def close(self, url):
        self.browser.close()

    def save_screenshot(self, path, force=False):
        if not os.path.exists(path) or force:

            if self.viewportonly is True:
                screenshot = Image.open(io.BytesIO(self.browser.get_screenshot_as_png()))
                screenshot.save(path)
            else:
                '''
                stick and scroll
                https://gist.github.com/fabtho/13e4a2e7cfbfde671b8fa81bbe9359fb
                from here http://stackoverflow.com/questions/1145850/how-to-get-height-of-entire-document-with-javascript
                this solution has one major drawback, fixed css elements (position: fixed) ear repeateed 
                better than this would be use virtualscreen and set browser height to body height and screenshot this
                '''
                js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'

                scrollheight = self.browser.execute_script(js)

                js = 'var x = document.getElementsByClassName("navbar-default"); if (x.length > 0) { x[0].style.position = "static";};'
                self.browser.execute_script(js)
                js = 'var x = document.getElementsByClassName("sticky-tagline"); if (x.length > 0) { x[0].style.display = "none";};'
                self.browser.execute_script(js)

                if self.verbose > 0:
                    print (scrollheight)

                slices = []
                offset = 0
                while offset < scrollheight:
                    if self.verbose > 1:
                        print (offset)

                    self.browser.execute_script("window.scrollTo(0, %s);" % offset)


                    # screenshot = driver.get_screenshot_as_base64()

                    img = Image.open(io.BytesIO(self.browser.get_screenshot_as_png()))

                    # img = Image.open(BytesIO(base64.b64decode(screenshot))

                    # img = Image.open( io.BytesIO( base64.b64decode(self.browser.get_screenshot_as_base64() ) ) )

                    offset += img.size[1]
                    slices.append(img)

                    self.browser.get_screenshot_as_file('%s/screen_%s.png' % (self.temppath, offset))

                screenshot = Image.new('RGB', (slices[0].size[0], scrollheight))
                offset = 0
                for img in slices:
                    screenshot.paste(img, (0, offset))
                    offset += img.size[1]

                screenshot.save(path)


class calcDiff():
    def __init__(self, project, width=1280):
        self.project = project
        self.storage = 'data'
        self.width = str(width) 

    def readAllImg(self):
        folder = '{}/{}'.format(self.storage, self.project)
        for subdir, dirs, files in os.walk(folder):
            files = [ fi for fi in files if fi.find(self.width) > 0 and not fi.endswith(".jpg") ]
            self.files = files
            print(files)
            print(self.width)
            return files
            # for file in files:
                # print (os.path.join(subdir, file)    

    def sortImg(self):
        files = self.readAllImg()
        # pages = {}
        pages = defaultdict(list)
        for f in files:
            # pid = f.split('-')[0]
            pid = f.split('__1-')[0]
            # pages[pid] = pages[pid].append(f)
            pages[pid].append(f)

        self.pages = pages
        print (pages)
        #sys.exit()

    def diffPages(self):
        print (self.pages)

        for pid in self.pages.items():
            print ('pid')
            print (pid[1])
            print (pid[0])

            for i in range(0, len(pid[1])-1):
                print ("i %s" % i)
                first = pid[1][i]
                second = pid[1][i+1]
                print(first)
                print(second)
                self.mkimgdiff(first, second)
            #for img in pid:
                #self.mkimgdiff()

    def mkimgdiff(self, first, second):
        print ('mkimgdiff')
        fname = '{}/{}/{}_{}.jpg'.format(self.storage, self.project, first, second)

        # only calculate diff, if not allready there
        if not os.path.isfile(fname):
            im1fname = '{}/{}/{}'.format(self.storage, self.project, first)
            im1 = Image.open(im1fname).convert('RGBA')
            im2fname = '{}/{}/{}'.format(self.storage, self.project, second)
            im2 = Image.open(im2fname).convert('RGBA')
            diff = ImageChops.difference(im2, im1)
            #h =  ImageChops.difference(im2, im1).histogram()

            # if any change          
            if not self.equal(diff):
                # save diff file  
                diff.save(fname)
                '''
                rect = diff.getbbox()
                crop = diff.crop(rect)
                # save rect on changed rect
                trans = Image.new('RGBA', im1.size, (255, 255, 255, 0))

                draw = ImageDraw.Draw(trans)
                draw.rectangle(rect, fill=(256, 0, 0, 128), outline=(128, 128, 128, 128))
                draw = ImageDraw.Draw(im2)
                draw.rectangle(rect, fill=None, outline=128)
                del draw
                try:
                    im1 = Image.alpha_composite(im1, trans)
                    filename =  '{}.jpg'.format(im1fname)
                    im1.save(filename)
                except:
                    raise
                    # pass
                try:
                    im2 = Image.alpha_composite(im2, trans)
                    filename =  '{}.jpg'.format(im2fname)
                    im2.save(filename)
                except:
                    # raise
                    pass
                '''    
                # invert = ImageOps.invert(crop)
                #crop.save(self.project + os.sep + first +'_'+second+'_crop.jpg')
        #rms =  math.sqrt(reduce(operator.add, map(lambda h, i: h*(i**2), h, range(256))) / (float(im1.size[0]) * im1.size[1]))
        #print (rms
        #diff.show()

    def equal(self, diff):
        print (diff.getbbox())
        return diff.getbbox() is None


def run():
    urllist = urlList()
    # pages = urllist.generateTypo3Links()
    pages = urllist.readFile('url.txt')

    project = urllist.project
    print(project)

    c = Compare(urllist.project, pages, 1600)
    c.loopPages()

    c = Compare(urllist.project, pages)
    c.loopPages()
    c = Compare(urllist.project, pages, 640)
    c.loopPages()
    c = Compare(urllist.project, pages, 360)
    c.loopPages()

    d = calcDiff(urllist.project, 1600)
    d.sortImg()
    d.diffPages()
    d = calcDiff(urllist.project)
    d.sortImg()
    d.diffPages()
    d = calcDiff(urllist.project, 640)
    d.sortImg()
    d.diffPages()
    d = calcDiff(urllist.project, 360)
    d.sortImg()
    d.diffPages()


run()

'''
baseurl = 'www.parkomatic.ch'
pids = [2, 67, 74, 77, 91, 92, 165, 174, 176, 386, 387, 137, 148, 151, 72, 73, 173, 152, 153, 154, 155, 138, 139, 140, 141, 170, 163, 164, 100, 101, 102, 497, 472, 447, 371, 94, 95, 96, 97, 79, 144, 78, 145, 142, 143, 171, 69, 150, 93, 166, 425, 384, 448, 473, 498]
lang = [2, 3]

#run(baseurl, pids, lang)

baseurl = 'www.parkomatic.ch:8081'

run(baseurl, pids, lang)

baseurl = 'www.vonballmoos.com'
lang = [2, 3]
pids = [175, 177, 178, 179, 180, 358, 249, 250, 280, 192, 193, 194, 195, 196, 366, 182, 432, 185, 187, 272, 198, 199, 184, 197, 186, 449, 354, 212, 213, 273, 214, 274, 215, 452, 253, 258, 261, 262, 485, 486, 202, 439, 357, 355, 205, 206, 349, 347, 426, 339, 338, 340, 341, 489, 490, 372, 482, 483, 267, 484, 223, 224, 458, 463, 467, 257, 259, 344, 343, 428, 351, 352, 353, 433, 434, 451, 495, 453, 444, 229, 230, 235, 236, 480, 481, 385, 441, 446, 440, 445, 454, 461, 460, 459, 466, 465, 464, 469, 471, 496]
    
run(baseurl, pids, lang)

baseurl = 'www.vonballmoos.com:8081'
    
run(baseurl, pids, lang)
'''
